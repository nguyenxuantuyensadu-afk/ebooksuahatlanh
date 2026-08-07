import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# 1. Update imports
content = content.replace(
    'import { collection, getDocs, onSnapshot, doc } from "firebase/firestore";',
    'import { collection, getDocs, onSnapshot, doc, updateDoc } from "firebase/firestore";'
)

# 2. Add toggle function and calculations
# Find where activeModuleId is defined
hook_code = """
  const toggleModuleCompletion = async () => {
    if (!currentUser || currentUser.role === 'admin') return;
    const completed = currentUser.completedModules || [];
    const isCompleted = completed.includes(activeModuleId);
    const newCompleted = isCompleted 
      ? completed.filter((id: string) => id !== activeModuleId)
      : [...completed, activeModuleId];
    
    try {
      await updateDoc(doc(db, "users", currentUser.id), {
        completedModules: newCompleted
      });
      if (!isCompleted) {
        toast.success("Chúc mừng bạn đã hoàn thành phần này!", { icon: "🎉" });
      }
    } catch (error) {
      console.error(error);
      toast.error("Lỗi khi lưu trạng thái");
    }
  };

  const completedModules = currentUser?.completedModules || [];
  const progressPercentage = Math.round((completedModules.length / courseData.modules.length) * 100) || 0;
"""
content = content.replace(
    'const [expandedRecipeId, setExpandedRecipeId] = useState<string | null>(null);',
    'const [expandedRecipeId, setExpandedRecipeId] = useState<string | null>(null);\n' + hook_code
)

# 3. Add progress bar to sidebar
sidebar_code = """
            <div className="mb-6 hidden lg:block pr-4">
              <div className="flex justify-between items-center mb-2">
                <span className="text-[11px] font-bold text-stone-400 uppercase tracking-widest">Tiến độ học tập</span>
                <span className="text-xs font-bold text-amber-600">{progressPercentage}%</span>
              </div>
              <div className="h-2 w-full bg-stone-200 rounded-full overflow-hidden">
                <div 
                  className="h-full bg-amber-500 transition-all duration-500 ease-out" 
                  style={{ width: `${progressPercentage}%` }}
                />
              </div>
            </div>
            <p className="text-[11px] font-bold text-stone-400 uppercase tracking-widest mb-4 mt-8 lg:mt-0">Mục lục khóa học</p>
"""
content = content.replace(
    '<p className="text-[11px] font-bold text-stone-400 uppercase tracking-widest mb-4 mt-8 lg:mt-0">Mục lục khóa học</p>',
    sidebar_code
)

# 4. Add checkmark to completed module in sidebar
content = content.replace(
    '<span className="flex-1 truncate">{module.title}</span>',
    '<span className="flex-1 truncate">{module.title}</span>\n                  {completedModules.includes(module.id) && !isLocked && <CheckCircle2 size={16} className="text-emerald-500 ml-2" />}'
)

# 5. Add button to mark as complete at the end of the module content
complete_btn_code = """
          <div className="mt-16 pt-8 border-t border-stone-200 flex flex-col sm:flex-row items-center justify-between gap-4 print:hidden">
            <div>
              <h4 className="font-bold text-stone-900">Hoàn thành bài học này?</h4>
              <p className="text-sm text-stone-500">Đánh dấu hoàn thành để theo dõi tiến độ của bạn</p>
            </div>
            <button
              onClick={toggleModuleCompletion}
              className={`px-6 py-3 rounded-xl font-bold flex items-center gap-2 transition-all ${
                completedModules.includes(activeModuleId)
                  ? "bg-emerald-100 text-emerald-700 hover:bg-emerald-200"
                  : "bg-stone-900 text-white hover:bg-stone-800"
              }`}
            >
              {completedModules.includes(activeModuleId) ? (
                <>
                  <CheckCircle2 size={18} /> Đã hoàn thành
                </>
              ) : (
                "Đánh dấu hoàn thành"
              )}
            </button>
          </div>
"""
content = content.replace(
    '{/* Footer */}',
    complete_btn_code + '\n          {/* Footer */}'
)

with open('src/App.tsx', 'w') as f:
    f.write(content)
