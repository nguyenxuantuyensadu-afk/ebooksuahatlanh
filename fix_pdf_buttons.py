import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Replace the buttons
old_btn = r'<button onClick=\{exportActiveModuleToPDF\} disabled=\{isDownloading\} data-html2canvas-ignore="true" className="flex items-center gap-2 px-4 py-2.5 bg-rose-50 text-rose-600 hover:bg-rose-100 rounded-xl text-sm font-bold transition-colors disabled:opacity-50"><Download size=\{16\} />\{isDownloading \? "Đang xuất PDF\.\.\." : "Xuất PDF slide"\}</button>'

new_btn = r'<button onClick={exportActiveModuleToPDF} className="print:hidden flex items-center gap-2 px-4 py-2.5 bg-rose-50 text-rose-600 hover:bg-rose-100 rounded-xl text-sm font-bold transition-colors"><Download size={16} />Xuất PDF slide</button>'

content = re.sub(old_btn, new_btn, content)

with open('src/App.tsx', 'w') as f:
    f.write(content)
