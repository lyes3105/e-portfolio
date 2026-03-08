import re
import os

html_path = r"c:\Users\Lyes\Documents\e-portfolio\index.html"
base_dir = r"c:\Users\Lyes\Documents\e-portfolio"

def check_path(path):
    if not path: return "MISSING_SRC"
    if path.startswith(('http://', 'https://')): return "EXTERNAL"
    clean_path = path.split('#')[0].split('?')[0].replace('/', os.sep)
    full_path = os.path.join(base_dir, clean_path)
    if os.path.exists(full_path): return "OK"
    return f"FAILED_{clean_path}"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

report = []
report.append("=== FINAL PORTFOLIO AUDIT ===")

# 1. Verification of all Img/SVG sources
report.append("\n[1] IMAGE SOURCES:")
img_sources = re.findall(r'src="([^"]+)"', html)
for src in img_sources:
    res = check_path(src)
    if "FAILED" in res or "MISSING" in res:
        report.append(f"  [X] {res} -> {src}")
    else:
        report.append(f"  [.] {res} -> {src}")

# 2. Verification of all document links
report.append("\n[2] DOCUMENT LINKS (PDF):")
pdf_links = re.findall(r'href="([^"]+\.pdf)"', html)
for href in set(pdf_links):
    res = check_path(href)
    if "FAILED" in res:
        report.append(f"  [X] {res} -> {href}")
    else:
        report.append(f"  [.] {res} -> {href}")

# 3. Structural checks
report.append("\n[3] STRUCTURAL INTEGRITY:")
checks = {
    "pfSense case": html.count("Pfsense") == 0,
    "Cachier typo": html.count("cachier") == 0,
    "Broken chars ()": html.count("") == 0,
    "Duplicate IDs": len(re.findall(r'id="([^"]+)"', html)) == len(set(re.findall(r'id="([^"]+)"', html))),
    "Double links (</a></a>)": html.count("</a></a>") == 0,
}
for name, passed in checks.items():
    report.append(f"  [{'OK' if passed else 'FAIL'}] {name}")

# 4. Check IDs duplication specifically
ids = re.findall(r'id="([^"]+)"', html)
seen = set()
dups = []
for x in ids:
    if x in seen: dups.append(x)
    seen.add(x)
if dups: report.append(f"  [FAIL] Duplicate IDs: {dups}")

# 5. Check Marquee sync counts
marquee_count = html.count('class="tech-card doc-card') # Should be items * 2
report.append(f"\n[4] MARQUEE SYNC: Found {marquee_count} items (Set 1 + Set 2).")

with open(r"c:\Users\Lyes\Documents\e-portfolio\final_audit_report.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(report))

print("AUDIT_COMPLETE")
