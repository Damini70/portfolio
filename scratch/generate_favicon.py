import struct
import zlib
import math
import os

def create_png_bytes(width, height, rgba_buffer):
    raw_lines = []
    stride = width * 4
    for y in range(height):
        raw_lines.append(b'\x00' + rgba_buffer[y * stride : (y + 1) * stride])
    raw_data = b''.join(raw_lines)
    compressed = zlib.compress(raw_data, 6)

    def chunk(chunk_type, data):
        length = len(data)
        crc = zlib.crc32(chunk_type + data) & 0xFFFFFFFF
        return struct.pack('>I', length) + chunk_type + data + struct.pack('>I', crc)

    ihdr = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)
    return (
        b'\x89PNG\r\n\x1a\n'
        + chunk(b'IHDR', ihdr)
        + chunk(b'IDAT', compressed)
        + chunk(b'IEND', b'')
    )

class Canvas:
    def __init__(self, size=128):
        self.size = size
        self.pixels = [[0.0, 0.0, 0.0, 0.0] for _ in range(size * size)]

    def blend_pixel(self, x, y, r, g, b, a):
        if 0 <= x < self.size and 0 <= y < self.size:
            idx = y * self.size + x
            bg_r, bg_g, bg_b, bg_a = self.pixels[idx]
            out_a = a + bg_a * (1.0 - a)
            if out_a > 0.001:
                out_r = (r * a + bg_r * bg_a * (1.0 - a)) / out_a
                out_g = (g * a + bg_g * bg_a * (1.0 - a)) / out_a
                out_b = (b * a + bg_b * bg_a * (1.0 - a)) / out_a
            else:
                out_r, out_g, out_b = 0.0, 0.0, 0.0
            self.pixels[idx] = [out_r, out_g, out_b, out_a]

    def draw_circle(self, cx, cy, radius, color):
        r, g, b, a_max = color
        for y in range(int(cy - radius - 2), int(cy + radius + 3)):
            if y < 0 or y >= self.size: continue
            for x in range(int(cx - radius - 2), int(cx + radius + 3)):
                if x < 0 or x >= self.size: continue
                d = math.hypot(x - cx, y - cy) - radius
                if d <= 0.0:
                    alpha = a_max
                elif d < 1.5:
                    alpha = a_max * max(0.0, 1.0 - d / 1.5)
                else:
                    alpha = 0.0
                if alpha > 0:
                    self.blend_pixel(x, y, r, g, b, alpha)

    def draw_ellipse(self, cx, cy, rx, ry, color):
        r, g, b, a_max = color
        for y in range(int(cy - ry - 2), int(cy + ry + 3)):
            if y < 0 or y >= self.size: continue
            for x in range(int(cx - rx - 2), int(cx + rx + 3)):
                if x < 0 or x >= self.size: continue
                dx = (x - cx) / max(0.1, rx)
                dy = (y - cy) / max(0.1, ry)
                d = math.hypot(dx, dy) - 1.0
                if d <= 0.0:
                    alpha = a_max
                elif d < 0.1:
                    alpha = a_max * max(0.0, 1.0 - d / 0.1)
                else:
                    alpha = 0.0
                if alpha > 0:
                    self.blend_pixel(x, y, r, g, b, alpha)

    def draw_rounded_rect(self, x0, y0, w, h, radius, color):
        r, g, b, a_max = color
        for y in range(int(y0) - 1, int(y0 + h) + 2):
            if y < 0 or y >= self.size: continue
            for x in range(int(x0) - 1, int(x0 + w) + 2):
                if x < 0 or x >= self.size: continue
                dx = max(abs(x - (x0 + w/2)) - (w/2 - radius), 0.0)
                dy = max(abs(y - (y0 + h/2)) - (h/2 - radius), 0.0)
                dist = math.hypot(dx, dy) - radius
                if dist <= 0.0:
                    alpha = a_max
                elif dist < 1.5:
                    alpha = a_max * max(0.0, 1.0 - dist / 1.5)
                else:
                    alpha = 0.0
                if alpha > 0:
                    self.blend_pixel(x, y, r, g, b, alpha)

    def draw_line(self, x1, y1, x2, y2, thickness, color):
        length = math.hypot(x2 - x1, y2 - y1)
        if length == 0: return
        ux = (x2 - x1) / length
        uy = (y2 - y1) / length
        steps = int(length * 2)
        for i in range(steps + 1):
            px = x1 + ux * (i / 2.0)
            py = y1 + uy * (i / 2.0)
            self.draw_circle(px, py, thickness / 2.0, color)

    def get_rgba_bytes(self):
        buf = bytearray()
        for p in self.pixels:
            r = int(max(0, min(255, round(p[0] * 255))))
            g = int(max(0, min(255, round(p[1] * 255))))
            b = int(max(0, min(255, round(p[2] * 255))))
            a = int(max(0, min(255, round(p[3] * 255))))
            buf.extend([r, g, b, a])
        return bytes(buf)

    def resize(self, new_size):
        out = Canvas(new_size)
        scale = self.size / float(new_size)
        for ny in range(new_size):
            sy = ny * scale
            sy_int = int(sy)
            for nx in range(new_size):
                sx = nx * scale
                sx_int = int(sx)
                # Sample 2x2 for clean downsampling
                r_sum = g_sum = b_sum = a_sum = 0.0
                count = 0
                for dy in range(max(1, int(math.ceil(scale)))):
                    py = min(self.size - 1, sy_int + dy)
                    for dx in range(max(1, int(math.ceil(scale)))):
                        px = min(self.size - 1, sx_int + dx)
                        idx = py * self.size + px
                        p = self.pixels[idx]
                        r_sum += p[0]
                        g_sum += p[1]
                        b_sum += p[2]
                        a_sum += p[3]
                        count += 1
                out.pixels[ny * new_size + nx] = [r_sum / count, g_sum / count, b_sum / count, a_sum / count]
        return out

