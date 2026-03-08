import re

html_path = r"c:\Users\Lyes\Documents\e-portfolio\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

def update_marquee(content):
    # Proxmox
    content = re.sub(
        r'(<a href="pdf/doc_technique/proxmox instalation.pdf"[^>]*>).*?(<span class="tech-name[^>]*>Installation<br>Proxmox</span>)',
        r'\1\n            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" alt="Proxmox" class="tech-icon mb-2" style="width: 40px; height: 40px;">\n            \2',
        content, flags=re.DOTALL
    )
    # Active Directory
    content = re.sub(
        r'(<a href="pdf/doc_technique/Documentation-Installation Active Directory \(AD DS\) Windows Server 2022.pdf"[^>]*>).*?(<span class="tech-name[^>]*>Active<br>Directory</span>)',
        r'\1\n            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/windows8/windows8-original.svg" alt="Windows" class="tech-icon mb-2" style="width: 35px; height: 35px;">\n            \2',
        content, flags=re.DOTALL
    )
    # SSH
    content = re.sub(
        r'(<a href="pdf/doc_technique/Documentation-Installation et Configuration SSH sur Debian.pdf"[^>]*>).*?(<span class="tech-name[^>]*>SSH<br>Debian</span>)',
        r'\1\n            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg" alt="SSH" class="tech-icon mb-2" style="width: 35px; height: 35px;">\n            \2',
        content, flags=re.DOTALL
    )
    # Debian 12
    content = re.sub(
        r'(<a href="pdf/projets/Documentation-Installation Debian 12.1.0.pdf"[^>]*>).*?(<span class="tech-name[^>]*>Installation<br>Debian 12</span>)',
        r'\1\n            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/debian/debian-original.svg" alt="Debian" class="tech-icon mb-2" style="width: 35px; height: 35px;">\n            \2',
        content, flags=re.DOTALL
    )
    # Sauvegarde (Already emoji 💾, but let's be sure of the structure)
    content = re.sub(
        r'(<a href="pdf/doc_technique/sauvegarde,restauration FIC \(full image copie\) site web.pdf"[^>]*>).*?(<span class="tech-name[^>]*>Sauvegarde<br>& Resta.</span>)',
        r'\1\n            <span class="text-3xl mb-2">💾</span>\n            \2',
        content, flags=re.DOTALL
    )
    # pfSense
    content = re.sub(
        r'(<a href="pdf/doc_technique/pfsense.pdf"[^>]*>).*?(<span class="tech-name[^>]*>Installation<br>pfSense</span>)',
        r'\1\n            <img src="logo/pfsense logo.png" alt="pfSense" class="tech-icon mb-2" style="width: 35px; height: 35px; object-fit: contain;">\n            \2',
        content, flags=re.DOTALL
    )
    # Metasploit
    content = re.sub(
        r'(<a href="pdf/doc_technique/Installation de Metasploitable 2 sur l\'Hyperviseur Proxmox VE.pdf"[^>]*>).*?(<span class="tech-name[^>]*>Metasploitable<br>2</span>)',
        r'\1\n            <img src="logo/metasploit 2 logo.png" alt="Metasploit" class="tech-icon mb-2" style="width: 35px; height: 35px; object-fit: contain;">\n            \2',
        content, flags=re.DOTALL
    )
    # Lynis
    content = re.sub(
        r'(<a href="pdf/doc_technique/documentation instalation et utilisation Lynis .pdf"[^>]*>).*?(<span class="tech-name[^>]*>Utilisation<br>Lynis</span>)',
        r'\1\n            <img src="logo/logo lynis.png" alt="Lynis" class="tech-icon mb-2" style="width: 35px; height: 35px; object-fit: contain;">\n            \2',
        content, flags=re.DOTALL
    )
    # GLPI
    content = re.sub(
        r'(<a href="pdf/doc_technique/Documentation-Installation GLPI sur Debian \(1\) \(1\).pdf"[^>]*>).*?(<span class="tech-name[^>]*>Installation<br>GLPI</span>)',
        r'\1\n            <img src="logo/logo glpi.png" alt="GLPI" class="tech-icon mb-2" style="width: 35px; height: 35px; object-fit: contain;">\n            \2',
        content, flags=re.DOTALL
    )
    # SNMP
    content = re.sub(
        r'(<a href="pdf/doc_technique/doc insta et utili de  SNMP.pdf"[^>]*>).*?(<span class="tech-name[^>]*>Installation<br>SNMP</span>)',
        r'\1\n            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/networkx/networkx-original.svg" alt="SNMP" class="tech-icon mb-2" style="width: 35px; height: 35px;">\n            \2',
        content, flags=re.DOTALL
    )
    return content

# Extract the marquee track content
marquee_pattern = re.compile(r'(<div class="marquee-track"[^>]*>)(.*?)(</div>)', re.DOTALL)
match = marquee_pattern.search(html)

if match:
    header, track_content, footer = match.groups()
    new_track_content = update_marquee(track_content)
    html = html.replace(match.group(0), header + new_track_content + footer)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("SUCCESS")
else:
    print("MARQUEE NOT FOUND")
