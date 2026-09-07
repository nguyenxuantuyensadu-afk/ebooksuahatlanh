import re

with open('src/recipesData.ts', 'r', encoding='utf-8') as f:
    content = f.read()

new_group = """    ]
  },
  {
    groupName: "15. Các Món Khác Từ Hạt (Smoothie, Bơ, Sữa Đặc...)",
    groupDesc: "Ứng dụng đa dạng khác từ hạt dinh dưỡng như làm sữa đặc thuần chay, bơ hạt, kem, trà sữa hạt và smoothie giúp tận dụng tối đa nguyên liệu.",
    recipes: [
      { name: "Sữa Đặc Hạt Điều", recipe: "Hạt điều (200g) + Nước ấm (200ml) + Chà là (100g)", usage: "Sữa đặc thuần chay thơm ngậy, dùng pha cà phê hoặc ăn bánh mì.", prepTip: "Hạt điều ngâm mềm, xay thật nhuyễn với chà là và chút nước ấm." },
      { name: "Kem Hạt Dẻ Cười (Pistachio)", recipe: "Hạt dẻ cười (100g) + Cốt dừa (200ml) + Chuối cấp đông (2 quả)", usage: "Món tráng miệng mát lạnh, béo ngậy không cần máy làm kem.", prepTip: "Xay dẻ cười với cốt dừa trước, sau đó cho chuối đông đá vào xay dẻo mịn." },
      { name: "Bơ Hạnh Nhân Nguyên Chất", recipe: "Hạnh nhân rang (200g) + Dầu oliu (10ml) + Muối hồng (1g)", usage: "Phết bánh mì hoặc làm sốt, giàu vitamin E, tốt cho tim mạch.", prepTip: "Rang hạnh nhân thơm, xay liên tục đến khi tươm dầu tự nhiên." },
      { name: "Trà Sữa Hạt Macca", recipe: "Macca (100g) + Cốt hồng trà (800ml) + Đường đen (20g)", usage: "Trà sữa thuần chay đậm đà vị trà, béo ngậy vị macca.", prepTip: "Xay macca trực tiếp bằng cốt hồng trà, thêm đường đen tùy khẩu vị." },
      { name: "Smoothie Yến Mạch Dâu Tây", recipe: "Yến mạch (50g) + Dâu tây (100g) + 800ml nước", usage: "Bữa sáng tiện lợi, giàu chất xơ, vitamin C và năng lượng.", prepTip: "Yến mạch rang sơ, dâu tây cấp đông, xay nhuyễn mịn không rây lọc." },
      { name: "Smoothie Hạt Điều Xoài Chín", recipe: "Hạt điều (50g) + Xoài chín (100g) + 800ml nước", usage: "Giải khát ngày hè, cực béo thơm vị xoài nhiệt đới.", prepTip: "Hạt điều ngâm mềm xay làm nền, thêm xoài chín cấp đông xay sánh." },
      { name: "Cà Phê Macchiato Hạt Điều", recipe: "Hạt điều (100g) + Cà phê (50ml) + 800ml nước", usage: "Sữa hạt điều béo ngậy kết hợp với shot espresso tỉnh táo.", prepTip: "Xay hạt điều làm nền, sau đó đổ nhẹ shot cà phê lên trên." },
      { name: "Trà Matcha Sữa Óc Chó", recipe: "Óc chó (100g) + Bột Matcha (5g) + 1000ml nước ấm", usage: "Thức uống detox nhẹ, chống oxy hóa, thư giãn tinh thần.", prepTip: "Óc chó ngâm 4h xay cốt nền, hòa tan matcha với nước ấm đổ vào." },
      { name: "Sốt Salad Hạt Macca", recipe: "Macca (100g) + Dầu oliu (20ml) + Chanh (1 quả) + Nước lọc (50ml)", usage: "Sốt trộn salad thuần chay, chua béo hài hòa.", prepTip: "Xay mịn tất cả nguyên liệu, thêm tiêu và muối hồng cho đậm đà." },
      { name: "Bơ Đậu Phộng Cacao", recipe: "Đậu phộng rang (200g) + Cacao (10g) + Mật ong (20ml)", usage: "Món ăn kèm bữa sáng, thơm nức mùi socola đậu phộng.", prepTip: "Xay đậu phộng tươm dầu, sau đó trộn đều cùng bột cacao và mật ong." }
    ]
  }
];"""

content = content.replace("    ]\n  }\n];", new_group)

with open('src/recipesData.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("Appended group 15 successfully.")
