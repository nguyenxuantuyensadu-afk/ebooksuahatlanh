import re

with open('src/App.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'const mergedModule = { ...m, icon: defaultModule?.icon || null };',
    'const mergedModule = { ...defaultModule, ...m, icon: defaultModule?.icon || null };'
)

with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated merge logic")
