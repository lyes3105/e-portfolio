import re

html_path = r"c:\Users\Lyes\Documents\e-portfolio\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Tech Grid: Add Switching card next to Routing card
routing_card_full = """            <a href="pdf/doc_technique/doc commandes routeur cisco.pdf" target="_blank"
              class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="logo/logo cisco.png" alt="Cisco" class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Commandes Cisco</h4>
                <p class="text-gray-500 text-xs mt-1">Routing</p>
              </div>
            </a>"""

switching_card_full = """            <a href="pdf/doc_technique/nouvelle doc.pdf" target="_blank"
              class="card card-hover flex items-center gap-4 p-5 min-h-[100px]">
              <img src="logo/logo cisco.png" alt="Cisco" class="w-10 h-10 object-contain flex-shrink-0">
              <div>
                <h4 class="font-medium text-white text-base leading-tight">Commandes Cisco</h4>
                <p class="text-gray-500 text-xs mt-1">Switching</p>
              </div>
            </a>"""

# Add Switching card after Routing card in grid
if routing_card_full in html:
    html = html.replace(routing_card_full, routing_card_full + "\n" + switching_card_full)

# 2. Update Marquee: Add both Routing and Switching
# We already have Routing (added in previous step). Let's make sure we have both and they are clean.
# I'll just find the set of tech-cards and insert the pair.

routing_marquee = """          <a href="pdf/doc_technique/doc commandes routeur cisco.pdf" target="_blank" class="tech-card doc-card">
            <img src="logo/logo cisco.png" alt="Cisco" class="tech-icon mb-2"
              style="width: 35px; height: 35px; object-fit: contain;">
            <span class="tech-name text-center leading-tight">Routing</span>
          </a>"""

switching_marquee = """          <a href="pdf/doc_technique/nouvelle doc.pdf" target="_blank" class="tech-card doc-card">
            <img src="logo/logo cisco.png" alt="Cisco" class="tech-icon mb-2"
              style="width: 35px; height: 35px; object-fit: contain;">
            <span class="tech-name text-center leading-tight">Switching</span>
          </a>"""

# First, remove any existing isolated Routing card in marquee to avoid duplicates if I run this again
html = html.replace(routing_marquee, "")

# Now add both after SNMP in both sets
pattern = re.compile(r'(<a href="pdf/doc_technique/doc insta et utili de  SNMP\.pdf".*?</a>)', re.DOTALL)
html = pattern.sub(r'\1\n' + routing_marquee + "\n" + switching_marquee, html)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS_TECH_AND_MARQUEE_UPDATE")
