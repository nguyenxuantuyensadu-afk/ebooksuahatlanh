import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add new recipe button
new_recipe_btn = """                  <p className="text-teal-800 text-sm font-medium flex-1">
                    {course.modules[6].recipeGroups[activeGroupIdx].groupDesc}
                  </p>
                  {currentUser?.role === 'admin' && (
                     <button onClick={() => setEditingItem({ type: 'new_recipe', path: { gIdx: activeGroupIdx }, data: { name: '', recipe: '', usage: '', prepTip: '' }})} className="px-3 py-1.5 bg-teal-600 hover:bg-teal-700 text-white text-sm font-bold rounded-lg shadow-sm flex items-center gap-1 shrink-0 transition-colors"><Plus size={14}/> Thêm món</button>
                  )}"""

content = re.sub(r'<p className="text-teal-800 text-sm font-medium">\s*\{course\.modules\[6\]\.recipeGroups\[activeGroupIdx\]\.groupDesc\}\s*</p>', new_recipe_btn, content)
content = content.replace('className="mb-6 p-4 bg-teal-50 rounded-xl border border-teal-100 print:hidden"', 'className="mb-6 p-4 bg-teal-50 rounded-xl border border-teal-100 print:hidden flex items-center justify-between gap-4"')

# Add edit/delete for recipes
old_recipe_actions = """                                <Star size={16} className={favoriteRecipes.includes(recipe.name) ? "fill-amber-500 text-amber-500" : ""} />
                              </button>
                            )}
                            <span"""

new_recipe_actions = """                                <Star size={16} className={favoriteRecipes.includes(recipe.name) ? "fill-amber-500 text-amber-500" : ""} />
                              </button>
                            )}
                            {currentUser?.role === 'admin' && (
                              <button
                                onClick={() => setEditingItem({ type: 'recipe', path: { gIdx: idx, rIdx }, data: recipe })}
                                className="p-1.5 text-stone-300 hover:text-teal-600 hover:bg-teal-50 rounded-lg transition-colors print:hidden"
                                title="Sửa công thức"
                              >
                                <Edit2 size={16} />
                              </button>
                            )}
                            {currentUser?.role === 'admin' && (
                              <button
                                onClick={async () => {
                                  if(window.confirm('Xóa công thức này?')) {
                                     let updatedCourse = JSON.parse(JSON.stringify(course));
                                     const recipeModuleIdx = updatedCourse.modules.findIndex((m: any) => m.id === "recipes");
                                     updatedCourse.modules[recipeModuleIdx].recipeGroups[idx].recipes.splice(rIdx, 1);
                                     const cloneToSave = JSON.parse(JSON.stringify(updatedCourse, (key, value) => key === 'icon' ? undefined : value));
                                     await setDoc(doc(db, "course_content", "main"), cloneToSave);
                                     toast.success('Đã xóa!');
                                  }
                                }}
                                className="p-1.5 text-stone-300 hover:text-rose-600 hover:bg-rose-50 rounded-lg transition-colors print:hidden"
                                title="Xóa công thức"
                              >
                                <Trash2 size={16} />
                              </button>
                            )}
                            <span"""
content = content.replace(old_recipe_actions, new_recipe_actions)

with open('src/App.tsx', 'w') as f:
    f.write(content)
