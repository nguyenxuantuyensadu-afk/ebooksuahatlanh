import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# 1. Add toggleFavoriteRecipe
hook_code = """
  const toggleFavoriteRecipe = async (recipeName: string, e: React.MouseEvent) => {
    e.stopPropagation();
    if (!currentUser || currentUser.role === 'admin') return;
    const favorites = currentUser.favoriteRecipes || [];
    const isFavorite = favorites.includes(recipeName);
    const newFavorites = isFavorite
      ? favorites.filter((name: string) => name !== recipeName)
      : [...favorites, recipeName];
    
    try {
      await updateDoc(doc(db, "users", currentUser.id), {
        favoriteRecipes: newFavorites
      });
      if (!isFavorite) {
        toast.success("Đã thêm công thức vào yêu thích!", { id: "fav-rec" });
      } else {
        toast.success("Đã gỡ công thức khỏi yêu thích", { id: "fav-rec" });
      }
    } catch (error) {
      console.error(error);
      toast.error("Lỗi khi cập nhật yêu thích");
    }
  };

  const favoriteRecipes = currentUser?.favoriteRecipes || [];
"""
content = content.replace(
    'const favoriteModules = currentUser?.favoriteModules || [];',
    'const favoriteModules = currentUser?.favoriteModules || [];\n' + hook_code
)

# 2. Update Recipe Header
old_header = """<h4 className="font-bold text-stone-900 text-lg leading-tight print:text-2xl">
                            {rIdx + 1}. {recipe.name}
                          </h4>
                          <span className={`px-2.5 py-1 text-[10px] uppercase tracking-wider font-bold rounded-md border shrink-0 print:border-stone-300 print:text-stone-700 ${"""

new_header = """<h4 className="font-bold text-stone-900 text-lg leading-tight print:text-2xl flex-1 pr-2">
                            {rIdx + 1}. {recipe.name}
                          </h4>
                          <div className="flex items-center gap-1 shrink-0">
                            {currentUser?.role !== 'admin' && (
                              <button
                                onClick={(e) => toggleFavoriteRecipe(recipe.name, e)}
                                className="p-1.5 text-stone-300 hover:text-amber-500 hover:bg-amber-50 rounded-lg transition-colors print:hidden"
                                title="Yêu thích"
                              >
                                <Star size={16} className={favoriteRecipes.includes(recipe.name) ? "fill-amber-500 text-amber-500" : ""} />
                              </button>
                            )}
                            <span className={`px-2.5 py-1 text-[10px] uppercase tracking-wider font-bold rounded-md border print:border-stone-300 print:text-stone-700 ${"""

content = content.replace(old_header, new_header)

with open('src/App.tsx', 'w') as f:
    f.write(content)