def render_lady_developer(size=128):
    c = Canvas(size)
    s = size / 128.0

    # Background circle (modern purple/indigo)
    c.draw_circle(64 * s, 64 * s, 62 * s, (0.45, 0.25, 0.90, 1.0))

    # Hair bun & back hair
    c.draw_circle(64 * s, 26 * s, 15 * s, (0.12, 0.10, 0.28, 1.0))
    c.draw_ellipse(64 * s, 50 * s, 27 * s, 28 * s, (0.12, 0.10, 0.28, 1.0))

    # Neck
    c.draw_rounded_rect(58 * s, 68 * s, 12 * s, 14 * s, 3 * s, (0.98, 0.75, 0.20, 1.0))

    # Pink Shirt / Shoulders
    c.draw_ellipse(64 * s, 98 * s, 34 * s, 22 * s, (0.92, 0.28, 0.60, 1.0))

    # Face
    c.draw_ellipse(64 * s, 56 * s, 22 * s, 24 * s, (0.98, 0.80, 0.35, 1.0))

    # Front bangs
    c.draw_circle(52 * s, 38 * s, 16 * s, (0.12, 0.10, 0.28, 1.0))
    c.draw_circle(76 * s, 38 * s, 16 * s, (0.12, 0.10, 0.28, 1.0))
    c.draw_ellipse(64 * s, 34 * s, 24 * s, 10 * s, (0.12, 0.10, 0.28, 1.0))

    # Glasses
    c.draw_rounded_rect(47 * s, 50 * s, 14 * s, 11 * s, 3 * s, (0.12, 0.15, 0.25, 1.0))
    c.draw_rounded_rect(49 * s, 52 * s, 10 * s, 7 * s, 2 * s, (0.98, 0.80, 0.35, 1.0))
    c.draw_rounded_rect(67 * s, 50 * s, 14 * s, 11 * s, 3 * s, (0.12, 0.15, 0.25, 1.0))
    c.draw_rounded_rect(69 * s, 52 * s, 10 * s, 7 * s, 2 * s, (0.98, 0.80, 0.35, 1.0))
    c.draw_line(61 * s, 55 * s, 67 * s, 55 * s, 2.5 * s, (0.12, 0.15, 0.25, 1.0))

    # Eyes & Glint
    c.draw_circle(54 * s, 55.5 * s, 2.5 * s, (0.12, 0.10, 0.25, 1.0))
    c.draw_circle(74 * s, 55.5 * s, 2.5 * s, (0.12, 0.10, 0.25, 1.0))
    c.draw_circle(55 * s, 54.5 * s, 1.0 * s, (1.0, 1.0, 1.0, 1.0))
    c.draw_circle(75 * s, 54.5 * s, 1.0 * s, (1.0, 1.0, 1.0, 1.0))

    # Cheeks
    c.draw_ellipse(47 * s, 65 * s, 4 * s, 2.5 * s, (0.95, 0.45, 0.70, 0.7))
    c.draw_ellipse(81 * s, 65 * s, 4 * s, 2.5 * s, (0.95, 0.45, 0.70, 0.7))

    # Smile
    c.draw_line(58 * s, 68 * s, 64 * s, 72 * s, 2 * s, (0.60, 0.25, 0.05, 1.0))
    c.draw_line(64 * s, 72 * s, 70 * s, 68 * s, 2 * s, (0.60, 0.25, 0.05, 1.0))

    # Laptop
    c.draw_rounded_rect(34 * s, 84 * s, 60 * s, 36 * s, 4 * s, (0.85, 0.90, 0.95, 1.0))
    c.draw_rounded_rect(38 * s, 87 * s, 52 * s, 28 * s, 2 * s, (0.08, 0.10, 0.16, 1.0))

    # Code on screen: < / >
    # <
    c.draw_line(49 * s, 101 * s, 44 * s, 97 * s, 2.5 * s, (0.20, 0.75, 1.0, 1.0))
    c.draw_line(44 * s, 97 * s, 49 * s, 93 * s, 2.5 * s, (0.20, 0.75, 1.0, 1.0))
    # /
    c.draw_line(56 * s, 105 * s, 61 * s, 89 * s, 2.5 * s, (0.95, 0.25, 0.45, 1.0))
    # >
    c.draw_line(68 * s, 93 * s, 73 * s, 97 * s, 2.5 * s, (0.30, 0.85, 0.50, 1.0))
    c.draw_line(73 * s, 97 * s, 68 * s, 101 * s, 2.5 * s, (0.30, 0.85, 0.50, 1.0))

    # Laptop keyboard base
    c.draw_rounded_rect(26 * s, 118 * s, 76 * s, 8 * s, 3 * s, (0.75, 0.80, 0.88, 1.0))

    return c

