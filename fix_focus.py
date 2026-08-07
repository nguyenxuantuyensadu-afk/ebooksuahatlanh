import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# 1. Update imports
if 'Maximize' not in content:
    content = content.replace(
        'import { Plus, Trash2, CheckCircle2, ChevronRight, Menu, X, Search, ChevronDown, ChevronUp, Printer, Download, LogOut, Lock, Star, Eye } from "lucide-react";',
        'import { Plus, Trash2, CheckCircle2, ChevronRight, Menu, X, Search, ChevronDown, ChevronUp, Printer, Download, LogOut, Lock, Star, Eye, Maximize, Minimize } from "lucide-react";'
    )

# 2. Add isFocusMode state
if 'const [isFocusMode, setIsFocusMode] = useState(false);' not in content:
    content = content.replace(
        'const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);',
        'const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);\n  const [isFocusMode, setIsFocusMode] = useState(false);'
    )

# 3. Apply isFocusMode to sidebar
content = content.replace(
    'isMobileMenuOpen ? "translate-x-0" : "-translate-x-full"',
    'isMobileMenuOpen ? "translate-x-0" : (isFocusMode ? "-translate-x-full" : "-translate-x-full")' # Wait, originally it was "-translate-x-full" for mobile
)

old_sidebar_class = '} lg:translate-x-0 fixed lg:sticky top-0 lg:top-0 h-screen w-72 bg-[#f8f7f5] border-r border-stone-200 p-6 overflow-y-auto transition-transform duration-300 z-40`}'
new_sidebar_class = '} ${isFocusMode ? "lg:-translate-x-full lg:hidden" : "lg:translate-x-0"} fixed lg:sticky top-0 lg:top-0 h-screen w-72 bg-[#f8f7f5] border-r border-stone-200 p-6 overflow-y-auto transition-transform duration-300 z-40`}'
content = content.replace(old_sidebar_class, new_sidebar_class)

# 4. Apply isFocusMode to NotesPanel
content = content.replace(
    '<NotesPanel currentUser={currentUser} activeModuleId={activeModuleId} />',
    '{!isFocusMode && <NotesPanel currentUser={currentUser} activeModuleId={activeModuleId} />}'
)

# 5. Add button to Hero section
old_hero = """          {/* Hero Section */}
          <div className="mb-14 pb-10 border-b border-stone-100 print:hidden">
            <div className="inline-flex items-center px-3.5 py-1.5 rounded-full bg-stone-100 text-stone-800 text-[11px] font-bold uppercase tracking-widest mb-6">
              Module Cốt Lõi
            </div>"""

new_hero = """          {/* Hero Section */}
          <div className="mb-14 pb-10 border-b border-stone-100 print:hidden">
            <div className="flex justify-between items-start mb-6">
              <div className="inline-flex items-center px-3.5 py-1.5 rounded-full bg-stone-100 text-stone-800 text-[11px] font-bold uppercase tracking-widest">
                Module Cốt Lõi
              </div>
              <button
                onClick={() => setIsFocusMode(!isFocusMode)}
                className="hidden lg:flex items-center gap-2 px-3 py-1.5 bg-white border border-stone-200 hover:bg-stone-50 hover:border-stone-300 text-stone-600 rounded-xl text-xs font-bold transition-colors shadow-sm"
                title={isFocusMode ? "Tắt chế độ tập trung" : "Bật chế độ tập trung"}
              >
                {isFocusMode ? (
                  <><Minimize size={14} /> Tắt Focus</>
                ) : (
                  <><Maximize size={14} /> Bật Focus</>
                )}
              </button>
            </div>"""
content = content.replace(old_hero, new_hero)

with open('src/App.tsx', 'w') as f:
    f.write(content)
