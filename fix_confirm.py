import re

with open('src/components/AdminDashboard.tsx', 'r') as f:
    content = f.read()

# Remove confirm from handleDeleteUser
content = content.replace('if (!confirm("Bạn có chắc chắn muốn xóa tài khoản này?")) return;', 'if (!window.confirm("Xóa tài khoản này? (Lưu ý: Mở app trong tab mới nếu nút không hoạt động)")) return;')

# Remove confirm from handleDeleteRecipe
content = content.replace('if (!confirm("Bạn có chắc chắn muốn xóa công thức này?")) return;', 'if (!window.confirm("Xóa công thức này? (Lưu ý: Mở app trong tab mới nếu nút không hoạt động)")) return;')

with open('src/components/AdminDashboard.tsx', 'w') as f:
    f.write(content)
