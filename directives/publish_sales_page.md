# Directive: Publish Sales Page

## Goal
Receive an HTML string (or file content) from the user and deploy it as a sales page (e.g., `vendas.html`) without modifying the content.

## Inputs
- **HTML Content**: The raw HTML code provided by the user.
- **Target Filename**: The desired filename for the sales page (default: `vendas.html`).

## Tools
- `execution/deploy_page.py`

## Steps
1.  Receive HTML content.
2.  Run `execution/deploy_page.py` with the HTML content as an argument or input.
3.  Verify the file was created successfully.
4.  Notify the user with the file path.

## Edge Cases
-   If the file already exists, confirm overwrite or use a different name (handled by script logic or user prompt, but for now we will overwrite as per "deixar ela no ar").
-   If the HTML is empty, return an error.
