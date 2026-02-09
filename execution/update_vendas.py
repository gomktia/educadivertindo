import os

def update_vendas():
    filepath = "/Users/pantera/Desktop/Projetos/Recetario Ancestral/vendas.html"
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Insert Utmify script
    utmify_script = """<script
  src="https://cdn.utmify.com.br/scripts/utms/latest.js"
  data-utmify-prevent-subids
  async
  defer
></script>
"""
    # Check if already installed
    if "cdn.utmify.com.br" not in content:
        content = content.replace("<body", utmify_script + "<body")
        print("Inserted Utmify script.")
    else:
        print("Utmify script already present.")

    # 2. Update Price Meta Tags
    content = content.replace('<meta property=og:price:amount content=17.990,00>', '<meta property=og:price:amount content=17.00>')
    content = content.replace('<meta property=og:price:currency content=ARS>', '<meta property=og:price:currency content=USD>')
    
    # 3. Update Visual Prices
    # Be careful with spaces
    content = content.replace(' $73.990,00 ARS', ' $74.00 USD')
    content = content.replace(' $17.990,00 ARS', ' $17.00 USD')
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print("Updates applied to vendas.html")

if __name__ == "__main__":
    update_vendas()
