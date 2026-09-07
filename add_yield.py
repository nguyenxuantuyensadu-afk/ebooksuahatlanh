import re
import json

with open('src/recipesData.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# find { name: "...", recipe: "...", usage: "...", prepTip: "..." }
# and insert yield_info: "1 L" after recipe
new_content = re.sub(r'(recipe: "[^"]+",)\s*(usage:)', r'\1 yield_info: "1 L", \2', content)

with open('src/recipesData.ts', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Added yield_info")
