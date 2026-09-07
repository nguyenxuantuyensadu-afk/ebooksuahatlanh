import re

with open('src/recipesData.ts', 'r', encoding='utf-8') as f:
    content = f.read()

new_groups = """,
  {
    groupName: "11. Nhóm Dành Cho Mẹ Bầu (An Thai, Lợi Sữa)",
    groupDesc: "Giàu Omega 3, Canxi, Axit Folic, Sắt giúp thai nhi phát triển trí não và mẹ bầu giảm nghén, lợi sữa sau sinh.",
    recipes: [
      { name: "Sữa Óc Chó Mè Đen", recipe: "Óc chó (60g) + Mè đen (40g) + 1000ml nước", usage: "Cung cấp Omega 3, phát triển trí não thai nhi.", prepTip: "Mè đen rang thơm, óc chó ngâm 4h. Xay kỹ lọc bã." },
      { name: "Sữa Hạnh Nhân Macca Đậu Xanh", recipe: "Hạnh nhân (40g) + Macca (30g) + Đậu xanh (30g) + 1000ml nước", usage: "Chống dị tật thai nhi nhờ Axit Folic cao, vị béo dịu.", prepTip: "Đậu xanh nấu chín nhừ, xay chung macca và hạnh nhân ngâm." },
      { name: "Sữa Đậu Lăng Óc Chó", recipe: "Đậu lăng (60g) + Óc chó (40g) + 1000ml nước", usage: "Ngăn ngừa tiểu đường thai kỳ, kiểm soát cân nặng.", prepTip: "Đậu lăng ngâm 4h đun chín, óc chó sống xay chung." },
      { name: "Sữa Mè Đen Gạo Lứt", recipe: "Mè đen (50g) + Gạo lứt (50g) + 1000ml nước", usage: "Gọi sữa về ướt áo cho mẹ sau sinh, giàu canxi.", prepTip: "Gạo lứt và mè đen rang chín thơm, đun lấy nước cốt xay." },
      { name: "Sữa Hạt Sen Đậu Xanh", recipe: "Hạt sen (50g) + Đậu xanh (50g) + 1000ml nước", usage: "An thai, giảm ốm nghén, giúp mẹ bầu ngủ ngon.", prepTip: "Sen và đậu xanh hầm nhừ nhuyễn, xay sánh đặc." },
      { name: "Sữa Hạt Điều Kỷ Tử", recipe: "Hạt điều (90g) + Kỷ tử (10g) + 1000ml nước", usage: "Bổ máu, giảm hoa mắt chóng mặt khi mang thai.", prepTip: "Kỷ tử nấu chín mềm đun ra nước, xay chung hạt điều ngâm mềm." },
      { name: "Sữa Macca Hạt Sen", recipe: "Macca (50g) + Hạt sen (50g) + 1000ml nước", usage: "Thơm béo nhẹ, dễ uống, giảm căng thẳng.", prepTip: "Hạt sen đun chín vừa, macca xay sống giúp giữ độ béo ngậy." },
      { name: "Sữa Yến Mạch Óc Chó", recipe: "Yến mạch (60g) + Óc chó (40g) + 1000ml nước", usage: "Lợi sữa, chống táo bón hiệu quả thai kỳ.", prepTip: "Yến mạch ngâm nở sơ đun mềm, óc chó xay sống." },
      { name: "Sữa Hạt Điều Chà Là", recipe: "Hạt điều (80g) + Chà là (20g) + 1000ml nước", usage: "Bổ sung sắt dồi dào, thay thế đường phèn.", prepTip: "Chà là ngâm mềm bỏ hạt, xay nhuyễn tự tạo độ ngọt dịu." },
      { name: "Sữa Hạnh Nhân Bí Đỏ", recipe: "Hạnh nhân (40g) + Bí đỏ (60g) + 1000ml nước", usage: "Sáng mắt, tăng cường hệ miễn dịch tự nhiên.", prepTip: "Bí đỏ hấp chín mềm, xay mịn với hạnh nhân ngâm bỏ vỏ lụa." }
    ]
  },
  {
    groupName: "12. Nhóm Dành Cho Giới Trẻ (Trendy & Boba)",
    groupDesc: "Bắt kịp xu hướng, mix vị lạ miệng, đậm đà, màu sắc bắt mắt, phù hợp làm thức uống giải khát hoặc healthy boba.",
    recipes: [
      { name: "Sữa Macca Matcha Trân Châu", recipe: "Macca (100g) + Matcha (5g) + Trân châu trắng (Topping) + 1000ml nước", usage: "Tỉnh táo, healthy boba thay thế trà sữa.", prepTip: "Macca xay nền, matcha hòa nước ấm, thêm trân châu giòn." },
      { name: "Sữa Hạt Điều Khoai Lang Tím", recipe: "Hạt điều (50g) + Khoai lang tím (50g) + 1000ml nước", usage: "Màu tím pastel siêu hot trend, vị bùi béo.", prepTip: "Khoai lang tím luộc chín, xay cùng hạt điều ngâm mềm." },
      { name: "Sữa Hạnh Nhân Cacao Cốt Dừa", recipe: "Hạnh nhân (100g) + Cacao (10g) + Cốt dừa (30ml) + 1000ml nước", usage: "Chuẩn vị dark chocolate béo ngậy cuốn hút.", prepTip: "Hạnh nhân xay sánh mịn, hòa cacao ấm và thêm cốt dừa cuối." },
      { name: "Sữa Gạo Lứt Trân Châu Đường Đen", recipe: "Gạo lứt (100g) + Trân châu đen (Topping) + 1000ml nước", usage: "Vị trà sữa trân châu nhưng tốt cho sức khỏe.", prepTip: "Gạo lứt rang kỹ đun đặc, trân châu đen nấu đường đen phủ lên." },
      { name: "Sữa Yến Mạch Bơ Dừa", recipe: "Yến mạch (100g) + Bơ sáp (50g) + Cốt dừa (20ml) + 1000ml nước", usage: "Néo ngậy cực độ, món ruột của hội ghiền béo.", prepTip: "Yến mạch nấu chín mềm, xay với bơ tươi và cốt dừa." },
      { name: "Sữa Hạt Điều Cà Phê", recipe: "Hạt điều (100g) + Bột cà phê đen (5g) + 1000ml nước", usage: "Vị cà phê sữa hạt thơm lừng, năng lượng buổi sáng.", prepTip: "Hạt điều xay sống béo ngậy, pha chút espresso hoặc cà phê pha phin." },
      { name: "Sữa Hạnh Nhân Việt Quất", recipe: "Hạnh nhân (70g) + Việt quất tươi (30g) + 1000ml nước", usage: "Màu tím mộng mơ, chua chua ngọt ngọt tươi mới.", prepTip: "Việt quất xay nhuyễn trộn vào cốt sữa hạnh nhân đã nguội." },
      { name: "Sữa Macca Vani Kem Muối", recipe: "Macca (100g) + Vani (1 giọt) + Lớp kem mặn (Topping) + 1000ml nước", usage: "Vị béo vani phủ kem muối mặn mặn cực bén.", prepTip: "Macca xay sống thêm vani, dùng foam macchiato muối bên trên." },
      { name: "Sữa Đậu Phộng Socola Dăm", recipe: "Đậu phộng (100g) + Socola đen (15g) + 1000ml nước", usage: "Đậm đà hương bơ đậu phộng và sô-cô-la.", prepTip: "Đậu phộng rang chín kỹ, xay mịn hòa cùng sốt socola chảy." },
      { name: "Sữa Óc Chó Khoai Môn Trân Châu", recipe: "Óc chó (40g) + Khoai môn (60g) + Trân châu (Topping) + 1000ml nước", usage: "Vị béo khoai môn sáp dẻo quánh, topping vui miệng.", prepTip: "Khoai môn hấp chín dẻo, xay chung óc chó ngâm, thả trân châu." }
    ]
  },
  {
    groupName: "13. Nhóm Hỗ Trợ Tim Mạch (Giảm Cholesterol)",
    groupDesc: "Ưu tiên các hạt giàu Omega 3-6-9, chất béo không bão hòa đơn giúp giảm cholesterol xấu, bảo vệ thành mạch, hạ huyết áp.",
    recipes: [
      { name: "Sữa Hạnh Nhân Óc Chó", recipe: "Hạnh nhân (50g) + Óc chó (50g) + 1000ml nước", usage: "Giảm mỡ máu, bảo vệ trái tim khỏe mạnh.", prepTip: "Cả hai hạt ngâm kỹ, hạnh nhân bóc vỏ, xay lấy cốt sữa sống." },
      { name: "Sữa Đậu Nành Hạt Chia", recipe: "Đậu nành (80g) + Hạt chia (20g) + 1000ml nước", usage: "Giàu isoflavone và omega 3, hạ huyết áp.", prepTip: "Đậu nành đun sôi chín kỹ, hạt chia ngâm nở pha vào sau." },
      { name: "Sữa Yến Mạch Hạnh Nhân", recipe: "Yến mạch (50g) + Hạnh nhân (50g) + 1000ml nước", usage: "Cung cấp Beta-glucan giảm hấp thụ cholesterol.", prepTip: "Yến mạch đun mềm, hạnh nhân sống xay hòa quyện." },
      { name: "Sữa Hạt Điều Táo Đỏ", recipe: "Hạt điều (80g) + Táo đỏ (20g) + 1000ml nước", usage: "Bổ khí huyết, tuần hoàn máu tốt, tim đập ổn định.", prepTip: "Táo đỏ bỏ hạt đun lấy cốt ngọt, xay cùng hạt điều ngâm sống." },
      { name: "Sữa Gạo Lứt Óc Chó", recipe: "Gạo lứt (50g) + Óc chó (50g) + 1000ml nước", usage: "Kiểm soát mỡ máu tuyệt vời, thanh lọc cơ thể.", prepTip: "Gạo lứt rang chín đun lấy nước, xay cùng óc chó sống béo ngậy." },
      { name: "Sữa Macca Mè Đen", recipe: "Macca (50g) + Mè đen (50g) + 1000ml nước", usage: "Nguồn chất béo thực vật lý tưởng cho tim mạch.", prepTip: "Mè đen rang chín kĩ, macca sống, xay nhuyễn không cần đun thêm." },
      { name: "Sữa Đậu Đen Óc Chó", recipe: "Đậu đen (60g) + Óc chó (40g) + 1000ml nước", usage: "Chống oxy hóa thành mạch, thanh nhiệt giải độc.", prepTip: "Đậu đen hầm chín nhừ, xay chung óc chó chưa rang." },
      { name: "Sữa Hạt Sen Macca", recipe: "Hạt sen (60g) + Macca (40g) + 1000ml nước", usage: "Giúp nhịp tim ổn định, an thần, ngủ sâu giấc.", prepTip: "Hạt sen luộc chín bở, xay cùng macca béo ngọt tự nhiên." },
      { name: "Sữa Quinoa Hạnh Nhân", recipe: "Quinoa (50g) + Hạnh nhân (50g) + 1000ml nước", usage: "Đạm hoàn chỉnh, duy trì cơ tim săn chắc.", prepTip: "Quinoa luộc kỹ loại bỏ vỏ đắng, xay chung hạnh nhân." },
      { name: "Sữa Yến Mạch Đậu Lăng", recipe: "Yến mạch (50g) + Đậu lăng đỏ (50g) + 1000ml nước", usage: "Ngừa xơ vữa động mạch, rất dồi dào chất xơ.", prepTip: "Đậu lăng đỏ và yến mạch đều đun chín mềm rồi xay mịn." }
    ]
  },
  {
    groupName: "14. Nhóm Hỗ Trợ Tiểu Đường (Chỉ số GI thấp)",
    groupDesc: "Không sử dụng đường tinh luyện (dùng cỏ ngọt hoặc chà là lượng ít), hạt có chỉ số đường huyết thấp giúp ổn định đường huyết.",
    recipes: [
      { name: "Sữa Gạo Lứt Đậu Đen", recipe: "Gạo lứt (50g) + Đậu đen (50g) + 1000ml nước", usage: "Giải độc gan, kiểm soát đường huyết sau ăn rất tốt.", prepTip: "Gạo lứt đỏ rang thơm, đậu đen nấu mềm, không thêm đường." },
      { name: "Sữa Yến Mạch Mè Đen", recipe: "Yến mạch (60g) + Mè đen (40g) + 1000ml nước", usage: "No lâu, không gây tăng đường huyết đột ngột.", prepTip: "Mè đen rang kỹ, yến mạch đun chín, có thể dùng đường cỏ ngọt." },
      { name: "Sữa Hạnh Nhân Đậu Nành", recipe: "Hạnh nhân (50g) + Đậu nành (50g) + 1000ml nước", usage: "Carb cực thấp, giàu đạm thực vật, an toàn tuyệt đối.", prepTip: "Đậu nành đun sôi kỹ 15p, hạnh nhân xay sống vắt lấy cốt." },
      { name: "Sữa Quinoa Đậu Đỏ", recipe: "Quinoa (50g) + Đậu đỏ (50g) + 1000ml nước", usage: "Bổ máu, ổn định insulin, hương vị đậm đà.", prepTip: "Cả Quinoa và đậu đỏ đều cần đun chín kỹ trước khi xay mịn." },
      { name: "Sữa Đậu Gà Mè Trắng", recipe: "Đậu gà (70g) + Mè trắng (30g) + 1000ml nước", usage: "Chất xơ hòa tan cao, cản trở hấp thu đường vào máu.", prepTip: "Đậu gà ngâm 12h luộc chín mềm, mè trắng rang thơm." },
      { name: "Sữa Đậu Lăng Xanh Hạt Chia", recipe: "Đậu lăng xanh (80g) + Hạt chia (20g) + 1000ml nước", usage: "Chỉ số GI thấp nhất trong các loại đậu, no cực lâu.", prepTip: "Đậu lăng xanh luộc chín, hạt chia ngâm nở pha riêng." },
      { name: "Sữa Hạt Sen Đậu Đen", recipe: "Hạt sen (50g) + Đậu đen (50g) + 1000ml nước", usage: "Mát gan, không làm biến động đường huyết.", prepTip: "Hai nguyên liệu đều hầm chín kỹ, dùng cỏ ngọt tạo vị thanh." },
      { name: "Sữa Óc Chó Yến Mạch", recipe: "Óc chó (50g) + Yến mạch (50g) + 1000ml nước", usage: "Tốt cho trí não và kiểm soát đường huyết kép.", prepTip: "Yến mạch nấu chín, óc chó sống xay chung, không cần rây lọc." },
      { name: "Sữa Macca Cải Bó Xôi", recipe: "Macca (60g) + Cải bó xôi (40g) + 1000ml nước", usage: "Giàu vitamin khoáng chất, lượng carb gần như bằng không.", prepTip: "Cải bó xôi ép/lấy cốt xay hòa cùng sữa macca sống mát." },
      { name: "Sữa Hạt Điều Mướp Đắng", recipe: "Hạt điều (80g) + Mướp đắng (20g) + 1000ml nước", usage: "Mướp đắng (khổ qua) hỗ trợ điều hòa insulin tuyệt vời.", prepTip: "Mướp đắng trụng nước sôi giảm đắng, xay chung hạt điều ngâm." }
    ]
  }
];"""

content = content.replace("  }\n];", new_groups)

with open('src/recipesData.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("Appended new groups successfully.")
