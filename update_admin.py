import re

with open('src/components/AdminDashboard.tsx', 'r') as f:
    content = f.read()

# Change export default function AdminDashboard({ onClose }: { onClose: () => void })
content = content.replace(
    'export default function AdminDashboard({ onClose }: { onClose: () => void }) {',
    'export default function AdminDashboard({ onClose, courseData }: { onClose: () => void, courseData: any }) {'
)

# Add full_content to activeTab
content = content.replace(
    "const [activeTab, setActiveTab] = useState<'users' | 'content'>('users');",
    "const [activeTab, setActiveTab] = useState<'users' | 'content' | 'full_content'>('users');\n  const [jsonContent, setJsonContent] = useState('');\n  const [jsonError, setJsonError] = useState('');"
)

# Load JSON on tab change
use_effect = """
  useEffect(() => {
    if (activeTab === 'full_content' && courseData) {
      const clone = JSON.parse(JSON.stringify(courseData, (key, value) => {
        if (key === 'icon') return undefined;
        return value;
      }));
      setJsonContent(JSON.stringify(clone, null, 2));
      setJsonError('');
    }
  }, [activeTab, courseData]);

  const handleSaveJson = async () => {
    try {
      const parsed = JSON.parse(jsonContent);
      await setDoc(doc(db, "course_content", "main"), parsed);
      toast.success("Đã cập nhật toàn bộ nội dung khoá học thành công!");
      setJsonError('');
    } catch (e: any) {
      setJsonError(e.message || "Lỗi cú pháp JSON");
      toast.error("Vui lòng kiểm tra lại cú pháp JSON!");
    }
  };
"""
content = content.replace(
    "const [editingUnlockedModules, setEditingUnlockedModules] = useState<string[]>([]);",
    "const [editingUnlockedModules, setEditingUnlockedModules] = useState<string[]>([]);\n" + use_effect
)

# Add Tab Button
old_tab_buttons = """        <button 
          onClick={() => setActiveTab('content')}
          className={`flex-1 py-3 px-6 rounded-xl font-bold flex items-center justify-center gap-2 transition-all ${
            activeTab === 'content' ? 'bg-stone-900 text-white shadow-md' : 'bg-stone-100 text-stone-600 hover:bg-stone-200'
          }`}
        >
          <FileText size={18} /> Quản lý Nội Dung & Công thức
        </button>
      </div>"""
new_tab_buttons = """        <button 
          onClick={() => setActiveTab('content')}
          className={`flex-1 py-3 px-6 rounded-xl font-bold flex items-center justify-center gap-2 transition-all ${
            activeTab === 'content' ? 'bg-stone-900 text-white shadow-md' : 'bg-stone-100 text-stone-600 hover:bg-stone-200'
          }`}
        >
          <Plus size={18} /> Thêm Công thức
        </button>
        <button 
          onClick={() => setActiveTab('full_content')}
          className={`flex-1 py-3 px-6 rounded-xl font-bold flex items-center justify-center gap-2 transition-all ${
            activeTab === 'full_content' ? 'bg-amber-500 text-white shadow-md' : 'bg-stone-100 text-stone-600 hover:bg-stone-200'
          }`}
        >
          <Edit2 size={18} /> Sửa Toàn Bộ Khoá Học
        </button>
      </div>"""
content = content.replace(old_tab_buttons, new_tab_buttons)

# Add full_content panel
full_content_panel = """
      {activeTab === 'full_content' && (
        <div className="bg-white rounded-[2rem] border border-stone-200 overflow-hidden shadow-sm p-6">
          <div className="flex justify-between items-center mb-6">
            <h3 className="font-bold text-lg text-stone-900">Chỉnh sửa nội dung khoá học (Dạng JSON)</h3>
            <button 
              onClick={handleSaveJson}
              className="px-6 py-2.5 bg-amber-500 hover:bg-amber-600 text-white font-bold rounded-xl flex items-center gap-2 transition-colors shadow-sm"
            >
              <Save size={18} /> Lưu Thay Đổi
            </button>
          </div>
          {jsonError && <div className="p-4 mb-4 bg-rose-50 text-rose-700 font-medium rounded-xl border border-rose-200">{jsonError}</div>}
          <div className="bg-stone-900 rounded-xl p-4">
            <textarea
              value={jsonContent}
              onChange={e => {
                setJsonContent(e.target.value);
                setJsonError('');
              }}
              className="w-full h-[600px] bg-transparent text-emerald-400 font-mono text-sm focus:outline-none resize-none"
              spellCheck="false"
            />
          </div>
        </div>
      )}
"""

content = content.replace(
    "    </div>\n  );\n}",
    full_content_panel + "\n    </div>\n  );\n}"
)

with open('src/components/AdminDashboard.tsx', 'w') as f:
    f.write(content)
