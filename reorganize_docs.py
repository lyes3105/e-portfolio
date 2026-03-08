import re

html_path = r"c:\Users\Lyes\Documents\e-portfolio\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Skill Logos
# Sécurité
html = html.replace(
    'src="logo/logo Flaticon (Sécurité, Supervision.jpg" alt="Sécurité"',
    'src="logo/sécurité logo.jpg" alt="Sécurité"'
)
# Supervision
html = html.replace(
    'src="logo/logo Flaticon (Sécurité, Supervision.jpg" alt="Supervision"',
    'src="logo/supervision logo.jpg" alt="Supervision"'
)

# 2. Reorganize Documentation Technique
# We need to rebuild the sections: Virtualisation, Systèmes & Administration, Réseau & Cybersécurité, Supervision & Gestion IT

virtualisation_content = """        <!-- Virtualisation -->
        <div class="mb-12 stagger-item">
          <div class="flex items-center gap-3 mb-6">
            <span class="text-3xl">☁️</span>
            <h3 class="text-2xl font-bold text-white">Virtualisation</h3>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            <a href="pdf/doc_technique/proxmox instalation.pdf" target="_blank"
              class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="logo/logo proxmox.png" alt="Proxmox" class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Installation Proxmox</h4>
                <p class="text-gray-500 text-xs mt-1">Configuration complète Proxmox VE</p>
              </div>
            </a>
          </div>
        </div>"""

systemes_content = """        <!-- Systèmes & Administration -->
        <div class="mb-12 stagger-item">
          <div class="flex items-center gap-3 mb-6">
            <span class="text-3xl">🖥️</span>
            <h3 class="text-2xl font-bold text-white">Systèmes & Administration</h3>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            <a href="pdf/doc_technique/Documentation-Installation Active Directory (AD DS) Windows Server 2022.pdf"
              target="_blank" class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/windows8/windows8-original.svg" alt="AD"
                class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Active Directory</h4>
                <p class="text-gray-500 text-xs mt-1">Sur Windows Server 2022</p>
              </div>
            </a>
            <a href="pdf/projets/Documentation-Installation Debian 12.1.0.pdf" target="_blank"
              class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/debian/debian-original.svg" alt="Debian"
                class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Installation Debian 12</h4>
                <p class="text-gray-500 text-xs mt-1">Déploiement Debian (CLI)</p>
              </div>
            </a>
          </div>
        </div>"""

reseau_content = """        <!-- Réseau & Cybersécurité -->
        <div class="mb-12 stagger-item">
          <div class="flex items-center gap-3 mb-6">
            <span class="text-3xl">🛡️</span>
            <h3 class="text-2xl font-bold text-white">Réseau & Cybersécurité</h3>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            <a href="pdf/doc_technique/pfsense.pdf" target="_blank"
              class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="logo/pfsense logo.png" alt="pfSense" class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Installation pfSense</h4>
                <p class="text-gray-500 text-xs mt-1">Déploiement pfSense</p>
              </div>
            </a>
            <a href="pdf/doc_technique/doc commandes routeur cisco.pdf" target="_blank"
              class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="logo/logo cisco.png" alt="Cisco" class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Commandes Cisco</h4>
                <p class="text-gray-500 text-xs mt-1">Routing</p>
              </div>
            </a>
            <a href="pdf/doc_technique/switch.pdf" target="_blank"
              class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="logo/logo cisco.png" alt="Cisco" class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Commandes Cisco</h4>
                <p class="text-gray-500 text-xs mt-1">Switching</p>
              </div>
            </a>
            <a href="pdf/doc_technique/Documentation-Installation et Configuration SSH sur Debian.pdf" target="_blank"
              class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg" alt="SSH"
                class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Service SSH</h4>
                <p class="text-gray-500 text-xs mt-1">Accès sécurisé Debian</p>
              </div>
            </a>
            <a href="pdf/doc_technique/Installation de Metasploitable 2 sur l'Hyperviseur Proxmox VE.pdf"
              target="_blank" class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="logo/metasploit 2 logo.png" alt="Metasploit" class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Metasploitable 2</h4>
                <p class="text-gray-500 text-xs mt-1">Lab de pénétration</p>
              </div>
            </a>
            <a href="pdf/doc_technique/documentation instalation et utilisation Lynis .pdf" target="_blank"
              class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="logo/logo lynis.png" alt="Lynis" class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Audit Lynis</h4>
                <p class="text-gray-500 text-xs mt-1">Hardening Système</p>
              </div>
            </a>
          </div>
        </div>"""

supervision_content = """        <!-- Supervision & Gestion IT -->
        <div class="mb-12 stagger-item">
          <div class="flex items-center gap-3 mb-6">
            <span class="text-3xl">📊</span>
            <h3 class="text-2xl font-bold text-white">Supervision & Gestion IT</h3>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            <a href="pdf/doc_technique/Documentation-Installation GLPI sur Debian (1) (1).pdf" target="_blank"
              class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="logo/logo glpi.png" alt="GLPI" class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Installation GLPI</h4>
                <p class="text-gray-500 text-xs mt-1">Gestion de parc & ITSM</p>
              </div>
            </a>
            <a href="pdf/doc_technique/doc insta et utili de  SNMP.pdf" target="_blank"
              class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/networkx/networkx-original.svg" alt="SNMP"
                class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Protocole SNMP</h4>
                <p class="text-gray-500 text-xs mt-1">Supervision réseau</p>
              </div>
            </a>
            <a href="pdf/doc_technique/sauvegarde,restauration FIC (full image copie) site web.pdf" target="_blank"
              class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <span class="text-3xl">💾</span>
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Sauvegarde & Rest.</h4>
                <p class="text-gray-500 text-xs mt-1">Stratégie de récuperage</p>
              </div>
            </a>
          </div>
        </div>"""

# Replace the entire content inside <div class="max-w-7xl mx-auto px-4"> ... </div>
# of the Section Documentation Technique
pattern = re.compile(r'(<!-- Documentation Technique -->.*?<div class="max-w-7xl mx-auto px-4">).*?(</div>\s*</section>)', re.DOTALL)
new_inner_content = f"\n\n{virtualisation_content}\n\n{systemes_content}\n\n{reseau_content}\n\n{supervision_content}\n\n        "
html = pattern.sub(r'\1' + new_inner_content + r'\2', html)

# 3. Update Marquee for Switching (added earlier but maybe with wrong link "nouvelle doc.pdf")
html = html.replace('href="pdf/doc_technique/nouvelle doc.pdf"', 'href="pdf/doc_technique/switch.pdf"')

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS_FULL_REORG")
