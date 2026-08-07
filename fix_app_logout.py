import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add LogOut icon
content = content.replace('Download } from "lucide-react";', 'Download, LogOut } from "lucide-react";')

logout_button = """            {currentUser?.role === 'admin' && (
              <button 
                onClick={() => setShowAdmin(!showAdmin)}
                className="w-full px-4 py-3 bg-stone-900 hover:bg-stone-800 text-white rounded-xl text-sm font-bold flex items-center justify-center gap-2 transition-colors mb-3"
              >
                {showAdmin ? 'Trở về Khóa học' : 'Quản trị viên'}
              </button>
            )}
            <button 
              onClick={() => {
                setCurrentUser(null);
                setShowAdmin(false);
              }}
              className="w-full px-4 py-3 bg-rose-50 hover:bg-rose-100 text-rose-600 rounded-xl text-sm font-bold flex items-center justify-center gap-2 transition-colors"
            >
              <LogOut size={18} /> Đăng xuất
            </button>"""

target = """            {currentUser?.role === 'admin' && (
              <button 
                onClick={() => setShowAdmin(!showAdmin)}
                className="w-full px-4 py-3 bg-stone-900 hover:bg-stone-800 text-white rounded-xl text-sm font-bold flex items-center justify-center gap-2 transition-colors"
              >
                {showAdmin ? 'Trở về Khóa học' : 'Quản trị viên'}
              </button>
            )}"""

content = content.replace(target, logout_button)

with open('src/App.tsx', 'w') as f:
    f.write(content)

print("Logout button added")
