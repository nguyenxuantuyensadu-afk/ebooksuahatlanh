import re

with open('src/recipesData.ts', 'r', encoding='utf-8') as f:
    content = f.read()

def round_number(match):
    num_str = match.group(1)
    unit = match.group(2)
    rounded_num = round(float(num_str))
    return f"{rounded_num}{unit}"

# Find any decimal number followed by g or ml
new_content = re.sub(r'(\d+\.\d+)(g|ml)', round_number, content)

with open('src/recipesData.ts', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Rounded numbers successfully.")
