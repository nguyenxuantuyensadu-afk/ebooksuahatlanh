import re

with open('src/data.ts', 'r') as f:
    content = f.read()

old_menu = """      id: "menu",
      title: "3. Thiết kế Menu Tối Ưu",
      icon: Coffee,
      description: "Phân khúc 15.000đ - 25.000đ: Đánh mạnh vào tệp khách hàng mua dùng hàng ngày (dân văn phòng, học sinh, người nội trợ). Menu cần ít món nhưng chất lượng, dễ chuẩn bị số lượng lớn.",
      menuStrategy: {"""

new_menu = """      id: "menu",
      title: "3. Thiết kế Menu Tối Ưu",
      icon: Coffee,
      description: "Phân khúc 15.000đ - 25.000đ: Đánh mạnh vào tệp khách hàng mua dùng hàng ngày (dân văn phòng, học sinh, người nội trợ). Menu cần ít món nhưng chất lượng, dễ chuẩn bị số lượng lớn.",
      targetAudience: {
        title: "Xác định khách hàng mục tiêu",
        groups: [
          {
            name: "Nhóm thế hệ trẻ",
            description: "Học sinh, sinh viên, dân văn phòng trẻ thích sự tiện lợi, thức uống có màu sắc bắt mắt, hương vị đậm đà và mới lạ. Bắt trend healthy nhưng vẫn cần ngon miệng, bao bì đẹp."
          },
          {
            name: "Những người giảm cân",
            description: "Quan tâm khắt khe đến lượng calo, chuộng sữa hạt không đường hoặc đường ăn kiêng (cỏ ngọt). Ưu tiên sữa ít tinh bột, giàu protein như hạnh nhân, macca, óc chó."
          },
          {
            name: "Mẹ bầu và bỉm sữa",
            description: "Tìm kiếm dinh dưỡng sạch, an toàn, giàu canxi, sắt, omega-3 tốt cho thai nhi và gọi sữa mẹ. Rất kỹ tính về nguồn gốc nguyên liệu, sẵn sàng chi trả cao cho chất lượng."
          },
          {
            name: "Nhóm dị ứng đạm và đường trong sữa bò",
            description: "Những người bất dung nạp Lactose, uống sữa bò bị đầy bụng, khó tiêu. Sữa hạt là thức uống dinh dưỡng thay thế hoàn hảo hàng ngày giúp họ yên tâm sử dụng."
          }
        ]
      },
      menuStrategy: {"""

content = content.replace(old_menu, new_menu)

with open('src/data.ts', 'w') as f:
    f.write(content)
