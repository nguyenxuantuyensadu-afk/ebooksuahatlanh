import re

with open('src/recipesData.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Recipes that are missing 1000ml nước
fixes = {
    'Yến mạch (66.7g) + Chuối (1 quả) + Bơ đậu phộng (33.3g)"': 'Yến mạch (66.7g) + Chuối (1 quả) + Bơ đậu phộng (33.3g) + 1000ml nước"',
    'Hạt điều (100g) + Gừng (1 lát) + Sả (1 nhánh)"': 'Hạt điều (100g) + Gừng (1 lát) + Sả (1 nhánh) + 1000ml nước"',
    'Hạt điều (100g) + Hoa đậu biếc (5 bông)"': 'Hạt điều (100g) + Hoa đậu biếc (5 bông) + 1000ml nước"',
    'Bắp ngọt (1 trái) + Hạt điều (100g) + Vani (1 giọt)"': 'Bắp ngọt (1 trái) + Hạt điều (100g) + Vani (1 giọt) + 1000ml nước"',
    'Yến mạch (100g) + Cacao (12.5g) + Sữa đặc (20ml)"': 'Yến mạch (100g) + Cacao (12.5g) + Sữa đặc (20ml) + 1000ml nước"',
    'Hạt chia (100g) + Cốt chanh dây (30ml) + Sữa nền"': 'Hạt chia (100g) + Cốt chanh dây (30ml) + 1000ml Sữa nền"',
    'Gạo lứt (57.1g) + Đậu đỏ (42.9g) + Táo đỏ (10g)"': 'Gạo lứt (57.1g) + Đậu đỏ (42.9g) + Táo đỏ (10g) + 1000ml nước"',
}

for old, new in fixes.items():
    content = content.replace(old, new)

with open('src/recipesData.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed missing water")
