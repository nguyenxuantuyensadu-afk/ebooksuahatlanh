import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# 1. Add nutritionFilter state
content = content.replace(
    'const [difficultyFilter, setDifficultyFilter] = useState<string | null>(null);',
    'const [difficultyFilter, setDifficultyFilter] = useState<string | null>(null);\n  const [nutritionFilter, setNutritionFilter] = useState<string | null>(null);'
)

# 2. Add healthGoals definition right above the filter UI
health_goals_def = """
              const healthGoals = [
                { id: 'giam-can', label: 'Giảm cân / Giữ dáng', color: 'text-rose-600 bg-rose-50 ring-rose-200/50', iconColor: 'bg-rose-500', keywords: ['giảm cân', 'giữ dáng', 'siết mỡ'] },
                { id: 'tang-co', label: 'Tăng cơ', color: 'text-blue-600 bg-blue-50 ring-blue-200/50', iconColor: 'bg-blue-500', keywords: ['tăng cơ', 'protein', 'gym', 'thể thao'] },
                { id: 'tang-can', label: 'Tăng cân', color: 'text-amber-600 bg-amber-50 ring-amber-200/50', iconColor: 'bg-amber-500', keywords: ['tăng cân', 'béo ngậy', 'calo cao'] },
                { id: 'canxi', label: 'Bổ sung canxi', color: 'text-emerald-600 bg-emerald-50 ring-emerald-200/50', iconColor: 'bg-emerald-500', keywords: ['canxi', 'xương khớp'] },
                { id: 'dep-da', label: 'Đẹp da', color: 'text-pink-600 bg-pink-50 ring-pink-200/50', iconColor: 'bg-pink-500', keywords: ['đẹp da', 'lão hóa', 'trẻ hóa'] },
                { id: 'tieu-hoa', label: 'Tiêu hóa / Mát gan', color: 'text-teal-600 bg-teal-50 ring-teal-200/50', iconColor: 'bg-teal-500', keywords: ['tiêu hóa', 'mát gan', 'thanh lọc', 'rau củ', 'giải nhiệt'] },
                { id: 'tri-nao', label: 'Trí não', color: 'text-indigo-600 bg-indigo-50 ring-indigo-200/50', iconColor: 'bg-indigo-500', keywords: ['trí não', 'stress', 'thần kinh'] },
              ];
"""

old_filter_ui = """              <div className="flex flex-col md:flex-row gap-4 justify-between items-start md:items-center mb-8 bg-white p-4 rounded-[1.5rem] shadow-sm border border-stone-200 print:hidden">
                <div className="relative w-full md:w-96">
                  <Search className="absolute left-4 top-1/2 -translate-y-1/2 text-stone-400" size={20} />
                  <input
                    type="text"
                    placeholder="Tìm kiếm công thức (ví dụ: macca, yến mạch...)"
                    value={recipeSearch}
                    onChange={(e) => setRecipeSearch(e.target.value)}
                    className="w-full pl-12 pr-4 py-3 bg-stone-50 border border-stone-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all font-medium text-stone-700"
                  />
                </div>
                <div className="flex bg-stone-100 p-1.5 rounded-2xl w-full md:w-auto overflow-x-auto shadow-inner border border-stone-200">
                  <button
                    onClick={() => setDifficultyFilter(null)}"""

new_filter_ui = health_goals_def + """
              <div className="flex flex-col gap-4 mb-8 bg-white p-4 rounded-[1.5rem] shadow-sm border border-stone-200 print:hidden">
                <div className="flex flex-col md:flex-row gap-4 justify-between items-start md:items-center">
                  <div className="relative w-full md:w-96">
                    <Search className="absolute left-4 top-1/2 -translate-y-1/2 text-stone-400" size={20} />
                    <input
                      type="text"
                      placeholder="Tìm kiếm công thức (ví dụ: macca, yến mạch...)"
                      value={recipeSearch}
                      onChange={(e) => setRecipeSearch(e.target.value)}
                      className="w-full pl-12 pr-4 py-3 bg-stone-50 border border-stone-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all font-medium text-stone-700"
                    />
                  </div>
                  <div className="flex bg-stone-100 p-1.5 rounded-2xl w-full md:w-auto overflow-x-auto shadow-inner border border-stone-200">
                    <button
                      onClick={() => setDifficultyFilter(null)}"""

content = content.replace(old_filter_ui, new_filter_ui)

# 3. Add the actual nutrition filters below the difficulty filter
old_filter_end = """                  </button>
                </div>
              </div>

              {/* Group Tabs */}
              {!recipeSearch && !difficultyFilter && ("""

