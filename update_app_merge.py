import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

old_logic = """        if (data.modules && Array.isArray(data.modules)) {
           merged.modules = data.modules.map((m: any) => {
             const defaultModule = defaultCourseData.modules.find(dm => dm.id === m.id);
             return { ...m, icon: defaultModule?.icon || null };
           });
        }"""

new_logic = """        if (data.modules && Array.isArray(data.modules)) {
           merged.modules = data.modules.map((m: any) => {
             const defaultModule = defaultCourseData.modules.find(dm => dm.id === m.id);
             const mergedModule = { ...m, icon: defaultModule?.icon || null };
             
             // Sync newly added recipe groups from defaultData if they are missing in Firebase
             if (mergedModule.id === "recipes" && defaultModule && defaultModule.recipeGroups) {
                if (!mergedModule.recipeGroups) mergedModule.recipeGroups = [];
                defaultModule.recipeGroups.forEach(defaultGroup => {
                   const existingGroup = mergedModule.recipeGroups.find((g: any) => g.groupName === defaultGroup.groupName);
                   if (!existingGroup) {
                      mergedModule.recipeGroups.push(defaultGroup);
                   }
                });
             }
             
             return mergedModule;
           });
        }"""

content = content.replace(old_logic, new_logic)

with open('src/App.tsx', 'w') as f:
    f.write(content)

print("Updated App.tsx merge logic")
