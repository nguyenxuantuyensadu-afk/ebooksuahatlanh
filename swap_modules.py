import re

# Update data.ts
with open('src/data.ts', 'r') as f:
    content = f.read()

# Swap in data.ts
# It's tricky with regex, we can just find the blocks and swap them.
menu_block_match = re.search(r'(\s*{\s*id:\s*"menu".*?)(?=\s*{\s*id:\s*"equipment")', content, re.DOTALL)
equipment_block_match = re.search(r'(\s*{\s*id:\s*"equipment".*?)(?=\s*{\s*id:\s*"costing")', content, re.DOTALL)

if menu_block_match and equipment_block_match:
    menu_block = menu_block_match.group(1)
    equipment_block = equipment_block_match.group(1)
    
    # Change titles
    menu_block = menu_block.replace('"2. Thiết kế Menu Tối Ưu"', '"3. Thiết kế Menu Tối Ưu"')
    equipment_block = equipment_block.replace('"3. Danh sách Dụng cụ Setup"', '"2. Danh sách Dụng cụ Setup"')
    
    # Replace in content
    # They are adjacent, so we can replace menu_block + equipment_block with equipment_block + menu_block
    target_blocks = menu_block + equipment_block
    replacement_blocks = equipment_block + menu_block
    
    content = content.replace(target_blocks, replacement_blocks)
    
    with open('src/data.ts', 'w') as f:
        f.write(content)
    print("data.ts swapped successfully")
else:
    print("Could not find blocks in data.ts")

# Update App.tsx
with open('src/App.tsx', 'r') as f:
    app_content = f.read()

# We need to swap courseData.modules[1] and courseData.modules[2]
# To do this safely, we can replace them with placeholders first
app_content = app_content.replace('courseData.modules[1]', 'COURSE_DATA_MODULES_TEMP_2')
app_content = app_content.replace('courseData.modules[2]', 'courseData.modules[1]')
app_content = app_content.replace('COURSE_DATA_MODULES_TEMP_2', 'courseData.modules[2]')

with open('src/App.tsx', 'w') as f:
    f.write(app_content)
print("App.tsx indices swapped successfully")

