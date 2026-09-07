import re

with open('src/App.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Add CostTable interface
cost_table_interface = """  interface CostRow {
    id: string;
    name: string;
    usage: number;
    buyQuantity: number;
    buyPrice: number;
    unit: string;
  }
  
  interface CostTable {
    id: string;
    name: string;
    yield: number;
    rows: CostRow[];
  }"""
content = re.sub(r'  interface CostRow \{[\s\S]*?\}', cost_table_interface, content)

# Define default tables
default_tables = """  const [costTables, setCostTables] = useState<CostTable[]>([
    {
      id: '1',
      name: 'Mẻ Sữa Bắp Nếp (Mẫu)',
      yield: 10,
      rows: [
        { id: '1', name: 'Bắp nếp tươi', usage: 600, buyQuantity: 1000, buyPrice: 15000, unit: 'g' },
        { id: '2', name: 'Đường phèn hạt nhỏ', usage: 150, buyQuantity: 1000, buyPrice: 30000, unit: 'g' },
        { id: '3', name: 'Sữa đặc', usage: 50, buyQuantity: 1000, buyPrice: 60000, unit: 'ml' },
        { id: '4', name: 'Chai PET + Nắp', usage: 10, buyQuantity: 10, buyPrice: 12000, unit: 'bộ' },
        { id: '5', name: 'Tem nhãn decal', usage: 10, buyQuantity: 10, buyPrice: 6000, unit: 'bộ' },
        { id: '6', name: 'Điện, nước, khấu hao', usage: 1, buyQuantity: 1, buyPrice: 3500, unit: 'mẻ' }
      ]
    },
    {
      id: '2',
      name: 'Mẻ Sữa Đậu Nành Mè Đen',
      yield: 10,
      rows: [
        { id: '1', name: 'Đậu nành', usage: 500, buyQuantity: 1000, buyPrice: 20000, unit: 'g' },
        { id: '2', name: 'Mè đen', usage: 100, buyQuantity: 1000, buyPrice: 40000, unit: 'g' },
        { id: '3', name: 'Đường phèn hạt nhỏ', usage: 150, buyQuantity: 1000, buyPrice: 30000, unit: 'g' },
        { id: '4', name: 'Chai PET + Nắp', usage: 10, buyQuantity: 10, buyPrice: 12000, unit: 'bộ' },
        { id: '5', name: 'Tem nhãn decal', usage: 10, buyQuantity: 10, buyPrice: 6000, unit: 'bộ' },
        { id: '6', name: 'Điện, nước, khấu hao', usage: 1, buyQuantity: 1, buyPrice: 3500, unit: 'mẻ' }
      ]
    },
    {
      id: '3',
      name: 'Mẻ Sữa Hạnh Nhân Cacao',
      yield: 10,
      rows: [
        { id: '1', name: 'Hạnh nhân', usage: 500, buyQuantity: 1000, buyPrice: 250000, unit: 'g' },
        { id: '2', name: 'Bột cacao', usage: 40, buyQuantity: 500, buyPrice: 80000, unit: 'g' },
        { id: '3', name: 'Đường phèn hạt nhỏ', usage: 150, buyQuantity: 1000, buyPrice: 30000, unit: 'g' },
        { id: '4', name: 'Chai PET + Nắp', usage: 10, buyQuantity: 10, buyPrice: 12000, unit: 'bộ' },
        { id: '5', name: 'Tem nhãn decal', usage: 10, buyQuantity: 10, buyPrice: 6000, unit: 'bộ' },
        { id: '6', name: 'Điện, nước, khấu hao', usage: 1, buyQuantity: 1, buyPrice: 3500, unit: 'mẻ' }
      ]
    }
  ]);
  const [expandedCostTableId, setExpandedCostTableId] = useState<string | null>('1');"""

old_detailedCostRows_state = r"const \[costYield, setCostYield\] = useState<number>\(10\);\s*const \[detailedCostRows, setDetailedCostRows\] = useState<CostRow\[\]>\(\[[\s\S]*?\]\);"
content = re.sub(old_detailedCostRows_state, default_tables, content)

with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced definitions")
