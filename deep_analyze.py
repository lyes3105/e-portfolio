import re
import os

html_path = r"c:\Users\Lyes\Documents\e-portfolio\index.html"
base_dir = r"c:\Users\Lyes\Documents\e-portfolio"

def check_file(path):
    if not path: return "MANQUANT (vide)"
    if path.startswith(('http://', 'https://')):
        return f"EXTERNE"
    
    clean_path = path.split('#')[0].split('?')[0] # Remove anchors/queries
    full_path = os.path.join(base_dir, clean_path.replace('/', os.sep))
    if os.path.exists(full_path):
        return "OK"
    else:
        return f"!!! MANQUANT ({full_path}) !!!"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

print("--- ANALYSE DU FICHIER index.html ---\n")

# 1. Check all images
print("--- Images (<img>) ---")
img_tags = re.findall(r'<img [^>]*src="([^"]+)"[^>]*alt="([^"]*)"', html)
for src, alt in img_tags:
    status = check_file(src)
    print(f"[{status}] src='{src}' alt='{alt}'")

# 2. Check all PDF links
print("\n--- Liens PDF (<a>) ---")
pdf_links = re.findall(r'<a [^>]*href="([^"]+\.pdf)"', html)
for href in set(pdf_links):
    status = check_file(href)
    print(f"[{status}] href='{href}'")

# 3. Check for obvious HTML structure errors
print("\n--- Erreurs Structurelles Potentielles ---")
# Broken tags
for tag in ['</a></a>', '</div></div></div>', '<div><div>', '<span><span>']:
    count = html.count(tag)
    if count > 0:
        print(f"[!] '{tag}' trouvé {count} fois.")

# Empty sections or headers
empty_headers = re.findall(r'<h[1-6]>[ \n\t]*</h[1-6]>', html)
if empty_headers:
    print(f"[!] {len(empty_headers)} headers vides trouvés.")

# 4. Check for "question mark" indicators
# Sometimes fonts or icons fail
if 'font-family: serif' in html or 'font-family: "Times New Roman"' in html:
    print("[!] Polices génériques (serif) détectées, vérifiez si c'est voulu.")

# 5. Check Marquee sync (again)
print("\n--- Cohérence Marquee vs Documentation ---")
marquee_match = re.search(r'marquee-track.*?<!-- First Set -->(.*?)<!-- Second Set', html, re.DOTALL)
if marquee_match:
    marquee_content = marquee_match.group(1)
    marquee_items = re.findall(r'href="([^"]+)"', marquee_content)
    print(f"Nombre d'items dans le marquee : {len(marquee_items)}")
else:
    print("[!] Structure du marquee non identifiée.")

# 6. Check for duplicate IDs
ids = re.findall(r'id="([^"]+)"', html)
duplicates = set([x for x in ids if ids.count(x) > 1])
if duplicates:
    print(f"[!] IDs dupliqués trouvés : {duplicates}")

print("\n--- ANALYSE TERMINÉE ---")
