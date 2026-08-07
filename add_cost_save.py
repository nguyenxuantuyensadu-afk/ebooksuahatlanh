import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add state and save function
cost_save_code = """
  const costDataLoaded = React.useRef(false);

  useEffect(() => {
    if (currentUser?.personalCostData && !costDataLoaded.current) {
      setDetailedCostRows(currentUser.personalCostData.rows);
      if (currentUser.personalCostData.yield) setCostYield(currentUser.personalCostData.yield);
      costDataLoaded.current = true;
    }
  }, [currentUser]);

  const savePersonalCostData = async () => {
    if (!currentUser || currentUser.role === 'admin') {
       toast.error("Vui lòng đăng nhập với tài khoản học viên để lưu.");
       return;
    }
    try {
      await updateDoc(doc(db, "users", currentUser.id), {
        personalCostData: {
          rows: detailedCostRows,
          yield: costYield
        }
      });
      toast.success("Đã lưu bảng tính chi phí cá nhân!");
    } catch (e) {
      toast.error("Lỗi khi lưu dữ liệu!");
    }
  };
"""

content = content.replace(
    'const [dailySales, setDailySales] = useState<number>(50);',
    cost_save_code + '\n  const [dailySales, setDailySales] = useState<number>(50);'
)

# Add save button in the UI
old_buttons = """                  <button 
                    onClick={() => setDetailedCostRows([...detailedCostRows, { id: Date.now().toString(), name: 'Nguyên liệu mới', usage: 100, buyQuantity: 1000, buyPrice: 0, unit: 'g' }])} 
                    className="print:hidden px-4 py-2 bg-emerald-500 hover:bg-emerald-600 text-white text-sm font-bold rounded-xl transition-colors flex items-center gap-2"
                  >
                    <Plus size={16} /> Thêm dòng
                  </button>"""

new_buttons = """                  <div className="flex items-center gap-3 print:hidden">
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
