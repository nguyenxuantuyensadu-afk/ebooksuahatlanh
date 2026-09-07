import { BookOpen, Calculator, CheckCircle2, Coffee, Laptop, LayoutDashboard, Settings, Smartphone, BookText, AlertTriangle, Leaf } from "lucide-react";
import { recipeGroups } from "./recipesData";

export const courseData = {
  title: "KINH DOANH SỮA HẠT THỰC CHIẾN",
  subtitle: "Từ Setup Đến Vận Hành (Mô hình Take-away / Xe đẩy)",
  description: "Module cốt lõi dành cho người khởi nghiệp vốn nhỏ. Hướng dẫn chi tiết cách xây dựng menu có lãi, setup quầy tinh gọn, tính toán giá vốn chuẩn xác và vận hành trơn tru mỗi ngày.",
  modules: [
    {
      id: "nutrition",
      title: "1. Tổng quan Dinh dưỡng & Phân loại Ngâm hạt",
      icon: Leaf,
      description: "Kiến thức cơ bản về thành phần dinh dưỡng của các loại hạt và phân loại thời gian ngâm hạt tiêu chuẩn, giúp bảo toàn dưỡng chất và loại bỏ các chất gây ức chế enzyme (như Phytic Acid).",
      definition: {
        title: "Sữa Hạt Là Gì?",
        content: [
          "Sữa hạt là thức uống được chế biến từ các loại hạt (hạt dinh dưỡng, ngũ cốc, đậu đỗ...) bằng phương pháp ngâm, xay nhuyễn kết hợp với nước, sau đó lọc bã hoặc giữ nguyên bã (tùy loại hạt và công thức).",
          "Về bản chất, đây không phải là sữa tiết ra từ động vật, mà là tên gọi thông dụng để chỉ \"nước ép/dịch chiết từ hạt\" có kết cấu sánh mịn và màu đục tương tự như sữa.",
          "Sữa hạt được xem là nguồn cung cấp dồi dào vitamin, khoáng chất, chất béo tốt (Omega 3-6-9) và protein thực vật. Thức uống này hoàn toàn không chứa Cholesterol và đường Lactose, cực kỳ phù hợp cho người dị ứng đạm sữa bò, người ăn thuần chay hoặc người muốn duy trì vóc dáng và sức khỏe toàn diện."
        ]
      },
      nutritionData: [
        {
          group: "Nhóm Hạt Tạo Béo (Cung cấp năng lượng, độ ngậy)",
          examples: "Macca, Óc chó, Hạnh nhân, Hạt điều, Đậu phộng...",
          role: "Tạo độ sánh mịn, béo ngậy tự nhiên cho sữa mà không cần thêm cốt dừa. Rất giàu Omega 3-6-9 tốt cho tim mạch và não bộ.",
          soakTime: "Macca, Óc chó, Điều tươi: Không cần ngâm hoặc ngâm nhanh 1-2h. Hạnh nhân: 8-12h (phải bóc vỏ lụa)."
        },
        {
          group: "Nhóm Hạt Nền / Tạo Bột (Cung cấp cấu trúc, no lâu)",
          examples: "Yến mạch, Gạo lứt, Hạt sen, Đậu xanh, Đậu đen, Diêm mạch (Quinoa)...",
          role: "Làm chất nền tạo độ sánh đặc cho sữa, giúp no lâu, dồi dào tinh bột phức hợp và chất xơ.",
          soakTime: "Yến mạch: Ngâm nước ấm 30p-1h. Gạo lứt: 12-24h (ủ nảy mầm càng tốt). Đậu xanh/đậu đen: 8-12h. Hạt sen khô: 2-3h (sen tươi không cần ngâm)."
        },
        {
          group: "Nhóm Hạt Tạo Mùi & Vitamin (Nhóm bổ trợ)",
          examples: "Mè đen, Kỷ tử, Táo đỏ, Lá dứa, Hoa đậu biếc...",
          role: "Tạo màu sắc bắt mắt, hương thơm đặc trưng và bổ sung vitamin, chất chống oxy hóa.",
          soakTime: "Mè đen: Cần rang thơm trước khi nấu. Táo đỏ, Kỷ tử: Rửa sạch, ngâm 15-30p cho mềm."
        }
      ],
      soakingRules: [
        "Nguyên tắc 1: Luôn rửa sạch hạt trước khi ngâm để loại bỏ bụi bẩn.",
        "Nguyên tắc 2: Nước ngâm hạt phải đổ bỏ đi, tuyệt đối không dùng để nấu sữa (vì chứa Phytic Acid và độc tố tiết ra trong quá trình ngâm).",
        "Nguyên tắc 3: Nếu ngâm trên 4 tiếng hoặc qua đêm, bắt buộc phải để trong ngăn mát tủ lạnh để hạt không bị lên men, ôi thiu.",
        "Nguyên tắc 4: Một số loại hạt như Hạnh nhân, Đậu nành, Óc chó sau khi ngâm nên bóc bỏ lớp màng vỏ lụa để sữa không bị chát và có màu đẹp hơn."
      ],
      specificSoakTimes: [
        { name: "Macca", time: "0h", note: "Không ngâm" },
        { name: "Hạt điều", time: "2h-2.5h", note: "Nước nguội" },
        { name: "Óc chó", time: "4h", note: "Ngâm ấm" },
        { name: "Hạnh nhân", time: "8h-12h", note: "Bóc vỏ lụa" },
        { name: "Yến mạch", time: "30p", note: "Nước ấm" },
        { name: "Gạo lứt", time: "12h-24h", note: "Để nảy mầm" },
        { name: "Hạt sen", time: "2h-3h", note: "Sen khô" },
        { name: "Đậu nành", time: "8h-12h", note: "Bóc vỏ" },
        { name: "Đậu đen", time: "8h-12h", note: "Nước nguội" },
        { name: "Đậu xanh", time: "12h-24h", note: "Nước nguội" },
        { name: "Mè đen", time: "0h", note: "Rang chín" },
        { name: "Kỷ tử", time: "15p", note: "Ngâm mềm" }
      ],
      sweeteners: [
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
      ],
      sweetenerSuggestions: [
        {
          milkType: "Sữa bắp, sữa bí đỏ (nhóm củ quả bùi)",
          recommended: "Đường phèn",
          reason: "Đường phèn có vị ngọt thanh mát, không lấn át mà làm nổi bật vị thơm tự nhiên của bắp và bí đỏ."
        },
        {
          milkType: "Sữa hạt điều, hạt macca, hạt óc chó (nhóm hạt béo ngậy)",
          recommended: "Siro lá phong / Chà là",
          reason: "Hương vị nồng ấm của siro lá phong hoặc vị ngọt dịu của chà là rất tôn lên độ béo ngậy đặc trưng của nhóm hạt này."
        },
        {
          milkType: "Sữa hạt sen, sữa đậu xanh (nhóm thanh mát, giải nhiệt)",
          recommended: "Đường thốt nốt / Đường phổi",
          reason: "Đường thốt nốt có mùi thơm đặc trưng, còn đường phổi ngọt thanh, cả hai đều cực kỳ hợp với tính mát của sen và đậu xanh."
        },
        {
          milkType: "Sữa dành cho người ăn kiêng, tiểu đường",
          recommended: "Bột cỏ ngọt (Stevia)",
          reason: "Hoàn toàn không có calo, không làm tăng đường huyết, chỉ cần một lượng rất nhỏ đã đủ tạo độ ngọt."
        },
        {
          milkType: "Sữa gạo lứt, sữa yến mạch (nhóm ngũ cốc)",
          recommended: "Đường mía thô / Đường nâu",
          reason: "Giữ lại một phần mật mía, tạo màu sắc hấp dẫn và bổ sung thêm vi lượng khoáng chất phù hợp với dòng ngũ cốc."
        }
      ],
      nutritionalPyramid: [
        { level: 5, name: "Chất tạo mùi & Vi chất", percentage: "< 1%", description: "Mè đen, kỷ tử, hoa đậu biếc... Tạo màu sắc, hương vị.", color: "bg-rose-100 border-rose-200 text-rose-800", width: "w-2/5" },
        { level: 4, name: "Chất tạo ngọt tự nhiên", percentage: "2-5%", description: "Đường phèn, chà là, cỏ ngọt... Cung cấp vị ngọt thanh.", color: "bg-orange-100 border-orange-200 text-orange-800", width: "w-1/2" },
        { level: 3, name: "Hạt tạo béo", percentage: "5-10%", description: "Macca, óc chó, hạt điều... Tạo độ ngậy, cung cấp lipid.", color: "bg-amber-100 border-amber-200 text-amber-800", width: "w-3/5" },
        { level: 2, name: "Hạt nền / Hạt tạo bột", percentage: "15-20%", description: "Yến mạch, gạo lứt, đậu xanh... Cung cấp carb phức hợp.", color: "bg-emerald-100 border-emerald-200 text-emerald-800", width: "w-4/5" },
        { level: 1, name: "Nước (Dung môi)", percentage: "70-80%", description: "Nước lọc tinh khiết, nước ấm hoặc nước khoáng. Làm nền tảng hòa tan dưỡng chất.", color: "bg-blue-100 border-blue-200 text-blue-800", width: "w-full" }
      ],
      brewingSteps: [
        { step: 1, name: "Chuẩn bị & Làm sạch", description: "Cân đong nguyên liệu theo tỷ lệ chuẩn. Rửa sạch hạt bằng nước muối loãng hoặc chanh để loại bỏ bụi bẩn, tạp chất." },
        { step: 2, name: "Ngâm hạt", description: "Ngâm hạt với nước sạch theo thời gian tiêu chuẩn của từng loại (từ 0h - 24h). Thay nước 1-2 lần, nếu ngâm qua đêm bắt buộc để tủ lạnh." },
        { step: 3, name: "Xử lý sau ngâm", description: "Đổ bỏ nước ngâm. Rửa lại hạt bằng nước sạch. Bóc vỏ lụa (đối với hạnh nhân, đậu nành, óc chó...)." },
        { step: 4, name: "Xay hạt", description: "Cho hạt vào máy xay sinh tố cùng với lượng nước lọc (hoặc nước ấm) phù hợp. Xay nhuyễn mịn từ 1-3 phút tùy công suất máy." },
        { step: 5, name: "Lọc bã (Tùy chọn)", description: "Dùng túi lọc sữa chuyên dụng hoặc rây lưới mịn để vắt lấy cốt sữa, loại bỏ phần bã để sữa được mịn màng (với máy làm sữa chuyên dụng có thể bỏ qua bước này)." },
        { step: 6, name: "Gia nhiệt (Nấu sữa)", description: "Đun sôi sữa trên bếp với lửa nhỏ, khuấy đều tay liên tục để không bị khê đáy. Đun riu riu thêm 15-20 phút cho sữa chín kỹ." },
        { step: 7, name: "Tạo ngọt & Bảo quản", description: "Tắt bếp, đợi sữa hạ nhiệt xuống khoảng 70-80 độ C mới cho chất tạo ngọt (đường phèn/sữa đặc). Để sữa nguội hẳn rồi chiết vào chai thủy tinh tiệt trùng, bảo quản ngăn mát tủ lạnh." }
      ],
      mixingFormulas: {
        description: "Nguyên tắc phối hạt giúp sữa đạt độ sánh mịn hoàn hảo, không bị loãng hay tách lớp quá nhanh, đồng thời hương vị hài hòa, thơm ngon.",
        twoTypes: {
          title: "Công Thức Mix 2 Loại Hạt",
          ratio: "70% Hạt nền (Tạo bột) : 30% Hạt béo (Tạo ngậy)",
          examples: [
            "70g Hạt sen + 30g Macca + 1000ml nước",
            "70g Đậu đen + 30g Óc chó + 1000ml nước",
            "70g Yến mạch + 30g Hạt điều + 1000ml nước"
          ]
        },
        threeTypes: {
          title: "Công Thức Mix 3 Loại Hạt (Hoặc 2 hạt + 1 rau củ/tạo mùi)",
          ratio: "60% Hạt nền : 30% Hạt béo : 10% Hạt tạo mùi/Rau củ",
          examples: [
            "60g Gạo lứt + 30g Hạt điều + 10g Mè đen + 1000ml nước",
            "60g Đậu nành + 30g Macca + 10g Lá dứa + 1000ml nước",
            "60g Hạt sen + 30g Hạnh nhân + 10g Củ dền + 1000ml nước"
          ]
        },
        goldenRules: [
          "Không mix quá 3 loại hạt trong 1 mẻ để tránh loạn vị và khó tiêu.",
          "Hạt nhiều tinh bột (nền) kết hợp với hạt nhiều dầu (béo) là sự kết hợp hoàn hảo nhất.",
          "Nếu dùng rau củ tươi (khoai lang, bí đỏ, bắp non), nên luộc/hấp chín trước rồi mới đem đi xay cùng các hạt khác."
        ]
      },
    },
    {
      id: "equipment",
      title: "2. Danh sách Dụng cụ Setup",
      icon: Settings,
      description: "Danh sách thiết bị tối giản, phù hợp cho mô hình xe đẩy/quầy nhỏ, đảm bảo vận hành linh hoạt không phụ thuộc quá nhiều vào mặt bằng lớn.",
      equipmentCategories: [
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
    },
    {
      id: "menu",
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
      menuStrategy: {
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
      menuItems: [
        {
          name: "Sữa Bắp Nếp Vani",
          price: "15.000đ",
          features: "Quốc dân, dễ uống, giá vốn cực thấp",
          reason: "Là món 'hút khách' (traffic builder) với biên độ lợi nhuận cao nhất. Mùi thơm nức mũi giúp thu hút khách đi đường vào buổi sáng."
        },
        {
          name: "Sữa Đậu Nành Lá Dứa",
          price: "15.000đ",
          features: "Thanh mát, truyền thống",
          reason: "Chi phí nguyên liệu rẻ, tệp khách hàng rộng lớn, có thể uống nóng vào mùa đông và đá vào mùa hè."
        },
        {
          name: "Sữa Đậu Xanh Cốt Dừa",
          price: "18.000đ",
          features: "Béo ngậy, no lâu",
          reason: "Sử dụng làm thức uống thay thế bữa sáng. Cốt dừa tạo sự béo ngậy gây nghiện, giữ chân khách hàng trung thành."
        },
        {
          name: "Sữa Gạo Lứt Huyết Rồng",
          price: "18.000đ",
          features: "Hỗ trợ giảm cân, thực dưỡng",
          reason: "Nhắm vào tệp khách hàng Eat-clean, dân văn phòng nữ. Có thể tư vấn bán theo combo tuần (5 chai/tuần)."
        },
        {
          name: "Sữa Hạt Sen Đường Phèn",
          price: "20.000đ",
          features: "Giải nhiệt, an thần, thanh tao",
          reason: "Giá trị cảm nhận (perceived value) rất cao. Khách sẵn sàng trả giá cao hơn cho hạt sen. Thích hợp bán vào mùa nắng nóng."
        },
        {
          name: "Sữa Hạnh Nhân Macca",
          price: "25.000đ",
          features: "Cao cấp, béo thơm đặc trưng",
          reason: "Đóng vai trò là 'Món chim mồi' (Decoy effect) để làm nổi bật sự hợp lý của các món 15-18k, đồng thời phục vụ tệp khách có thu nhập khá."
        }
      ]
    ,
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
    },
    {
      id: "costing",
      title: "4. Công Thức Tính Cost (Giá Vốn)",
      icon: Calculator,
      description: "Quản lý dòng tiền bắt đầu từ việc hiểu rõ từng đồng chi phí trong 1 chai sữa. Biên lợi nhuận lý tưởng cho sữa hạt take-away nên nằm ở mức 60% - 75%.",
      costExplanation: [
        "Giá vốn 1 chai = (Nguyên liệu hạt + Chất tạo ngọt/béo + Bao bì + Phụ phí) / Số chai thu được.",
        "Nguyên liệu hạt: Cân chính xác lượng hạt sống/khô trước khi ngâm.",
        "Chất tạo ngọt: Đường phèn, sữa đặc, cốt dừa, lá dứa (mua sỉ theo kg).",
        "Bao bì: Chai PET, nắp, tem nhãn, túi xách, ống hút (nếu có).",
        "Phụ phí: Khấu hao máy móc, điện, nước, đá lạnh, hao hụt (quy chuẩn khoảng 5% - 10% tổng nguyên liệu)."
      ],
      costTableData: {
        recipe: "Mẻ Sữa Bắp Nếp (Thu được 10 chai 330ml)",
        rows: [
          { item: "Bắp nếp tươi (2 trái lớn)", quantity: "600g", unitCost: "15.000đ/kg", total: "9.000đ" },
          { item: "Đường phèn hạt nhỏ", quantity: "150g", unitCost: "30.000đ/kg", total: "4.500đ" },
          { item: "Sữa đặc / Sữa tươi", quantity: "50ml", unitCost: "60.000đ/L", total: "3.000đ" },
          { item: "Chai PET + Nắp", quantity: "10 bộ", unitCost: "1.200đ/bộ", total: "12.000đ" },
          { item: "Tem nhãn decal + Túi xách", quantity: "10 bộ", unitCost: "600đ/bộ", total: "6.000đ" },
          { item: "Điện, Nước, Khấu hao", quantity: "1 mẻ", unitCost: "3.500đ/mẻ", total: "3.500đ" }
        ],
        summary: {
          totalCost: "38.000đ",
          yield: "10 chai",
          costPerBottle: "3.800đ",
          sellingPrice: "15.000đ",
          profitMargin: "74.6% (Cực kỳ lý tưởng)"
        }
      }
    },
    {
      id: "operations",
      title: "5. Quy Trình Vận Hành & Ứng Dụng Công Nghệ",
      icon: Laptop,
      description: "Quy trình làm việc (SOP) được thiết kế tinh gọn để 1 người có thể tự vận hành mượt mà trong giờ cao điểm buổi sáng (6:30 - 8:30).",
      sopSteps: [
        { time: "Buổi tối hôm trước", task: "Cân định lượng và ngâm hạt (đối với các loại hạt cần ngâm như đậu nành, hạnh nhân). Chuẩn bị sẵn chai lọ, dán tem nhãn trước." },
        { time: "4:30 Sáng", task: "Bắt đầu chu trình xay nấu (máy tự động). Tranh thủ chuẩn bị cốt dừa, nước đường phèn." },
        { time: "5:30 Sáng", task: "Lọc bã (nếu cần). Áp dụng kỹ thuật Sốc nhiệt làm nguội nhanh (ngâm âu sữa vào thau nước đá) để giữ sữa lâu hư, không bị chua." },
        { time: "6:00 Sáng", task: "Chiết rót vào chai. Đóng chặt nắp niêm phong. Đưa toàn bộ vào thùng đá ủ lạnh sâu." },
        { time: "6:30 - 8:30 Sáng", task: "Đẩy xe ra điểm bán. Giờ cao điểm bán hàng take-away." }
      ],
      techTips: [
        {
          title: "Sử dụng App Quản lý (KiotViet / Sổ Bán Hàng / PosApp)",
          desc: "Tải app quản lý bán hàng trên điện thoại (giao diện F&B). Tạo sẵn danh mục món và Combo."
        },
        {
          title: "Bán hàng không chạm tay (Hands-free Mode)",
          desc: "Sử dụng tính năng 'Nhập liệu bằng giọng nói' trên bàn phím điện thoại hoặc app (ví dụ đọc: '2 bắp, 1 sen') để tạo đơn nhanh chóng khi tay đang bận lấy sữa, đeo găng tay."
        },
        {
          title: "Thanh toán QR Động (Dynamic QR)",
          desc: "In sẵn mã QR thanh toán của ngân hàng để trên quầy. Khách quét mã tự động chuyển đúng số tiền hoặc khách tự nhập. Giảm thiểu rủi ro thối tiền lẻ, tiết kiệm 15 giây/đơn."
        },
        {
          title: "Quản lý tồn kho cuối ngày",
          desc: "Kiểm đếm vỏ chai chênh lệch trên phần mềm để biết doanh thu thực tế, tránh thất thoát."
        }
      ]
    },
    {
      id: "marketing",
      title: "6. Xây Kênh TikTok Từ Con Số 0",
      icon: Smartphone,
      description: "Bí quyết dùng 1 chiếc điện thoại để thu hút khách hàng địa phương (bán kính 3-5km), tăng đơn hàng mà không cần ngân sách quảng cáo.",
      concepts: [
        { name: "Kênh Vlog Khởi Nghiệp Xe Đẩy", desc: "Kể câu chuyện hành trình từ lúc thức dậy 4h sáng nấu sữa, khó khăn lúc đẩy xe, những vị khách dễ thương. Tạo sự đồng cảm và ủng hộ từ cộng đồng (Local Pride)." },
        { name: "Kênh ASMR Thư Giãn", desc: "Không cần nói. Tập trung vào âm thanh rót sữa đặc, tiếng đá lanh canh, tiếng máy xay nhuyễn mịn, tiếng xé mác chai. Chú trọng hình ảnh sắc nét, bắt mắt." },
        { name: "Kênh Chuyên Gia 'Bình Dân'", desc: "Chia sẻ lợi ích các loại hạt, mẹo ngâm hạt, cách mix vị độc lạ. Định vị là một người bán hàng có tâm, am hiểu sức khỏe nhưng rất gần gũi." }
      ],
      contentFunnel: [
        { type: "Nội dung Thu Hút (Reach)", percentage: "40%", desc: "Bắt trend nhạc TikTok, POV (Góc nhìn) hài hước khi bán hàng, biến hình trước/sau khi dọn hàng." },
        { type: "Nội dung Trao Giá Trị (Value)", percentage: "40%", desc: "Phân biệt hạt sen Huế và sen thường, mẹo ngâm hạt không bị chua, tại sao sữa bắp lại kết tủa..." },
        { type: "Nội dung Bán Hàng (Sale)", percentage: "20%", desc: "Giới thiệu combo bữa sáng, quay menu tại quầy, hướng dẫn đường đi đến điểm bán, CTA mời khách ghé mua." }
      ],
      shootingGuidelines: [
        { title: "Góc máy & Cấu hình", desc: "Luôn quay dọc (Tỷ lệ 9:16). Chỉnh camera điện thoại ở độ phân giải 1080p - 60fps. Lau thật sạch ống kính trước khi quay." },
        { title: "Ánh sáng tự nhiên", desc: "Tận dụng ánh sáng tự nhiên (6h-8h sáng là đẹp nhất). Đứng đối diện nguồn sáng, tuyệt đối không quay ngược sáng." },
        { title: "Âm thanh", desc: "Dùng tai nghe có mic để thu âm hoặc lồng tiếng sau (Voice-over) trong môi trường yên tĩnh. Âm thanh gốc (như tiếng rót sữa) phải rõ ràng." },
        { title: "App chỉnh sửa (CapCut)", desc: "Sử dụng CapCut với 4 thao tác cơ bản: Cắt bỏ đoạn thừa, lồng tiếng (Voiceover), Auto Caption (Phụ đề tự động để người xem không bật tiếng vẫn hiểu), thêm nhạc nền xu hướng (âm lượng nhạc 10-15%)." }
      ],
      perfectVideoBlueprint: {
        title: "Kịch Bản Mẫu: Mẻ Sữa Hạt Sen Đầu Ngày (35-45 giây)",
        steps: [
          { time: "0s - 3s (Hook - Thu hút)", action: "Cảnh quay cận cảnh (Close-up) rót sữa hạt sen đặc sánh, bốc khói nhẹ vào ly đá.", audio: "[Âm thanh rót sữa] Lồng tiếng: 'Để có một ly sữa hạt sen sánh mịn thế này, mình phải dậy từ 4h sáng các bạn ạ!'" },
          { time: "3s - 15s (Body 1 - Nội dung)", action: "Góc máy ngang (Eye-level) quay cảnh rửa sen, lấy tim sen. Chuyển cảnh nhanh thả sen vào máy nấu.", audio: "'Bí quyết của mình là phải lẩy sạch tim sen để sữa không bị nhẫn đắng. Sen ngâm đủ 4 tiếng sẽ cực kỳ bở và thơm.'" },
          { time: "15s - 25s (Body 2 - Nội dung)", action: "Quay cảnh chiết sữa vào chai, đóng nắp, xếp vào thùng đá. Góc máy từ trên xuống (Top-down).", audio: "'Sữa nấu xong mình sốc nhiệt và ủ đá ngay để giữ độ tươi. Mình chỉ làm đúng 30 chai mỗi sáng bán hết rồi về.'" },
          { time: "25s - 35s (CTA - Kêu gọi)", action: "Quay toàn cảnh xe đẩy, có bảng tên đường/biển hiệu. Tay cầm 1 chai sữa giơ lên trước ống kính.", audio: "'Sáng nay xe sữa của mình đứng ở góc đường Nguyễn Trãi, Quận 5. Bạn nào đi làm ngang qua ghé ủng hộ mình 1 chai nha. Bán đến 8 rưỡi thôi!'" }
        ]
      },
      localSEO: [
        { title: "Gắn Vị Trí (Location)", desc: "Luôn luôn Check-in vị trí bán hàng trước khi bấm Đăng (Ví dụ: 'Quận 5', 'Đường Nguyễn Trãi', hoặc tự tạo Location trên bản đồ)." },
        { title: "Sử dụng Local Hashtags", desc: "Đừng chỉ dùng hashtag chung chung, hãy dùng thêm từ khóa địa phương: #suahatquan5, #anvatquan5, #ancungtiktok, #ten_duong." },
        { title: "Text On Screen (Chữ trên video)", desc: "Thuật toán TikTok đọc được chữ trên màn hình. Hãy gõ tên đường, khu vực bán ngay trên 3 giây đầu tiên của video." }
      ]
    },
    {
      id: "recipes",
      title: "7. Từ Điển 100+ Công Thức Mở Rộng",
      icon: BookText,
      description: "Hệ thống menu phân loại theo nhu cầu khách hàng, dễ thao tác và tối ưu hóa nguyên liệu. Tên món được chuẩn hóa ngắn gọn, dễ nhớ để hỗ trợ nhập liệu bằng giọng nói. Dưới đây là 100 công thức phân theo 10 nhóm mục đích sử dụng (Định lượng cho 1 mẻ 1 lít sữa).",
      recipeGroups: recipeGroups
    },
    {
      id: "troubleshooting",
      title: "8. Cách Khắc Phục Lỗi Khi Nấu",
      icon: AlertTriangle,
      description: "Tổng hợp các lỗi thường gặp trong quá trình nấu sữa hạt cùng với nguyên nhân và cách khắc phục chi tiết để đảm bảo chất lượng mẻ sữa luôn hoàn hảo.",
      issues: [
        {
          name: "Sữa bị tách lớp (Lắng cặn)",
          cause: "Do hạt chứa nhiều tinh bột (đậu xanh, bắp, khoai...) nặng hơn nước nên chìm xuống. Hoặc do tỷ lệ nước và hạt chưa chuẩn, hạt nở chưa đủ.",
          solution: "Đây là hiện tượng vật lý bình thường với sữa không dùng chất nhũ hóa công nghiệp. Trước khi uống chỉ cần lắc đều. Để giảm thiểu: Ngâm hạt đủ thời gian, rang chín hạt trước khi nấu (như gạo lứt, mè đen) hoặc phối hợp với các hạt chứa nhiều chất béo (macca, óc chó, điều) để tạo độ sánh tự nhiên."
        },
        {
          name: "Sữa bị vón cục (Lợn cợn, kết tủa)",
          cause: "Thường gặp khi nấu các loại hạt giàu axit (như hạnh nhân kết hợp với một số loại trái cây) hoặc do nhiệt độ nấu quá cao làm protein kết tủa. Cũng có thể do đường phèn/sữa đặc cho vào lúc nước đang sôi bùng.",
          solution: "Chỉ cho đường hoặc chất tạo ngọt vào khi sữa đã nấu xong và đang ở nhiệt độ ấm (dưới 80 độ C). Đảm bảo vệ sinh kỹ dụng cụ. Nếu mix với trái cây, chỉ mix ở dạng xay lạnh không gia nhiệt. Khi nấu các hạt giàu protein, chú ý điều chỉnh nhiệt độ vừa phải (không đun sôi trào liên tục)."
        },
        {
          name: "Sữa có mùi chua, nhanh hỏng",
          cause: "Ngâm hạt quá lâu ở nhiệt độ phòng mà không thay nước. Sữa nấu xong làm nguội quá chậm, đậy nắp chai khi sữa còn nóng, hoặc chai lọ chưa được tiệt trùng kỹ.",
          solution: "Ngâm hạt trên 4 tiếng bắt buộc phải để ngăn mát tủ lạnh, thay nước 1-2 lần. Sữa nấu xong phải làm nguội nhanh (sốc nhiệt bằng cách ngâm âu sữa vào chậu nước đá). Đợi sữa nguội hẳn (dưới 30 độ C) mới đậy kín nắp chai. Chai nhựa cần được tráng sơ nước sôi hoặc dùng tủ sấy UV."
        },
        {
          name: "Sữa bị khê, cháy đáy máy/nồi",
          cause: "Do lượng hạt quá nhiều so với lượng nước, hoặc hạt chứa tinh bột lắng xuống nhưng không được khuấy. Một số máy làm sữa hạt gia nhiệt quá mạnh ở đáy.",
          solution: "Tuân thủ tỷ lệ hạt và nước chuẩn (thường là 100g hạt / 1 lít nước). Có thể hấp/luộc chín hạt trước rồi mới cho vào máy xay với nước ấm để tránh gia nhiệt nấu gây khê đáy mà vẫn giữ tối đa dinh dưỡng."
        },
        {
          name: "Sữa bị nhẫn đắng",
          cause: "Chưa loại bỏ lớp màng vỏ lụa của một số loại hạt (óc chó, hạnh nhân, đậu nành), chưa bỏ sạch tim sen, hoặc rang hạt quá lửa bị cháy xém.",
          solution: "Bóc sạch màng vỏ lụa của óc chó, hạnh nhân, đậu nành sau khi ngâm. Lấy sạch hoàn toàn tim sen trước khi nấu. Khi rang các loại hạt như gạo lứt, mè đen, đậu đen chỉ rang lửa nhỏ đến khi chín thơm."
        },
        {
          name: "Sữa loãng, nhạt nhẽo, kém béo",
          cause: "Tỷ lệ nước quá nhiều so với hạt. Chọn sai nguyên liệu phối hợp (không có hạt tạo béo).",
          solution: "Tăng lượng hạt hoặc giảm nước. Để tạo độ béo ngậy tự nhiên, nên phối hợp các hạt nền (đậu nành, gạo lứt...) với các hạt tạo béo (hạt điều, macca, óc chó, hạnh nhân) theo tỷ lệ 70% hạt nền - 30% hạt béo."
        }
      ]
    }
  ]
};
