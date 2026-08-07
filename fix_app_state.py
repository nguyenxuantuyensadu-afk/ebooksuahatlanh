import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Change isAuthenticated to hold user object
if "const [isAuthenticated, setIsAuthenticated]" in content:
    content = content.replace("const [isAuthenticated, setIsAuthenticated] = useState(false);", 
                              "const [currentUser, setCurrentUser] = useState<any>(null);")

if "if (!isAuthenticated) {" in content:
    content = content.replace("""  if (!isAuthenticated) {
    return <Login onLogin={() => setIsAuthenticated(true)} />;
  }""", """  if (!currentUser) {
    return <Login onLogin={(user) => setCurrentUser(user)} />;
  }""")

# Add AdminDashboard import
if "import AdminDashboard" not in content:
    content = content.replace('import Login from "./components/Login";', 'import Login from "./components/Login";\nimport AdminDashboard from "./components/AdminDashboard";')

# Add showAdmin state
if "const [showAdmin, setShowAdmin]" not in content:
    content = content.replace('const [currentUser, setCurrentUser] = useState<any>(null);', 'const [currentUser, setCurrentUser] = useState<any>(null);\n  const [showAdmin, setShowAdmin] = useState(false);')

# Add Admin button to UI
admin_button_code = """
              {currentUser?.role === 'admin' && (
                <button 
                  onClick={() => setShowAdmin(!showAdmin)}
                  className="px-4 py-2 bg-rose-600 text-white rounded-xl text-sm font-bold flex items-center gap-2"
                >
                  {showAdmin ? 'Trở về Khóa học' : 'Quản trị viên'}
                </button>
              )}
"""

if "Quản trị viên" not in content:
    target_header = """            <button onClick={() => setIsMobileMenuOpen(true)} className="p-2 -ml-2 text-stone-600 lg:hidden rounded-lg hover:bg-stone-100">
              <Menu size={24} />
            </button>
            <div className="flex-1 flex justify-end">"""
    
    if target_header in content:
        content = content.replace(target_header, target_header + admin_button_code)

# Wrap main content in a conditional to show Admin Dashboard
admin_render = """
        {showAdmin ? (
          <AdminDashboard onClose={() => setShowAdmin(false)} />
        ) : (
"""

if "<AdminDashboard" not in content:
    # Find the main tag
    main_tag = """        <main className="flex-1 lg:pl-[280px] min-h-screen">"""
    content = content.replace(main_tag, main_tag + admin_render)
    
    # We need to close the conditional right before </main>
    # Find </main> at the end
    content = content.replace("        </main>", "        )}\n        </main>")

with open('src/App.tsx', 'w') as f:
    f.write(content)

print("Updated App.tsx state")
