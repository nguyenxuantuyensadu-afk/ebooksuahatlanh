import { toast } from 'react-hot-toast';
import React, { useState, useEffect } from 'react';
import { Users, FileText, X, Plus, Trash2, Edit2, Save, Lock, Unlock, Settings2 } from 'lucide-react';
import { courseData } from '../data';
import { collection, getDocs, doc, setDoc, deleteDoc, addDoc } from 'firebase/firestore';
import { db } from '../lib/firebase';


const extractLockablePaths = (course: any) => {
  const paths: any[] = [];
  course.modules?.forEach((module: any) => {
    const modObj = { moduleId: module.id, moduleTitle: module.title, arrays: [] as any[] };
    Object.entries(module).forEach(([key, value]) => {
      if (Array.isArray(value)) {
        const arrObj = { key, items: [] as any[] };
        value.forEach((item: any, idx: number) => {
          let label = `Mục ${idx + 1}`;
          if (typeof item === 'string') label = item.substring(0, 50) + (item.length > 50 ? '...' : '');
          else if (item.name) label = item.name;
          else if (item.title) label = item.title;
          else if (item.group) label = item.group;
          else if (item.groupName) label = item.groupName;
          else if (item.task) label = item.task;
          else if (item.problem) label = item.problem;
          
          arrObj.items.push({ path: `${module.id}.${key}.${idx}`, label });
        });
        modObj.arrays.push(arrObj);
      }
    });
    if (modObj.arrays.length > 0) paths.push(modObj);
  });
  return paths;
};

export default function AdminDashboard({ onClose, courseData }: { onClose: () => void, courseData: any }) {
  const [activeTab, setActiveTab] = useState<'users' | 'content' | 'full_content'>('users');
  const [userSubTab, setUserSubTab] = useState<'list' | 'locks'>('list');
  const [jsonContent, setJsonContent] = useState('');
  const [jsonError, setJsonError] = useState('');
  const [users, setUsers] = useState<any[]>([]);
  const [recipes, setRecipes] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  
  // New User Form
  const [newUsername, setNewUsername] = useState('');
  const [newPassword, setNewPassword] = useState('');

  // New Recipe Form
  const [newRecipeName, setNewRecipeName] = useState('');
  const [newRecipeFormula, setNewRecipeFormula] = useState('');
  const [newRecipeYield, setNewRecipeYield] = useState('');
  const [newRecipeDifficulty, setNewRecipeDifficulty] = useState('Easy');
  const [editingUser, setEditingUser] = useState<any>(null);
  const [itemToDelete, setItemToDelete] = useState<{id: string, type: "user" | "recipe"} | null>(null);

  const [editingUnlockedModules, setEditingUnlockedModules] = useState<string[]>([]);
  const [editingLockedPaths, setEditingLockedPaths] = useState<string[]>([]);

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

  
  const toggleLock = async (path: string) => {
    const currentLocks = courseData.lockedPaths || [];
    const newLocks = currentLocks.includes(path) 
      ? currentLocks.filter((p: string) => p !== path) 
      : [...currentLocks, path];
    
    const updatedCourse = { ...courseData, lockedPaths: newLocks };
    const cloneToSave = JSON.parse(JSON.stringify(updatedCourse, (key, value) => key === 'icon' ? undefined : value));
    
    try {
      await setDoc(doc(db, "course_content", "main"), cloneToSave);
      toast.success(newLocks.includes(path) ? 'Đã khoá nội dung' : 'Đã mở khoá nội dung');
    } catch (e) {
      toast.error('Lỗi khi cập nhật khoá!');
    }
  };

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



  const fetchUsers = async () => {
    setLoading(true);
    try {
      const snapshot = await getDocs(collection(db, "users"));
      const userList: any[] = [];
      snapshot.forEach((doc) => {
        userList.push({ id: doc.id, ...doc.data() });
      });
      setUsers(userList);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  const fetchRecipes = async () => {
    setLoading(true);
    try {
      const snapshot = await getDocs(collection(db, "recipes"));
      const recipeList: any[] = [];
      snapshot.forEach((doc) => {
        recipeList.push({ id: doc.id, ...doc.data() });
      });
      setRecipes(recipeList);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (activeTab === 'users') {
      fetchUsers();
    } else {
      fetchRecipes();
    }
  }, [activeTab]);

  const handleCreateUser = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newUsername || !newPassword) return;
    try {
      await setDoc(doc(db, "users", newUsername), {
        username: newUsername,
        password: newPassword,
        role: "student",
        createdAt: new Date().toISOString(),
        unlockedModules: []
      });
      setNewUsername('');
      setNewPassword('');
      fetchUsers();
      toast.success("Tạo tài khoản học viên thành công!");
    } catch (e) {
      console.error(e);
      toast.error("Lỗi khi tạo tài khoản");
    }
  };

  const handleDeleteUser = async (id: string) => {
    try {
      await deleteDoc(doc(db, "users", id));
      fetchUsers();
    } catch (e) {
      console.error(e);
      toast.error("Lỗi khi xóa");
    }
  };

  const handleCreateRecipe = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newRecipeName || !newRecipeFormula) return;
    try {
      await addDoc(collection(db, "recipes"), {
        name: newRecipeName,
        recipe: newRecipeFormula,
        usage: newRecipeYield,
        difficulty: newRecipeDifficulty,
        group: "Công thức tùy chỉnh (Mới)",
        createdAt: new Date().toISOString()
      });
      setNewRecipeName('');
      setNewRecipeFormula('');
      setNewRecipeYield('');
      setNewRecipeDifficulty('Easy');
      fetchRecipes();
      toast.success("Thêm công thức mới thành công!");
    } catch (e) {
      console.error(e);
      toast.error("Lỗi khi thêm công thức");
    }
  };
  

  const handleSavePermissions = async () => {
    if (!editingUser) return;
    try {
      await setDoc(doc(db, "users", editingUser.id), {
        ...editingUser,
        unlockedModules: editingUnlockedModules,
        lockedPaths: editingLockedPaths
      });
      setEditingUser(null);
      fetchUsers();
      toast.success("Cập nhật quyền thành công!");
    } catch (e) {
      console.error(e);
      toast.error("Lỗi khi cập nhật");
    }
  };
  const handleDeleteRecipe = async (id: string) => {
    try {
      await deleteDoc(doc(db, "recipes", id));
      fetchRecipes();
    } catch (e) {
      console.error(e);
    }
  };
