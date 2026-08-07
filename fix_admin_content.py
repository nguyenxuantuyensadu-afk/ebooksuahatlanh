import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Replace import courseData
content = content.replace(
    'import { courseData } from "./data";',
    'import { courseData as defaultCourseData } from "./data";'
)

# Add state
hook_code = """
  const [course, setCourse] = useState(defaultCourseData);
  useEffect(() => {
    const unsubscribe = onSnapshot(doc(db, "course_content", "main"), (docSnap) => {
      if (docSnap.exists()) {
        const data = docSnap.data();
        const merged = { ...defaultCourseData, ...data };
        if (data.modules && Array.isArray(data.modules)) {
           merged.modules = data.modules.map((m: any) => {
             const defaultModule = defaultCourseData.modules.find(dm => dm.id === m.id);
             return { ...m, icon: defaultModule?.icon || null };
           });
        }
        setCourse(merged);
      }
    });
    return () => unsubscribe();
  }, []);
"""
content = content.replace(
    'const [showAdmin, setShowAdmin] = useState(false);',
    'const [showAdmin, setShowAdmin] = useState(false);\n' + hook_code
)

# Replace all courseData with course
content = re.sub(r'\bcourseData\b', 'course', content)

# But wait, defaultCourseData was also changed by the regex! Let's fix it back
content = content.replace('defaultcourse', 'defaultCourseData')

# Now pass course to AdminDashboard
content = content.replace(
    '<AdminDashboard onClose={() => setShowAdmin(false)} />',
    '<AdminDashboard onClose={() => setShowAdmin(false)} courseData={course} />'
)

with open('src/App.tsx', 'w') as f:
    f.write(content)
