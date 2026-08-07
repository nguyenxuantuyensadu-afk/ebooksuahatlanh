import re

with open('src/components/AdminDashboard.tsx', 'r') as f:
    content = f.read()

# Add state
if 'const [itemToDelete, setItemToDelete]' not in content:
    state_injection = '  const [itemToDelete, setItemToDelete] = useState<{id: string, type: "user" | "recipe"} | null>(null);\n'
    content = content.replace('  const [editingUser, setEditingUser] = useState<any>(null);', '  const [editingUser, setEditingUser] = useState<any>(null);\n' + state_injection)

# Modify handleDeleteUser
content = re.sub(
    r'const handleDeleteUser = async \(id: string\) => {[\s\S]*?if \(!.*?\) return;[\s\S]*?try {',
    'const handleDeleteUser = async (id: string) => {\n    try {',
    content
)

content = content.replace('onClick={(e) => {\n                                  e.preventDefault();\n                                  e.stopPropagation();\n                                  handleDeleteUser(user.id);\n                                }}', 'onClick={(e) => {\n                                  e.preventDefault();\n                                  e.stopPropagation();\n                                  setItemToDelete({id: user.id, type: "user"});\n                                }}')

# Modify handleDeleteRecipe
content = re.sub(
    r'const handleDeleteRecipe = async \(id: string\) => {[\s\S]*?if \(!.*?\) return;[\s\S]*?try {',
    'const handleDeleteRecipe = async (id: string) => {\n    try {',
    content
)

content = content.replace('onClick={(e) => { e.preventDefault(); e.stopPropagation(); handleDeleteRecipe(recipe.id); }}', 'onClick={(e) => { e.preventDefault(); e.stopPropagation(); setItemToDelete({id: recipe.id, type: "recipe"}); }}')

# Add modal JSX
modal_jsx = """
      {itemToDelete && (
        <div className="fixed inset-0 bg-stone-900/40 backdrop-blur-sm z-[100] flex items-center justify-center p-4">
          <div className="bg-white rounded-3xl p-6 w-full max-w-sm shadow-xl border border-stone-200 text-center">
            <h3 className="text-xl font-bold text-stone-900 mb-2">Xác nhận xóa</h3>
            <p className="text-stone-500 mb-6">Bạn có chắc chắn muốn xóa {itemToDelete.type === 'user' ? 'tài khoản' : 'công thức'} này không? Hành động này không thể hoàn tác.</p>
            <div className="flex gap-3">
              <button 
                onClick={() => setItemToDelete(null)}
                className="flex-1 py-3 bg-stone-100 hover:bg-stone-200 text-stone-700 font-bold rounded-xl transition-colors"
              >
                Hủy
              </button>
              <button 
                onClick={() => {
                  if (itemToDelete.type === 'user') handleDeleteUser(itemToDelete.id);
                  if (itemToDelete.type === 'recipe') handleDeleteRecipe(itemToDelete.id);
                  setItemToDelete(null);
                }}
                className="flex-1 py-3 bg-rose-500 hover:bg-rose-600 text-white font-bold rounded-xl transition-colors"
              >
                Xóa ngay
              </button>
            </div>
          </div>
        </div>
      )}
"""

target = 'return (\n    <div className="animate-in fade-in slide-in-from-bottom-4 duration-500 bg-white rounded-3xl p-2 md:p-8 relative">'
if modal_jsx not in content:
    content = re.sub(r'return\s*\(\s*<div className="animate-in fade-in slide-in-from-bottom-4 duration-500 bg-white rounded-3xl p-2 md:p-8 relative">', target + modal_jsx, content)

with open('src/components/AdminDashboard.tsx', 'w') as f:
    f.write(content)
