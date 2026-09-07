import re

with open('src/components/AdminDashboard.tsx', 'r') as f:
    content = f.read()

# 1. Add editingLockedPaths state
content = content.replace(
    "const [editingUnlockedModules, setEditingUnlockedModules] = useState<string[]>([]);",
    "const [editingUnlockedModules, setEditingUnlockedModules] = useState<string[]>([]);\n  const [editingLockedPaths, setEditingLockedPaths] = useState<string[]>([]);"
)

# 2. Update setEditingUser logic
old_set_user = """                                  setEditingUser(user);
                                  setEditingUnlockedModules(user.unlockedModules || []);"""
new_set_user = """                                  setEditingUser(user);
                                  setEditingUnlockedModules(user.unlockedModules || []);
                                  setEditingLockedPaths(user.lockedPaths || []);"""
content = content.replace(old_set_user, new_set_user)

# 3. Update handleSavePermissions
old_save = """      await setDoc(doc(db, "users", editingUser.id), {
        ...editingUser,
        unlockedModules: editingUnlockedModules
      });"""
new_save = """      await setDoc(doc(db, "users", editingUser.id), {
        ...editingUser,
        unlockedModules: editingUnlockedModules,
        lockedPaths: editingLockedPaths
      });"""
content = content.replace(old_save, new_save)

# 4. Modify the modal UI for permissions
old_modal_inner = """            <div className="space-y-2 mb-6 max-h-96 overflow-y-auto pr-2">
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
            </div>"""

new_modal_inner = """            <div className="space-y-3 mb-6 max-h-[60vh] overflow-y-auto pr-2">
              {courseData.modules.map(mod => {
                const isUnlocked = editingUnlockedModules.includes(mod.id);
                // Lấy các mục có thể khoá của module này
                const lockableData = extractLockablePaths(courseData).find(m => m.moduleId === mod.id);
                
                return (
                  <div key={mod.id} className="bg-stone-50 rounded-xl border border-stone-200 overflow-hidden">
                    <div className="flex items-center justify-between p-3 bg-stone-100/50">
                      <div className="flex items-center gap-3">
                        {isUnlocked ? <Unlock size={18} className="text-emerald-500" /> : <Lock size={18} className="text-stone-400" />}
                        <span className="text-sm font-bold text-stone-800 truncate w-48">{mod.title}</span>
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
                        {isUnlocked ? "Khóa Toàn Bộ" : "Mở Module"}
                      </button>
                    </div>
                    
                    {/* Các mục nhỏ bên trong module */}
                    {isUnlocked && lockableData && lockableData.arrays.length > 0 && (
                      <div className="p-3 bg-white border-t border-stone-200 space-y-4">
                        {lockableData.arrays.map(arr => (
                          <div key={arr.key}>
                            <h5 className="font-bold text-stone-600 text-[10px] mb-2 uppercase tracking-wider">{arr.key}</h5>
                            <div className="space-y-1">
                              {arr.items.map(item => {
                                const isItemLocked = editingLockedPaths.includes(item.path);
                                // Cũng kiểm tra xem có bị khoá chung không
                                const isGlobalLocked = courseData.lockedPaths?.includes(item.path);
                                
                                return (
                                  <div key={item.path} className="flex items-center justify-between p-2 hover:bg-stone-50 rounded-lg transition-colors border border-transparent">
                                    <span className={`text-xs font-medium truncate pr-2 ${isItemLocked || isGlobalLocked ? 'text-stone-400 line-through' : 'text-stone-700'}`}>
                                      {item.label}
                                      {isGlobalLocked && <span className="ml-2 text-[9px] bg-rose-100 text-rose-600 px-1.5 py-0.5 rounded">Khoá chung</span>}
                                    </span>
                                    {!isGlobalLocked && (
                                      <button
                                        onClick={() => {
                                          setEditingLockedPaths(prev => 
                                            isItemLocked ? prev.filter(p => p !== item.path) : [...prev, item.path]
                                          );
                                        }}
                                        className={`p-1.5 rounded-md transition-colors shrink-0 flex items-center justify-center ${isItemLocked ? 'bg-rose-100 text-rose-600 hover:bg-rose-200' : 'bg-stone-100 text-stone-400 hover:bg-stone-200 hover:text-stone-600'}`}
                                        title={isItemLocked ? "Mở khoá mục này" : "Khoá mục này"}
                                      >
                                        {isItemLocked ? <Lock size={14} /> : <Unlock size={14} />}
                                      </button>
                                    )}
                                  </div>
                                );
                              })}
                            </div>
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>"""

content = content.replace(old_modal_inner, new_modal_inner)

with open('src/components/AdminDashboard.tsx', 'w') as f:
    f.write(content)

