import re

html_path = r"c:\Users\Lyes\Documents\e-portfolio\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Surgical replacement of the broken block with clean text
# We use a very specific block to avoid mismatches
old_block = """          <div class="flex flex-col gap-2 mt-3">
            <a href="pdf/projets/Inext cahier des charges.pdf" target="_blank" class="btn-doc"> Cahier Des
              Charges</a>
            <a href="pdf/projets/cahier de recette inext.pdf" target="_blank" class="btn-doc">📝 Cahier De Recette</a>
            <a href="pdf/projets/journaldebord inext.pdf" target="_blank" class="btn-doc">📓 Journal De Bord</a>
            <button onclick="document.getElementById('inextSuiviModal').style.display='flex'" class="btn-doc">📊 Suivi
              De Projet</button>
          </div>"""

new_block = """          <div class="flex flex-col gap-2 mt-3">
            <a href="pdf/projets/Inext cahier des charges.pdf" target="_blank" class="btn-doc">📋 Cahier Des
              Charges</a>
            <a href="pdf/projets/cahier de recette inext.pdf" target="_blank" class="btn-doc">📝 Cahier De Recette</a>
            <a href="pdf/projets/journaldebord inext.pdf" target="_blank" class="btn-doc">📓 Journal De Bord</a>
            <button onclick="document.getElementById('inextSuiviModal').style.display='flex'" class="btn-doc">📊 Suivi
              De Projet</button>
          </div>"""

# Since "" can be tricky to match, let's use a regex that matches any character before "Cahier" 
# within that specific document list.

pattern = re.compile(r'<div class="flex flex-col gap-2 mt-3">.*?Inext cahier des charges\.pdf.*?</div>', re.DOTALL)
html = pattern.sub(new_block, html)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS_ENCODING_FIX")
