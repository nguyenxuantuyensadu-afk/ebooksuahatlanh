import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

old_minus = "onClick={(e) => { e.stopPropagation(); setRecipeMultiplier(prev => Math.max(0.5, prev - 0.5)); }}"
new_minus = "onClick={(e) => { e.stopPropagation(); setRecipeMultiplier(prev => prev === 0.5 ? 0.3 : (prev <= 0.3 ? 0.3 : prev - 0.5)); }}"

old_plus = "onClick={(e) => { e.stopPropagation(); setRecipeMultiplier(prev => prev + 0.5); }}"
new_plus = "onClick={(e) => { e.stopPropagation(); setRecipeMultiplier(prev => prev === 0.3 ? 0.5 : prev + 0.5); }}"

if old_minus in content and old_plus in content:
    content = content.replace(old_minus, new_minus)
    content = content.replace(old_plus, new_plus)
    with open('src/App.tsx', 'w') as f:
        f.write(content)
    print("Updated successfully")
else:
    print("Could not find the target strings")
