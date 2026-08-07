import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# 1. Update imports
content = content.replace(
    'import { collection, getDocs, onSnapshot, doc, updateDoc } from "firebase/firestore";',
    'import { collection, getDocs, onSnapshot, doc, updateDoc, increment, setDoc } from "firebase/firestore";'
)

if 'Eye' not in content:
    content = content.replace(
        'import { Plus, Trash2, CheckCircle2, ChevronRight, Menu, X, Search, ChevronDown, ChevronUp, Printer, Download, LogOut, Lock, Star } from "lucide-react";',
        'import { Plus, Trash2, CheckCircle2, ChevronRight, Menu, X, Search, ChevronDown, ChevronUp, Printer, Download, LogOut, Lock, Star, Eye } from "lucide-react";'
    )

# 2. Add State and Logic for Module Views
hook_code = """
  const [moduleViews, setModuleViews] = useState<Record<string, number>>({});
  const [viewedModules] = useState(() => new Set<string>());

  useEffect(() => {
    const unsubscribe = onSnapshot(collection(db, "module_stats"), (snapshot) => {
      const views: Record<string, number> = {};
      snapshot.forEach(doc => {
        views[doc.id] = doc.data().views || 0;
      });
      setModuleViews(views);
    });
    return () => unsubscribe();
  }, []);

  useEffect(() => {
    if (activeModuleId && !viewedModules.has(activeModuleId)) {
      viewedModules.add(activeModuleId);
      const docRef = doc(db, "module_stats", activeModuleId);
      setDoc(docRef, { views: increment(1) }, { merge: true }).catch(console.error);
    }
  }, [activeModuleId, viewedModules]);
"""

content = content.replace(
    'const [expandedRecipeId, setExpandedRecipeId] = useState<string | null>(null);',
    'const [expandedRecipeId, setExpandedRecipeId] = useState<string | null>(null);\n' + hook_code
)

# 3. Add view counter to the buttons
old_title_span_reg = '<span className="flex-1 truncate">{module.title}</span>'
new_title_span_reg = """<div className="flex-1 overflow-hidden">
                    <span className="block truncate">{module.title}</span>
                    <span className="flex items-center gap-1 text-[10px] opacity-70 mt-0.5">
                      <Eye size={10} /> {moduleViews[module.id] || 0} lượt xem
                    </span>
                  </div>"""
content = content.replace(old_title_span_reg, new_title_span_reg)

with open('src/App.tsx', 'w') as f:
    f.write(content)
