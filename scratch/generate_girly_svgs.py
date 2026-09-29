import os

def create_girly_svgs():
    img_dir = r"c:\Users\lenovo\Desktop\Damini\Portfolio\developerFolio\src\assets\images"
    os.makedirs(img_dir, exist_ok=True)

    # 1. girlCoding.svg - for Greeting
    girl_coding_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fdf2f8" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#ede9fe" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#e0e7ff" stop-opacity="0.7"/>
    </linearGradient>
    <linearGradient id="deskGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fda4af"/>
      <stop offset="100%" stop-color="#f43f5e"/>
    </linearGradient>
    <linearGradient id="hairGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#312e81"/>
      <stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
    <linearGradient id="hoodieGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f472b6"/>
      <stop offset="100%" stop-color="#ec4899"/>
    </linearGradient>
    <linearGradient id="screenGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="chairGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#7c3aed"/>
    </linearGradient>
  </defs>

  <!-- Ambient Backdrop Circles -->
  <circle cx="300" cy="250" r="210" fill="url(#bgGlow)"/>
  <circle cx="480" cy="140" r="35" fill="#fbcfe8" opacity="0.6"/>
  <circle cx="120" cy="160" r="25" fill="#c7d2fe" opacity="0.6"/>
  
  <!-- Floating Sparkles & Tech Stars -->
  <path d="M470 90 Q475 105 490 110 Q475 115 470 130 Q465 115 450 110 Q465 105 470 90 Z" fill="#ec4899"/>
  <path d="M140 110 Q144 122 156 126 Q144 130 140 142 Q136 130 124 126 Q136 122 140 110 Z" fill="#8b5cf6"/>
  <path d="M420 280 Q423 290 433 293 Q423 296 420 306 Q417 296 407 293 Q417 290 420 280 Z" fill="#38bdf8"/>

  <!-- Ergonomic Cute Gaming/Office Chair -->
  <rect x="230" y="160" width="140" height="200" rx="35" fill="url(#chairGrad)" opacity="0.95"/>
  <rect x="250" y="140" width="100" height="40" rx="15" fill="#c084fc"/>
  <rect x="290" y="360" width="20" height="80" fill="#64748b"/>
  <path d="M250 440 L350 440" stroke="#475569" stroke-width="8" stroke-linecap="round"/>
  <circle cx="250" cy="445" r="8" fill="#334155"/>
  <circle cx="350" cy="445" r="8" fill="#334155"/>

  <!-- Girl Coder Body & Hoodie -->
  <path d="M245 280 Q300 250 355 280 L370 380 L230 380 Z" fill="url(#hoodieGrad)"/>
  <!-- Hoodie Strings -->
  <line x1="285" y1="285" x2="285" y2="330" stroke="#fdf2f8" stroke-width="3" stroke-linecap="round"/>
  <line x1="315" y1="285" x2="315" y2="330" stroke="#fdf2f8" stroke-width="3" stroke-linecap="round"/>

  <!-- Head & Hair (Bun + Cute Ponytail + Bangs) -->
  <circle cx="300" cy="140" r="32" fill="url(#hairGrad)"/>
  <ellipse cx="300" cy="210" rx="42" ry="46" fill="url(#hairGrad)"/>
  <!-- Bun scrunchie in pink -->
  <circle cx="300" cy="140" r="16" fill="#f43f5e"/>

  <!-- Girl Face -->
  <ellipse cx="300" cy="220" rx="34" ry="36" fill="#fcd34d"/>
  
  <!-- Headphones in cute pastel purple -->
  <path d="M256 220 A44 44 0 0 1 344 220" stroke="#a855f7" stroke-width="8" fill="none" stroke-linecap="round"/>
  <rect x="252" y="205" width="12" height="28" rx="6" fill="#ec4899"/>
  <rect x="336" y="205" width="12" height="28" rx="6" fill="#ec4899"/>

  <!-- Hair Bangs framing face -->
  <path d="M266 200 C275 175 325 175 334 200 C320 190 310 185 300 188 C290 185 280 190 266 200 Z" fill="url(#hairGrad)"/>
  <path d="M266 200 Q272 230 268 245 Q262 225 266 200 Z" fill="url(#hairGrad)"/>
  <path d="M334 200 Q328 230 332 245 Q338 225 334 200 Z" fill="url(#hairGrad)"/>

  <!-- Eyebrows -->
  <path d="M278 206 Q286 202 292 206" stroke="#1e1b4b" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <path d="M308 206 Q314 202 322 206" stroke="#1e1b4b" stroke-width="2.5" fill="none" stroke-linecap="round"/>

  <!-- Cute Glasses -->
  <rect x="274" y="210" width="20" height="16" rx="5" fill="none" stroke="#312e81" stroke-width="3"/>
  <rect x="306" y="210" width="20" height="16" rx="5" fill="none" stroke="#312e81" stroke-width="3"/>
  <line x1="294" y1="218" x2="306" y2="218" stroke="#312e81" stroke-width="3"/>

  <!-- Eyes behind glasses -->
  <circle cx="284" cy="218" r="3.5" fill="#1e1b4b"/>
  <circle cx="316" cy="218" r="3.5" fill="#1e1b4b"/>
  <circle cx="285.5" cy="216.5" r="1.2" fill="#ffffff"/>
  <circle cx="317.5" cy="216.5" r="1.2" fill="#ffffff"/>

  <!-- Blush Cheeks -->
  <ellipse cx="274" cy="232" rx="5" ry="3" fill="#f43f5e" opacity="0.65"/>
  <ellipse cx="326" cy="232" rx="5" ry="3" fill="#f43f5e" opacity="0.65"/>

  <!-- Sweet Smile -->
  <path d="M292 236 Q300 243 308 236" stroke="#b45309" stroke-width="2.5" fill="none" stroke-linecap="round"/>

  <!-- Modern Desk in Pastel Rose/Coral -->
  <rect x="80" y="370" width="440" height="14" rx="7" fill="url(#deskGrad)"/>
  <rect x="110" y="384" width="16" height="90" rx="6" fill="#cbd5e1"/>
  <rect x="474" y="384" width="16" height="90" rx="6" fill="#cbd5e1"/>

  <!-- Modern Laptop on Desk -->
  <rect x="220" y="310" width="160" height="100" rx="8" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2"/>
  <rect x="228" y="316" width="144" height="84" rx="4" fill="url(#screenGrad)"/>
  <path d="M190" y="410" d="M190 410 L410 410 L395 422 L205 422 Z" fill="#cbd5e1"/>

  <!-- Code Syntax on Laptop Screen: React & Python -->
  <text x="238" y="336" fill="#38bdf8" font-family="monospace" font-size="11" font-weight="bold">&lt;Damini /&gt;</text>
  <text x="238" y="354" fill="#a78bfa" font-family="monospace" font-size="10">const app = () =&gt;</text>
  <text x="238" y="372" fill="#34d399" font-family="monospace" font-size="10">def solve_ai():</text>
  <text x="238" y="390" fill="#fbbf24" font-family="monospace" font-size="10">  return "Success ✨"</text>

  <!-- Laptop Back Apple/Heart Logo Sticker -->
  <circle cx="300" cy="358" r="8" fill="#f43f5e" opacity="0.2"/>

  <!-- Cute Coffee Mug with Steam on Desk -->
  <rect x="420" y="342" width="28" height="30" rx="5" fill="#fda4af"/>
  <path d="M448 350 Q456 357 448 364" stroke="#fda4af" stroke-width="3" fill="none"/>
  <!-- Heart on mug -->
  <path d="M434 353 C434 350, 431 349, 430 351 C429 349, 426 350, 426 353 C426 356, 430 359, 430 360 C430 359, 434 356, 434 353 Z" fill="#e11d48"/>
  <!-- Steam curls -->
  <path d="M428 334 Q432 328 428 322" stroke="#fda4af" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M436 332 Q440 326 436 320" stroke="#fda4af" stroke-width="2" fill="none" stroke-linecap="round"/>

  <!-- Potted Plant on Desk (Cute Succulent) -->
  <path d="M140 370 L160 370 L156 350 L144 350 Z" fill="#fb923c"/>
  <circle cx="150" cy="342" r="10" fill="#34d399"/>
  <circle cx="144" cy="346" r="8" fill="#10b981"/>
  <circle cx="156" cy="346" r="8" fill="#059669"/>
