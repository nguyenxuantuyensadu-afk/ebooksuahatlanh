import re
with open('src/App.tsx', 'r') as f:
    content = f.read()

old_stepper = """<div className="flex items-center gap-1 bg-white rounded-lg border border-teal-200 p-0.5 shadow-sm">
                                        <button 
                                          onClick={(e) => { e.stopPropagation(); setRecipeMultiplier(prev => Math.max(0.5, prev - 0.5)); }} 
                                          className="w-7 h-7 flex justify-center items-center rounded hover:bg-teal-50 text-teal-700 font-bold"
                                        >-</button>
                                        <span className="w-10 text-center text-sm font-bold text-teal-900">{recipeMultiplier}L</span>
                                        <button 
                                          onClick={(e) => { e.stopPropagation(); setRecipeMultiplier(prev => prev + 0.5); }} 
                                          className="w-7 h-7 flex justify-center items-center rounded hover:bg-teal-50 text-teal-700 font-bold"
                                        >+</button>
                                      </div>"""

new_stepper = """<div className="flex items-center gap-1 bg-white rounded-lg border border-teal-200 p-0.5 shadow-sm">
                                        <button 
                                          onClick={(e) => { e.stopPropagation(); setRecipeMultiplier(prev => Math.max(0.5, prev - 0.5)); }} 
                                          className="download-section w-7 h-7 flex justify-center items-center rounded hover:bg-teal-50 text-teal-700 font-bold"
                                        >-</button>
                                        <span className="w-10 text-center text-sm font-bold text-teal-900">{recipeMultiplier}L</span>
                                        <button 
                                          onClick={(e) => { e.stopPropagation(); setRecipeMultiplier(prev => prev + 0.5); }} 
                                          className="download-section w-7 h-7 flex justify-center items-center rounded hover:bg-teal-50 text-teal-700 font-bold"
                                        >+</button>
                                      </div>"""

content = content.replace(old_stepper, new_stepper)
with open('src/App.tsx', 'w') as f:
    f.write(content)
