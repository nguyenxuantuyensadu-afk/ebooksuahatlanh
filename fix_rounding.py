import re

with open('src/App.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

old_code = """                                        const val = parseFloat(num) * recipeMultiplier;
                                        // format to remove trailing .0 if integer
                                        const displayVal = val % 1 === 0 ? val : val.toFixed(1);"""

new_code = """                                        const val = parseFloat(num) * recipeMultiplier;
                                        // làm tròn số nguyên liệu
                                        const displayVal = Math.round(val);"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('src/App.tsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated App.tsx successfully.")
else:
    print("Could not find the target code in App.tsx")
