import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

content = content.replace("const recipeCard = document.getElementById(`recipe-${id}`);", "const recipeCard = document.getElementById(`recipe-${id}`) as HTMLElement;")

with open('src/App.tsx', 'w') as f:
    f.write(content)
