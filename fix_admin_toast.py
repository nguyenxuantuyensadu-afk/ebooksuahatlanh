import re

with open('src/components/AdminDashboard.tsx', 'r') as f:
    content = f.read()

# Add import
if "import { toast } from 'react-hot-toast';" not in content:
    content = content.replace('import React,', "import { toast } from 'react-hot-toast';\nimport React,")

# Replace alerts
content = content.replace('alert("Tạo tài khoản học viên thành công!");', 'toast.success("Tạo tài khoản học viên thành công!");')
content = content.replace('alert("Lỗi khi tạo tài khoản");', 'toast.error("Lỗi khi tạo tài khoản");')
content = content.replace('alert("Lỗi khi xóa");', 'toast.error("Lỗi khi xóa");')
content = content.replace('alert("Thêm công thức mới thành công!");', 'toast.success("Thêm công thức mới thành công!");')
content = content.replace('alert("Lỗi khi thêm công thức");', 'toast.error("Lỗi khi thêm công thức");')
content = content.replace('alert("Cập nhật quyền thành công!");', 'toast.success("Cập nhật quyền thành công!");')
content = content.replace('alert("Lỗi khi cập nhật");', 'toast.error("Lỗi khi cập nhật");')

with open('src/components/AdminDashboard.tsx', 'w') as f:
    f.write(content)
