import re

with open('src/components/AdminDashboard.tsx', 'r') as f:
    content = f.read()

# Add lockedPaths to destructuring if needed, but we pass courseData
# We need to add the extract function
extract_func = """
const extractLockablePaths = (course: any) => {
  const paths: any[] = [];
  course.modules?.forEach((module: any) => {
    const modObj = { moduleId: module.id, moduleTitle: module.title, arrays: [] as any[] };
    Object.entries(module).forEach(([key, value]) => {
      if (Array.isArray(value)) {
        const arrObj = { key, items: [] as any[] };
        value.forEach((item: any, idx: number) => {
          let label = `Mục ${idx + 1}`;
          if (typeof item === 'string') label = item.substring(0, 50) + (item.length > 50 ? '...' : '');
          else if (item.name) label = item.name;
          else if (item.title) label = item.title;
          else if (item.group) label = item.group;
          else if (item.groupName) label = item.groupName;
          else if (item.task) label = item.task;
          else if (item.problem) label = item.problem;
          
          arrObj.items.push({ path: `${module.id}.${key}.${idx}`, label });
        });
        modObj.arrays.push(arrObj);
      }
    });
    if (modObj.arrays.length > 0) paths.push(modObj);
  });
  return paths;
};
"""

# Insert extract_func before AdminDashboard function
content = content.replace("export default function AdminDashboard", extract_func + "\nexport default function AdminDashboard")

# Add the locks tab state
# const [activeTab, setActiveTab] = useState<'users' | 'content' | 'full_content'>('users');
content = content.replace(
    "useState<'users' | 'content' | 'full_content'>('users');",
    "useState<'users' | 'content' | 'locks' | 'full_content'>('users');"
)

# Add locks tab button
btn_old = """        <button 
          onClick={() => setActiveTab('full_content')}"""
btn_new = """        <button 
          onClick={() => setActiveTab('locks')}
          className={`flex items-center gap-2 px-6 py-3 rounded-xl font-bold transition-all ${
            activeTab === 'locks' ? 'bg-stone-900 text-white shadow-md' : 'bg-stone-100 text-stone-600 hover:bg-stone-200'
          }`}
        >
          <Lock size={18} /> Khoá Nội Dung
        </button>
        <button 
          onClick={() => setActiveTab('full_content')}"""
content = content.replace(btn_old, btn_new)

# Add toggleLock function inside AdminDashboard
toggle_func = """
  const toggleLock = async (path: string) => {
    const currentLocks = courseData.lockedPaths || [];
    const newLocks = currentLocks.includes(path) 
      ? currentLocks.filter((p: string) => p !== path) 
      : [...currentLocks, path];
    
    const updatedCourse = { ...courseData, lockedPaths: newLocks };
    const cloneToSave = JSON.parse(JSON.stringify(updatedCourse, (key, value) => key === 'icon' ? undefined : value));
    
    try {
      await setDoc(doc(db, "course_content", "main"), cloneToSave);
      toast.success(newLocks.includes(path) ? 'Đã khoá nội dung' : 'Đã mở khoá nội dung');
    } catch (e) {
      toast.error('Lỗi khi cập nhật khoá!');
    }
  };
"""
content = content.replace("const handleSaveJson = async () => {", toggle_func + "\n  const handleSaveJson = async () => {")

# Add locks tab content
locks_tab = """
      {activeTab === 'locks' && (
        <div className="bg-stone-50 p-6 rounded-[2rem] border border-stone-200 max-w-4xl">
          <h3 className="font-bold text-lg text-stone-900 mb-6 flex items-center gap-2"><Lock size={20} className="text-stone-500"/> Quản lý Khoá nội dung</h3>
          <p className="text-stone-500 text-sm mb-6">Bạn có thể chọn khoá các mục nhỏ bên trong từng module. Người học thông thường sẽ không nhìn thấy các nội dung bị khoá.</p>
          <div className="space-y-6">
            {extractLockablePaths(courseData).map((mod: any) => (
              <div key={mod.moduleId} className="bg-white p-5 rounded-2xl border border-stone-100 shadow-sm">
                <h4 className="font-bold text-stone-800 text-lg mb-4 pb-2 border-b border-stone-100">{mod.moduleTitle}</h4>
                <div className="space-y-6">
                  {mod.arrays.map((arr: any) => (
                    <div key={arr.key}>
                      <h5 className="font-bold text-stone-600 text-sm mb-3 uppercase tracking-wider bg-stone-50 py-1.5 px-3 rounded-lg inline-block">{arr.key}</h5>
                      <div className="flex flex-col gap-2 pl-2">
                        {arr.items.map((item: any) => {
                          const isLocked = courseData.lockedPaths?.includes(item.path);
                          return (
                            <div key={item.path} className="flex items-center justify-between p-3 hover:bg-stone-50 rounded-xl transition-colors border border-transparent hover:border-stone-100">
                              <span className={`text-sm font-medium truncate pr-4 ${isLocked ? 'text-stone-400 line-through' : 'text-stone-700'}`}>{item.label}</span>
                              <button
                                onClick={() => toggleLock(item.path)}
                                className={`p-2 rounded-lg transition-colors shrink-0 flex items-center justify-center ${isLocked ? 'bg-rose-100 text-rose-600 hover:bg-rose-200' : 'bg-stone-100 text-stone-400 hover:bg-stone-200 hover:text-stone-600'}`}
                                title={isLocked ? "Mở khoá" : "Khoá lại"}
                              >
                                {isLocked ? <Lock size={16} /> : <Unlock size={16} />}
                              </button>
                            </div>
                          );
                        })}
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
"""
content = content.replace("{activeTab === 'full_content' && (", locks_tab + "\n      {activeTab === 'full_content' && (")

with open('src/components/AdminDashboard.tsx', 'w') as f:
    f.write(content)

