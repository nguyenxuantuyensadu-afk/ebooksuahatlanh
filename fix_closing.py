import re

with open('src/recipesData.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# I need to find `    ],\n  {\n    groupName: "11.` and change it to `    ]\n  },\n  {\n    groupName: "11.`
content = content.replace('    ],\n  {\n    groupName: "11.', '    ]\n  },\n  {\n    groupName: "11.')
# Wait, looking at sed output:
#      { name: "Sữa Hạt Sen Xoài Chín" ... }
#    ],
#  {
#    groupName: "11. Nhóm Dành Cho Mẹ Bầu (An Thai, Lợi Sữa)",

content = content.replace('    ],\n  {\n    groupName: "11.', '    ]\n  },\n  {\n    groupName: "11.')

with open('src/recipesData.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed closing brace.")
