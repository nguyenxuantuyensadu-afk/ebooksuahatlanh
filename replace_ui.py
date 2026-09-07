import re

with open('src/App.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

new_ui = """              <div className="mt-10 flex flex-col gap-6">
                <div className="flex items-center justify-between">
                  <h4 className="font-bold text-stone-900 text-xl">Bảng Tính Giá Vốn Tương Tác</h4>
                  <div className="flex items-center gap-3">
                    {currentUser?.role !== 'admin' && (
                      <button 
                        onClick={savePersonalCostData} 
                        className="px-4 py-2 bg-amber-500 hover:bg-amber-600 text-white text-sm font-bold rounded-xl transition-colors flex items-center gap-2 shadow-sm"
                      >
                        <Save size={16} /> Lưu thay đổi
                      </button>
                    )}
                    <button 
                      onClick={addNewCostTable} 
                      className="px-4 py-2 bg-emerald-500 hover:bg-emerald-600 text-white text-sm font-bold rounded-xl transition-colors flex items-center gap-2 shadow-sm"
                    >
                      <Plus size={16} /> Thêm món mới
                    </button>
                  </div>
                </div>

                <div className="flex flex-col gap-4">
                  {costTables.map((table) => {
                    const totalCost = table.rows.reduce((acc, r) => acc + (r.usage / (r.buyQuantity || 1)) * r.buyPrice, 0);
                    const isExpanded = expandedCostTableId === table.id;

                    return (
                      <div key={table.id} className="bg-white rounded-[2rem] shadow-sm border border-stone-200 overflow-hidden transition-all duration-300">
                        <div 
                          className="px-8 py-5 flex flex-wrap justify-between items-center gap-4 cursor-pointer hover:bg-stone-50 transition-colors"
                          onClick={() => setExpandedCostTableId(isExpanded ? null : table.id)}
                        >
                          <div className="flex items-center gap-3 flex-1 min-w-[250px]">
                            <div className={`p-1.5 rounded-full transition-transform duration-300 ${isExpanded ? 'rotate-180 bg-stone-200 text-stone-600' : 'bg-stone-100 text-stone-500'}`}>
                              <ChevronDown size={20} />
                            </div>
                            <input 
                              type="text" 
                              value={table.name} 
                              onChange={e => updateCostTableName(table.id, e.target.value)} 
                              onClick={e => e.stopPropagation()}
                              className="font-bold text-stone-800 text-lg bg-transparent border-b border-transparent hover:border-stone-300 focus:border-emerald-500 focus:outline-none transition-colors px-2 py-1 w-full max-w-sm" 
                            />
                          </div>
                          
                          {!isExpanded && (
                            <div className="flex items-center gap-6 text-sm">
                              <p className="text-stone-500 font-medium">Thành phẩm: <span className="font-bold text-stone-800">{table.yield} chai</span></p>
                              <p className="text-stone-500 font-medium">Giá vốn: <span className="font-bold text-rose-600">{(totalCost / (table.yield || 1)).toLocaleString(undefined, { maximumFractionDigits: 0 })}đ</span>/chai</p>
                            </div>
                          )}

                          <div className="flex items-center gap-2">
                             <button 
                               onClick={(e) => { e.stopPropagation(); deleteCostTable(table.id); }} 
                               className="p-2 text-stone-400 hover:text-rose-500 hover:bg-rose-50 rounded-xl transition-colors print:hidden"
                               title="Xóa món"
                             >
                               <Trash2 size={18} />
                             </button>
                          </div>
                        </div>

                        <AnimatePresence>
                          {isExpanded && (
                            <motion.div
                              initial={{ height: 0, opacity: 0 }}
                              animate={{ height: "auto", opacity: 1 }}
                              exit={{ height: 0, opacity: 0 }}
                              transition={{ duration: 0.2 }}
                              className="overflow-hidden border-t border-stone-200"
                            >
                              <div className="bg-stone-50 px-8 py-3 flex justify-between items-center print:hidden border-b border-stone-200">
                                <p className="text-xs font-bold text-stone-500 uppercase tracking-widest">Chi tiết thành phần</p>
                                <div className="flex gap-2">
                                  <button 
                                    onClick={() => exportCostTableToCSV(table)} 
                                    className="px-3 py-1.5 bg-white border border-stone-200 hover:border-indigo-300 hover:text-indigo-600 text-stone-600 text-xs font-bold rounded-lg transition-colors flex items-center gap-2 shadow-sm"
                                  >
                                    <Download size={14} /> Xuất CSV
                                  </button>
                                  <button 
                                    onClick={() => addCostRow(table.id)} 
                                    className="px-3 py-1.5 bg-emerald-50 text-emerald-700 border border-emerald-200 hover:bg-emerald-100 hover:border-emerald-300 text-xs font-bold rounded-lg transition-colors flex items-center gap-2 shadow-sm"
                                  >
                                    <Plus size={14} /> Thêm nguyên liệu
                                  </button>
                                </div>
                              </div>
                              <div className="overflow-x-auto">
                                <table className="w-full text-left border-collapse min-w-[800px]">
                                  <thead>
                                    <tr className="bg-white border-b border-stone-100">
                                      <th className="py-4 px-8 text-[11px] uppercase tracking-widest font-bold text-stone-500 w-1/3">Tên Chi Phí</th>
                                      <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500">Đ.Lượng dùng</th>
                                      <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500">Quy cách mua</th>
                                      <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500">Giá mua (VNĐ)</th>
                                      <th className="py-4 px-8 text-[11px] uppercase tracking-widest font-bold text-stone-500 text-right">Thành tiền</th>
                                      <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500 text-center print:hidden">Xóa</th>
                                    </tr>
                                  </thead>
                                  <tbody className="divide-y divide-stone-50">
                                    {table.rows.map(row => (
                                      <tr key={row.id} className="hover:bg-stone-50 transition-colors bg-white">
                                        <td className="py-3 px-8">
                                          <input type="text" value={row.name} onChange={e => updateCostRow(table.id, row.id, 'name', e.target.value)} className="w-full bg-transparent font-bold text-stone-800 focus:outline-none focus:border-emerald-500 border-b border-transparent hover:border-stone-200 px-1 py-1" />
                                        </td>
                                        <td className="py-3 px-6 flex items-center gap-2">
                                          <input type="number" value={row.usage || ''} onChange={e => updateCostRow(table.id, row.id, 'usage', Number(e.target.value))} className="w-20 bg-stone-100/80 rounded-lg text-right font-medium text-stone-800 focus:outline-none focus:ring-1 focus:ring-emerald-500 px-2 py-1.5" />
                                          <input type="text" value={row.unit} onChange={e => updateCostRow(table.id, row.id, 'unit', e.target.value)} className="w-12 bg-transparent text-sm text-stone-500 focus:outline-none" />
                                        </td>
                                        <td className="py-3 px-6">
                                          <div className="flex items-center gap-2">
                                            <input type="number" value={row.buyQuantity || ''} onChange={e => updateCostRow(table.id, row.id, 'buyQuantity', Number(e.target.value))} className="w-20 bg-stone-100/80 rounded-lg text-right font-medium text-stone-800 focus:outline-none focus:ring-1 focus:ring-emerald-500 px-2 py-1.5" />
                                            <span className="text-sm text-stone-500">{row.unit}</span>
                                          </div>
                                        </td>
                                        <td className="py-3 px-6">
                                          <input type="number" value={row.buyPrice || ''} onChange={e => updateCostRow(table.id, row.id, 'buyPrice', Number(e.target.value))} className="w-28 bg-stone-100/80 rounded-lg text-right font-medium text-stone-800 focus:outline-none focus:ring-1 focus:ring-emerald-500 px-2 py-1.5" />
                                        </td>
                                        <td className="py-3 px-8 text-right font-bold text-stone-900">
                                          {((row.usage / (row.buyQuantity || 1)) * row.buyPrice).toLocaleString()}đ
                                        </td>
                                        <td className="py-3 px-6 text-center print:hidden">
                                          <button onClick={() => removeCostRow(table.id, row.id)} className="p-2 text-stone-400 hover:text-rose-500 hover:bg-rose-50 rounded-lg transition-colors">
                                            <Trash2 size={16} />
                                          </button>
                                        </td>
                                      </tr>
                                    ))}
                                  </tbody>
                                  <tfoot className="bg-stone-50/80 border-t border-stone-200">
                                    <tr>
                                      <td colSpan={4} className="py-4 px-8 font-bold text-right text-stone-600 uppercase text-xs tracking-wider">Tổng Chi Phí Mẻ:</td>
                                      <td className="py-4 px-8 font-black text-right text-stone-900 text-lg">
                                        {totalCost.toLocaleString()}đ
                                      </td>
                                      <td className="print:hidden"></td>
                                    </tr>
                                    <tr>
                                      <td colSpan={4} className="py-4 px-8 font-bold text-right text-stone-600 uppercase text-xs tracking-wider flex items-center justify-end gap-3">
                                        Thành phẩm thu được:
                                        <div className="flex items-center gap-2">
                                          <input type="number" value={table.yield} onChange={e => updateCostTableYield(table.id, Number(e.target.value) || 1)} className="w-16 bg-white border border-stone-300 rounded-lg text-center font-bold text-stone-800 focus:outline-none focus:ring-2 focus:ring-emerald-500 px-2 py-1" />
                                          <span className="text-stone-600 lowercase">chai</span>
                                        </div>
                                      </td>
                                      <td className="py-4 px-8 font-bold text-right text-stone-900">
                                      </td>
                                      <td className="print:hidden"></td>
                                    </tr>
                                    <tr className="bg-emerald-50">
                                      <td colSpan={4} className="py-5 px-8 font-bold text-right text-emerald-800 border-t border-emerald-100 uppercase text-xs tracking-wider">Giá Vốn (Cost) / 1 Chai:</td>
                                      <td className="py-5 px-8 font-black text-right text-rose-600 text-xl border-t border-emerald-100">
                                        {(totalCost / (table.yield || 1)).toLocaleString(undefined, { maximumFractionDigits: 0 })}đ
                                      </td>
                                      <td className="print:hidden border-t border-emerald-100"></td>
                                    </tr>
                                  </tfoot>
                                </table>
                              </div>
                            </motion.div>
                          )}
                        </AnimatePresence>
                      </div>
                    );
                  })}
                </div>
              </div>"""

start_str = r'<div className="mt-10 bg-white rounded-\[2rem\] shadow-sm border border-stone-200 overflow-hidden">'
end_str = r'Giá Vốn \(Cost\) / 1 Chai:</td>\s*<td className="py-5 px-6 font-black text-right text-rose-600 text-xl border-t border-emerald-200">\s*\{\(totalDetailedCost / \(costYield \|\| 1\)\)\.toLocaleString\(undefined, \{ maximumFractionDigits: 0 \}\)\}đ\s*</td>\s*<td className="print:hidden border-t border-emerald-200"></td>\s*</tr>\s*</tfoot>\s*</table>\s*</div>\s*</div>'

pattern = start_str + r"[\s\S]*?" + end_str

content = re.sub(pattern, new_ui.strip(), content)

with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced UI")
