import re

with open('src/data.ts', 'r') as f:
    content = f.read()

equipment_start = r'      equipmentCategories: \['
equipment_end = r'      \]\n    \},'

# We'll use a regex to replace the equipmentCategories block
match = re.search(equipment_start + r'.*?' + equipment_end, content, re.DOTALL)
if match:
    new_equipment = """      equipmentCategories: [
        {
          name: "Nhóm Dụng Cụ Sản Xuất & Pha Chế",
          items: [
            { name: "Máy làm sữa hạt bán công nghiệp", desc: "Dung tích 1.75L - 2L, công suất lớn (xay & nấu kết hợp). Khuyên dùng máy có lồng cản âm để giảm tiếng ồn khi xay." },
            { name: "Nồi inox đáy dày (3-5 lớp)", desc: "Dung tích 10L-20L, chuyên dụng để nấu thanh trùng sữa với số lượng lớn mà không bị bén đáy/khê." },
            { name: "Bếp từ công nghiệp hoặc Bếp gas mini", desc: "Đảm bảo gia nhiệt nhanh chóng và ổn định khi cần đun sôi, nấu sữa trực tiếp." },
            { name: "Túi lọc sữa & Rây inox", desc: "Túi vải nilon mắt lưới siêu mịn giúp sữa mượt không lợn cợn. Rây inox dùng để lọc thô trước." },
            { name: "Cân tiểu ly điện tử", desc: "Độ chính xác 0.1g, thiết yếu để cân chuẩn xác tỉ lệ hạt, đường, muối cho đồng đều chất lượng mỗi mẻ." },
            { name: "Ca đong định lượng (Pitcher)", desc: "Các kích cỡ 1L, 2L, 5L, chất liệu nhựa an toàn trong suốt có vạch chia ml rõ ràng." },
            { name: "Nhiệt kế thực phẩm (Que đo nhiệt)", desc: "Kiểm soát nhiệt độ thanh trùng và nhiệt độ ủ lạnh, tránh sữa bị chua do sốc nhiệt." },
            { name: "Phới lồng (Whisk) cỡ lớn", desc: "Dùng để khuấy đều hỗn hợp sữa, đường phèn, cốt dừa... giúp hòa tan nhanh chóng." },
            { name: "Thau, rổ, khay Inox", desc: "Dùng để ngâm hạt qua đêm, rửa hạt và phơi ráo nước, đảm bảo vệ sinh ATTP." }
          ]
        },
        {
          name: "Nhóm Dụng Cụ Vận Hành & Bán Hàng",
          items: [
            { name: "Xe đẩy bán hàng (Inox 304)", desc: "Kích thước 1.2m - 1.5m, bánh xe xoay 360 độ, có mái che. Dán decal nổi bật thương hiệu bao quanh xe." },
            { name: "Thùng đá giữ nhiệt", desc: "Dung tích 50L - 70L, loại 2-3 lớp cách nhiệt tốt. Dùng để ướp lạnh chai sữa, giữ nhiệt độ 2-4 độ C suốt ca bán." },
            { name: "Chai nhựa PET & Nắp niêm phong", desc: "Chai nhựa dáng vuông, tròn mập (330ml/500ml). Nắp khóa niêm phong tạo sự chuyên nghiệp và an toàn." },
            { name: "Tem nhãn Decal (Chống nước)", desc: "In logo thương hiệu, có ô để tích/ghi ngày sản xuất, hạn sử dụng. Bắt buộc dùng loại decal nhựa chống thấm nước." },
            { name: "Túi đựng mang đi (Takeaway)", desc: "Túi chữ T tiết kiệm chi phí, dễ xách; hoặc túi giấy kraft thân thiện với môi trường, sang trọng hơn." },
            { name: "Bảng Menu & Decor quầy", desc: "Menu mica để bàn hoặc bảng đen viết phấn nhỏ. Thêm một số vật dụng decor: dây đèn LED, bình hoa nhỏ, thảm cỏ giả lót mặt quầy." },
            { name: "Dụng cụ vệ sinh tại quầy", desc: "Khăn lau Microfiber sạch, bình xịt cồn 70 độ sát khuẩn, thùng rác mini có nắp đậy." },
            { name: "Tạp dề & Đồng phục", desc: "Tạp dề canvas hoặc kaki có in/thêu logo, mũ đội đầu, găng tay y tế, giúp tăng độ uy tín và sạch sẽ trong mắt khách hàng." }
          ]
        }
      ]
    },"""
    content = content[:match.start()] + new_equipment + content[match.end():]
    with open('src/data.ts', 'w') as f:
        f.write(content)
    print("Replaced equipment data.")
else:
    print("Could not find equipment module.")
