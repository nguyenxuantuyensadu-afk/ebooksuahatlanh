import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add state
if 'const [recipeMultiplier, setRecipeMultiplier] = useState(1);' not in content:
    content = content.replace(
        'const [sweetenerPrefs, setSweetenerPrefs] = useState<Record<string, \'sugar\' | \'milk\'>>({});',
        'const [sweetenerPrefs, setSweetenerPrefs] = useState<Record<string, \'sugar\' | \'milk\'>>({});\n  const [recipeMultiplier, setRecipeMultiplier] = useState(1);'
    )

# Update onClick
content = content.replace(
    'onClick={() => setExpandedRecipeId(isExpanded ? null : recipeId)}',
    'onClick={() => { setExpandedRecipeId(isExpanded ? null : recipeId); setRecipeMultiplier(1); }}'
)

# Update expanded recipe
# From: <p className="text-sm font-bold text-teal-900 leading-relaxed">{recipe.recipe}</p>
# To: 
replacement = """
                                    <div className="mb-4 flex items-center justify-between print:hidden">
                                      <span className="text-xs font-bold text-teal-800 uppercase tracking-wider">Khẩu phần (Lít)</span>
                                      <div className="flex items-center gap-1 bg-white rounded-lg border border-teal-200 p-0.5 shadow-sm">
                                        <button 
                                          onClick={(e) => { e.stopPropagation(); setRecipeMultiplier(prev => Math.max(0.5, prev - 0.5)); }} 
                                          className="w-7 h-7 flex justify-center items-center rounded hover:bg-teal-50 text-teal-700 font-bold"
                                        >-</button>
                                        <span className="w-10 text-center text-sm font-bold text-teal-900">{recipeMultiplier}L</span>
                                        <button 
                                          onClick={(e) => { e.stopPropagation(); setRecipeMultiplier(prev => prev + 0.5); }} 
                                          className="w-7 h-7 flex justify-center items-center rounded hover:bg-teal-50 text-teal-700 font-bold"
                                        >+</button>
                                      </div>
                                    </div>
                                    <p className="text-sm font-bold text-teal-900 leading-relaxed">
                                      {recipe.recipe.replace(/(\\d+(?:\\.\\d+)?)(\\s*)(g|ml|lít|trái|quả)/gi, (match, num, space, unit) => {
                                        const val = parseFloat(num) * recipeMultiplier;
                                        // format to remove trailing .0 if integer
                                        const displayVal = val % 1 === 0 ? val : val.toFixed(1);
                                        return `${displayVal}${space}${unit}`;
                                      })}
                                    </p>
"""

content = content.replace('<p className="text-sm font-bold text-teal-900 leading-relaxed">{recipe.recipe}</p>', replacement.strip())

with open('src/App.tsx', 'w') as f:
    f.write(content)
