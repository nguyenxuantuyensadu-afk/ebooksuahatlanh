import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

pattern = re.compile(
    r'(<div className="flex items-center gap-4 mb-6">\s*<div className="p-3\.5[^"]+">\s*<[A-Za-z]+Icon size=\{24\} />\s*</div>\s*<h3 className="text-\[1\.75rem\][^"]+">.*?</h3>\s*</div>)',
    re.DOTALL
)

def repl(match):
    original = match.group(1)
    
    if "Xuất PDF slide" in original:
        return original
        
    new_str = original.replace('<div className="flex items-center gap-4 mb-6">', '<div className="flex flex-wrap items-center justify-between gap-4 mb-6">\n                <div className="flex items-center gap-4">')
    
    new_str = new_str.replace('</h3>\n              </div>', '</h3>\n                </div>\n                <button onClick={exportActiveModuleToPDF} disabled={isDownloading} data-html2canvas-ignore="true" className="flex items-center gap-2 px-4 py-2.5 bg-rose-50 text-rose-600 hover:bg-rose-100 rounded-xl text-sm font-bold transition-colors disabled:opacity-50"><Download size={16} />{isDownloading ? "Đang xuất PDF..." : "Xuất PDF slide"}</button>\n              </div>')
    
    return new_str

new_content = pattern.sub(repl, content)

with open('src/App.tsx', 'w') as f:
    f.write(new_content)
