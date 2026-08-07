import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add import
import_statement = "import NotesPanel from './components/NotesPanel';\n"
content = content.replace('import AdminDashboard from "./components/AdminDashboard";', 'import AdminDashboard from "./components/AdminDashboard";\n' + import_statement)

# Add to render tree, just before closing main
target = "</main>"
content = content.replace(target, target + "\n        <NotesPanel currentUser={currentUser} activeModuleId={activeModuleId} />")

with open('src/App.tsx', 'w') as f:
    f.write(content)
