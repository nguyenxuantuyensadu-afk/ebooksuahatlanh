import re

with open('src/data.ts', 'r') as f:
    content = f.read()

# First, let's extract sampleMenus block
sample_menus_regex = r"(\s+sampleMenus: \[.*?\]\s*\n\s*\},\s*\n\s*\{)"
match = re.search(r"(\s+sampleMenus: \[.*?\]\s*)(\n\s*\},\s*\n\s*\{\s*\n\s*id: \"equipment\")", content, re.DOTALL)
if match:
    sample_menus_str = match.group(1)
    
    # Remove it from the current position
    content = content.replace(sample_menus_str, "")
    
    # Insert it into module[2] (id: "menu")
    # Let's find the end of module[2]
    # module 2 ends where module 3 begins, or where it closes if it's the last one.
    # Module 3 is id: "costing"
    match_menu = re.search(r"(      menuItems: \[.*?\]\s*\n\s*\}\s*,)", content, re.DOTALL)
    if match_menu:
        menu_items_str = match_menu.group(1)
        # We replace the end of menu module with the sampleMenus appended
        # We need to ensure we don't mess up the braces.
        
        # Let's try a safer replace for the menu insertion
        target_replacement = menu_items_str[:-2] + "," + sample_menus_str + "    },"
        content = content.replace(menu_items_str, target_replacement)

with open('src/data.ts', 'w') as f:
    f.write(content)