return (
    <div className="animate-in fade-in slide-in-from-bottom-4 duration-500 bg-white rounded-3xl p-2 md:p-8 relative">
      {itemToDelete && (
        <div className="fixed inset-0 bg-stone-900/40 backdrop-blur-sm z-[100] flex items-center justify-center p-4">
          <div className="bg-white rounded-3xl p-6 w-full max-w-sm shadow-xl border border-stone-200 text-center">
            <h3 className="text-xl font-bold text-stone-900 mb-2">Xác nhận xóa</h3>
            <p className="text-stone-500 mb-6">Bạn có chắc chắn muốn xóa {itemToDelete.type === 'user' ? 'tài khoản' : 'công thức'} này không? Hành động này không thể hoàn tác.</p>
            <div className="flex gap-3">
              <button 
                onClick={() => setItemToDelete(null)}
                className="flex-1 py-3 bg-stone-100 hover:bg-stone-200 text-stone-700 font-bold rounded-xl transition-colors"
              >
                Hủy
              </button>
              <button 
                onClick={() => {
                  if (itemToDelete.type === 'user') handleDeleteUser(itemToDelete.id);
                  if (itemToDelete.type === 'recipe') handleDeleteRecipe(itemToDelete.id);
                  setItemToDelete(null);
                }}
                className="flex-1 py-3 bg-rose-500 hover:bg-rose-600 text-white font-bold rounded-xl transition-colors"
              >
                Xóa ngay
              </button>
            </div>
          </div>
        </div>
      )}

      {editingUser && (
        <div className="fixed inset-0 bg-stone-900/40 backdrop-blur-sm z-50 flex items-center justify-center p-4 z-[100]">
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
            <div className="space-y-3 mb-6 max-h-[60vh] overflow-y-auto pr-2">
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
            </div>
            <button onClick={handleSavePermissions} className="w-full py-3 bg-stone-900 text-white rounded-xl font-bold flex items-center justify-center gap-2">
              <Save size={18} /> Lưu Thay Đổi
            </button>
          </div>
        </div>
      )}

      <div className="flex justify-between items-center mb-8 pb-6 border-b border-stone-200">
        <div>
          <h2 className="text-3xl font-black text-stone-900 mb-2">Bảng Điều Khiển</h2>
          <p className="text-stone-500 font-medium">Quản lý hệ thống khóa học</p>
        </div>
        <button onClick={onClose} className="p-2 text-stone-400 hover:text-stone-900 bg-stone-100 hover:bg-stone-200 rounded-xl transition-colors">
          <X size={24} />
        </button>
      </div>

      <div className="flex gap-4 mb-8">
        <button 
          onClick={() => setActiveTab('users')}
          className={`flex items-center gap-2 px-6 py-3 rounded-xl font-bold transition-all ${
            activeTab === 'users' ? 'bg-stone-900 text-white shadow-md' : 'bg-stone-100 text-stone-600 hover:bg-stone-200'
          }`}
        >
          <Users size={18} /> Quản lý Học Viên
        </button>
        <button 
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
      </div>

      {activeTab === 'users' && (
        <div className="space-y-6">
          <div className="flex gap-4 border-b border-stone-200 pb-4">
             <button onClick={() => setUserSubTab('list')} className={`px-4 py-2.5 font-bold rounded-xl transition-colors ${userSubTab === 'list' ? 'bg-stone-800 text-white shadow-sm' : 'text-stone-500 hover:bg-stone-100'}`}>Danh sách Học viên</button>
             <button onClick={() => setUserSubTab('locks')} className={`px-4 py-2.5 font-bold rounded-xl flex items-center gap-2 transition-colors ${userSubTab === 'locks' ? 'bg-stone-800 text-white shadow-sm' : 'text-stone-500 hover:bg-stone-100'}`}><Lock size={16}/> Khoá Nội Dung Chung</button>
          </div>
          {userSubTab === 'list' && (
            <div className="grid md:grid-cols-3 gap-8">
          <div className="md:col-span-1">
            <div className="bg-stone-50 p-6 rounded-[2rem] border border-stone-200 sticky top-24">
              <h3 className="font-bold text-lg text-stone-900 mb-6">Tạo tài khoản mới</h3>
              <form onSubmit={handleCreateUser} className="space-y-4">
                <div>
                  <label className="block text-sm font-bold text-stone-700 mb-2">Tên đăng nhập</label>
                  <input type="text" value={newUsername} onChange={e => setNewUsername(e.target.value)} className="w-full px-4 py-3 bg-white border border-stone-200 rounded-xl font-medium focus:ring-2 focus:ring-emerald-500 focus:outline-none" placeholder="VD: hv_nguyenvan" required />
                </div>
                <div>
                  <label className="block text-sm font-bold text-stone-700 mb-2">Mật khẩu</label>
                  <input type="text" value={newPassword} onChange={e => setNewPassword(e.target.value)} className="w-full px-4 py-3 bg-white border border-stone-200 rounded-xl font-medium focus:ring-2 focus:ring-emerald-500 focus:outline-none" placeholder="Mật khẩu mặc định" required />
                </div>
                <button type="submit" className="w-full py-3 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-xl flex items-center justify-center gap-2 transition-colors">
                  <Plus size={18} /> Cấp Tài Khoản
                </button>
              </form>
            </div>
          </div>
          <div className="md:col-span-2">
            <div className="bg-white rounded-[2rem] border border-stone-200 overflow-hidden shadow-sm">
              <div className="px-6 py-5 bg-stone-50 border-b border-stone-200">
                <h3 className="font-bold text-lg text-stone-900">Danh sách tài khoản ({users.length})</h3>
              </div>
              {loading ? (
                <div className="p-10 text-center text-stone-500 font-medium">Đang tải dữ liệu...</div>
              ) : (
                <div className="overflow-x-auto">
                  <table className="w-full text-left border-collapse">
                    <thead>
                      <tr className="bg-stone-50/50">
                        <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500">Tên Đăng Nhập</th>
                        <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500">Vai Trò</th>
                        <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500 text-right">Thao tác</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-stone-100">
                      {users.map(user => (
                        <tr key={user.id} className="hover:bg-stone-50">
                          <td className="py-4 px-6 font-bold text-stone-800">{user.username}</td>
                          <td className="py-4 px-6">
                            <span className={`px-2.5 py-1 text-xs font-bold rounded-md border ${
                              user.role === 'admin' ? 'bg-amber-50 text-amber-700 border-amber-200' : 'bg-blue-50 text-blue-700 border-blue-200'
                            }`}>
                              {user.role}
                            </span>
                          </td>
                          <td className="py-4 px-6 text-right">
                            {user.role !== 'admin' && (
                              <div className="flex justify-end gap-2">
                                <button type="button" onClick={(e) => {
                                  e.preventDefault();
                                  e.stopPropagation();
                                  setEditingUser(user);
                                  setEditingUnlockedModules(user.unlockedModules || []);
                                  setEditingLockedPaths(user.lockedPaths || []);
                                }} className="p-2 text-stone-400 hover:text-emerald-500 bg-white hover:bg-emerald-50 rounded-lg transition-colors border border-transparent hover:border-emerald-100" title="Cấp quyền">
                                  <Settings2 size={16} />
                                </button>
                                <button type="button" onClick={(e) => {
                                  e.preventDefault();
                                  e.stopPropagation();
                                  setItemToDelete({id: user.id, type: "user"});
                                }} className="p-2 text-stone-400 hover:text-rose-500 bg-white hover:bg-rose-50 rounded-lg transition-colors border border-transparent hover:border-rose-100" title="Xóa tài khoản">
                                  <Trash2 size={16} />
                                </button>
                              </div>
                            )}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}
            </div>
          </div>
        </div>
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
      {activeTab === 'content' && (
        <div className="grid md:grid-cols-3 gap-8">
          <div className="md:col-span-1">
            <div className="bg-stone-50 p-6 rounded-[2rem] border border-stone-200 sticky top-24">
              <h3 className="font-bold text-lg text-stone-900 mb-6">Thêm công thức mới</h3>
              <form onSubmit={handleCreateRecipe} className="space-y-4">
                <div>
                  <label className="block text-sm font-bold text-stone-700 mb-2">Tên món</label>
                  <input type="text" value={newRecipeName} onChange={e => setNewRecipeName(e.target.value)} className="w-full px-4 py-3 bg-white border border-stone-200 rounded-xl font-medium focus:ring-2 focus:ring-emerald-500 focus:outline-none" placeholder="VD: Sữa Đậu Nành Yến Mạch" required />
                </div>
                <div>
                  <label className="block text-sm font-bold text-stone-700 mb-2">Công thức (Gram)</label>
                  <textarea value={newRecipeFormula} onChange={e => setNewRecipeFormula(e.target.value)} className="w-full px-4 py-3 bg-white border border-stone-200 rounded-xl font-medium focus:ring-2 focus:ring-emerald-500 focus:outline-none h-24" placeholder="VD: 50g đậu nành, 30g yến mạch..." required />
                </div>
                <div>
                  <label className="block text-sm font-bold text-stone-700 mb-2">Ghi chú / Sản lượng</label>
                  <input type="text" value={newRecipeYield} onChange={e => setNewRecipeYield(e.target.value)} className="w-full px-4 py-3 bg-white border border-stone-200 rounded-xl font-medium focus:ring-2 focus:ring-emerald-500 focus:outline-none" placeholder="VD: Thu được 3 chai 330ml" />
                </div>
                <div>
                  <label className="block text-sm font-bold text-stone-700 mb-2">Độ khó</label>
                  <select value={newRecipeDifficulty} onChange={e => setNewRecipeDifficulty(e.target.value)} className="w-full px-4 py-3 bg-white border border-stone-200 rounded-xl font-medium focus:ring-2 focus:ring-emerald-500 focus:outline-none">
                    <option value="Easy">Dễ (Easy)</option>
                    <option value="Medium">Trung bình (Medium)</option>
                    <option value="Hard">Khó (Hard)</option>
                  </select>
                </div>
                <button type="submit" className="w-full py-3 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-xl flex items-center justify-center gap-2 transition-colors">
                  <Save size={18} /> Lưu Công Thức
                </button>
              </form>
            </div>
          </div>
          
          <div className="md:col-span-2">
            <div className="bg-white rounded-[2rem] border border-stone-200 overflow-hidden shadow-sm">
              <div className="px-6 py-5 bg-stone-50 border-b border-stone-200">
                <h3 className="font-bold text-lg text-stone-900">Danh sách Công thức tùy chỉnh ({recipes.length})</h3>
              </div>
              {loading ? (
                <div className="p-10 text-center text-stone-500 font-medium">Đang tải dữ liệu...</div>
              ) : recipes.length === 0 ? (
                <div className="p-10 text-center text-stone-500 font-medium">Chưa có công thức tùy chỉnh nào được thêm.</div>
              ) : (
                <div className="overflow-x-auto">
                  <table className="w-full text-left border-collapse">
                    <thead>
                      <tr className="bg-stone-50/50">
                        <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500">Tên Món</th>
                        <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500">Công thức</th>
                        <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500 text-right">Xóa</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-stone-100">
                      {recipes.map(recipe => (
                        <tr key={recipe.id} className="hover:bg-stone-50">
                          <td className="py-4 px-6 font-bold text-stone-800">
                            {recipe.name}
                            <div className="mt-1">
                              <span className={`px-2 py-0.5 text-[10px] font-bold rounded border ${
                                recipe.difficulty === 'Easy' ? 'bg-green-50 text-green-700 border-green-200' :
                                recipe.difficulty === 'Medium' ? 'bg-amber-50 text-amber-700 border-amber-200' :
                                'bg-rose-50 text-rose-700 border-rose-200'
                              }`}>
                                {recipe.difficulty}
                              </span>
                            </div>
                          </td>
                          <td className="py-4 px-6">
                            <p className="text-sm font-medium text-stone-600 line-clamp-2">{recipe.recipe}</p>
                          </td>
                          <td className="py-4 px-6 text-right">
                            <button type="button" onClick={(e) => { e.preventDefault(); e.stopPropagation(); setItemToDelete({id: recipe.id, type: "recipe"}); }} className="p-2 text-stone-400 hover:text-rose-500 bg-white hover:bg-rose-50 rounded-lg transition-colors border border-transparent hover:border-rose-100">
                              <Trash2 size={16} />
                            </button>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      

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

    </div>
  );
}
