import re

html_path = r"c:\Users\Lyes\Documents\e-portfolio\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Marquee Labels (Remove verbs)
replacements = {
    r'Installation<br>Proxmox': 'Proxmox',
    r'Installation<br>Debian 12': 'Debian 12',
    r'Installation<br>pfSense': 'pfSense',
    r'Utilisation<br>Lynis': 'Lynis',
    r'Installation<br>GLPI': 'GLPI',
    r'Installation<br>SNMP': 'SNMP'
}

for old, new in replacements.items():
    html = html.replace(f'<span class="tech-name text-center leading-tight">{old}</span>', 
                        f'<span class="tech-name text-center leading-tight">{new}</span>')

# 2. Add Cisco Card to Marquee
cisco_marquee_card = """          <a href="pdf/doc_technique/doc commandes routeur cisco.pdf" target="_blank" class="tech-card doc-card">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cisco/cisco-original.svg" alt="Cisco" class="tech-icon mb-2" style="width: 35px; height: 35px;">
            <span class="tech-name text-center leading-tight">Cisco</span>
          </a>"""

# Insert Cisco card after SNMP in each Set
# There are two </a> blocks ending SNMP in the marquee
snmp_marquee_pattern = r'(<a href="pdf/doc_technique/doc insta et utili de  SNMP\.pdf".*?</a>)'
html = re.sub(snmp_marquee_pattern, r'\1\n' + cisco_marquee_card, html, flags=re.DOTALL)

# 3. Add Cisco Card to Documentation Technique Grid (Réseau & Sécurité)
cisco_grid_card = """            <a href="pdf/doc_technique/doc commandes routeur cisco.pdf" target="_blank" class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cisco/cisco-original.svg" alt="Cisco" class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Commandes Cisco</h4>
                <p class="text-gray-500 text-xs mt-1">Switching & Routing</p>
              </div>
            </a>"""

# Insert in Réseau & Sécurité grid (after Lynis)
lynis_grid_pattern = r'(<a href="pdf/doc_technique/documentation instalation et utilisation Lynis \.pdf".*?</a>)'
html = re.sub(lynis_grid_pattern, r'\1\n' + cisco_grid_card, html, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS")
