import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Insert state
state_code = """
  interface CostRow {
    id: string;
    name: string;
    usage: number;
    buyQuantity: number;
    buyPrice: number;
    unit: string;
  }
  
  const [costYield, setCostYield] = useState<number>(10);
  const [detailedCostRows, setDetailedCostRows] = useState<CostRow[]>([
    { id: '1', name: 'Bắp nếp tươi', usage: 600, buyQuantity: 1000, buyPrice: 15000, unit: 'g' },
    { id: '2', name: 'Đường phèn hạt nhỏ', usage: 150, buyQuantity: 1000, buyPrice: 30000, unit: 'g' },
    { id: '3', name: 'Sữa đặc', usage: 50, buyQuantity: 1000, buyPrice: 60000, unit: 'ml' },
    { id: '4', name: 'Chai PET + Nắp', usage: 10, buyQuantity: 10, buyPrice: 12000, unit: 'bộ' },
    { id: '5', name: 'Tem nhãn decal', usage: 10, buyQuantity: 10, buyPrice: 6000, unit: 'bộ' },
    { id: '6', name: 'Điện, nước, khấu hao', usage: 1, buyQuantity: 1, buyPrice: 3500, unit: 'mẻ' }
  ]);

  const updateCostRow = (id: string, field: keyof CostRow, value: any) => {
    setDetailedCostRows(rows => rows.map(r => r.id === id ? { ...r, [field]: value } : r));
  };

  const removeCostRow = (id: string) => {
    setDetailedCostRows(rows => rows.filter(r => r.id !== id));
  };
  
  const totalDetailedCost = detailedCostRows.reduce((acc, r) => acc + (r.usage / (r.buyQuantity || 1)) * r.buyPrice, 0);
  
"""

if "interface CostRow" not in content:
    content = content.replace("const [dailySales, setDailySales]", state_code + "  const [dailySales, setDailySales]")


