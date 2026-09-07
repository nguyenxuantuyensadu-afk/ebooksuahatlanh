import re

with open('src/recipesData.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find all recipes that have "ml" or "trái" or "quả" or "lát"
items = re.findall(r'recipe:\s*"([^"]+)"', content)
for item in items:
    if 'ml' in item or 'trái' in item or 'quả' in item or 'lát' in item or 'bông' in item or 'giọt' in item:
        print(item)

