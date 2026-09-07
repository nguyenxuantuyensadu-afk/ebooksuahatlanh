import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

old_code = """               setTimeout(() => {
                   setDoc(doc(db, "course_content", "main"), merged).catch(console.error);
               }, 2000);"""

new_code = """               setTimeout(() => {
                   const cloneToSave = JSON.parse(JSON.stringify(merged, (key, value) => key === 'icon' ? undefined : value));
                   setDoc(doc(db, "course_content", "main"), cloneToSave).catch(console.error);
               }, 2000);"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('src/App.tsx', 'w') as f:
        f.write(content)
    print("Fixed setDoc")
else:
    print("Could not find the target string")
