import struct
import zlib
import math
import os

def create_png(filename, width, height, rgba_buffer):
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
    png_data = (
        b'\x89PNG\r\n\x1a\n'
        + chunk(b'IHDR', ihdr)
        + chunk(b'IDAT', compressed)
        + chunk(b'IEND', b'')
    )
    with open(filename, 'wb') as f:
        f.write(png_data)

class Canvas:
    def __init__(self, size=256):
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

    def draw_rounded_rect(self, x0, y0, w, h, radius, grad_top, grad_bot):
        # grad_top, grad_bot are (r, g, b) in [0..1]
        for y in range(int(y0) - 1, int(y0 + h) + 2):
            if y < 0 or y >= self.size: continue
            t = (y - y0) / max(1.0, h)
            t = max(0.0, min(1.0, t))
            r = grad_top[0] * (1 - t) + grad_bot[0] * t
            g = grad_top[1] * (1 - t) + grad_bot[1] * t
            b = grad_top[2] * (1 - t) + grad_bot[2] * t

            for x in range(int(x0) - 1, int(x0 + w) + 2):
                if x < 0 or x >= self.size: continue
                # Compute signed distance to rounded box
                dx = max(abs(x - (x0 + w/2)) - (w/2 - radius), 0.0)
                dy = max(abs(y - (y0 + h/2)) - (h/2 - radius), 0.0)
                dist = math.hypot(dx, dy) - radius
                if dist <= 0.0:
                    alpha = 1.0
                elif dist < 1.5:
                    alpha = max(0.0, 1.0 - dist / 1.5)
                else:
                    alpha = 0.0

                if alpha > 0:
                    self.blend_pixel(x, y, r, g, b, alpha)

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

    def draw_rect(self, x0, y0, w, h, color):
        r, g, b, a = color
        for y in range(int(y0), int(y0 + h)):
            if y < 0 or y >= self.size: continue
            for x in range(int(x0), int(x0 + w)):
                if x < 0 or x >= self.size: continue
                self.blend_pixel(x, y, r, g, b, a)

    def draw_line(self, x1, y1, x2, y2, thickness, color):
        r, g, b, a = color
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

