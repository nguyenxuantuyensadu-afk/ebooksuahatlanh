import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add state
if "const [moduleSearch, setModuleSearch] = useState" not in content:
    content = content.replace(
        'const [recipeSearch, setRecipeSearch] = useState("");',
        'const [recipeSearch, setRecipeSearch] = useState("");\n  const [moduleSearch, setModuleSearch] = useState("");'
    )

# Filter modules
filtered_modules_code = """
            {courseData.modules.filter((module) => 
              module.title.toLowerCase().includes(moduleSearch.toLowerCase())
            ).map((module) => {
"""
content = content.replace('{courseData.modules.map((module) => {', filtered_modules_code)

# Add Search Input above progress bar or "Mục lục khóa học"
search_bar_jsx = """
            <div className="mb-6 relative">
              <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <Search size={16} className="text-stone-400" />
              </div>
              <input
                type="text"
                placeholder="Tìm kiếm bài học..."
                value={moduleSearch}
                onChange={(e) => setModuleSearch(e.target.value)}
                className="w-full pl-9 pr-3 py-2.5 bg-white border border-stone-200 rounded-xl text-sm focus:outline-none focus:border-amber-500 focus:ring-1 focus:ring-amber-500 text-stone-700 placeholder:text-stone-400 transition-colors"
              />
              {moduleSearch && (
                <button 
                  onClick={() => setModuleSearch("")}
                  className="absolute inset-y-0 right-0 pr-3 flex items-center text-stone-400 hover:text-stone-600"
                >
                  <X size={14} />
                </button>
              )}
            </div>
"""

content = content.replace(
    '<p className="text-[11px] font-bold text-stone-400 uppercase tracking-widest mb-4 mt-8 lg:mt-0">Mục lục khóa học</p>',
    search_bar_jsx + '\n            <p className="text-[11px] font-bold text-stone-400 uppercase tracking-widest mb-4 mt-8 lg:mt-0">Mục lục khóa học</p>'
)

with open('src/App.tsx', 'w') as f:
    f.write(content)
