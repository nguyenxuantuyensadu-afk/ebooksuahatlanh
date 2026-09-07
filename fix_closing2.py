import re

with open('src/recipesData.ts', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("    ],\n  {\n    groupName: \"11.", "    ]\n  },\n  {\n    groupName: \"11.")
content = content.replace("    ],\n  {\n    groupName: '11.", "    ]\n  },\n  {\n    groupName: '11.")
# Wait, let's just use regex
content = re.sub(r'    \],\s*\{\s*groupName:\s*"11\.', '    ]\n  },\n  {\n    groupName: "11.', content)

with open('src/recipesData.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed closing brace 2.")
