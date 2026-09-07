import re

with open('src/App.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('Thành Tiền (VNĐ)\n";', 'Thành Tiền (VNĐ)\\n";')
content = content.replace('Tổng Chi Phí Mẻ\n', '\\nTổng Chi Phí Mẻ')
content = content.replace('chai\n\n`;', 'chai\\n`;')
content = content.replace('chai\n`;', 'chai\\n`;')
content = content.replace('0)}\n`;', '0)}\\n`;')
content = content.replace('0)}\n\n`;', '0)}\\n`;')

with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed newlines")
