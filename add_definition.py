import re

with open('src/data.ts', 'r', encoding='utf-8') as f:
    content = f.read()

definition_str = """      description: "Kiến thức cơ bản về thành phần dinh dưỡng của các loại hạt và phân loại thời gian ngâm hạt tiêu chuẩn, giúp bảo toàn dưỡng chất và loại bỏ các chất gây ức chế enzyme (như Phytic Acid).",
      definition: {
        title: "Sữa Hạt Là Gì?",
        content: [
          "Sữa hạt là thức uống được chế biến từ các loại hạt (hạt dinh dưỡng, ngũ cốc, đậu đỗ...) bằng phương pháp ngâm, xay nhuyễn kết hợp với nước, sau đó lọc bã hoặc giữ nguyên bã (tùy loại hạt và công thức).",
          "Về bản chất, đây không phải là sữa tiết ra từ động vật, mà là tên gọi thông dụng để chỉ \"nước ép/dịch chiết từ hạt\" có kết cấu sánh mịn và màu đục tương tự như sữa.",
          "Sữa hạt được xem là nguồn cung cấp dồi dào vitamin, khoáng chất, chất béo tốt (Omega 3-6-9) và protein thực vật. Thức uống này hoàn toàn không chứa Cholesterol và đường Lactose, cực kỳ phù hợp cho người dị ứng đạm sữa bò, người ăn thuần chay hoặc người muốn duy trì vóc dáng và sức khỏe toàn diện."
        ]
      },
      nutritionData:"""

content = content.replace('      description: "Kiến thức cơ bản về thành phần dinh dưỡng của các loại hạt và phân loại thời gian ngâm hạt tiêu chuẩn, giúp bảo toàn dưỡng chất và loại bỏ các chất gây ức chế enzyme (như Phytic Acid).",\n      nutritionData:', definition_str)

with open('src/data.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added definition to data.ts")
