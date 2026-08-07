import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add export function
export_func_code = """
  const exportCostTableToCSV = () => {
    let csvContent = "data:text/csv;charset=utf-8,\\uFEFF";
    csvContent += "Tên Chi Phí,Định Lượng Dùng,Đơn Vị,Quy Cách Mua,Đơn Vị,Giá Mua (VNĐ),Thành Tiền (VNĐ)\\n";

    detailedCostRows.forEach(row => {
      const rowCost = (row.usage / (row.buyQuantity || 1)) * row.buyPrice;
      const rowArray = [
        `"${row.name}"`,
        row.usage,
        `"${row.unit}"`,
        row.buyQuantity,
        `"${row.unit}"`,
        row.buyPrice,
        rowCost
      ];
      csvContent += rowArray.join(",") + "\\n";
    });

    csvContent += `\\nTổng Chi Phí Mẻ,,,,,,${totalDetailedCost}\\n`;
    csvContent += `Thành phẩm thu được,,,,,,${costYield} chai\\n`;
    const costPerBottle = (totalDetailedCost / (costYield || 1));
    csvContent += `Giá Vốn / 1 Chai,,,,,,${costPerBottle.toFixed(0)}\\n`;

    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "Bang_Tinh_Gia_Von.csv");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    toast.success("Đã xuất file CSV thành công!");
  };
"""

content = content.replace(
    'const removeCostRow = (id: string) => {',
    export_func_code + '\n  const removeCostRow = (id: string) => {'
)

old_buttons = """                  <div className="flex items-center gap-3 print:hidden">
                    {currentUser?.role !== 'admin' && (
                      <button 
                        onClick={savePersonalCostData} 
                        className="px-4 py-2 bg-amber-500 hover:bg-amber-600 text-white text-sm font-bold rounded-xl transition-colors flex items-center gap-2 shadow-sm"
                      >
                        <Save size={16} /> Lưu kết quả
                      </button>
                    )}
                    <button 
                      onClick={() => setDetailedCostRows([...detailedCostRows, { id: Date.now().toString(), name: 'Nguyên liệu mới', usage: 100, buyQuantity: 1000, buyPrice: 0, unit: 'g' }])} 
                      className="px-4 py-2 bg-emerald-500 hover:bg-emerald-600 text-white text-sm font-bold rounded-xl transition-colors flex items-center gap-2 shadow-sm"
                    >
                      <Plus size={16} /> Thêm dòng
                    </button>
                  </div>"""

new_buttons = """                  <div className="flex flex-wrap items-center justify-end gap-3 print:hidden">
                    <button 
                      onClick={exportCostTableToCSV} 
                      className="px-4 py-2 bg-indigo-500 hover:bg-indigo-600 text-white text-sm font-bold rounded-xl transition-colors flex items-center gap-2 shadow-sm"
                    >
                      <Download size={16} /> Xuất CSV
                    </button>
                    {currentUser?.role !== 'admin' && (
                      <button 
                        onClick={savePersonalCostData} 
                        className="px-4 py-2 bg-amber-500 hover:bg-amber-600 text-white text-sm font-bold rounded-xl transition-colors flex items-center gap-2 shadow-sm"
                      >
                        <Save size={16} /> Lưu kết quả
                      </button>
                    )}
                    <button 
                      onClick={() => setDetailedCostRows([...detailedCostRows, { id: Date.now().toString(), name: 'Nguyên liệu mới', usage: 100, buyQuantity: 1000, buyPrice: 0, unit: 'g' }])} 
                      className="px-4 py-2 bg-emerald-500 hover:bg-emerald-600 text-white text-sm font-bold rounded-xl transition-colors flex items-center gap-2 shadow-sm"
                    >
                      <Plus size={16} /> Thêm dòng
                    </button>
                  </div>"""

content = content.replace(old_buttons, new_buttons)

with open('src/App.tsx', 'w') as f:
    f.write(content)
