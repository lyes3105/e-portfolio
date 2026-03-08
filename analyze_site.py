import re
import os

html_path = r"c:\Users\Lyes\Documents\e-portfolio\index.html"
base_dir = r"c:\Users\Lyes\Documents\e-portfolio"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Find all img src
images = re.findall(r'<img [^>]*src="([^"]+)"', html)
# Find all style background images
bg_images = re.findall(r'url\((["\']?)([^)]+)\1\)', html)

print("--- ANALYSE DES IMAGES ---")
for img in images:
    if img.startswith('http'):
        print(f"[EXTERNE] {img}")
    else:
        full_path = os.path.join(base_dir, img.replace('/', os.sep))
        exists = os.path.exists(full_path)
        status = "OK" if exists else "!!! MANQUANT !!!"
        print(f"[LOCAL] {img} -> {status}")

for quote, img in bg_images:
    if img.startswith('http'):
        print(f"[EXTERNE BG] {img}")
    else:
        full_path = os.path.join(base_dir, img.replace('/', os.sep))
        exists = os.path.exists(full_path)
        status = "OK" if exists else "!!! MANQUANT !!!"
        print(f"[LOCAL BG] {img} -> {status}")

# Check for SVGs or other elements that might look like question marks
# (Empty items in grid, etc.)
print("\n--- ANALYSE DE LA STRUCTURE ---")
if '<div class="grid' in html:
    print("[STRUCTURE] Grille de documentation trouvée.")

# Check for duplicates or orphaned tags
print("\n--- VÉRIFICATION DES DOUBLONS ET ERREURS HTML ---")
tag_counts = {
    'marquee-track': html.count('marquee-track'),
    'section id="marquee"': html.count('section id="marquee"'),
    '</a></a>': html.count('</a></a>'), # Common error
    '</div></div></div>': html.count('</div></div></div>')
}
for tag, count in tag_counts.items():
    print(f"{tag}: {count}")

# Check for specific "question mark" logos
if '?' in html:
    print("[ATTENTION] Le caractère '?' a été trouvé dans le fichier. Vérifiez s'il ne s'agit pas d'un placeholder.")
