import re

html_path = r"c:\Users\Lyes\Documents\e-portfolio\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Reconstruct the Marquee track completely to avoid regex mess
marquee_item_template = """          <a href="{href}" target="_blank" class="tech-card doc-card{extra_class}">
            {icon_html}
            <span class="tech-name text-center leading-tight">{label}</span>
          </a>"""

items = [
    {"href": "pdf/doc_technique/proxmox instalation.pdf", "label": "Proxmox", "icon_html": '<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" alt="Proxmox" class="tech-icon mb-2" style="width: 40px; height: 40px;">', "extra_class": ""},
    {"href": "pdf/doc_technique/Documentation-Installation Active Directory (AD DS) Windows Server 2022.pdf", "label": "Active<br>Directory", "icon_html": '<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/windows8/windows8-original.svg" alt="Windows" class="tech-icon mb-2" style="width: 35px; height: 35px;">', "extra_class": " active"},
    {"href": "pdf/doc_technique/Documentation-Installation et Configuration SSH sur Debian.pdf", "label": "SSH<br>Debian", "icon_html": '<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg" alt="SSH" class="tech-icon mb-2" style="width: 35px; height: 35px;">', "extra_class": ""},
    {"href": "pdf/projets/Documentation-Installation Debian 12.1.0.pdf", "label": "Debian 12", "icon_html": '<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/debian/debian-original.svg" alt="Debian" class="tech-icon mb-2" style="width: 35px; height: 35px;">', "extra_class": ""},
    {"href": "pdf/doc_technique/sauvegarde,restauration FIC (full image copie) site web.pdf", "label": "Sauvegarde<br>& Resta.", "icon_html": '<span class="text-3xl mb-2">💾</span>', "extra_class": ""},
    {"href": "pdf/doc_technique/pfsense.pdf", "label": "pfSense", "icon_html": '<img src="logo/pfsense logo.png" alt="pfSense" class="tech-icon mb-2" style="width: 35px; height: 35px; object-fit: contain;">', "extra_class": ""},
    {"href": "pdf/doc_technique/Installation de Metasploitable 2 sur l\'Hyperviseur Proxmox VE.pdf", "label": "Metasploitable<br>2", "icon_html": '<img src="logo/metasploit 2 logo.png" alt="Metasploit" class="tech-icon mb-2" style="width: 35px; height: 35px; object-fit: contain;">', "extra_class": ""},
    {"href": "pdf/doc_technique/documentation instalation et utilisation Lynis .pdf", "label": "Lynis", "icon_html": '<img src="logo/logo lynis.png" alt="Lynis" class="tech-icon mb-2" style="width: 35px; height: 35px; object-fit: contain;">', "extra_class": ""},
    {"href": "pdf/doc_technique/Documentation-Installation GLPI sur Debian (1) (1).pdf", "label": "GLPI", "icon_html": '<img src="logo/logo glpi.png" alt="GLPI" class="tech-icon mb-2" style="width: 35px; height: 35px; object-fit: contain;">', "extra_class": ""},
    {"href": "pdf/doc_technique/doc insta et utili de  SNMP.pdf", "label": "SNMP", "icon_html": '<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/networkx/networkx-original.svg" alt="SNMP" class="tech-icon mb-2" style="width: 35px; height: 35px;">', "extra_class": ""},
    {"href": "pdf/doc_technique/doc commandes routeur cisco.pdf", "label": "Cisco", "icon_html": '<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cisco/cisco-original.svg" alt="Cisco" class="tech-icon mb-2" style="width: 35px; height: 35px;">', "extra_class": ""}
]

marquee_set_1 = "\n".join([marquee_item_template.format(**item) for item in items])
marquee_set_2 = marquee_set_1 # Duplicate

new_track_content = f"""
          <!-- First Set -->
{marquee_set_1}

          <!-- Second Set (Duplicate for seamless scroll) -->
{marquee_set_2}
        """

# Replace the marquee-track content
html = re.sub(r'(<div class="marquee-track"[^>]*>).*?(</div>)', 
              r'\1' + new_track_content + r'\2', 
              html, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS")
