import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add useEffect and imports for Firestore
if "import { collection," not in content:
    content = content.replace('import { motion, AnimatePresence } from "motion/react";', 'import { motion, AnimatePresence } from "motion/react";\nimport { collection, getDocs, onSnapshot } from "firebase/firestore";\nimport { db } from "./lib/firebase";')

# Inject useEffect inside App
use_effect_code = """
  useEffect(() => {
    // Listen to custom recipes
    const unsubscribe = onSnapshot(collection(db, "recipes"), (snapshot) => {
      const customRecipes: any[] = [];
      snapshot.forEach(doc => customRecipes.push({ id: doc.id, ...doc.data() }));
      
      // Find module index for recipes
      const recipeModuleIdx = courseData.modules.findIndex(m => m.id === "recipes");
      if (recipeModuleIdx !== -1 && courseData.modules[recipeModuleIdx].recipeGroups) {
        let groups = courseData.modules[recipeModuleIdx].recipeGroups;
        
        // Remove old custom group if it exists
        groups = groups.filter((g: any) => g.groupName !== "Công thức tùy chỉnh (Mới)");
        
        if (customRecipes.length > 0) {
          groups.push({
            groupName: "Công thức tùy chỉnh (Mới)",
            groupDesc: "Các công thức do Quản trị viên thêm vào",
            recipes: customRecipes
          });
        }
        
        courseData.modules[recipeModuleIdx].recipeGroups = groups;
        
        // Force a small state update if we are on the recipes tab
        if (activeModuleId === 'recipes') {
           setRecipeSearch(prev => prev + " ");
           setTimeout(() => setRecipeSearch(prev => prev.trim()), 0);
        }
      }
    });
    
    return () => unsubscribe();
  }, [activeModuleId]);
"""

if "onSnapshot(collection(db" not in content:
    content = content.replace("  const [showAdmin, setShowAdmin] = useState(false);\n", "  const [showAdmin, setShowAdmin] = useState(false);\n" + use_effect_code)

with open('src/App.tsx', 'w') as f:
    f.write(content)

print("Added recipes listener")