</svg>'''
    with open(os.path.join(img_dir, "girlCoding.svg"), "w", encoding="utf-8") as f:
        f.write(girl_coding_svg)

    # 2. girlDeveloper.svg - for Skills
    girl_developer_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 500" width="100%" height="100%">
  <defs>
    <linearGradient id="skillsBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fae8ff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#ede9fe" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#fce7f3" stop-opacity="0.7"/>
    </linearGradient>
    <linearGradient id="girlOutfit" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#6366f1"/>
    </linearGradient>
    <linearGradient id="hairDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2e1065"/>
      <stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
  </defs>

  <!-- Ambient Backdrop -->
  <circle cx="300" cy="250" r="220" fill="url(#skillsBg)"/>

  <!-- Floating Tech Screens & Code Windows -->
  <!-- Screen 1: React & UI -->
  <rect x="60" y="80" width="170" height="115" rx="12" fill="#ffffff" stroke="#c084fc" stroke-width="2" filter="drop-shadow(0 8px 16px rgba(168,85,247,0.15))"/>
  <rect x="60" y="80" width="170" height="24" rx="12" fill="#f3e8ff"/>
  <circle cx="76" cy="92" r="4" fill="#f43f5e"/>
  <circle cx="88" cy="92" r="4" fill="#fbbf24"/>
  <circle cx="100" cy="92" r="4" fill="#34d399"/>
  <!-- Code lines -->
  <rect x="75" y="116" width="70" height="6" rx="3" fill="#61dafb"/>
  <rect x="75" y="130" width="110" height="6" rx="3" fill="#a855f7"/>
  <rect x="75" y="144" width="90" height="6" rx="3" fill="#ec4899"/>
  <rect x="75" y="158" width="50" height="6" rx="3" fill="#38bdf8"/>
  <circle cx="195" cy="155" r="16" fill="#eff6ff"/>
  <text x="195" y="160" font-size="14" text-anchor="middle" fill="#0284c7">⚛</text>

  <!-- Screen 2: Python, Backend & AI -->
  <rect x="370" y="70" width="170" height="120" rx="12" fill="#ffffff" stroke="#818cf8" stroke-width="2" filter="drop-shadow(0 8px 16px rgba(99,102,241,0.15))"/>
  <rect x="370" y="70" width="170" height="24" rx="12" fill="#e0e7ff"/>
  <circle cx="386" cy="82" r="4" fill="#f43f5e"/>
  <circle cx="398" cy="82" r="4" fill="#fbbf24"/>
  <circle cx="410" cy="82" r="4" fill="#34d399"/>
  <rect x="385" y="106" width="85" height="6" rx="3" fill="#3b82f6"/>
  <rect x="385" y="120" width="120" height="6" rx="3" fill="#10b981"/>
  <rect x="385" y="134" width="75" height="6" rx="3" fill="#f59e0b"/>
  <rect x="385" y="148" width="105" height="6" rx="3" fill="#8b5cf6"/>
  <!-- Python & AI Badge -->
  <circle cx="505" cy="150" r="16" fill="#fef3c7"/>
  <text x="505" y="155" font-size="12" text-anchor="middle" fill="#d97706">🐍</text>

  <!-- Floating Tech Orbs -->
  <g transform="translate(80, 240)">
    <circle cx="20" cy="20" r="22" fill="#ffffff" stroke="#f472b6" stroke-width="2"/>
    <text x="20" y="26" font-size="18" text-anchor="middle">⚡</text>
  </g>
  <g transform="translate(480, 230)">
    <circle cx="20" cy="20" r="24" fill="#ffffff" stroke="#38bdf8" stroke-width="2"/>
    <text x="20" y="26" font-size="16" text-anchor="middle">☁️</text>
  </g>
  <g transform="translate(390, 270)">
    <circle cx="18" cy="18" r="20" fill="#ffffff" stroke="#34d399" stroke-width="2"/>
    <text x="18" y="24" font-size="14" text-anchor="middle">🤖</text>
  </g>
  <g transform="translate(160, 270)">
    <circle cx="18" cy="18" r="20" fill="#ffffff" stroke="#c084fc" stroke-width="2"/>
    <text x="18" y="24" font-size="14" text-anchor="middle">&lt;&gt;</text>
  </g>

  <!-- Central Girl Developer (Creative, Confident & Tech Savvy) -->
  <!-- Long Flowing Hair with Highlights -->
  <path d="M250 200 C230 290 240 370 250 420 C280 430 320 430 350 420 C360 370 370 290 350 200 Z" fill="url(#hairDark)"/>

  <!-- Girl Torso / Jumper -->
  <path d="M260 270 Q300 250 340 270 L360 440 L240 440 Z" fill="url(#girlOutfit)"/>
  <!-- Chic belt / detail -->
  <rect x="250" y="380" width="100" height="10" rx="5" fill="#f472b6"/>

  <!-- Head -->
  <ellipse cx="300" cy="200" rx="36" ry="40" fill="#fcd34d"/>

  <!-- Front Hair Style (Cute wavy layers) -->
  <path d="M264 190 C274 150 326 150 336 190 C320 175 310 170 300 173 C290 170 280 175 264 190 Z" fill="url(#hairDark)"/>
  <path d="M264 190 Q270 240 262 270 Q254 230 264 190 Z" fill="url(#hairDark)"/>
  <path d="M336 190 Q330 240 338 270 Q346 230 336 190 Z" fill="url(#hairDark)"/>

  <!-- Glasses -->
  <rect x="274" y="190" width="22" height="17" rx="5" fill="none" stroke="#312e81" stroke-width="2.8"/>
  <rect x="304" y="190" width="22" height="17" rx="5" fill="none" stroke="#312e81" stroke-width="2.8"/>
  <line x1="296" y1="198" x2="304" y2="198" stroke="#312e81" stroke-width="2.8"/>

  <!-- Eyes -->
  <circle cx="285" cy="198" r="3.5" fill="#1e1b4b"/>
  <circle cx="315" cy="198" r="3.5" fill="#1e1b4b"/>
  <circle cx="286.5" cy="196.5" r="1.2" fill="#ffffff"/>
  <circle cx="316.5" cy="196.5" r="1.2" fill="#ffffff"/>

  <!-- Blush -->
  <ellipse cx="274" cy="214" rx="6" ry="3.5" fill="#f43f5e" opacity="0.7"/>
  <ellipse cx="326" cy="214" rx="6" ry="3.5" fill="#f43f5e" opacity="0.7"/>

  <!-- Smile -->
  <path d="M292 220 Q300 228 308 220" stroke="#b45309" stroke-width="2.5" fill="none" stroke-linecap="round"/>

  <!-- Tablet / Laptop Held in Hand -->
  <rect x="250" y="300" width="100" height="70" rx="8" fill="#f8fafc" stroke="#c084fc" stroke-width="2"/>
  <rect x="256" y="306" width="88" height="54" rx="4" fill="#0f172a"/>
  <!-- Glow code on tablet -->
  <path d="M275 328 L268 333 L275 338" stroke="#38bdf8" stroke-width="2" fill="none"/>
  <line x1="282" y1="340" x2="288" y2="326" stroke="#ec4899" stroke-width="2"/>
  <path d="M295 328 L302 333 L295 338" stroke="#34d399" stroke-width="2" fill="none"/>
</svg>'''
    with open(os.path.join(img_dir, "girlDeveloper.svg"), "w", encoding="utf-8") as f:
        f.write(girl_developer_svg)

    # 3. girlContact.svg - for Contact
    girl_contact_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 500" width="100%" height="100%">
  <defs>
    <linearGradient id="contactBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fdf4ff" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#fce7f3" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#ede9fe" stop-opacity="0.9"/>
    </linearGradient>
    <linearGradient id="envelopeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f472b6"/>
      <stop offset="100%" stop-color="#e11d48"/>
    </linearGradient>
  </defs>

  <circle cx="300" cy="250" r="215" fill="url(#contactBg)"/>

  <!-- Floating Mail & Notification Bubbles -->
  <!-- Big Friendly Envelope -->
  <g transform="translate(100, 100)">
    <rect x="0" y="0" width="150" height="100" rx="14" fill="#ffffff" stroke="#f43f5e" stroke-width="2" filter="drop-shadow(0 10px 20px rgba(244,63,94,0.18))"/>
    <path d="M0 0 L75 55 L150 0" stroke="#f43f5e" stroke-width="2" fill="none"/>
    <circle cx="75" cy="55" r="14" fill="#f43f5e"/>
    <path d="M70 55 L74 59 L81 51" stroke="#ffffff" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  </g>

  <!-- Floating Paper Plane -->
  <path d="M430 90 L490 120 L445 135 L430 90 Z" fill="#c084fc"/>
  <path d="M445 135 L465 110" stroke="#7c3aed" stroke-width="1.5"/>
  <path d="M410 110 Q380 120 400 150 Q420 180 440 145" stroke="#e879f9" stroke-width="2" stroke-dasharray="4,4" fill="none"/>

  <!-- Floating Heart & Chat Bubbles -->
  <g transform="translate(420, 220)">
    <circle cx="26" cy="26" r="26" fill="#f43f5e" filter="drop-shadow(0 6px 14px rgba(244,63,94,0.3))"/>
    <path d="M26 36 C26 36, 14 28, 14 20 C14 15, 18 13, 21 15 C24 17, 26 20, 26 20 C26 20, 28 17, 31 15 C34 13, 38 15, 38 20 C38 28, 26 36, 26 36 Z" fill="#ffffff"/>
  </g>

  <!-- Girl Standing Waving with Phone -->
  <!-- Hair (High chic ponytail) -->
  <ellipse cx="290" cy="180" rx="42" ry="44" fill="#1e1b4b"/>
  <circle cx="340" cy="150" r="26" fill="#1e1b4b"/>
  <path d="M340 150 Q380 190 370 240 Q350 200 340 150 Z" fill="#1e1b4b"/>
  <!-- Hair scrunchie -->
  <circle cx="335" cy="155" r="10" fill="#f43f5e"/>

  <!-- Dress / Outfit in stylish rose & violet -->
  <path d="M255 250 Q290 230 325 250 L345 430 L235 430 Z" fill="url(#envelopeGrad)"/>

  <!-- Face -->
  <ellipse cx="290" cy="190" rx="34" ry="38" fill="#fcd34d"/>

  <!-- Eyebrows -->
  <path d="M272 178 Q280 174 286 178" stroke="#1e1b4b" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <path d="M298 178 Q304 174 310 178" stroke="#1e1b4b" stroke-width="2.5" fill="none" stroke-linecap="round"/>

  <!-- Glasses -->
  <rect x="268" y="180" width="18" height="15" rx="4" fill="none" stroke="#312e81" stroke-width="2.5"/>
  <rect x="296" y="180" width="18" height="15" rx="4" fill="none" stroke="#312e81" stroke-width="2.5"/>
  <line x1="286" y1="187" x2="296" y2="187" stroke="#312e81" stroke-width="2.5"/>

  <!-- Eyes -->
  <circle cx="277" cy="187" r="3" fill="#1e1b4b"/>
  <circle cx="305" cy="187" r="3" fill="#1e1b4b"/>
  <circle cx="278" cy="185.5" r="1" fill="#ffffff"/>
  <circle cx="306" cy="185.5" r="1" fill="#ffffff"/>

  <!-- Smile & Blush -->
  <ellipse cx="270" cy="204" rx="5" ry="3" fill="#f43f5e" opacity="0.65"/>
  <ellipse cx="314" cy="204" rx="5" ry="3" fill="#f43f5e" opacity="0.65"/>
  <path d="M284 210 Q292 218 300 210" stroke="#b45309" stroke-width="2.5" fill="none" stroke-linecap="round"/>

  <!-- Arm Waving Hello -->
  <path d="M320 260 Q365 240 375 190" stroke="#fcd34d" stroke-width="14" stroke-linecap="round" fill="none"/>
  <circle cx="375" cy="185" r="9" fill="#fcd34d"/>
  <!-- Sparkles near hand -->
  <path d="M390 165 Q395 175 405 180 Q395 185 390 195 Q385 185 375 180 Q385 175 390 165 Z" fill="#fbbf24"/>

  <!-- Other Hand Holding Smartphone -->
  <rect x="210" y="275" width="28" height="50" rx="5" fill="#1e293b"/>
  <rect x="213" y="280" width="22" height="38" rx="2" fill="#38bdf8"/>
  <path d="M235 295 L224 295" stroke="#fcd34d" stroke-width="8" stroke-linecap="round"/>
</svg>'''
    with open(os.path.join(img_dir, "girlContact.svg"), "w", encoding="utf-8") as f:
        f.write(girl_contact_svg)

    print("All 3 girly SVG illustrations created successfully!")

if __name__ == "__main__":
    create_girly_svgs()
