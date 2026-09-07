import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

old_logic = """             // Sync newly added recipe groups from defaultData if they are missing in Firebase
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
                mergedModule._needsSync = hasChanges; // flag for after map
             }"""

content = content.replace(old_logic, new_logic)

# Now we need to handle the after map sync.
old_after_map = """           });
        }
        setCourseState(merged);"""

new_after_map = """           });
           
           const recipeMod = merged.modules.find((m: any) => m.id === "recipes");
           if (recipeMod && recipeMod._needsSync) {
               delete recipeMod._needsSync;
               setTimeout(() => {
                   setDoc(doc(db, "course_content", "main"), merged).catch(console.error);
               }, 2000);
           }
        }
        setCourseState(merged);"""

content = content.replace(old_after_map, new_after_map)

with open('src/App.tsx', 'w') as f:
    f.write(content)
print("Fixed App.tsx mapping issue.")
