import re

with open('src/data.ts', 'r') as f:
    content = f.read()

sample_menus_data = """        ]
      },
      sampleMenus: [
        {
          groupName: "Menu cho Nhóm thế hệ trẻ",
          description: "Tập trung vào sự bắt mắt, hương vị đậm đà và xu hướng mới.",
          items: [
            { name: "Sữa bắp nếp lá dứa macchiato", price: "25.000đ" },
            { name: "Sữa đậu xanh cốt dừa trân châu", price: "22.000đ" },
            { name: "Sữa khoai môn kem cheese", price: "28.000đ" },
            { name: "Sữa gạo lứt đậu đỏ trân châu trắng", price: "25.000đ" },
            { name: "Sữa hạt điều matcha", price: "25.000đ" }
          ]
        },
        {
          groupName: "Menu cho Người giảm cân",
          description: "Calo thấp, sử dụng cỏ ngọt, hạt giàu protein, ít tinh bột.",
          items: [
            { name: "Sữa hạnh nhân nguyên chất (Stevia)", price: "25.000đ" },
            { name: "Sữa óc chó yến mạch hạt chia", price: "30.000đ" },
            { name: "Sữa đậu đen mè đen cỏ ngọt", price: "20.000đ" },
            { name: "Sữa hạt điều cần tây xanh", price: "25.000đ" },
            { name: "Sữa diêm mạch đậu gà", price: "35.000đ" }
          ]
        },
        {
          groupName: "Menu cho Mẹ bầu và bỉm sữa",
          description: "Giàu canxi, sắt, omega-3, vị thanh nhẹ dễ uống, nguyên liệu organic.",
          items: [
            { name: "Sữa óc chó hạnh nhân mè đen", price: "35.000đ" },
            { name: "Sữa hạt sen macca kỷ tử", price: "35.000đ" },
            { name: "Sữa gạo lứt đậu đỏ nảy mầm", price: "25.000đ" },
            { name: "Sữa đậu nành nguyên hạt bí xanh", price: "25.000đ" },
            { name: "Sữa yến mạch chuối hạt chia", price: "30.000đ" }
          ]
        },
        {
          groupName: "Menu cho Nhóm dị ứng đạm bò",
          description: "Hoàn toàn thuần chay, thay thế sữa bò nhưng vẫn đảm bảo canxi và độ ngậy.",
          items: [
            { name: "Sữa đậu nành hạnh nhân", price: "25.000đ" },
            { name: "Sữa yến mạch macca hương vani", price: "30.000đ" },
            { name: "Sữa gạo rang hạt điều", price: "25.000đ" },
            { name: "Sữa hạt sen cốt dừa", price: "25.000đ" },
            { name: "Sữa hạt điều cacao", price: "28.000đ" }
          ]
        }
      ]
    },"""

content = content.replace("        ]\n      }\n    },", sample_menus_data)

with open('src/data.ts', 'w') as f:
    f.write(content)
