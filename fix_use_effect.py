import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Extract the useEffect block
use_effect_pattern = r"  useEffect\(\(\) => \{[\s\S]*?\}, \[activeModuleId\]\);\n"
match = re.search(use_effect_pattern, content)

if match:
    use_effect_block = match.group(0)
    # Remove from its current position
    content = content.replace(use_effect_block, "")
    
    # Insert it before if (!currentUser) {
    target = "  if (!currentUser) {"
    content = content.replace(target, use_effect_block + "\n" + target)

    with open('src/App.tsx', 'w') as f:
        f.write(content)
    print("Fixed useEffect position")
else:
    print("Could not find useEffect block")
