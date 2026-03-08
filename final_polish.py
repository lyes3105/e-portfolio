import re
import os

html_path = r"c:\Users\Lyes\Documents\e-portfolio\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Fix iNext typos: "cachier" -> "cahier" and fix broken bullet points/emojis
# The user mentioned "cachier" -> "cahier". 
# Lines 642-644 have binary garbage / broken icons
html = html.replace('Inext cachier des charges.pdf', 'Inext cahier des charges.pdf')
html = html.replace(' Cahier Des Charges', '📋 Cahier Des Charges')
html = html.replace(' Cahier De Recette', '📝 Cahier De Recette')

# 2. Fix pfSense case: "Pfsense" -> "pfSense"
html = html.replace('Installation Pfsense', 'Installation pfSense')
html = html.replace('Déploiement Pfsense', 'Déploiement pfSense')

# 3. Update Proxmox logos (Local file: logo/logo proxmox.png)
# Marquee
html = html.replace('https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" alt="Proxmox" class="tech-icon mb-2" style="width: 40px; height: 40px;"', 
                   'logo/logo proxmox.png" alt="Proxmox" class="tech-icon mb-2" style="width: 40px; height: 40px; object-fit: contain;"')

# Documentation grid
html = html.replace('https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" alt="Proxmox"\n                class="w-10 h-10 object-contain flex-shrink-0"',
                   'logo/logo proxmox.png" alt="Proxmox" class="w-10 h-10 object-contain flex-shrink-0"')

# 4. Any logo with a "question mark" according to previous audit
# Flaticon icons for security and supervision might be broken
# Security logo (line 332)
html = html.replace('https://cdn-icons-png.flaticon.com/512/2092/2092663.png', 'logo/logo Flaticon (Sécurité, Supervision.jpg')
# Supervision logo (line 359)
html = html.replace('https://cdn-icons-png.flaticon.com/512/1055/1055687.png', 'logo/logo Flaticon (Sécurité, Supervision.jpg')

# 5. Fix potential encoding issues/garbage characters globally
# (Just in case there are others)
html = html.replace('', '')

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS")
