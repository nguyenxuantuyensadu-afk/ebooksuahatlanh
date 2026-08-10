import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

old_ui = """                              <p className="text-sm text-stone-600 font-medium">{item.note}</p>
                              <div className="mt-auto pt-3 border-t border-stone-100 flex items-center gap-2">
                                <span className="text-xs text-stone-500 font-bold uppercase tracking-wider">Năng lượng (10g):</span>
                                <span className="text-sm font-black text-pink-600">{item.calories} kcal</span>
                              </div>"""

new_ui = """                              <p className="text-sm text-stone-600 font-medium">{item.note}</p>
                              <div className="bg-pink-50/50 p-2.5 rounded-lg border border-pink-100">
                                <p className="text-[11px] uppercase tracking-wider font-bold text-pink-800 mb-1">Cách dùng nấu sữa</p>
                                <p className="text-xs font-medium text-pink-900 leading-relaxed">{item.prepTip}</p>
                              </div>
                              <div className="mt-auto pt-3 border-t border-stone-100 flex items-center gap-2">
                                <span className="text-xs text-stone-500 font-bold uppercase tracking-wider">Năng lượng (10g):</span>
                                <span className="text-sm font-black text-pink-600">{item.calories} kcal</span>
                              </div>"""

content = content.replace(old_ui, new_ui)

old_table_headers = """                                 <tr className="bg-stone-50 border-b border-stone-200">
                                   <th className="py-4 px-6 text-xs uppercase tracking-widest font-bold text-stone-500">Nguyên liệu</th>
                                   <th className="py-4 px-6 text-xs uppercase tracking-widest font-bold text-stone-500">Phân loại</th>
                                   <th className="py-4 px-6 text-xs uppercase tracking-widest font-bold text-stone-500 text-right">Năng lượng (kcal)</th>
                                 </tr>"""
new_table_headers = """                                 <tr className="bg-stone-50 border-b border-stone-200">
                                   <th className="py-4 px-6 text-xs uppercase tracking-widest font-bold text-stone-500">Nguyên liệu</th>
                                   <th className="py-4 px-6 text-xs uppercase tracking-widest font-bold text-stone-500">Phân loại</th>
                                   <th className="py-4 px-6 text-xs uppercase tracking-widest font-bold text-stone-500">Cách sơ chế / Nấu chung</th>
                                   <th className="py-4 px-6 text-xs uppercase tracking-widest font-bold text-stone-500 text-right">Năng lượng (kcal)</th>
                                 </tr>"""
content = content.replace(old_table_headers, new_table_headers)

old_table_rows = """                                    <tr key={idx} className="hover:bg-stone-50 transition-colors">
                                      <td className="py-3 px-6 font-bold text-stone-800">{item.name}</td>
                                      <td className="py-3 px-6 font-medium text-stone-600">{item.type}</td>
                                      <td className="py-3 px-6 font-black text-pink-600 text-right">{item.calories}</td>
                                    </tr>"""
new_table_rows = """                                    <tr key={idx} className="hover:bg-stone-50 transition-colors">
                                      <td className="py-3 px-6 font-bold text-stone-800">{item.name}</td>
                                      <td className="py-3 px-6 font-medium text-stone-600">{item.type}</td>
                                      <td className="py-3 px-6 text-sm text-stone-700">{item.prepTip}</td>
                                      <td className="py-3 px-6 font-black text-pink-600 text-right">{item.calories}</td>
                                    </tr>"""
content = content.replace(old_table_rows, new_table_rows)

with open('src/App.tsx', 'w') as f:
    f.write(content)
