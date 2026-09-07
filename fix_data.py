import re

with open('src/data.ts', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'chỉ "nước ép/dịch chiết từ hạt" có kết cấu',
    'chỉ \\"nước ép/dịch chiết từ hạt\\" có kết cấu'
)

with open('src/data.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed data.ts quotes")
