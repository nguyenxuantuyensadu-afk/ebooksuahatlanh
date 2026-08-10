import re

with open('src/data.ts', 'r') as f:
    content = f.read()

old_block = """            { name: "Sữa hạt điều cacao", price: "28.000đ" }
          ]
        }
      ]    },"""

new_block = """            { name: "Sữa hạt điều cacao", price: "28.000đ" }
          ]
        }
      ],
      menuTips: {
        title: "Mẹo thiết kế menu tăng doanh số",
        tips: [
          {
            title: "Nguyên tắc vị trí",
            content: "Đặt các món mang lại lợi nhuận cao nhất ở góc trên cùng bên phải hoặc giữa menu, vì đó là nơi mắt khách hàng thường tập trung đầu tiên."
          },
          {
            title: "Tên món hấp dẫn",
            content: "Sử dụng các từ ngữ miêu tả hương vị, xuất xứ. Ví dụ thay vì 'Sữa bắp', hãy dùng 'Sữa bắp nếp non lá dứa' hoặc 'Sữa bắp macchiato'."
          },
          {
            title: "Hiệu ứng chim mồi (Decoy Effect)",
            content: "Đưa ra mức giá size Lớn chỉ nhỉnh hơn size Vừa một chút (vd: Size M 25k, Size L 29k) để hướng khách hàng chọn size Lớn."
          },
          {
            title: "Tối giản ký hiệu tiền tệ",
            content: "Sử dụng '25k' hoặc '25' thay vì '25.000 VNĐ' giúp giảm bớt rào cản tâm lý về việc tiêu tiền của khách hàng."
          },
          {
            title: "Tạo Combo giá trị",
            content: "Kết hợp bán sữa hạt kèm bánh ngọt ăn sáng, hoặc combo gia đình (Mua 3 tặng 1) để tăng giá trị trung bình đơn hàng."
          }
        ]
      }
    },"""

content = content.replace(old_block, new_block)

with open('src/data.ts', 'w') as f:
    f.write(content)