def generate_all_logos():
    out_dir = r"c:\Users\lenovo\Desktop\Damini\Portfolio\developerFolio\src\assets\images"
    os.makedirs(out_dir, exist_ok=True)

    # 1. Techugo Logo
    c = Canvas(256)
    # Background rounded rect with rich dark violet/indigo gradient
    c.draw_rounded_rect(16, 16, 224, 224, 48, (0.12, 0.15, 0.45), (0.28, 0.10, 0.55))
    # Techugo Stylized 'T' with cyan accent
    c.draw_rounded_rect(58, 64, 140, 28, 10, (1.0, 1.0, 1.0), (0.9, 0.95, 1.0))
    c.draw_rounded_rect(114, 88, 28, 104, 8, (1.0, 1.0, 1.0), (0.85, 0.9, 1.0))
    # Futuristic cyan accent dot/slash
    c.draw_circle(180, 78, 12, (0.1, 0.85, 0.95, 1.0))
    create_png(os.path.join(out_dir, "techugoLogo.png"), 256, 256, c.get_rgba_bytes())

    # 2. Indiana Commerce Logo
    c = Canvas(256)
    # Background rounded rect with modern emerald / deep teal gradient
    c.draw_rounded_rect(16, 16, 224, 224, 48, (0.05, 0.35, 0.35), (0.02, 0.20, 0.25))
    # 'I' pillar
    c.draw_rounded_rect(68, 68, 24, 120, 8, (1.0, 1.0, 1.0), (0.9, 1.0, 0.95))
    # 'C' arc
    c.draw_rounded_rect(106, 68, 82, 24, 8, (0.2, 0.9, 0.7), (0.2, 0.9, 0.7))
    c.draw_rounded_rect(106, 92, 24, 72, 6, (0.2, 0.9, 0.7), (0.2, 0.9, 0.7))
    c.draw_rounded_rect(106, 164, 82, 24, 8, (0.2, 0.9, 0.7), (0.2, 0.9, 0.7))
    # Commerce sparkle
    c.draw_circle(170, 128, 10, (1.0, 0.8, 0.2, 1.0))
    create_png(os.path.join(out_dir, "indianaLogo.png"), 256, 256, c.get_rgba_bytes())

    # 3. Iotas Solutions Logo
    c = Canvas(256)
    # Background rounded rect with deep cobalt / sapphire gradient
    c.draw_rounded_rect(16, 16, 224, 224, 48, (0.08, 0.28, 0.65), (0.04, 0.14, 0.40))
    # 'i' dot and stem
    c.draw_circle(85, 80, 14, (0.3, 0.8, 1.0, 1.0))
    c.draw_rounded_rect(73, 106, 24, 82, 8, (1.0, 1.0, 1.0), (0.85, 0.95, 1.0))
    # 'S' sleek curve lines
    c.draw_rounded_rect(115, 80, 68, 22, 7, (0.3, 0.8, 1.0), (0.3, 0.8, 1.0))
    c.draw_rounded_rect(115, 102, 22, 34, 6, (0.3, 0.8, 1.0), (0.3, 0.8, 1.0))
    c.draw_rounded_rect(115, 136, 68, 22, 7, (1.0, 1.0, 1.0), (1.0, 1.0, 1.0))
    c.draw_rounded_rect(161, 158, 22, 30, 6, (1.0, 1.0, 1.0), (1.0, 1.0, 1.0))
    c.draw_rounded_rect(115, 188, 68, 22, 7, (1.0, 1.0, 1.0), (1.0, 1.0, 1.0))
    create_png(os.path.join(out_dir, "iotasLogo.png"), 256, 256, c.get_rgba_bytes())

    # 4. Newton School Logo
    c = Canvas(256)
    # Background rounded rect with fiery orange / crimson gradient
    c.draw_rounded_rect(16, 16, 224, 224, 48, (0.95, 0.35, 0.10), (0.80, 0.15, 0.15))
    # Newton 'N'
    c.draw_rounded_rect(65, 65, 24, 126, 8, (1.0, 1.0, 1.0), (1.0, 1.0, 1.0))
    c.draw_rounded_rect(167, 65, 24, 126, 8, (1.0, 1.0, 1.0), (1.0, 1.0, 1.0))
    # Diagonal of N
    c.draw_line(77, 75, 179, 181, 24, (1.0, 1.0, 1.0, 1.0))
    create_png(os.path.join(out_dir, "newtonLogo.png"), 256, 256, c.get_rgba_bytes())

    # 5. Aryabhatta Knowledge University (AKU) Logo
    c = Canvas(256)
    # Background rounded rect with dignified academic royal navy / gold crest colors
    c.draw_rounded_rect(16, 16, 224, 224, 48, (0.10, 0.18, 0.40), (0.05, 0.08, 0.22))
    # University graduation cap icon
    # Cap diamond
    for i in range(48):
        c.draw_line(128 - i * 1.5, 95 + i * 0.7, 128 + i * 1.5, 95 + i * 0.7, 2, (0.95, 0.78, 0.25, 1.0))
    for i in range(25):
        c.draw_line(128 - 72 + i * 1.5, 128 + i * 0.7, 128 + 72 - i * 1.5, 128 + i * 0.7, 2, (0.85, 0.68, 0.20, 1.0))
    # Cap base & tassel
    c.draw_rounded_rect(88, 142, 80, 20, 6, (0.95, 0.82, 0.35), (0.85, 0.68, 0.20))
    c.draw_line(128, 110, 185, 130, 4, (1.0, 1.0, 1.0, 1.0))
    c.draw_circle(185, 145, 8, (1.0, 1.0, 1.0, 1.0))
    # Pillars under cap
    c.draw_rounded_rect(84, 170, 88, 14, 4, (1.0, 1.0, 1.0), (1.0, 1.0, 1.0))
    create_png(os.path.join(out_dir, "akuLogo.png"), 256, 256, c.get_rgba_bytes())

    # 6. Autaras Project Logo (Vehicle Mobility)
    c = Canvas(256)
    c.draw_rounded_rect(16, 16, 224, 224, 48, (0.15, 0.35, 0.85), (0.08, 0.18, 0.55))
    # Car silhouette / mobility symbol
    # Roof
    c.draw_rounded_rect(80, 85, 96, 35, 12, (1.0, 1.0, 1.0), (1.0, 1.0, 1.0))
    # Body
    c.draw_rounded_rect(52, 115, 152, 45, 14, (0.35, 0.85, 1.0), (0.2, 0.7, 0.95))
    # Wheels
    c.draw_circle(85, 165, 20, (0.05, 0.1, 0.2, 1.0))
    c.draw_circle(85, 165, 10, (1.0, 1.0, 1.0, 1.0))
    c.draw_circle(171, 165, 20, (0.05, 0.1, 0.2, 1.0))
    c.draw_circle(171, 165, 10, (1.0, 1.0, 1.0, 1.0))
    create_png(os.path.join(out_dir, "autarasLogo.png"), 256, 256, c.get_rgba_bytes())

    # 7. Unigoal Project Logo (Career Counselling)
    c = Canvas(256)
    c.draw_rounded_rect(16, 16, 224, 224, 48, (0.45, 0.18, 0.75), (0.25, 0.08, 0.50))
    # Concentric target / compass / goal circles
    c.draw_circle(128, 128, 64, (0.9, 0.8, 1.0, 0.25))
    c.draw_circle(128, 128, 46, (0.9, 0.8, 1.0, 0.45))
    c.draw_circle(128, 128, 28, (1.0, 0.85, 0.2, 1.0))
    c.draw_circle(128, 128, 12, (1.0, 1.0, 1.0, 1.0))
    # Target crosshairs
    c.draw_line(128, 52, 128, 80, 6, (1.0, 1.0, 1.0, 0.8))
    c.draw_line(128, 176, 128, 204, 6, (1.0, 1.0, 1.0, 0.8))
    c.draw_line(52, 128, 80, 128, 6, (1.0, 1.0, 1.0, 0.8))
    c.draw_line(176, 128, 204, 128, 6, (1.0, 1.0, 1.0, 0.8))
    create_png(os.path.join(out_dir, "unigoalLogo.png"), 256, 256, c.get_rgba_bytes())

    # 8. UCAAS Project Logo (Communication & Messaging)
    c = Canvas(256)
    c.draw_rounded_rect(16, 16, 224, 224, 48, (0.05, 0.65, 0.55), (0.02, 0.40, 0.35))
    # Primary Speech bubble
    c.draw_rounded_rect(60, 68, 110, 78, 24, (1.0, 1.0, 1.0), (1.0, 1.0, 1.0))
    # Bubble tail
    for i in range(20):
        c.draw_line(80 + i, 144, 70, 165, 2, (1.0, 1.0, 1.0, 1.0))
    # Secondary chat bubble
    c.draw_rounded_rect(110, 110, 86, 62, 18, (0.2, 0.85, 0.75), (0.2, 0.85, 0.75))
    for i in range(16):
        c.draw_line(160 + i, 170, 180, 188, 2, (0.2, 0.85, 0.75, 1.0))
    create_png(os.path.join(out_dir, "ucaasLogo.png"), 256, 256, c.get_rgba_bytes())

    # 9. GOTRUST Project Logo (DSR & Privacy)
    c = Canvas(256)
    c.draw_rounded_rect(16, 16, 224, 224, 48, (0.10, 0.22, 0.45), (0.05, 0.12, 0.30))
    # Security Shield
    # Upper shield
    c.draw_rounded_rect(76, 65, 104, 55, 10, (0.2, 0.75, 0.95), (0.2, 0.75, 0.95))
    # Lower shield pointed
    for y in range(120, 185):
        w = int(52 * (1.0 - (y - 120) / 65.0))
        c.draw_line(128 - w, y, 128 + w, y, 2, (0.2, 0.75, 0.95, 1.0))
    # Shield inner checkmark
    c.draw_line(105, 120, 122, 140, 8, (1.0, 1.0, 1.0, 1.0))
    c.draw_line(122, 140, 155, 95, 8, (1.0, 1.0, 1.0, 1.0))
    create_png(os.path.join(out_dir, "gotrustLogo.png"), 256, 256, c.get_rgba_bytes())

    # 10. LeetCode Achievement Logo
    c = Canvas(256)
    c.draw_rounded_rect(16, 16, 224, 224, 48, (0.15, 0.15, 0.18), (0.08, 0.08, 0.10))
    # LeetCode yellow-orange curly bracket / hook
    # Top bar
    c.draw_rounded_rect(95, 68, 70, 20, 8, (1.0, 0.65, 0.10), (1.0, 0.65, 0.10))
    # Diagonal slash
    c.draw_line(95, 78, 75, 128, 20, (1.0, 0.65, 0.10, 1.0))
    # Bottom diagonal and bar
    c.draw_line(75, 128, 95, 178, 20, (1.0, 0.65, 0.10, 1.0))
    c.draw_rounded_rect(95, 168, 70, 20, 8, (1.0, 0.65, 0.10), (1.0, 0.65, 0.10))
    # Middle line
    c.draw_rounded_rect(105, 122, 75, 14, 6, (0.9, 0.9, 0.95), (0.9, 0.9, 0.95))
    create_png(os.path.join(out_dir, "leetcodeLogo.png"), 256, 256, c.get_rgba_bytes())

    print("All logos generated successfully!")

if __name__ == "__main__":
    generate_all_logos()
