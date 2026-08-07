import re

with open('src/components/AdminDashboard.tsx', 'r') as f:
    content = f.read()

# Add Lock, Unlock icons
content = content.replace("Save } from 'lucide-react';", "Save, Lock, Unlock, Settings2 } from 'lucide-react';\nimport { courseData } from '../data';")

# Add state
new_state = """  const [editingUser, setEditingUser] = useState<any>(null);
  const [editingUnlockedModules, setEditingUnlockedModules] = useState<string[]>([]);
"""
content = content.replace("const [newRecipeDifficulty, setNewRecipeDifficulty] = useState('Easy');", "const [newRecipeDifficulty, setNewRecipeDifficulty] = useState('Easy');\n" + new_state)

# Create user handle - add default unlockedModules
content = content.replace("""        role: "student",
        createdAt: new Date().toISOString()
      });""", """        role: "student",
        createdAt: new Date().toISOString(),
        unlockedModules: []
      });""")

# Update save permissions handle
save_permissions = """
  const handleSavePermissions = async () => {
    if (!editingUser) return;
    try {
      await setDoc(doc(db, "users", editingUser.id), {
        ...editingUser,
        unlockedModules: editingUnlockedModules
      });
      setEditingUser(null);
      fetchUsers();
      alert("Cập nhật quyền thành công!");
    } catch (e) {
      console.error(e);
      alert("Lỗi khi cập nhật");
    }
  };
"""
content = content.replace("  const handleDeleteRecipe = async (id: string) => {", save_permissions + "  const handleDeleteRecipe = async (id: string) => {")

# Render modal
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
                      {isUnlocked ? "Mở khóa" : "Đã khóa"}
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

content = content.replace("  return (\n    <div", modal_jsx + "  return (\n    <div")

# Add button to table
edit_btn = """                            {user.role !== 'admin' && (
                              <div className="flex justify-end gap-2">
                                <button onClick={() => {
                                  setEditingUser(user);
                                  setEditingUnlockedModules(user.unlockedModules || []);
                                }} className="p-2 text-stone-400 hover:text-emerald-500 bg-white hover:bg-emerald-50 rounded-lg transition-colors border border-transparent hover:border-emerald-100" title="Cấp quyền">
                                  <Settings2 size={16} />
                                </button>
                                <button onClick={() => handleDeleteUser(user.id)} className="p-2 text-stone-400 hover:text-rose-500 bg-white hover:bg-rose-50 rounded-lg transition-colors border border-transparent hover:border-rose-100" title="Xóa tài khoản">
                                  <Trash2 size={16} />
                                </button>
                              </div>
                            )}"""
content = content.replace("""                            {user.role !== 'admin' && (
                              <button onClick={() => handleDeleteUser(user.id)} className="p-2 text-stone-400 hover:text-rose-500 bg-white hover:bg-rose-50 rounded-lg transition-colors border border-transparent hover:border-rose-100">
                                <Trash2 size={16} />
                              </button>
                            )}""", edit_btn)

with open('src/components/AdminDashboard.tsx', 'w') as f:
    f.write(content)

print("Modified AdminDashboard")
