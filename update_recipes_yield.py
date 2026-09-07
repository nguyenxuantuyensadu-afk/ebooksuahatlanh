import re

with open('src/recipesData.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Add yield_info: "1 L" to all recipes
# The recipes have the format: { name: "...", recipe: "...", usage: "...", prepTip: "..." }
# Or since I already did it earlier: wait, did I do it? No, I ran the python script but wait, did it succeed?
# Let's check src/recipesData.ts
