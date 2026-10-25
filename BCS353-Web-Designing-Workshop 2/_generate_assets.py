# Generates all SVG assets (logo, book covers, background patterns) for the project.
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

BOOKS = [
    # (file, title line 1, title line 2, footer, color, light color)
    ("xml-bible.svg",        "XML",            "Bible",            "WILEY",            "#2b6cb0", "#bee3f8"),
    ("java2.svg",            "JAVA 2",         "Complete Ref.",    "BPB PUBLICATIONS", "#c05621", "#feebc8"),
    ("html24.svg",           "HTML",           "in 24 Hours",      "SAM PUBLICATION",  "#2f855a", "#c6f6d5"),
    ("ai.svg",               "ARTIFICIAL",     "INTELLIGENCE",     "PRINCETON HALL",   "#6b46c1", "#e9d8fd"),
    ("digital-electronics.svg","DIGITAL",      "ELECTRONICS",      "MCGRAW HILL",      "#b83280", "#fed7e5"),
    ("signals.svg",          "SIGNALS &",      "SYSTEMS",          "OXFORD",           "#2c7a7b", "#b2f5ea"),
    ("electric-machines.svg","ELECTRIC",       "MACHINES",         "PEARSON",          "#c53030", "#fed7d7"),
    ("power-systems.svg",    "POWER",          "SYSTEMS",          "CAMBRIDGE",        "#975a16", "#faf089"),
    ("structural.svg",       "STRUCTURAL",     "ANALYSIS",         "TATA MCGRAW HILL", "#4a5568", "#e2e8f0"),
    ("geotechnical.svg",     "GEOTECHNICAL",   "ENGINEERING",      "ELSEVIER",         "#38a169", "#c6f6d5"),
]

COVER_TMPL = """<svg xmlns="http://www.w3.org/2000/svg" width="130" height="170" viewBox="0 0 130 170">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{color}"/>
      <stop offset="1" stop-color="{dark}"/>
    </linearGradient>
  </defs>
  <rect width="130" height="170" rx="7" fill="url(#g)"/>
  <rect x="7" y="7" width="116" height="156" rx="3" fill="none" stroke="#ffffff" stroke-opacity="0.55" stroke-width="1.5"/>
  <rect x="0" y="0" width="14" height="170" rx="4" fill="#00000022"/>
  <text x="72" y="66" text-anchor="middle" font-family="Georgia, serif" font-size="15" fill="#ffffff" font-weight="bold">{t1}</text>
  <text x="72" y="88" text-anchor="middle" font-family="Georgia, serif" font-size="12" fill="#ffffff">{t2}</text>
  <line x1="30" y1="104" x2="114" y2="104" stroke="#ffffff" stroke-opacity="0.5"/>
  <text x="72" y="150" text-anchor="middle" font-family="Arial, sans-serif" font-size="8.5" fill="{light}" font-weight="bold">{footer}</text>
</svg>
"""

LOGO_TMPL = """<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
  <circle cx="32" cy="32" r="30" fill="#1f3a5f"/>
  <path d="M32 16 C26 12 18 12 12 15 L12 44 C18 41 26 41 32 45 C38 41 46 41 52 44 L52 15 C46 12 38 12 32 16 Z" fill="#f4a261"/>
  <path d="M32 16 L32 45" stroke="#1f3a5f" stroke-width="1.6"/>
  <path d="M18 22 L27 21 M18 27 L27 26 M46 22 L37 21 M46 27 L37 26" stroke="#1f3a5f" stroke-width="1.4" stroke-linecap="round"/>
</svg>
"""

PATTERN_TMPL = """<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">
  <rect width="48" height="48" fill="{bg}"/>
  <circle cx="12" cy="12" r="4" fill="{fg}" fill-opacity="0.55"/>
  <circle cx="36" cy="36" r="4" fill="{fg}" fill-opacity="0.55"/>
  <path d="M0 24 L24 0 M24 48 L48 24" stroke="{fg}" stroke-opacity="0.25" stroke-width="2"/>
</svg>
"""

def esc(text):
    """Escape XML special characters so titles like 'Signals & Systems' stay valid SVG."""
    return (str(text).replace("&", "&amp;").replace("<", "&lt;")
                    .replace(">", "&gt;").replace('"', "&quot;"))

def darken(hexcolor, factor=0.72):
    h = hexcolor.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return "#%02x%02x%02x" % (int(r * factor), int(g * factor), int(b * factor))

target_dirs = [
    "Exp01_Homepage_Frames/images",
    "Exp03_Catalogue_Page/images",
]

for d in target_dirs:
    full = os.path.join(ROOT, d)
    for fname, t1, t2, footer, color, light in BOOKS:
        with open(os.path.join(full, fname), "w") as f:
            f.write(COVER_TMPL.format(color=color, dark=darken(color), light=light,
                                      t1=esc(t1), t2=esc(t2), footer=esc(footer)))
    with open(os.path.join(full, "logo.svg"), "w") as f:
        f.write(LOGO_TMPL)

# Background pattern assets for Exp08 & Exp09
for d, bg, fg in [
    ("Exp08_CSS_Fonts_Background/images", "#eaf2fb", "#9ec5e8"),
    ("Exp09_CSS_Repeat_Links/images",     "#fff6ec", "#f0b27a"),
]:
    full = os.path.join(ROOT, d)
    with open(os.path.join(full, "pattern.svg"), "w") as f:
        f.write(PATTERN_TMPL.format(bg=bg, fg=fg))
    with open(os.path.join(full, "logo.svg"), "w") as f:
        f.write(LOGO_TMPL)

print("Assets generated:")
for d, _, files in os.walk(ROOT):
    for fn in sorted(files):
        if fn.endswith(".svg"):
            print(os.path.relpath(os.path.join(d, fn), ROOT))