def generate_favicons():
    public_dir = r"c:\Users\lenovo\Desktop\Damini\Portfolio\developerFolio\public"
    master = render_lady_developer(192)

    # 1. android-chrome-192x192.png
    png192 = create_png_bytes(192, 192, master.get_rgba_bytes())
    with open(os.path.join(public_dir, "android-chrome-192x192.png"), "wb") as f:
        f.write(png192)

    # 2. apple-touch-icon.png (180x180)
    c180 = master.resize(180)
    png180 = create_png_bytes(180, 180, c180.get_rgba_bytes())
    with open(os.path.join(public_dir, "apple-touch-icon.png"), "wb") as f:
        f.write(png180)

    # 3. favicon-32x32.png (32x32)
    c32 = master.resize(32)
    png32 = create_png_bytes(32, 32, c32.get_rgba_bytes())
    with open(os.path.join(public_dir, "favicon-32x32.png"), "wb") as f:
        f.write(png32)

    # 4. favicon-16x16.png (16x16)
    c16 = master.resize(16)
    png16 = create_png_bytes(16, 16, c16.get_rgba_bytes())
    with open(os.path.join(public_dir, "favicon-16x16.png"), "wb") as f:
        f.write(png16)

    # 5. favicon.ico containing 32x32 and 16x16 PNGs
    # ICO header: 0, 1, num_images
    ico_header = struct.pack('<HHH', 0, 1, 2)
    offset = 6 + 16 * 2
    
    # 16x16 dir entry: width, height, colors, reserved, planes, bpp, size, offset
    entry16 = struct.pack('<BBBBHHII', 16, 16, 0, 0, 1, 32, len(png16), offset)
    offset += len(png16)
    # 32x32 dir entry
    entry32 = struct.pack('<BBBBHHII', 32, 32, 0, 0, 1, 32, len(png32), offset)
    
    with open(os.path.join(public_dir, "favicon.ico"), "wb") as f:
        f.write(ico_header + entry16 + entry32 + png16 + png32)

    print("All lady developer favicons generated successfully!")

if __name__ == "__main__":
    generate_favicons()
