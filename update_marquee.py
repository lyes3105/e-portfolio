import re

html_path = r"c:\Users\Lyes\Documents\e-portfolio\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

routing_card = """          <a href="pdf/doc_technique/doc commandes routeur cisco.pdf" target="_blank" class="tech-card doc-card">
            <img src="logo/logo cisco.png" alt="Cisco" class="tech-icon mb-2"
              style="width: 35px; height: 35px; object-fit: contain;">
            <span class="tech-name text-center leading-tight">Routing</span>
          </a>"""

# Add after SNMP in both sets
# SNMP in set 1: a href="pdf/doc_technique/doc insta et utili de  SNMP.pdf"
# SNMP in set 2: a href="pdf/doc_technique/doc insta et utili de  SNMP.pdf" (duplicate)

# Find all occurrences of the SNMP card and append Routing card after them
pattern = re.compile(r'(<a href="pdf/doc_technique/doc insta et utili de  SNMP\.pdf".*?</a>)', re.DOTALL)
html = pattern.sub(r'\1\n' + routing_card, html)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS_MARQUEE_UPDATE")
