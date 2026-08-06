import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# For each module from 1 to 7, the ending div for the header needs the button added
pattern = re.compile(
    r'(<h3 className="text-\[1\.75rem\][^"]+">\{courseData\.modules\[\d+\]\.title\}</h3>\n\s*</div>)',
    re.DOTALL
)

def repl(match):
    original = match.group(1)
    
    # Extract the indentation of the </div>
    lines = original.split('\n')
    div_line = lines[-1]
    indent = div_line[:len(div_line) - len(div_line.lstrip())]
    
    if "Xuất PDF slide" in original:
        return original
        
    button = f'{indent}  <button onClick={{exportActiveModuleToPDF}} disabled={{isDownloading}} data-html2canvas-ignore="true" className="flex items-center gap-2 px-4 py-2.5 bg-rose-50 text-rose-600 hover:bg-rose-100 rounded-xl text-sm font-bold transition-colors disabled:opacity-50"><Download size={{16}} />{{isDownloading ? "Đang xuất PDF..." : "Xuất PDF slide"}}</button>'
    
    new_str = lines[0] + f'\n{indent}</div>\n' + button + f'\n{indent[:-2]}</div>'
    return new_str

new_content = pattern.sub(repl, content)

with open('src/App.tsx', 'w') as f:
    f.write(new_content)
