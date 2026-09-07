import re

with open('src/App.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

old_str = """                                      })}
                                    </p>
                                    <div className="mt-3 pt-3 border-t border-teal-100/50">
                                      <p className="text-xs font-bold text-teal-800 mb-2">Chất tạo ngọt (chọn 1)</p>"""

new_str = """                                      })}
                                    </p>
                                    {recipe.yield_info && (
                                      <div className="mt-2 pt-2 border-t border-teal-100/30">
                                        <p className="text-sm font-bold text-teal-800">
                                          Thành phẩm: {recipe.yield_info.replace('1 L', recipeMultiplier + ' L').replace('1 Lít', recipeMultiplier + ' Lít')}
                                        </p>
                                      </div>
                                    )}
                                    <div className="mt-3 pt-3 border-t border-teal-100/50">
                                      <p className="text-xs font-bold text-teal-800 mb-2">Chất tạo ngọt (chọn 1)</p>"""

content = content.replace(old_str, new_str)

with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added expanded yield")
