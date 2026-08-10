import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Replace state
content = content.replace(
    'const [showOnlyEasy, setShowOnlyEasy] = useState(false);',
    'const [difficultyFilter, setDifficultyFilter] = useState<string | null>(null);'
)

# Replace buttons
old_button = """                <button 
                  onClick={() => setShowOnlyEasy(!showOnlyEasy)}
                  className={`px-8 py-4 rounded-2xl font-bold transition-all border whitespace-nowrap shadow-sm flex items-center gap-2 justify-center ${showOnlyEasy ? 'bg-teal-600 text-white border-teal-600' : 'bg-white text-stone-600 border-stone-200 hover:border-teal-200 hover:bg-teal-50'}`}
                >
                  {showOnlyEasy ? (
                    <>
                      <CheckCircle2 size={20} className="text-teal-200" />
                      Đang lọc: Easy
                    </>
                  ) : (
                    'Chỉ hiện món Easy'
                  )}
                </button>"""

new_buttons = """                <div className="flex bg-stone-100 p-1.5 rounded-2xl w-full md:w-auto overflow-x-auto shadow-inner border border-stone-200">
                  <button
                    onClick={() => setDifficultyFilter(null)}
                    className={`px-4 py-2.5 rounded-xl font-bold text-sm transition-all whitespace-nowrap ${
                      difficultyFilter === null ? 'bg-white text-stone-800 shadow-sm ring-1 ring-stone-200/50' : 'text-stone-500 hover:text-stone-700 hover:bg-stone-200/50'
                    }`}
                  >
                    Tất cả
                  </button>
                  <button
                    onClick={() => setDifficultyFilter('Easy')}
                    className={`flex items-center gap-2 px-4 py-2.5 rounded-xl font-bold text-sm transition-all whitespace-nowrap ${
                      difficultyFilter === 'Easy' ? 'bg-green-50 text-green-700 shadow-sm ring-1 ring-green-200/50' : 'text-stone-500 hover:text-green-700 hover:bg-green-50/50'
                    }`}
                  >
                    <span className="w-1.5 h-1.5 rounded-full bg-green-500 shrink-0"></span>
                    Dễ (Easy)
                  </button>
                  <button
                    onClick={() => setDifficultyFilter('Medium')}
                    className={`flex items-center gap-2 px-4 py-2.5 rounded-xl font-bold text-sm transition-all whitespace-nowrap ${
                      difficultyFilter === 'Medium' ? 'bg-amber-50 text-amber-700 shadow-sm ring-1 ring-amber-200/50' : 'text-stone-500 hover:text-amber-700 hover:bg-amber-50/50'
                    }`}
                  >
                    <span className="w-1.5 h-1.5 rounded-full bg-amber-500 shrink-0"></span>
                    Trung bình
                  </button>
                  <button
                    onClick={() => setDifficultyFilter('Hard')}
                    className={`flex items-center gap-2 px-4 py-2.5 rounded-xl font-bold text-sm transition-all whitespace-nowrap ${
                      difficultyFilter === 'Hard' ? 'bg-rose-50 text-rose-700 shadow-sm ring-1 ring-rose-200/50' : 'text-stone-500 hover:text-rose-700 hover:bg-rose-50/50'
                    }`}
                  >
                    <span className="w-1.5 h-1.5 rounded-full bg-rose-500 shrink-0"></span>
                    Nâng cao
                  </button>
                </div>"""

content = content.replace(old_button, new_buttons)

content = content.replace(
    '{!recipeSearch && !showOnlyEasy && (',
    '{!recipeSearch && !difficultyFilter && ('
)

content = content.replace(
    '{!recipeSearch && !showOnlyEasy && course.modules[6].recipeGroups && (',
    '{!recipeSearch && !difficultyFilter && course.modules[6].recipeGroups && ('
)

content = content.replace(
    'if (!recipeSearch && !showOnlyEasy && idx !== activeGroupIdx) {',
    'if (!recipeSearch && !difficultyFilter && idx !== activeGroupIdx) {'
)

old_filter_logic = """                    if (showOnlyEasy) {
                      return searchMatch && getDifficulty(recipe.prepTip) === "Easy";
                    }
                    return searchMatch;"""
new_filter_logic = """                    if (difficultyFilter) {
                      return searchMatch && getDifficulty(recipe.prepTip) === difficultyFilter;
                    }
                    return searchMatch;"""
content = content.replace(old_filter_logic, new_filter_logic)

content = content.replace(
    '{(recipeSearch || showOnlyEasy) && (',
    '{(recipeSearch || difficultyFilter) && ('
)

with open('src/App.tsx', 'w') as f:
    f.write(content)
