import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Current logic:
#  const course = useMemo(() => {
#    if (currentUser?.role === 'admin' || !courseState.lockedPaths || courseState.lockedPaths.length === 0) return courseState;
#    
#    const clone = JSON.parse(JSON.stringify(courseState));
#    
#    clone.modules?.forEach((module: any) => {

old_memo = """  const course = useMemo(() => {
    if (currentUser?.role === 'admin' || !courseState.lockedPaths || courseState.lockedPaths.length === 0) return courseState;
    
    const clone = JSON.parse(JSON.stringify(courseState));
    
    clone.modules?.forEach((module: any) => {
      Object.keys(module).forEach(key => {
        if (Array.isArray(module[key])) {
          module[key] = module[key].map((item: any, idx: number) => {
            if (clone.lockedPaths.includes(`${module.id}.${key}.${idx}`)) {"""

new_memo = """  const course = useMemo(() => {
    const userLockedPaths = currentUser?.lockedPaths || [];
    const globalLockedPaths = courseState.lockedPaths || [];
    const allLockedPaths = [...new Set([...globalLockedPaths, ...userLockedPaths])];

    if (currentUser?.role === 'admin' || allLockedPaths.length === 0) return courseState;
    
    const clone = JSON.parse(JSON.stringify(courseState));
    
    clone.modules?.forEach((module: any) => {
      Object.keys(module).forEach(key => {
        if (Array.isArray(module[key])) {
          module[key] = module[key].map((item: any, idx: number) => {
            if (allLockedPaths.includes(`${module.id}.${key}.${idx}`)) {"""

if old_memo in content:
    content = content.replace(old_memo, new_memo)
    with open('src/App.tsx', 'w') as f:
        f.write(content)
    print("App.tsx updated successfully")
else:
    print("Failed to find memo block")
