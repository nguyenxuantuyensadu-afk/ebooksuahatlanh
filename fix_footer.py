import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

target = """          <footer className="mt-24 pt-8 pb-4 border-t border-stone-200 text-center">
            <p className="text-sm text-stone-500 font-medium">
              Thiết kế dành riêng cho Học Viên Khởi Nghiệp - Mô hình Take-away Thực Chiến
            </p>
            <p className="text-xs text-stone-400 font-medium mt-2">
              Made by XUANTUYEN
            </p>
          </footer>"""

replacement = """          <footer className="mt-24 pt-8 pb-4 border-t border-stone-200 text-center">
            <p className="text-sm text-stone-500 font-medium">
              Thiết kế dành riêng cho Học Viên Khởi Nghiệp - Mô hình Take-away Thực Chiến
            </p>
            <p className="text-xs text-stone-400 font-medium mt-2">
              Made in by XUANTUYEN
            </p>
          </footer>"""

content = content.replace(target, replacement)

with open('src/App.tsx', 'w') as f:
    f.write(content)
