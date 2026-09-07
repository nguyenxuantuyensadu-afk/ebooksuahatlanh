import { courseData } from './src/data';
const extractLockablePaths = (course: any) => {
  const paths: any[] = [];
  course.modules.forEach((module: any) => {
    const modObj = { moduleId: module.id, moduleTitle: module.title, arrays: [] as any[] };
    Object.entries(module).forEach(([key, value]) => {
      if (Array.isArray(value)) {
        const arrObj = { key, items: [] as any[] };
        value.forEach((item: any, idx: number) => {
          let label = `Item ${idx + 1}`;
          if (typeof item === 'string') label = item.substring(0, 50) + '...';
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
console.log(JSON.stringify(extractLockablePaths(courseData), null, 2).substring(0, 1000));
