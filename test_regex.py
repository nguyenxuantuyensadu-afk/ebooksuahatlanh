import re
with open('src/App.tsx', 'r') as f:
    content = f.read()
pattern = re.compile(
    r'(<div className="flex items-center gap-4 mb-6">\s*<div className="p-3\.5[^"]+">\s*<[A-Za-z]+(?:Icon)? size=\{24\} />\s*</div>\s*<h3 className="text-\[1\.75rem\][^"]+">.*?</h3>\s*</div>)',
    re.DOTALL
)
matches = pattern.findall(content)
print(f"Found {len(matches)} matches")
