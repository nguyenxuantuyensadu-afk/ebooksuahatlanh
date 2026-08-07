import re

with open('src/components/AdminDashboard.tsx', 'r') as f:
    content = f.read()

# Extract the modal
modal_pattern = r"\s*\{editingUser && \(\s*<div className=\"fixed inset-0[\s\S]*?</div>\s*</div>\s*\)\}\s*"
match = re.search(modal_pattern, content)

if match:
    modal_jsx = match.group(0)
    # Remove it from its current position
    content = content.replace(modal_jsx, "\n")
    
    # Insert it inside the return div
    target = '  return (\n    <div className="animate-in fade-in slide-in-from-bottom-4 duration-500 bg-white rounded-3xl p-2 md:p-8 relative">'
    content = content.replace(target, target + "\n" + modal_jsx)
    
    # Also fix the text "Mở khóa" vs "Đã khóa" to be clearer
    content = content.replace('{isUnlocked ? "Mở khóa" : "Đã khóa"}', '{isUnlocked ? "Khóa lại" : "Mở khóa"}')

    with open('src/components/AdminDashboard.tsx', 'w') as f:
        f.write(content)
    print("Fixed modal position")
else:
    print("Could not find modal")
