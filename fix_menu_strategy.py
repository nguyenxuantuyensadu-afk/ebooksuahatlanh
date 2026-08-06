import re

with open('src/data.ts', 'r') as f:
    content = f.read()

menu_strategy_data = """      menuStrategy: {
        title: "Bí quyết làm menu tối ưu hoá lợi nhuận",
        description: "Phân bổ danh mục đồ uống theo thuật toán tỷ lệ vàng giúp tối đa hóa doanh thu và đánh lừa thị giác (Hiệu ứng chim mồi).",
        strategies: [
          {
            name: "Món Thu Hút Khách (Traffic Builder)",
            percentage: "20%",
            priceLevel: "Thấp - Cạnh tranh",
            role: "Sản phẩm phễu, giá rẻ, dễ uống, cực thơm để kéo khách mới.",
            examples: "Sữa bắp nếp, Sữa đậu nành lá dứa (12.000đ - 15.000đ)"
          },
          {
            name: "Món Mồi Nhử (Decoy)",
            percentage: "10%",
            priceLevel: "Thấp - Mức giá lấp lửng",
            role: "Sản phẩm làm nền, kích thích khách hàng chọn món chính có biên lợi nhuận cao hơn vì thấy 'hời' hơn.",
            examples: "Sữa hạt mix cơ bản size nhỏ (chênh giá ít so với size lớn)"
          },
          {
            name: "Món Chính Lợi Nhuận (Cash Cow)",
            percentage: "60%",
            priceLevel: "Trung bình khá",
            role: "Sản phẩm bán chạy nhất, mang lại 80% lợi nhuận. Chi phí cost thấp nhưng giá trị cảm nhận cao.",
            examples: "Sữa đậu xanh cốt dừa, Sữa gạo lứt huyết rồng (18.000đ - 20.000đ)"
          },
          {
            name: "Món Cao Cấp (Premium / Anchor)",
            percentage: "10%",
            priceLevel: "Cao",
            role: "Mỏ neo giá, giúp các món ở mức giá trung bình trông có vẻ rẻ và hợp lý hơn. Phục vụ nhóm khách cao.",
            examples: "Sữa hạnh nhân macca, Sữa hạt điều mix saffron (25.000đ - 35.000đ)"
          }
        ]
      },
"""

target = """      menuItems: ["""
if target in content and "menuStrategy:" not in content:
    content = content.replace(target, menu_strategy_data + target)
    with open('src/data.ts', 'w') as f:
        f.write(content)
    print("Added menu strategy to data.ts")
else:
    print("Target not found or already added")
