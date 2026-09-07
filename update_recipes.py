import re
import json

with open('src/recipesData.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the recipes list. We will replace all recipe strings in place.
# A recipe string looks like: recipe: "Đậu nành (40g) + Mè trắng (20g) + 1 lít nước"
# We want to scale the g and ml so that the main ingredients sum to 100g.
# Actually, I can just replace all of them.

def scale_recipe(match):
    full_string = match.group(1)
    
    # We want to find all (...) patterns with g.
    # E.g. Đậu nành (40g), Mè trắng (20g)
    items = re.findall(r'([A-Za-zÀ-ỹ\s]+)\((\d+(?:\.\d+)?)g\)', full_string)
    
    total_g = 0.0
    for name, amount in items:
        name = name.strip().lower()
        if 'cacao' not in name and 'matcha' not in name and 'nghệ' not in name and 'vỏ cam' not in name and 'quế' not in name:
            total_g += float(amount)
            
    if total_g == 0:
        total_g = 1 # Avoid division by zero if no g found
        
    scale_factor = 100.0 / total_g
    
    def replace_g(m):
        name = m.group(1)
        amount = float(m.group(2))
        unit = m.group(3)
        name_lower = name.strip().lower()
        
        # Don't scale small flavorings as aggressively or scale them the same?
        # Let's scale everything by the same factor so proportions are kept.
        new_amount = amount * scale_factor
        
        # Format cleanly
        if new_amount.is_integer():
            new_amount = int(new_amount)
        else:
            new_amount = round(new_amount, 1)
            
        return f"{name}({new_amount}{unit})"
        
    # Replace all (Xg) 
    new_string = re.sub(r'([A-Za-zÀ-ỹ\s]+)\((\d+(?:\.\d+)?)(g)\)', replace_g, full_string)
    
    # Replace 1 lít nước with 1000ml nước
    new_string = new_string.replace('1 lít nước', '1000ml nước').replace('1 lít nước ấm', '1000ml nước ấm').replace('800ml nước', '800ml nước') # Wait, if it's 800ml, maybe it should be 1000ml?
    # If the user says 300ml water -> 1000ml water is the 1L base. So let's replace any "1 lít nước" with "1000ml nước"
    # Actually, the user multiplier parses "lít" or "ml". If we use "1000ml nước", 1000 * 0.3 = 300ml. Perfect.
    # What about '800ml nước' and '200ml sữa tươi'?
    # It would scale automatically if we leave it, since 200ml * 0.3 = 60ml. 
    # Just need to fix the '1 lít nước' to '1000ml nước'.
    
    return f'recipe: "{new_string}"'

new_content = re.sub(r'recipe:\s*"([^"]+)"', scale_recipe, content)

with open('src/recipesData.ts', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated recipes successfully.")
