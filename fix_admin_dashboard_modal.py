import re

with open('src/components/AdminDashboard.tsx', 'r') as f:
    content = f.read()

modal_jsx = """
      {editingUser && (
        <div className="fixed inset-0 bg-stone-900/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-3xl p-6 w-full max-w-md shadow-xl border border-stone-200">
            <div className="flex justify-between items-center mb-6">
              <h3 className="text-xl font-bold text-stone-900">Quyền truy cập</h3>
              <button onClick={() => setEditingUser(null)} className="p-2 text-stone-400 hover:text-stone-900 bg-stone-100 rounded-xl">
                <X size={20} />
              </button>
            </div>
            <p className="text-sm font-medium text-stone-500 mb-4">
              Học viên: <span className="font-bold text-stone-900">{editingUser.username}</span>
            </p>
            <div className="space-y-2 mb-6 max-h-96 overflow-y-auto pr-2">
              {courseData.modules.map(mod => {
                const isUnlocked = editingUnlockedModules.includes(mod.id);
                return (
                  <div key={mod.id} className="flex items-center justify-between p-3 bg-stone-50 rounded-xl border border-stone-200">
                    <div className="flex items-center gap-3">
                      {isUnlocked ? <Unlock size={18} className="text-emerald-500" /> : <Lock size={18} className="text-stone-400" />}
                      <span className="text-sm font-semibold text-stone-700 truncate w-48">{mod.title}</span>
                    </div>
                    <button 
                      onClick={() => {
                        if (isUnlocked) {
                          setEditingUnlockedModules(prev => prev.filter(id => id !== mod.id));
                        } else {
                          setEditingUnlockedModules(prev => [...prev, mod.id]);
                        }
                      }}
                      className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-colors ${
                        isUnlocked ? "bg-emerald-100 text-emerald-700 hover:bg-emerald-200" : "bg-stone-200 text-stone-600 hover:bg-stone-300"
                      }`}
                    >
                      {isUnlocked ? "Khóa lại" : "Mở khóa"}
                    </button>
                  </div>
                );
              })}
            </div>
            <button onClick={handleSavePermissions} className="w-full py-3 bg-stone-900 text-white rounded-xl font-bold flex items-center justify-center gap-2">
              <Save size={18} /> Lưu Thay Đổi
            </button>
          </div>
        </div>
      )}
"""

target = '  return (\n    <div className="animate-in fade-in slide-in-from-bottom-4 duration-500 bg-white rounded-3xl p-2 md:p-8 relative">'

if target in content:
    content = content.replace(target, target + modal_jsx)
    with open('src/components/AdminDashboard.tsx', 'w') as f:
        f.write(content)
    print("Modal injected")
else:
    print("Target not found")
