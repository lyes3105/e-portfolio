import re

html_path = r"c:\Users\Lyes\Documents\e-portfolio\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

new_section = """    <!-- Documentation Technique -->
    <section id="doc_technique" class="section" data-aos="fade-up">
      <h2 class="section-title"><span>Documentation Technique</span></h2>
      <div class="section-divider"></div>

      <div class="max-w-7xl mx-auto px-4">
        
        <!-- Virtualisation -->
        <div class="mb-12 stagger-item">
          <div class="flex items-center gap-3 mb-6">
            <span class="text-3xl">☁️</span>
            <h3 class="text-2xl font-bold text-white">Virtualisation</h3>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            <a href="pdf/doc_technique/proxmox instalation.pdf" target="_blank" class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" alt="Proxmox" class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Installation Proxmox</h4>
                <p class="text-gray-500 text-xs mt-1">Configuration complète Proxmox VE</p>
              </div>
            </a>
          </div>
        </div>

        <!-- Infrastructure & Services -->
        <div class="mb-12 stagger-item">
          <div class="flex items-center gap-3 mb-6">
            <span class="text-3xl">🪟</span>
            <h3 class="text-2xl font-bold text-white">Infra & Services</h3>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            <a href="pdf/doc_technique/Documentation-Installation Active Directory (AD DS) Windows Server 2022.pdf" target="_blank" class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/windows8/windows8-original.svg" alt="AD" class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Active Directory</h4>
                <p class="text-gray-500 text-xs mt-1">Sur Windows Server 2022</p>
              </div>
            </a>
            <a href="pdf/doc_technique/Documentation-Installation et Configuration SSH sur Debian.pdf" target="_blank" class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg" alt="SSH" class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Installation SSH</h4>
                <p class="text-gray-500 text-xs mt-1">Déploiement sur Debian</p>
              </div>
            </a>
            <a href="pdf/projets/Documentation-Installation Debian 12.1.0.pdf" target="_blank" class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/debian/debian-original.svg" alt="Debian" class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Installation Debian 12</h4>
                <p class="text-gray-500 text-xs mt-1">Déploiement Debian (CLI)</p>
              </div>
            </a>
            <a href="pdf/doc_technique/sauvegarde,restauration FIC (full image copie) site web.pdf" target="_blank" class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="https://upload.wikimedia.org/wikipedia/commons/3/33/Veeam_Software_logo.png" alt="Backup" class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Sauvegarde & Rest.</h4>
                <p class="text-gray-500 text-xs mt-1">Full Image Copie (FIC)</p>
              </div>
            </a>
          </div>
        </div>

        <!-- Réseau & Sécurité -->
        <div class="mb-12 stagger-item">
          <div class="flex items-center gap-3 mb-6">
            <span class="text-3xl">🛡️</span>
            <h3 class="text-2xl font-bold text-white">Réseau & Sécurité</h3>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            <a href="pdf/doc_technique/pfsense.pdf" target="_blank" class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="https://upload.wikimedia.org/wikipedia/commons/4/47/PfSense_logo.png" alt="pfSense" class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Installation Pfsense</h4>
                <p class="text-gray-500 text-xs mt-1">Déploiement Pfsense</p>
              </div>
            </a>
            <a href="pdf/doc_technique/Installation de Metasploitable 2 sur l'Hyperviseur Proxmox VE.pdf" target="_blank" class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Metasploit_logo.svg" alt="Metasploit" class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Metasploitable 2</h4>
                <p class="text-gray-500 text-xs mt-1">Déploiement Proxmox VE</p>
              </div>
            </a>
            <a href="pdf/doc_technique/documentation instalation et utilisation Lynis .pdf" target="_blank" class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="https://upload.wikimedia.org/wikipedia/commons/d/dd/Kali_Linux_logo.svg" alt="Lynis" class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Utilisation Lynis</h4>
                <p class="text-gray-500 text-xs mt-1">Audit de sécurité</p>
              </div>
            </a>
          </div>
        </div>

        <!-- Supervision & ITSM -->
        <div class="mb-8 stagger-item">
          <div class="flex items-center gap-3 mb-6">
            <span class="text-3xl">📊</span>
            <h3 class="text-2xl font-bold text-white">Supervision & ITSM</h3>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            <a href="pdf/doc_technique/Documentation-Installation GLPI sur Debian (1) (1).pdf" target="_blank" class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="https://upload.wikimedia.org/wikipedia/commons/4/4d/GLPI_logo.png" alt="GLPI" class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Installation GLPI</h4>
                <p class="text-gray-500 text-xs mt-1">Déploiement sur Debian</p>
              </div>
            </a>
            <a href="pdf/doc_technique/doc insta et utili de  SNMP.pdf" target="_blank" class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/networkx/networkx-original.svg" alt="SNMP" class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Installation SNMP</h4>
                <p class="text-gray-500 text-xs mt-1">Supervision réseau SNMP</p>
              </div>
            </a>
          </div>
        </div>

      </div>
    </section>"""

pattern = re.compile(r'    <!-- Documentation Technique -->\n    <section id="doc_technique" class="section" data-aos="fade-up">.*?    </section>', re.DOTALL)

if pattern.search(html):
    html = pattern.sub(new_section, html)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("SUCCESS")
else:
    print("FAIL")
