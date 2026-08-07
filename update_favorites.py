import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# 1. Update imports
content = content.replace(
    'import { Plus, Trash2, CheckCircle2, ChevronRight, Menu, X, Search, ChevronDown, ChevronUp, Printer, Download, LogOut, Lock } from "lucide-react";',
    'import { Plus, Trash2, CheckCircle2, ChevronRight, Menu, X, Search, ChevronDown, ChevronUp, Printer, Download, LogOut, Lock, Star } from "lucide-react";'
)

# 2. Add toggleFavoriteModule
hook_code = """
  const toggleFavoriteModule = async (moduleId: string) => {
    if (!currentUser || currentUser.role === 'admin') return;
    const favorites = currentUser.favoriteModules || [];
    const isFavorite = favorites.includes(moduleId);
    const newFavorites = isFavorite
      ? favorites.filter((id: string) => id !== moduleId)
      : [...favorites, moduleId];
    
    try {
      await updateDoc(doc(db, "users", currentUser.id), {
        favoriteModules: newFavorites
      });
      if (!isFavorite) {
        toast.success("Đã thêm vào mục yêu thích!", { id: "fav" });
      } else {
        toast.success("Đã gỡ khỏi mục yêu thích", { id: "fav" });
      }
    } catch (error) {
      console.error(error);
      toast.error("Lỗi khi cập nhật yêu thích");
    }
  };

  const favoriteModules = currentUser?.favoriteModules || [];
"""
content = content.replace(
    'const progressPercentage = Math.round((completedModules.length / courseData.modules.length) * 100) || 0;',
    'const progressPercentage = Math.round((completedModules.length / courseData.modules.length) * 100) || 0;\n' + hook_code
)

# 3. Add to sidebar
fav_sidebar = """
            {favoriteModules.length > 0 && !moduleSearch && (
              <div className="mb-8">
                <p className="text-[11px] font-bold text-amber-600 uppercase tracking-widest mb-3 flex items-center gap-1.5">
                  <Star size={12} className="fill-amber-600" /> Bài học yêu thích
                </p>
                <div className="space-y-1.5">
                  {courseData.modules.filter(m => favoriteModules.includes(m.id)).map(module => {
                    const Icon = module.icon;
                    const isActive = activeModuleId === module.id;
                    const isLocked = currentUser?.role !== 'admin' && !(currentUser?.unlockedModules || []).includes(module.id);
                    return (
                      <button
                        key={`fav-${module.id}`}
                        onClick={() => {
                          if (isLocked) return;
                          setActiveModuleId(module.id);
                          setIsMobileMenuOpen(false);
                        }}
                        disabled={isLocked}
                        className={`w-full flex items-center gap-3.5 px-4 py-2.5 text-left text-sm font-semibold rounded-xl transition-all duration-200 group ${
                          isLocked 
                            ? "opacity-50 cursor-not-allowed text-stone-400"
                            : isActive
                              ? "bg-amber-50 text-amber-700 shadow-sm border border-amber-100"
                              : "text-stone-600 hover:bg-white hover:text-stone-900 border border-transparent"
                        }`}
                      >
                        {isLocked ? (
                          <Lock size={16} className="text-stone-400" />
                        ) : (
                          <Icon size={16} className={`transition-colors ${isActive ? "text-amber-600" : "text-stone-400 group-hover:text-stone-600"}`} />
                        )}
                        <span className="flex-1 truncate">{module.title}</span>
                      </button>
                    );
                  })}
                </div>
              </div>
            )}
"""
content = content.replace(
    '<p className="text-[11px] font-bold text-stone-400 uppercase tracking-widest mb-4 mt-8 lg:mt-0">Mục lục khóa học</p>',
    fav_sidebar + '\n            <p className="text-[11px] font-bold text-stone-400 uppercase tracking-widest mb-4 mt-8 lg:mt-0">Mục lục khóa học</p>'
)

# 4. Update the export buttons to include Favorite button
btn_replacement = """
                    <div className="print:hidden flex items-center gap-3">
                      {currentUser?.role !== 'admin' && (
                        <button 
                          onClick={() => toggleFavoriteModule(activeModuleId)} 
                          className={`p-2.5 rounded-xl border transition-colors ${favoriteModules.includes(activeModuleId) ? 'bg-amber-50 border-amber-200 text-amber-500' : 'bg-white border-stone-200 text-stone-400 hover:text-amber-500 hover:border-amber-200 shadow-sm'}`}
                          title={favoriteModules.includes(activeModuleId) ? "Bỏ yêu thích" : "Thêm vào yêu thích"}
                        >
                          <Star size={18} className={favoriteModules.includes(activeModuleId) ? "fill-amber-500" : ""} />
                        </button>
                      )}
                      <button onClick={exportActiveModuleToPDF} className="flex items-center gap-2 px-4 py-2.5 bg-rose-50 text-rose-600 hover:bg-rose-100 rounded-xl text-sm font-bold transition-colors"><Download size={16} />Xuất PDF slide</button>
                    </div>
"""

content = content.replace(
    '<button onClick={exportActiveModuleToPDF} className="print:hidden flex items-center gap-2 px-4 py-2.5 bg-rose-50 text-rose-600 hover:bg-rose-100 rounded-xl text-sm font-bold transition-colors"><Download size={16} />Xuất PDF slide</button>',
    btn_replacement.strip()
)

with open('src/App.tsx', 'w') as f:
    f.write(content)
