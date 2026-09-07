import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

old_logic = """             // Sync newly added recipe groups from defaultData if they are missing in Firebase
             if (mergedModule.id === "recipes" && defaultModule && defaultModule.recipeGroups) {
                if (!mergedModule.recipeGroups) mergedModule.recipeGroups = [];
                defaultModule.recipeGroups.forEach(defaultGroup => {
                   const existingGroup = mergedModule.recipeGroups.find((g: any) => g.groupName === defaultGroup.groupName);
                   if (!existingGroup) {
                      mergedModule.recipeGroups.push(defaultGroup);
                   }
                });
             }"""

new_logic = """             // Sync newly added recipe groups from defaultData if they are missing in Firebase
             if (mergedModule.id === "recipes" && defaultModule && defaultModule.recipeGroups) {
                let currentGroups = mergedModule.recipeGroups ? [...mergedModule.recipeGroups] : [];
                let hasChanges = false;
                defaultModule.recipeGroups.forEach(defaultGroup => {
                   const existingGroup = currentGroups.find((g: any) => g.groupName === defaultGroup.groupName);
                   if (!existingGroup) {
                      currentGroups.push(defaultGroup);
                      hasChanges = true;
                   }
                });
                mergedModule.recipeGroups = currentGroups;
                
                if (hasChanges) {
                    setTimeout(() => {
                        setDoc(doc(db, "course_content", "main"), { ...defaultCourseData, ...data, modules: merged.modules }, { merge: true }).catch(console.error);
                    }, 2000);
                }
             }"""

content = content.replace(old_logic, new_logic)

with open('src/App.tsx', 'w') as f:
    f.write(content)

print("Updated App.tsx again")
