import re

html_path = r"c:\Users\Lyes\Documents\e-portfolio\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Replace Cisco SVG URL with local logo path
html = html.replace('https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cisco/cisco-original.svg', 'logo/logo cisco.png')

# 2. Remove the accidental card in Supervision & ITSM section
# Based on the view_file, it's roughly between lines 530 and 533
cisco_accidental_pattern = r'\s*<a href="pdf/doc_technique/doc commandes routeur cisco\.pdf" target="_blank" class="tech-card doc-card">\s*<img src="logo/logo cisco\.png" alt="Cisco" class="tech-icon mb-2" style="width: 35px; height: 35px;">\s*<span class="tech-name text-center leading-tight">Cisco</span>\s*</a>'

html = re.sub(cisco_accidental_pattern, '', html, flags=re.DOTALL)

# 3. Ensure the Réseau & Sécurité card has the correct class and layout
# (It might have been lost or mangled in previous steps, let's make sure it's там)
# We want to find the one that has h4 "Commandes Cisco" and p "Switching & Routing"

# Correct grid card for Cisco
cisco_grid_card = """            <a href="pdf/doc_technique/doc commandes routeur cisco.pdf" target="_blank" class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="logo/logo cisco.png" alt="Cisco" class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Commandes Cisco</h4>
                <p class="text-gray-500 text-xs mt-1">Switching & Routing</p>
              </div>
            </a>"""

# Let's check if there's already a grid card for Cisco but with the old logo
# If there's none, we might need to re-insert it in the right place (after Lynis)
if 'Commandes Cisco</h4>' not in html:
    lynis_pattern = r'(<a href="pdf/doc_technique/documentation instalation et utilisation Lynis \.pdf".*?</a>)'
    html = re.sub(lynis_pattern, r'\1\n' + cisco_grid_card, html, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS")
