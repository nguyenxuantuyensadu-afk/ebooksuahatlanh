import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

bad_order = """  const profitChartData = useMemo(() => {
    const data = [];
    for (let i = 0; i <= 300; i += 20) {
      const revenue = i * sellingPrice;
      const cost = (i * costPerBottle) + dailyOpsCost;
      data.push({
        sales: i,
        profit: revenue - cost,
        revenue,
        cost
      });
    }
    return data;
  }, [sellingPrice, costPerBottle, dailyOpsCost]);

  const [dailySales, setDailySales] = useState<number>(50);
  const [sellingPrice, setSellingPrice] = useState<number>(15000);
  const [costPerBottle, setCostPerBottle] = useState<number>(3800);
  const [dailyOpsCost, setDailyOpsCost] = useState<number>(100000);"""

good_order = """  const [dailySales, setDailySales] = useState<number>(50);
  const [sellingPrice, setSellingPrice] = useState<number>(15000);
  const [costPerBottle, setCostPerBottle] = useState<number>(3800);
  const [dailyOpsCost, setDailyOpsCost] = useState<number>(100000);

  const profitChartData = useMemo(() => {
    const data = [];
    for (let i = 0; i <= 300; i += 20) {
      const revenue = i * sellingPrice;
      const cost = (i * costPerBottle) + dailyOpsCost;
      data.push({
        sales: i,
        profit: revenue - cost,
        revenue,
        cost
      });
    }
    return data;
  }, [sellingPrice, costPerBottle, dailyOpsCost]);"""

content = content.replace(bad_order, good_order)

with open('src/App.tsx', 'w') as f:
    f.write(content)
