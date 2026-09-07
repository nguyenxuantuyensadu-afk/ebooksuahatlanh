import re

with open('src/components/AdminDashboard.tsx', 'r') as f:
    content = f.read()

# 1. Add userSubTab state
content = content.replace("const [activeTab, setActiveTab] = useState<'users' | 'content' | 'locks' | 'full_content'>('users');", 
                          "const [activeTab, setActiveTab] = useState<'users' | 'content' | 'full_content'>('users');\n  const [userSubTab, setUserSubTab] = useState<'list' | 'locks'>('list');")

# 2. Remove locks tab from top nav
locks_btn_pattern = r"""        <button 
          onClick=\{\(\) => setActiveTab\('locks'\)\}
          className=\{`flex items-center gap-2 px-6 py-3 rounded-xl font-bold transition-all \$\{
            activeTab === 'locks' \? 'bg-stone-900 text-white shadow-md' : 'bg-stone-100 text-stone-600 hover:bg-stone-200'
          \}`\}
        >
          <Lock size=\{18\} /> Khoá Nội Dung
        </button>
"""
content = re.sub(locks_btn_pattern, "", content)

# 3. Restructure 'users' tab
# Find {activeTab === 'users' && (
# Replace with the sub-tab structure

users_start = r"      \{activeTab === 'users' && \(\n        <div className=\"grid md:grid-cols-3 gap-8\">"
users_start_new = """      {activeTab === 'users' && (
        <div className="space-y-6">
          <div className="flex gap-4 border-b border-stone-200 pb-4">
             <button onClick={() => setUserSubTab('list')} className={`px-4 py-2.5 font-bold rounded-xl transition-colors ${userSubTab === 'list' ? 'bg-stone-800 text-white shadow-sm' : 'text-stone-500 hover:bg-stone-100'}`}>Danh sách Học viên</button>
             <button onClick={() => setUserSubTab('locks')} className={`px-4 py-2.5 font-bold rounded-xl flex items-center gap-2 transition-colors ${userSubTab === 'locks' ? 'bg-stone-800 text-white shadow-sm' : 'text-stone-500 hover:bg-stone-100'}`}><Lock size={16}/> Khoá Nội Dung Chung</button>
          </div>
          {userSubTab === 'list' && (
            <div className="grid md:grid-cols-3 gap-8">"""

content = content.replace("      {activeTab === 'users' && (\n        <div className=\"grid md:grid-cols-3 gap-8\">", users_start_new)

# Find the end of the users list, which is just before {activeTab === 'content' && (
# The original structure:
#         </div>
#       )}
#       {activeTab === 'content' && (
end_users_pattern = r"        </div>\n      \)\}\n      \{activeTab === 'content' && \("
end_users_new = """        </div>
          )}
          {userSubTab === 'locks' && (
            <div className="bg-stone-50 p-6 rounded-[2rem] border border-stone-200 max-w-4xl">
              <h3 className="font-bold text-lg text-stone-900 mb-6 flex items-center gap-2"><Lock size={20} className="text-stone-500"/> Quản lý Khoá nội dung</h3>
              <p className="text-stone-500 text-sm mb-6">Khoá các mục nhỏ bên trong từng module. Áp dụng cho tất cả học viên.</p>
              <div className="space-y-6">
                {extractLockablePaths(courseData).map((mod: any) => (
                  <div key={mod.moduleId} className="bg-white p-5 rounded-2xl border border-stone-100 shadow-sm">
                    <h4 className="font-bold text-stone-800 text-lg mb-4 pb-2 border-b border-stone-100">{mod.moduleTitle}</h4>
                    <div className="space-y-6">
                      {mod.arrays.map((arr: any) => (
                        <div key={arr.key}>
                          <h5 className="font-bold text-stone-600 text-sm mb-3 uppercase tracking-wider bg-stone-50 py-1.5 px-3 rounded-lg inline-block">{arr.key}</h5>
                          <div className="flex flex-col gap-2 pl-2">
                            {arr.items.map((item: any) => {
                              const isLocked = courseData.lockedPaths?.includes(item.path);
                              return (
                                <div key={item.path} className="flex items-center justify-between p-3 hover:bg-stone-50 rounded-xl transition-colors border border-transparent hover:border-stone-100">
                                  <span className={`text-sm font-medium truncate pr-4 ${isLocked ? 'text-stone-400 line-through' : 'text-stone-700'}`}>{item.label}</span>
                                  <button
                                    onClick={() => toggleLock(item.path)}
                                    className={`p-2 rounded-lg transition-colors shrink-0 flex items-center justify-center ${isLocked ? 'bg-rose-100 text-rose-600 hover:bg-rose-200' : 'bg-stone-100 text-stone-400 hover:bg-stone-200 hover:text-stone-600'}`}
                                    title={isLocked ? "Mở khoá" : "Khoá lại"}
                                  >
                                    {isLocked ? <Lock size={16} /> : <Unlock size={16} />}
                                  </button>
                                </div>
                              );
                            })}
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      )}
      {activeTab === 'content' && ("""

content = re.sub(end_users_pattern, end_users_new, content)

# 4. Remove the old {activeTab === 'locks' && ( ... )} block
old_locks_block_pattern = r"      \{activeTab === 'locks' && \(\n        <div className=\"bg-stone-50 p-6 rounded-\[2rem\] border border-stone-200 max-w-4xl\">.*?        </div>\n      \)\}\n"
content = re.sub(old_locks_block_pattern, "", content, flags=re.DOTALL)

with open('src/components/AdminDashboard.tsx', 'w') as f:
    f.write(content)
print("Done")
