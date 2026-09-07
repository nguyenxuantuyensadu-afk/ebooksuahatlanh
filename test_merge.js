const defaultModule = { id: "recipes", recipeGroups: [{groupName: "1", val: 1}, {groupName: "2", val: 2}] };
const m = { id: "recipes", recipeGroups: [{groupName: "1", val: 1}] };

const mergedModule = { ...m };
if (mergedModule.id === "recipes" && defaultModule && defaultModule.recipeGroups) {
    if (!mergedModule.recipeGroups) mergedModule.recipeGroups = [];
    defaultModule.recipeGroups.forEach(defaultGroup => {
        const existingGroup = mergedModule.recipeGroups.find(g => g.groupName === defaultGroup.groupName);
        if (!existingGroup) {
            mergedModule.recipeGroups.push(defaultGroup);
        }
    });
}
console.log(mergedModule.recipeGroups);
