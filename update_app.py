import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# 1. Rename course to courseState
content = content.replace("const [course, setCourse] = useState(defaultCourseData);", "const [courseState, setCourseState] = useState(defaultCourseData);")
content = content.replace("setCourse(merged);", "setCourseState(merged);")

# 2. Pass courseState to AdminDashboard
content = content.replace("<AdminDashboard onClose={() => setShowAdmin(false)} courseData={course} />", "<AdminDashboard onClose={() => setShowAdmin(false)} courseData={courseState} />")

# 3. Add useMemo logic
usememo_logic = """
  const course = useMemo(() => {
    if (currentUser?.role === 'admin' || !courseState.lockedPaths || courseState.lockedPaths.length === 0) return courseState;
    
    const clone = JSON.parse(JSON.stringify(courseState));
    
    clone.modules?.forEach((module: any) => {
      Object.keys(module).forEach(key => {
        if (Array.isArray(module[key])) {
          module[key] = module[key].map((item: any, idx: number) => {
            if (clone.lockedPaths.includes(`${module.id}.${key}.${idx}`)) {
              if (typeof item === 'string') return "🔒 Nội dung bị khoá (Yêu cầu quyền truy cập)";
              
              const maskedItem: any = { __isLocked: true };
              Object.keys(item).forEach(k => {
                const val = item[k];
                if (typeof val === 'string') {
                  if (['name', 'title', 'group', 'groupName', 'task', 'problem', 'desc', 'description', 'role', 'recipe', 'usage', 'prepTip', 'item'].includes(k)) {
                     maskedItem[k] = "🔒 Nội dung bị khoá";
                  } else if (k === 'color') {
                     maskedItem[k] = "bg-stone-100 text-stone-500 border-stone-200";
                  } else if (k === 'iconColor') {
                     maskedItem[k] = "bg-stone-300";
                  } else if (k.toLowerCase().includes('time') || k === 'percentage' || k === 'width' || k === 'level' || k === 'price' || k === 'quantity' || k === 'unitCost' || k === 'total' || k === 'id') {
                     maskedItem[k] = val; // structural
                  } else {
                     maskedItem[k] = "***";
                  }
                } else if (typeof val === 'number') {
                  maskedItem[k] = val; // structural/math
                } else if (Array.isArray(val)) {
                  maskedItem[k] = [];
                } else {
                  maskedItem[k] = val;
                }
              });
              return maskedItem;
            }
            return item;
          });
        }
      });
    });
    
    return clone;
  }, [courseState, currentUser]);
"""

# Insert the useMemo right after useEffect that sets it.
content = content.replace("    return () => unsubscribe();\n  }, []);", "    return () => unsubscribe();\n  }, []);\n" + usememo_logic)

with open('src/App.tsx', 'w') as f:
    f.write(content)

