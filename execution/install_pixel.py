import os

def install_pixel():
    filepath = "/Users/pantera/Desktop/Projetos/Recetario Ancestral/vendas.html"
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    pixel_script = """<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '1536230360782560');
fbq('track', 'PageView');
</script>
"""

    pixel_noscript = """<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1536230360782560&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->
"""

    # 1. Insert Pixel Script
    # Anchor: Before Utmify script if exists, else before </head> or <body
    if "fbq('init'" not in content:
        if "cdn.utmify.com.br" in content:
            # Insert before Utmify
            content = content.replace('<script\n  src="https://cdn.utmify.com.br', pixel_script + '<script\n  src="https://cdn.utmify.com.br')
            print("Inserted Pixel Script before Utmify.")
        elif "</head>" in content:
            content = content.replace("</head>", pixel_script + "</head>")
            print("Inserted Pixel Script before </head>.")
        else:
            # Fallback: Before body
            content = content.replace("<body", pixel_script + "<body")
            print("Inserted Pixel Script before <body>.")
    else:
        print("Pixel Script already present.")

    # 2. Insert Pixel Noscript
    # Anchor: After <body class=gradient>
    # Note: We need to be careful not to double insert if running multiple times, 
    # but exact string matching "height=1" might vary if formatted.
    if "facebook.com/tr?id=1536230360782560" not in content:
        # Try specific body tag from previous knowledge
        if "<body class=gradient>" in content:
            content = content.replace("<body class=gradient>", "<body class=gradient>\n" + pixel_noscript)
            print("Inserted Pixel Noscript after <body class=gradient>.")
        else:
            # Generic body replacement if class changed or differs
            # This is risky if body has other attributes we missed, but grep showed 'class=gradient'
            # Let's try a regex-like approach or just simple replace if we are sure
            import re
            # Match <body ... > or <body ...>
            # But simple replace is safer if we know the string.
            # Let's try finding the tag end
            body_pos = content.find("<body")
            if body_pos != -1:
                # Find closing >
                close_pos = content.find(">", body_pos)
                if close_pos != -1:
                    content = content[:close_pos+1] + "\n" + pixel_noscript + content[close_pos+1:]
                    print("Inserted Pixel Noscript after generic <body> tag.")
                else:
                    print("Could not find closing > for <body>.")
            else:
                print("Could not find <body> tag.")
    else:
        print("Pixel Noscript already present.")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print("Pixel installation checks completed.")

if __name__ == "__main__":
    install_pixel()