# Insert table
table_code = """
              <div className="mt-10 bg-white rounded-[2rem] shadow-sm border border-stone-200 overflow-hidden">
                <div className="bg-stone-900 px-8 py-5 flex flex-wrap justify-between items-center gap-4">
                  <h4 className="font-bold text-white text-lg tracking-wide">
                    Bảng Tính Giá Vốn Chi Tiết (Tương Tác)
                  </h4>
                  <button 
                    onClick={() => setDetailedCostRows([...detailedCostRows, { id: Date.now().toString(), name: 'Nguyên liệu mới', usage: 100, buyQuantity: 1000, buyPrice: 0, unit: 'g' }])} 
                    className="print:hidden px-4 py-2 bg-emerald-500 hover:bg-emerald-600 text-white text-sm font-bold rounded-xl transition-colors flex items-center gap-2"
                  >
                    <Plus size={16} /> Thêm dòng
                  </button>
                </div>
                <div className="overflow-x-auto">
                  <table className="w-full text-left border-collapse min-w-[800px]">
                    <thead>
                      <tr className="bg-stone-50/80 border-b border-stone-200">
                        <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500 w-1/3">Tên Chi Phí</th>
                        <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500">Đ.Lượng dùng</th>
                        <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500">Quy cách mua</th>
                        <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500">Giá mua (VNĐ)</th>
                        <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500 text-right">Thành tiền</th>
                        <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500 text-center print:hidden">Xóa</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-stone-100">
                      {detailedCostRows.map(row => (
                        <tr key={row.id} className="hover:bg-stone-50 transition-colors">
                          <td className="py-3 px-6">
                            <input type="text" value={row.name} onChange={e => updateCostRow(row.id, 'name', e.target.value)} className="w-full bg-transparent font-bold text-stone-800 focus:outline-none focus:border-emerald-500 border-b border-transparent hover:border-stone-200 px-1 py-1" />
                          </td>
                          <td className="py-3 px-6 flex items-center gap-2">
                            <input type="number" value={row.usage || ''} onChange={e => updateCostRow(row.id, 'usage', Number(e.target.value))} className="w-20 bg-stone-100 rounded-lg text-right font-medium text-stone-800 focus:outline-none focus:ring-1 focus:ring-emerald-500 px-2 py-1.5" />
                            <input type="text" value={row.unit} onChange={e => updateCostRow(row.id, 'unit', e.target.value)} className="w-12 bg-transparent text-sm text-stone-500 focus:outline-none" />
                          </td>
                          <td className="py-3 px-6 flex items-center gap-2">
                            <input type="number" value={row.buyQuantity || ''} onChange={e => updateCostRow(row.id, 'buyQuantity', Number(e.target.value))} className="w-20 bg-stone-100 rounded-lg text-right font-medium text-stone-800 focus:outline-none focus:ring-1 focus:ring-emerald-500 px-2 py-1.5" />
                            <span className="text-sm text-stone-500">{row.unit}</span>
                          </td>
                          <td className="py-3 px-6">
                            <input type="number" value={row.buyPrice || ''} onChange={e => updateCostRow(row.id, 'buyPrice', Number(e.target.value))} className="w-28 bg-stone-100 rounded-lg text-right font-medium text-stone-800 focus:outline-none focus:ring-1 focus:ring-emerald-500 px-2 py-1.5" />
                          </td>
                          <td className="py-3 px-6 text-right font-bold text-stone-900">
                            {((row.usage / (row.buyQuantity || 1)) * row.buyPrice).toLocaleString()}đ
                          </td>
                          <td className="py-3 px-6 text-center print:hidden">
                            <button onClick={() => removeCostRow(row.id)} className="p-2 text-stone-400 hover:text-rose-500 hover:bg-rose-50 rounded-lg transition-colors">
                              <Trash2 size={16} />
                            </button>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                    <tfoot className="bg-emerald-50/50 border-t border-emerald-100">
                      <tr>
                        <td colSpan={4} className="py-4 px-6 font-bold text-right text-stone-600 uppercase text-xs tracking-wider">Tổng Chi Phí Mẻ:</td>
                        <td className="py-4 px-6 font-black text-right text-stone-900 text-lg">
                          {totalDetailedCost.toLocaleString()}đ
                        </td>
                        <td className="print:hidden"></td>
                      </tr>
                      <tr>
                        <td colSpan={4} className="py-4 px-6 font-bold text-right text-stone-600 uppercase text-xs tracking-wider flex items-center justify-end gap-3">
                          Thành phẩm thu được:
                          <div className="flex items-center gap-2">
                            <input type="number" value={costYield} onChange={e => setCostYield(Number(e.target.value) || 1)} className="w-16 bg-white border border-emerald-200 rounded-lg text-center font-bold text-emerald-800 focus:outline-none focus:ring-2 focus:ring-emerald-500 px-2 py-1" />
                            <span className="text-emerald-800 lowercase">chai</span>
                          </div>
                        </td>
                        <td className="py-4 px-6 font-bold text-right text-stone-900">
                        </td>
                        <td className="print:hidden"></td>
                      </tr>
                      <tr className="bg-emerald-100/50">
                        <td colSpan={4} className="py-5 px-6 font-bold text-right text-emerald-800 border-t border-emerald-200 uppercase text-xs tracking-wider">Giá Vốn (Cost) / 1 Chai:</td>
                        <td className="py-5 px-6 font-black text-right text-rose-600 text-xl border-t border-emerald-200">
                          {(totalDetailedCost / (costYield || 1)).toLocaleString(undefined, { maximumFractionDigits: 0 })}đ
                        </td>
                        <td className="print:hidden border-t border-emerald-200"></td>
                      </tr>
                    </tfoot>
                  </table>
                </div>
              </div>
"""

target_loc = """                    </tfoot>
                  </table>
                </div>
              </div>"""

if "Bảng Tính Giá Vốn Chi Tiết (Tương Tác)" not in content:
    content = content.replace(target_loc, target_loc + table_code, 1)


with open('src/App.tsx', 'w') as f:
    f.write(content)

print("Done python")
