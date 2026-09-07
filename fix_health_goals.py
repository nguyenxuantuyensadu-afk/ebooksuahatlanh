with open('src/App.tsx', 'r') as f:
    content = f.read()

health_goals_def = """
const healthGoals = [
  { id: 'giam-can', label: 'Giảm cân / Giữ dáng', color: 'text-rose-600 bg-rose-50 ring-rose-200/50', iconColor: 'bg-rose-500', keywords: ['giảm cân', 'giữ dáng', 'siết mỡ'] },
  { id: 'tang-co', label: 'Tăng cơ', color: 'text-blue-600 bg-blue-50 ring-blue-200/50', iconColor: 'bg-blue-500', keywords: ['tăng cơ', 'protein', 'gym', 'thể thao'] },
  { id: 'tang-can', label: 'Tăng cân', color: 'text-amber-600 bg-amber-50 ring-amber-200/50', iconColor: 'bg-amber-500', keywords: ['tăng cân', 'béo ngậy', 'calo cao'] },
  { id: 'canxi', label: 'Bổ sung canxi', color: 'text-emerald-600 bg-emerald-50 ring-emerald-200/50', iconColor: 'bg-emerald-500', keywords: ['canxi', 'xương khớp'] },
  { id: 'dep-da', label: 'Đẹp da', color: 'text-pink-600 bg-pink-50 ring-pink-200/50', iconColor: 'bg-pink-500', keywords: ['đẹp da', 'lão hóa', 'trẻ hóa'] },
  { id: 'tieu-hoa', label: 'Tiêu hóa / Mát gan', color: 'text-teal-600 bg-teal-50 ring-teal-200/50', iconColor: 'bg-teal-500', keywords: ['tiêu hóa', 'mát gan', 'thanh lọc', 'rau củ', 'giải nhiệt'] },
  { id: 'tri-nao', label: 'Trí não', color: 'text-indigo-600 bg-indigo-50 ring-indigo-200/50', iconColor: 'bg-indigo-500', keywords: ['trí não', 'stress', 'thần kinh'] },
];

"""

if 'const healthGoals =' not in content:
    content = content.replace('export default function App() {', health_goals_def + 'export default function App() {')
    with open('src/App.tsx', 'w') as f:
        f.write(content)

