import re

with open('src/components/AdminDashboard.tsx', 'r') as f:
    content = f.read()

recipe_trash_old = """                            <button onClick={() => handleDeleteRecipe(recipe.id)} className="p-2 text-stone-400 hover:text-rose-500 bg-white hover:bg-rose-50 rounded-lg transition-colors border border-transparent hover:border-rose-100">"""
recipe_trash_new = """                            <button type="button" onClick={(e) => { e.preventDefault(); e.stopPropagation(); handleDeleteRecipe(recipe.id); }} className="p-2 text-stone-400 hover:text-rose-500 bg-white hover:bg-rose-50 rounded-lg transition-colors border border-transparent hover:border-rose-100">"""

content = content.replace(recipe_trash_old, recipe_trash_new)

with open('src/components/AdminDashboard.tsx', 'w') as f:
    f.write(content)
