import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Make sure UI doesn't crash if yield_info is undefined
old_str = "Thành phẩm: {recipe.yield_info.replace('1 L', recipeMultiplier + ' L').replace('1 Lít', recipeMultiplier + ' Lít')}"
new_str = "Thành phẩm: {(recipe.yield_info || '1 L').replace('1 L', recipeMultiplier + ' L').replace('1 Lít', recipeMultiplier + ' Lít')}"
content = content.replace(old_str, new_str)

with open('src/App.tsx', 'w') as f:
    f.write(content)

print("Protected yield_info against undefined")
