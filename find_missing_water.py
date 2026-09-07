import re
with open('src/recipesData.ts', 'r', encoding='utf-8') as f:
    for line in f:
        if 'recipe:' in line and 'nước' not in line.lower() and 'sữa' not in line.lower() and 'Sữa nền' not in line:
            print(line.strip())
