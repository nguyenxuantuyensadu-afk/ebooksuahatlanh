with open('src/components/AdminDashboard.tsx', 'r') as f:
    content = f.read()

# Right now we have:
#           {userSubTab === 'list' && (
#             <div className="grid md:grid-cols-3 gap-8">
# ...
#         </div>
#       )}
#       {activeTab === 'content' && (

# Let's find the string:
target = """        </div>
      )}
      {activeTab === 'content' && ("""

new_code = """        </div>
          )}
          {userSubTab === 'locks' && (
            <div className="bg-stone-50 p-6 rounded-[2rem] border border-stone-200 max-w-4xl">
              <h3 className="font-bold text-lg text-stone-900 mb-6 flex items-center gap-2"><Lock size={20} className="text-stone-500"/> Quản lý Khoá nội dung</h3>
              <p className="text-stone-500 text-sm mb-6">Bạn có thể chọn khoá các mục nhỏ bên trong từng module. Người học thông thường sẽ không nhìn thấy các nội dung bị khoá.</p>
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

if target in content:
    content = content.replace(target, new_code)
    with open('src/components/AdminDashboard.tsx', 'w') as f:
        f.write(content)
    print("Replaced successfully")
else:
    print("Target not found. Let's do a regex search.")
    import re
    match = re.search(r"        </div>\n      \)\}\n      \{activeTab === 'content' && \(", content)
    if match:
        print("Found with regex")
        content = content[:match.start()] + new_code + content[match.end():]
        with open('src/components/AdminDashboard.tsx', 'w') as f:
            f.write(content)
    else:
        print("Still not found")
