import re

with open('src/components/AdminDashboard.tsx', 'r') as f:
    content = f.read()

old_tab_buttons = """        <button 
          onClick={() => setActiveTab('content')}
          className={`flex items-center gap-2 px-6 py-3 rounded-xl font-bold transition-all ${
            activeTab === 'content' ? 'bg-stone-900 text-white shadow-md' : 'bg-stone-100 text-stone-600 hover:bg-stone-200'
          }`}
        >
          <FileText size={18} /> Quản lý Nội Dung & Công thức
        </button>
      </div>"""

new_tab_buttons = """        <button 
          onClick={() => setActiveTab('content')}
          className={`flex items-center gap-2 px-6 py-3 rounded-xl font-bold transition-all ${
            activeTab === 'content' ? 'bg-stone-900 text-white shadow-md' : 'bg-stone-100 text-stone-600 hover:bg-stone-200'
          }`}
        >
          <FileText size={18} /> Công Thức
        </button>
        <button 
          onClick={() => setActiveTab('full_content')}
          className={`flex items-center gap-2 px-6 py-3 rounded-xl font-bold transition-all ${
            activeTab === 'full_content' ? 'bg-stone-900 text-white shadow-md' : 'bg-stone-100 text-stone-600 hover:bg-stone-200'
          }`}
        >
          <Edit2 size={18} /> Sửa Toàn Bộ Khoá Học
        </button>
      </div>"""

content = content.replace(old_tab_buttons, new_tab_buttons)

with open('src/components/AdminDashboard.tsx', 'w') as f:
    f.write(content)
