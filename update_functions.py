import re

with open('src/App.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

new_functions = """
  const updateCostRow = (tableId: string, rowId: string, field: keyof CostRow, value: any) => {
    setCostTables(tables => tables.map(t => {
      if (t.id === tableId) {
        return {
          ...t,
          rows: t.rows.map(r => r.id === rowId ? { ...r, [field]: value } : r)
        };
      }
      return t;
    }));
  };
  
  const updateCostTableYield = (tableId: string, newYield: number) => {
    setCostTables(tables => tables.map(t => t.id === tableId ? { ...t, yield: newYield } : t));
  };
  
  const updateCostTableName = (tableId: string, newName: string) => {
    setCostTables(tables => tables.map(t => t.id === tableId ? { ...t, name: newName } : t));
  };

  const exportCostTableToCSV = (table: CostTable) => {
    let csvContent = "data:text/csv;charset=utf-8,\uFEFF";
    csvContent += "Tên Chi Phí,Định Lượng Dùng,Đơn Vị,Quy Cách Mua,Đơn Vị,Giá Mua (VNĐ),Thành Tiền (VNĐ)\\n";
    
    let totalDetailedCost = 0;
    table.rows.forEach(row => {
      const rowCost = (row.usage / (row.buyQuantity || 1)) * row.buyPrice;
      totalDetailedCost += rowCost;
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
    csvContent += `Thành phẩm thu được,,,,,,${table.yield} chai\\n`;
    const costPerBottle = (totalDetailedCost / (table.yield || 1));
    csvContent += `Giá Vốn / 1 Chai,,,,,,${costPerBottle.toFixed(0)}\\n`;

    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", `Bang_Tinh_Gia_Von_${table.name}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const removeCostRow = (tableId: string, rowId: string) => {
    setCostTables(tables => tables.map(t => {
      if (t.id === tableId) {
        return { ...t, rows: t.rows.filter(r => r.id !== rowId) };
      }
      return t;
    }));
  };

  const addCostRow = (tableId: string) => {
    setCostTables(tables => tables.map(t => {
      if (t.id === tableId) {
        return {
          ...t,
          rows: [...t.rows, { id: Date.now().toString(), name: 'Nguyên liệu mới', usage: 100, buyQuantity: 1000, buyPrice: 0, unit: 'g' }]
        };
      }
      return t;
    }));
  };

  const addNewCostTable = () => {
    const newId = Date.now().toString();
    setCostTables(tables => [
      ...tables,
      {
        id: newId,
        name: 'Mẻ Sữa Hạt Mới',
        yield: 10,
        rows: [
          { id: '1', name: 'Nguyên liệu 1', usage: 100, buyQuantity: 1000, buyPrice: 0, unit: 'g' },
          { id: '2', name: 'Nguyên liệu 2', usage: 50, buyQuantity: 1000, buyPrice: 0, unit: 'g' },
          { id: '4', name: 'Chai PET + Nắp', usage: 10, buyQuantity: 10, buyPrice: 12000, unit: 'bộ' },
          { id: '5', name: 'Tem nhãn decal', usage: 10, buyQuantity: 10, buyPrice: 6000, unit: 'bộ' },
          { id: '6', name: 'Điện, nước, khấu hao', usage: 1, buyQuantity: 1, buyPrice: 3500, unit: 'mẻ' }
        ]
      }
    ]);
    setExpandedCostTableId(newId);
  };
  
  const deleteCostTable = (tableId: string) => {
    if(window.confirm('Bạn có chắc muốn xóa bản tính này?')) {
      setCostTables(tables => tables.filter(t => t.id !== tableId));
    }
  };

  const costDataLoaded = React.useRef(false);

  useEffect(() => {
    if (currentUser?.personalCostData && !costDataLoaded.current) {
      if (Array.isArray(currentUser.personalCostData.tables)) {
        setCostTables(currentUser.personalCostData.tables);
      } else if (currentUser.personalCostData.rows) {
        setCostTables([{
          id: '1',
          name: 'Bản tính của bạn',
          yield: currentUser.personalCostData.yield || 10,
          rows: currentUser.personalCostData.rows
        }]);
      }
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
          tables: costTables
        }
      });
      toast.success("Đã lưu bảng tính chi phí cá nhân!");
    } catch (e) {
      toast.error("Lỗi khi lưu dữ liệu!");
    }
  };
"""

# replace from const updateCostRow up to the end of savePersonalCostData
pattern = r"const updateCostRow = [\s\S]*?toast\.error\(\"Lỗi khi lưu dữ liệu!\"\);\s*\}\s*};"

content = re.sub(pattern, new_functions.strip(), content)

with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced functions")
