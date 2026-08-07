import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add Lock
content = content.replace('LogOut } from "lucide-react";', 'LogOut, Lock } from "lucide-react";')

# Listen to currentUser updates to sync unlockedModules if the user is a student
use_effect_user = """
  // Sync currentUser with DB in case admin changes permissions while user is logged in
  useEffect(() => {
    if (!currentUser || currentUser.role === 'admin') return;
    const unsubscribe = onSnapshot(doc(db, "users", currentUser.id), (doc) => {
      if (doc.exists()) {
        setCurrentUser({ id: doc.id, ...doc.data() });
      }
    });
    return () => unsubscribe();
  }, [currentUser?.id, currentUser?.role]);
"""
content = content.replace('  const [showAdmin, setShowAdmin] = useState(false);\n', '  const [showAdmin, setShowAdmin] = useState(false);\n' + use_effect_user)
content = content.replace('import { collection, getDocs, onSnapshot } from "firebase/firestore";', 'import { collection, getDocs, onSnapshot, doc } from "firebase/firestore";')

nav_item_old = """            {courseData.modules.map((module) => {
              const Icon = module.icon;
              const isActive = activeModuleId === module.id;
              return (
                <button
                  key={module.id}
                  onClick={() => {
                    setActiveModuleId(module.id);
                    setIsMobileMenuOpen(false);
                  }}
                  className={`w-full flex items-center gap-3.5 px-4 py-3 text-left text-sm font-semibold rounded-xl transition-all duration-200 group ${
                    isActive
                      ? "bg-white text-amber-700 shadow-sm border border-stone-200/60"
                      : "text-stone-600 hover:bg-white hover:text-stone-900 border border-transparent"
                  }`}
                >
                  <Icon size={18} className={`transition-colors ${isActive ? "text-amber-600" : "text-stone-400 group-hover:text-stone-600"}`} />
                  <span className="flex-1 truncate">{module.title}</span>
                  <ChevronRight size={14} className={`transition-all ${isActive ? "opacity-100 text-amber-600 translate-x-0" : "opacity-0 -translate-x-2 group-hover:opacity-100 text-stone-300 group-hover:translate-x-0"}`} />
                </button>
              );
            })}"""

nav_item_new = """            {courseData.modules.map((module) => {
              const Icon = module.icon;
              const isActive = activeModuleId === module.id;
              const isLocked = currentUser?.role !== 'admin' && !(currentUser?.unlockedModules || []).includes(module.id);
              
              return (
                <button
                  key={module.id}
                  onClick={() => {
                    if (isLocked) return;
                    setActiveModuleId(module.id);
                    setIsMobileMenuOpen(false);
                  }}
                  disabled={isLocked}
                  className={`w-full flex items-center gap-3.5 px-4 py-3 text-left text-sm font-semibold rounded-xl transition-all duration-200 group ${
                    isLocked 
                      ? "opacity-50 cursor-not-allowed text-stone-400"
                      : isActive
                        ? "bg-white text-amber-700 shadow-sm border border-stone-200/60"
                        : "text-stone-600 hover:bg-white hover:text-stone-900 border border-transparent"
                  }`}
                >
                  {isLocked ? (
                    <Lock size={18} className="text-stone-400" />
                  ) : (
                    <Icon size={18} className={`transition-colors ${isActive ? "text-amber-600" : "text-stone-400 group-hover:text-stone-600"}`} />
                  )}
                  <span className="flex-1 truncate">{module.title}</span>
                  {!isLocked && (
                    <ChevronRight size={14} className={`transition-all ${isActive ? "opacity-100 text-amber-600 translate-x-0" : "opacity-0 -translate-x-2 group-hover:opacity-100 text-stone-300 group-hover:translate-x-0"}`} />
                  )}
                </button>
              );
            })}"""

content = content.replace(nav_item_old, nav_item_new)

# Force user to activeModuleId that is unlocked
force_unlocked = """
  // Ensure activeModuleId is unlocked, else switch to first unlocked
  useEffect(() => {
    if (currentUser && currentUser.role !== 'admin') {
      const unlocked = currentUser.unlockedModules || [];
      if (!unlocked.includes(activeModuleId)) {
        if (unlocked.length > 0) {
          setActiveModuleId(unlocked[0]);
        }
      }
    }
  }, [currentUser, activeModuleId]);
"""
content = content.replace("  const [costYield, setCostYield] = useState<number>(10);\n", force_unlocked + "  const [costYield, setCostYield] = useState<number>(10);\n")


with open('src/App.tsx', 'w') as f:
    f.write(content)

print("Modified App.tsx permissions")
