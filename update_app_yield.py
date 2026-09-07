import re

with open('src/App.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Add label for yield_info in editing form
old_form = "                       key === 'prepTip' ? 'Lưu ý sơ chế & Độ khó' : key}"
new_form = "                       key === 'yield_info' ? 'Thành phẩm' : \n                       key === 'prepTip' ? 'Lưu ý sơ chế & Độ khó' : key}"
content = content.replace(old_form, new_form)

# Add yield_info display in collapsed view (around line 2085, after diff tag)
old_diff_tag = """                            'bg-rose-50 text-rose-700 border-rose-200'
                          }`}>
                            {diff}
                          </span>"""
new_diff_tag = """                            'bg-rose-50 text-rose-700 border-rose-200'
                          }`}>
                            {diff}
                          </span>
                          {recipe.yield_info && (
                            <span className="px-2.5 py-1 text-[10px] uppercase tracking-wider font-bold rounded-md border bg-blue-50 text-blue-700 border-blue-200 print:border-stone-300 print:text-stone-700">
                              Thành phẩm: {recipe.yield_info.replace('1 L', recipeMultiplier + ' L').replace('1 Lít', recipeMultiplier + ' Lít')}
                            </span>
                          )}"""
content = content.replace(old_diff_tag, new_diff_tag)

# Wait, in the expanded view we should also display it
# Let's find expanded view
