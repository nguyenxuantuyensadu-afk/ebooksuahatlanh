import re

with open('src/components/AdminDashboard.tsx', 'r') as f:
    content = f.read()

# Settings button
settings_old = """                                <button onClick={() => {
                                  setEditingUser(user);
                                  setEditingUnlockedModules(user.unlockedModules || []);
                                }} className="p-2 text-stone-400 hover:text-emerald-500 bg-white hover:bg-emerald-50 rounded-lg transition-colors border border-transparent hover:border-emerald-100" title="Cấp quyền">"""
settings_new = """                                <button type="button" onClick={(e) => {
                                  e.preventDefault();
                                  e.stopPropagation();
                                  setEditingUser(user);
                                  setEditingUnlockedModules(user.unlockedModules || []);
                                }} className="p-2 text-stone-400 hover:text-emerald-500 bg-white hover:bg-emerald-50 rounded-lg transition-colors border border-transparent hover:border-emerald-100" title="Cấp quyền">"""
content = content.replace(settings_old, settings_new)

# Trash button for user
trash_old = """                                <button onClick={() => handleDeleteUser(user.id)} className="p-2 text-stone-400 hover:text-rose-500 bg-white hover:bg-rose-50 rounded-lg transition-colors border border-transparent hover:border-rose-100" title="Xóa tài khoản">"""
trash_new = """                                <button type="button" onClick={(e) => {
                                  e.preventDefault();
                                  e.stopPropagation();
                                  handleDeleteUser(user.id);
                                }} className="p-2 text-stone-400 hover:text-rose-500 bg-white hover:bg-rose-50 rounded-lg transition-colors border border-transparent hover:border-rose-100" title="Xóa tài khoản">"""
content = content.replace(trash_old, trash_new)

with open('src/components/AdminDashboard.tsx', 'w') as f:
    f.write(content)
