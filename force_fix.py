import re

with open('src/recipesData.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find the exact block around Xoài Chín
pattern = r'(Sữa Hạt Sen Xoài Chín.*?\}\s*\])\s*,\s*\{\s*groupName:\s*"11\.'
replacement = r'\1\n  },\n  {\n    groupName: "11.'
content = re.sub(pattern, replacement, content)

with open('src/recipesData.ts', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done force fix")
