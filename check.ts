import { courseData } from './src/data';
courseData.modules.forEach(m => {
  Object.entries(m).forEach(([k,v]) => {
    if (Array.isArray(v)) console.log(`${m.id}.${k}`);
  });
});
