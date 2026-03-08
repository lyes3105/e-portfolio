import re

html_path = r"c:\Users\Lyes\Documents\e-portfolio\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

replacements = {
    # Backup / Veeam
    'https://upload.wikimedia.org/wikipedia/commons/3/33/Veeam_Software_logo.png': 'https://commons.wikimedia.org/wiki/Special:FilePath/Veeam_Software_logo.svg',
    
    # pfSense
    'https://upload.wikimedia.org/wikipedia/commons/4/47/PfSense_logo.png': 'https://commons.wikimedia.org/wiki/Special:FilePath/PfSense_logo.svg',
    
    # Metasploit
    'https://upload.wikimedia.org/wikipedia/commons/4/4e/Metasploit_logo.svg': 'https://commons.wikimedia.org/wiki/Special:FilePath/Metasploit_logo.svg',
    
    # Lynis / Kali
    'https://upload.wikimedia.org/wikipedia/commons/d/dd/Kali_Linux_logo.svg': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kalilinux/kalilinux-original.svg',
    
    # GLPI
    'https://upload.wikimedia.org/wikipedia/commons/4/4d/GLPI_logo.png': 'https://commons.wikimedia.org/wiki/Special:FilePath/GLPI_logo.png'
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("SUCCESS")
