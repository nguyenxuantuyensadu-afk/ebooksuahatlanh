import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

content = content.replace(
    'import { course as defaultCourseData } from "./data";',
    'import { courseData as defaultCourseData } from "./data";'
)

with open('src/App.tsx', 'w') as f:
    f.write(content)
