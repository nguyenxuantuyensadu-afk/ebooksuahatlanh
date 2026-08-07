import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add imports
content = content.replace("import { Toaster, toast } from 'react-hot-toast';", "") # remove if exists
content = content.replace('import Login from "./components/Login";', 'import Login from "./components/Login";\nimport { Toaster, toast } from "react-hot-toast";')

# Inject Toaster for early return
content = re.sub(r'if \(!currentUser\) {\n\s*return <Login (.*?) />;\n\s*}', r'if (!currentUser) {\n    return (\n      <>\n        <Toaster position="bottom-center" />\n        <Login \1 />\n      </>\n    );\n  }', content)

# Inject Toaster for main app
content = re.sub(r'return \(\n\s*<div className="min-h-screen bg-\[#f8f7f5\]', r'return (\n    <>\n      <Toaster position="bottom-center" />\n      <div className="min-h-screen bg-[#f8f7f5]', content)
content = re.sub(r'\s*<NotesPanel currentUser={currentUser} activeModuleId={activeModuleId} />\n\s*</div>', r'        <NotesPanel currentUser={currentUser} activeModuleId={activeModuleId} />\n      </div>\n    </>', content)

# Find Logout and add toast
content = content.replace('setCurrentUser(null);\n                setShowAdmin(false);', 'setCurrentUser(null);\n                setShowAdmin(false);\n                toast.success("Đăng xuất thành công!");')

with open('src/App.tsx', 'w') as f:
    f.write(content)
