import re

with open('src/App.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix broken newlines in string literals
content = content.replace('Thành Tiền (VNĐ)"\n', 'Thành Tiền (VNĐ)\\n"')
content = content.replace('csvContent += rowArray.join(",") + "\n";', 'csvContent += rowArray.join(",") + "\\n";')
content = content.replace('csvContent += `\nTổng Chi Phí Mẻ', 'csvContent += `\\nTổng Chi Phí Mẻ')
content = content.replace('chai\n`;', 'chai\\n`;')
content = content.replace('toFixed(0)}\n`;', 'toFixed(0)}\\n`;')

with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed strings")
