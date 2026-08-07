import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# I need to find where the `span` closes, and close the `div` right after it
target = r"                            \{diff\}\n                          </span>"
replacement = "                            {diff}\n                          </span>\n                          </div>"
content = re.sub(target, replacement, content)

with open('src/App.tsx', 'w') as f:
    f.write(content)
