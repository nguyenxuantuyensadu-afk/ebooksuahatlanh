import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add import
if 'import Quiz from' not in content:
    content = content.replace(
        "import NotesPanel from './components/NotesPanel';",
        "import NotesPanel from './components/NotesPanel';\nimport Quiz from './components/Quiz';"
    )

# Add Quiz to the end of each module
# We can just put it right before the </main> tag since it uses activeModuleId
quiz_component = "          <Quiz moduleId={activeModuleId} currentUser={currentUser} />"
if quiz_component not in content:
    content = content.replace(
        "          {/* Footer */}",
        f"{quiz_component}\n          {{/* Footer */}}"
    )

with open('src/App.tsx', 'w') as f:
    f.write(content)
