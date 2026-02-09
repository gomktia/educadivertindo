
import os
import sys

def deploy_page(html_content, filename="vendas.html"):
    """
    Deploys the provided HTML content to a file.
    
    Args:
        html_content (str): The HTML content to write.
        filename (str): The name of the file to create. Defaults to "vendas.html".
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Successfully deployed page to {os.path.abspath(filename)}")
    except Exception as e:
        print(f"Error deploying page: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Read from stdin if no argument provided
        html_content = sys.stdin.read()
    else:
        html_content = sys.argv[1]
    
    deploy_page(html_content)
