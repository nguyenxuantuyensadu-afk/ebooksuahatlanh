import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Remove the broken `</>)}`
content = content.replace("        </>)}\n        </main>", "        </main>")

# Add button to Sidebar
sidebar_end = """            <p className="text-xs text-stone-500 font-medium leading-relaxed">
              Tài liệu độc quyền thiết kế cho mô hình quầy và xe đẩy nhỏ lẻ.
            </p>
          </div>
        </aside>"""

admin_button = """            <p className="text-xs text-stone-500 font-medium leading-relaxed mb-4">
              Tài liệu độc quyền thiết kế cho mô hình quầy và xe đẩy nhỏ lẻ.
            </p>
            {currentUser?.role === 'admin' && (
              <button 
                onClick={() => setShowAdmin(!showAdmin)}
                className="w-full px-4 py-3 bg-stone-900 hover:bg-stone-800 text-white rounded-xl text-sm font-bold flex items-center justify-center gap-2 transition-colors"
              >
                {showAdmin ? 'Trở về Khóa học' : 'Quản trị viên'}
              </button>
            )}
          </div>
        </aside>"""

content = content.replace(sidebar_end, admin_button)

# Add conditional render for main
main_start = """        {/* Main Content */}
        <main className="flex-1 px-5 py-8 lg:px-16 lg:py-16 max-w-5xl w-full mx-auto bg-white min-h-screen border-l border-stone-100 shadow-[0_0_40px_rgba(0,0,0,0.02)] print:border-none print:shadow-none print:m-0 print:p-0 print:max-w-none print:w-full">"""

main_start_replaced = """        {/* Main Content */}
        <main className="flex-1 px-5 py-8 lg:px-16 lg:py-16 max-w-5xl w-full mx-auto bg-white min-h-screen border-l border-stone-100 shadow-[0_0_40px_rgba(0,0,0,0.02)] print:border-none print:shadow-none print:m-0 print:p-0 print:max-w-none print:w-full">
        {showAdmin ? (
          <AdminDashboard onClose={() => setShowAdmin(false)} />
        ) : (
          <>"""

content = content.replace(main_start, main_start_replaced)

main_end = """          </footer>
        </main>"""
        
main_end_replaced = """          </footer>
          </>
        )}
        </main>"""

content = content.replace(main_end, main_end_replaced)

with open('src/App.tsx', 'w') as f:
    f.write(content)

print("Fixed App")
