import re

with open('src/components/NotesPanel.tsx', 'r') as f:
    content = f.read()

if "import { toast } from 'react-hot-toast';" not in content:
    content = content.replace("import React, {", "import { toast } from 'react-hot-toast';\nimport React, {")

# Add toast to save success
content = content.replace('setSaved(true);', 'setSaved(true);\n        toast.success("Ghi chú đã được lưu", { id: "note-save", duration: 2000 });')
content = content.replace('alert(', 'toast.error(') # Just in case

with open('src/components/NotesPanel.tsx', 'w') as f:
    f.write(content)
