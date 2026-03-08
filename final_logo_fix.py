import re
import os

html_path = r"c:\Users\Lyes\Documents\e-portfolio\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# mapping based on implementation plan
replacements = {
    # pfSense (Marquee and Grid)
    r'<svg[^>]*?class="tech-icon mb-2"[^>]*?>\s*<path[^>]*?d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>\s*</svg>': r'<img src="logo/pfsense logo.png" alt="pfSense" class="tech-icon mb-2" style="width: 35px; height: 35px; object-fit: contain;">',
    r'<img src="https://commons\.wikimedia\.org/wiki/Special:FilePath/PfSense_logo\.svg"[^>]*?>': r'<img src="logo/pfsense logo.png" alt="pfSense" class="w-10 h-10 object-contain flex-shrink-0">',
    
    # Metasploit (Marquee and Grid)
    r'<svg[^>]*?class="tech-icon mb-2"[^>]*?>\s*<circle cx="12" cy="12" r="10"></circle>\s*<line x1="12" y1="8" x2="12" y2="12"></line>\s*<line x1="12" y1="16" x2="12\.01" y2="16"></line>\s*</svg>': r'<img src="logo/metasploit 2 logo.png" alt="Metasploit" class="tech-icon mb-2" style="width: 35px; height: 35px; object-fit: contain;">',
    r'<img src="https://commons\.wikimedia\.org/wiki/Special:FilePath/Metasploit_logo\.svg"[^>]*?>': r'<img src="logo/metasploit 2 logo.png" alt="Metasploit" class="w-10 h-10 object-contain flex-shrink-0">',
    
    # GLPI (Marquee and Grid)
    r'<svg[^>]*?class="tech-icon mb-2"[^>]*?>\s*<path[^>]*?d="M19 3h-4\.18C14\.4 1\.84 13\.3 1 12 1c-1\.3 0-2\.4\.84-2\.82 2H5c-1\.1 0-2\.9-2 2v14c0 1\.1\.9 2 2 2h14c1\.1 0 2-\.9 2-2V5c0-1\.1-\.9-2-2-2zm-7 0c\.55 0 1\.45 1 1s-\.45 1-1 1-1-\.45-1-1\.45-1 1-1zm2 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"[^>]*?/>\s*</svg>': r'<img src="logo/logo glpi.png" alt="GLPI" class="tech-icon mb-2" style="width: 35px; height: 35px; object-fit: contain;">',
    r'<img src="https://commons\.wikimedia\.org/wiki/Special:FilePath/GLPI_logo\.png"[^>]*?>': r'<img src="logo/logo glpi.png" alt="GLPI" class="w-10 h-10 object-contain flex-shrink-0">',
    
    # Lynis (Marquee and Grid)
    r'<svg[^>]*?class="tech-icon mb-2"[^>]*?>\s*<circle cx="11" cy="11" r="8"></circle>\s*<line x1="21" y1="21" x2="16\.65" y2="16\.65"></line>\s*</svg>': r'<img src="logo/logo lynis.png" alt="Lynis" class="tech-icon mb-2" style="width: 35px; height: 35px; object-fit: contain;">',
    r'<img src="https://cdn\.jsdelivr\.net/gh/devicons/devicon/icons/kalilinux/kalilinux-original\.svg" alt="Lynis"[^>]*?>': r'<img src="logo/logo lynis.png" alt="Lynis" class="w-10 h-10 object-contain flex-shrink-0">',
    
    # Veeam / Sauvegarde (Marquee and Grid)
    r'<svg[^>]*?class="tech-icon mb-2"[^>]*?>\s*<path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"></path>\s*<polyline points="17 21 17 13 7 13 7 21"></polyline>\s*<polyline points="7 3 7 8 15 8"></polyline>\s*</svg>': r'<img src="logo/veeam.svg" alt="Veeam" class="tech-icon mb-2" style="width: 35px; height: 35px; object-fit: contain;">',
    r'<img src="https://commons\.wikimedia\.org/wiki/Special:FilePath/Veeam_Software_logo\.svg"[^>]*?>': r'<img src="logo/veeam.svg" alt="Veeam" class="w-10 h-10 object-contain flex-shrink-0">',

    # Proxmox (Marquee) - Missing SVG was found in previous scan
    r'<svg[^>]*?class="tech-icon mb-2"[^>]*?>\s*<path\s*d="M4 3h16a2 2 0 012 2v4a2 2 0 01-2 2H4a2 2 0 01-2-2V5a2 2 0 012-2zm0 10h16a2 2 0 012 2v4a2 2 0 01-2 2H4a2 2 0 01-2-2v-4a2 2 0 012-2zM6 7a1 1 0 100-2 1 1 0 000 2zm0 10a1 1 0 100-2 1 1 0 000 2zm3-10a1 1 0 100-2 1 1 0 000 2zm0 10a1 1 0 100-2 1 1 0 000 2z"\s*/>\s*</svg>': r'<img src="logo/pfsense logo.png" alt="Proxmox" class="tech-icon mb-2" style="width: 40px; height: 40px; object-fit: contain; filter: hue-rotate(180deg);">' # Fallback until better logo, but user said pfSense logo is there. Actually let is use generic icon for now or keep devicon if it was there.
}

# Simple string replacements for remaining tags
simple_replacements = {
    'https://commons.wikimedia.org/wiki/Special:FilePath/PfSense_logo.svg': 'logo/pfsense logo.png',
    'https://commons.wikimedia.org/wiki/Special:FilePath/Metasploit_logo.svg': 'logo/metasploit 2 logo.png',
    'https://commons.wikimedia.org/wiki/Special:FilePath/Veeam_Software_logo.svg': 'logo/veeam.svg',
    'https://commons.wikimedia.org/wiki/Special:FilePath/GLPI_logo.png': 'logo/logo glpi.png',
    'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kalilinux/kalilinux-original.svg': 'logo/kali.svg' if 'kali.svg' in os.listdir("logo") else 'logo/logo lynis.png'
}

import os
logo_files = os.listdir("logo")
print(f"Files in logo: {logo_files}")

# 1. Regex replacements for complex SVG blocks
for pattern, replacement in replacements.items():
    html = re.sub(pattern, replacement, html, flags=re.DOTALL)

# 2. Simple URL replacements for <img> tags already there
for old, new in simple_replacements.items():
    html = html.replace(old, new)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("SUCCESS")
