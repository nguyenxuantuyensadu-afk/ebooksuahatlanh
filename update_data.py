import re

with open('src/data.ts', 'r') as f:
    content = f.read()

old_sweeteners_data = """      sweeteners: [
        { name: "Chà là", type: "Trái cây khô", calories: 28, note: "Tạo ngọt tự nhiên, nhiều chất xơ" },
        { name: "Kỷ tử", type: "Trái cây khô", calories: 35, note: "Vị ngọt nhẹ, bổ mắt, đẹp da" },
        { name: "Mứt trái cây", type: "Mứt", calories: 28, note: "Thơm mùi trái cây, lượng calo thay đổi theo loại" },
        { name: "Bột cỏ ngọt (Stevia)", type: "Chiết xuất", calories: 0, note: "Không calo, không tăng đường huyết" },
        { name: "Mật ong", type: "Mật tự nhiên", calories: 30, note: "Nhiều vitamin, không hợp nấu nhiệt cao" },
        { name: "Mật mía", type: "Mật tự nhiên", calories: 29, note: "Chứa nhiều khoáng chất (Sắt, Canxi)" },
        { name: "Đường phổi", type: "Đường thô", calories: 40, note: "Vị ngọt thanh, thơm dịu" },
        { name: "Siro lá phong", type: "Siro tự nhiên", calories: 26, note: "Hương vị thơm ngon, giàu kẽm" },
        { name: "Siro cây thùa", type: "Siro tự nhiên", calories: 31, note: "Chỉ số GI thấp, ngọt hơn đường trắng" },
        { name: "Đường thốt nốt", type: "Đường thô", calories: 38, note: "Nhiều vitamin nhóm B, thơm đặc trưng" },
        { name: "Đường phèn", type: "Đường kết tinh", calories: 40, note: "Ngọt thanh mát, tan chậm" },
        { name: "Đường nâu", type: "Đường thô", calories: 38, note: "Còn giữ lại chút mật mía, thơm nhẹ" },
        { name: "Đường mía thô", type: "Đường thô", calories: 38, note: "Ít tinh chế, giàu vi lượng hơn đường trắng" }
      ],"""

new_sweeteners_data = """      sweeteners: [
        { name: "Chà là", type: "Trái cây khô", calories: 28, note: "Tạo ngọt tự nhiên, nhiều chất xơ", prepTip: "Bỏ hạt, ngâm mềm (nếu cứng), xay nhuyễn cùng hạt trước khi nấu." },
        { name: "Kỷ tử", type: "Trái cây khô", calories: 35, note: "Vị ngọt nhẹ, bổ mắt, đẹp da", prepTip: "Rửa sạch, ngâm nước ấm 15p cho mềm, có thể xay cùng hạt hoặc hãm như trà." },
        { name: "Mứt trái cây", type: "Mứt", calories: 28, note: "Thơm mùi trái cây, lượng calo thay đổi theo loại", prepTip: "Nên khuấy vào sữa sau khi đã nấu chín để giữ trọn vẹn hương vị trái cây." },
        { name: "Bột cỏ ngọt (Stevia)", type: "Chiết xuất", calories: 0, note: "Không calo, không tăng đường huyết", prepTip: "Chỉ dùng một lượng rất nhỏ, khuấy vào sau khi sữa chín." },
        { name: "Mật ong", type: "Mật tự nhiên", calories: 30, note: "Nhiều vitamin, không hợp nấu nhiệt cao", prepTip: "Chỉ khuấy vào sữa khi đã nguội bớt (dưới 50 độ C) để không làm mất dưỡng chất." },
        { name: "Mật mía", type: "Mật tự nhiên", calories: 29, note: "Chứa nhiều khoáng chất (Sắt, Canxi)", prepTip: "Có thể nấu chung với sữa hoặc khuấy sau khi sữa chín đều được." },
        { name: "Đường phổi", type: "Đường thô", calories: 40, note: "Vị ngọt thanh, thơm dịu", prepTip: "Đập nhỏ, cho vào nồi nấu cùng sữa cho tan hoàn toàn." },
        { name: "Siro lá phong", type: "Siro tự nhiên", calories: 26, note: "Hương vị thơm ngon, giàu kẽm", prepTip: "Nên cho vào sau cùng, khuấy tan khi sữa đã nguội bớt." },
        { name: "Siro cây thùa", type: "Siro tự nhiên", calories: 31, note: "Chỉ số GI thấp, ngọt hơn đường trắng", prepTip: "Cho vào khuấy tan sau khi sữa đã nấu xong." },
        { name: "Đường thốt nốt", type: "Đường thô", calories: 38, note: "Nhiều vitamin nhóm B, thơm đặc trưng", prepTip: "Cắt nhỏ hoặc đập vụn, đun tan cùng với sữa trong quá trình nấu." },
        { name: "Đường phèn", type: "Đường kết tinh", calories: 40, note: "Ngọt thanh mát, tan chậm", prepTip: "Cho trực tiếp vào nồi đun cùng sữa cho tan, hoặc nấu thành syrup (nước đường) để dễ pha chế." },
        { name: "Đường nâu", type: "Đường thô", calories: 38, note: "Còn giữ lại chút mật mía, thơm nhẹ", prepTip: "Cho trực tiếp vào nồi nấu cùng sữa." },
        { name: "Đường mía thô", type: "Đường thô", calories: 38, note: "Ít tinh chế, giàu vi lượng", prepTip: "Cho trực tiếp vào nồi nấu cùng sữa." }
      ],"""

content = content.replace(old_sweeteners_data, new_sweeteners_data)

with open('src/data.ts', 'w') as f:
    f.write(content)