new_filter_end = """                  </button>
                  </div>
                </div>

                <div className="flex flex-wrap items-center gap-2 pt-3 border-t border-stone-100">
                  <span className="text-sm font-bold text-stone-500 mr-2 flex items-center gap-1.5"><Heart size={16} className="text-rose-400"/> Nhu cầu:</span>
                  <button
                    onClick={() => setNutritionFilter(null)}
                    className={`px-3 py-1.5 rounded-lg font-bold text-xs transition-all whitespace-nowrap ${
                      nutritionFilter === null ? 'bg-stone-800 text-white shadow-sm' : 'bg-stone-100 text-stone-500 hover:bg-stone-200'
                    }`}
                  >
                    Tất cả
                  </button>
                  {healthGoals.map(goal => (
                    <button
                      key={goal.id}
                      onClick={() => setNutritionFilter(goal.id)}
                      className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-bold text-xs transition-all whitespace-nowrap ${
                        nutritionFilter === goal.id 
                          ? goal.color + ' shadow-sm ring-1' 
                          : 'bg-stone-50 text-stone-500 hover:bg-stone-100 border border-stone-200'
                      }`}
                    >
                      {nutritionFilter === goal.id && <span className={`w-1.5 h-1.5 rounded-full ${goal.iconColor} shrink-0`}></span>}
                      {goal.label}
                    </button>
                  ))}
                </div>
              </div>

              {/* Group Tabs */}
              {!recipeSearch && !difficultyFilter && !nutritionFilter && ("""

content = content.replace(old_filter_end, new_filter_end)

# Fix group description showing constraint
content = content.replace(
    '{!recipeSearch && !difficultyFilter && course.modules[6].recipeGroups && (',
    '{!recipeSearch && !difficultyFilter && !nutritionFilter && course.modules[6].recipeGroups && ('
)
content = content.replace(
    'if (!recipeSearch && !difficultyFilter && idx !== activeGroupIdx) {',
    'if (!recipeSearch && !difficultyFilter && !nutritionFilter && idx !== activeGroupIdx) {'
)

# 4. Modify the filter logic inside the map
old_filter_logic = """                  const filteredRecipes = group.recipes.filter(recipe => {
                    const searchMatch = matchGroup || 
                      recipe.name.toLowerCase().includes(searchLower) ||
                      recipe.usage.toLowerCase().includes(searchLower) ||
                      recipe.recipe.toLowerCase().includes(searchLower) ||
                      recipe.prepTip.toLowerCase().includes(searchLower);
                    
                    if (difficultyFilter) {
                      return searchMatch && getDifficulty(recipe.prepTip) === difficultyFilter;
                    }
                    return searchMatch;
                  });"""

new_filter_logic = """                  const filteredRecipes = group.recipes.filter(recipe => {
                    const searchMatch = matchGroup || 
                      recipe.name.toLowerCase().includes(searchLower) ||
                      recipe.usage.toLowerCase().includes(searchLower) ||
                      recipe.recipe.toLowerCase().includes(searchLower) ||
                      recipe.prepTip.toLowerCase().includes(searchLower);
                    
                    let isMatch = searchMatch;

                    if (difficultyFilter) {
                      isMatch = isMatch && (getDifficulty(recipe.prepTip) === difficultyFilter);
                    }

                    if (nutritionFilter) {
                      const goal = healthGoals.find(g => g.id === nutritionFilter);
                      if (goal) {
                        const targetText = (group.groupName + " " + recipe.name + " " + recipe.usage).toLowerCase();
                        const hasKeyword = goal.keywords.some(kw => targetText.includes(kw));
                        isMatch = isMatch && hasKeyword;
                      }
                    }

                    return isMatch;
                  });"""

content = content.replace(old_filter_logic, new_filter_logic)

# Show active filters badge
old_badge = """                        {(recipeSearch || difficultyFilter) && (
                          <div className="mb-4">
                            <span className="inline-block px-2.5 py-1 bg-stone-100 text-stone-600 text-[10px] font-bold uppercase tracking-widest rounded-lg">
                              {group.groupName}
                            </span>
                          </div>
                        )}"""

new_badge = """                        {(recipeSearch || difficultyFilter || nutritionFilter) && (
                          <div className="mb-4">
                            <span className="inline-block px-2.5 py-1 bg-stone-100 text-stone-600 text-[10px] font-bold uppercase tracking-widest rounded-lg">
                              {group.groupName}
                            </span>
                          </div>
                        )}"""

content = content.replace(old_badge, new_badge)

# Import Heart icon
content = content.replace(
    'import { Plus, Trash2, CheckCircle2, ChevronRight, Menu, X, Search, ChevronDown, ChevronUp, Printer, Download, LogOut, Lock, Star, Eye, Maximize, Minimize , Edit2, Save, Snowflake } from "lucide-react";',
    'import { Plus, Trash2, CheckCircle2, ChevronRight, Menu, X, Search, ChevronDown, ChevronUp, Printer, Download, LogOut, Lock, Star, Eye, Maximize, Minimize , Edit2, Save, Snowflake, Heart } from "lucide-react";'
)

with open('src/App.tsx', 'w') as f:
    f.write(content)
