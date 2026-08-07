import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add imports for recharts
import_statement = 'import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ReferenceLine } from "recharts";\n'
content = content.replace('import React, { useState, useEffect } from "react";', import_statement + 'import React, { useState, useEffect, useMemo } from "react";')

# Add the chart data memo
chart_data_code = """
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
  }, [sellingPrice, costPerBottle, dailyOpsCost]);
"""

content = content.replace('const [dailySales, setDailySales] = useState<number>(50);', chart_data_code + '\n  const [dailySales, setDailySales] = useState<number>(50);')

# Add the chart UI
chart_ui = """
                    </div>
                  </div>
                  
                  {/* Biểu đồ lợi nhuận */}
                  <div className="mt-8 bg-white p-6 rounded-[1.5rem] border border-stone-200">
                    <h5 className="font-bold text-stone-900 mb-6 text-lg">Biểu đồ dự phóng lợi nhuận theo sản lượng</h5>
                    <div className="h-[300px] w-full">
                      <ResponsiveContainer width="100%" height="100%">
                        <LineChart
                          data={profitChartData}
                          margin={{
                            top: 5,
                            right: 30,
                            left: 20,
                            bottom: 5,
                          }}
                        >
                          <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e5e7eb" />
                          <XAxis dataKey="sales" tickFormatter={(value) => `${value} chai`} stroke="#9ca3af" fontSize={12} tickLine={false} axisLine={false} />
                          <YAxis tickFormatter={(value) => `${(value/1000).toLocaleString()}k`} stroke="#9ca3af" fontSize={12} tickLine={false} axisLine={false} />
                          <Tooltip 
                            formatter={(value: number) => [`${value.toLocaleString()} đ`, '']} 
                            labelFormatter={(label) => `Sản lượng: ${label} chai`}
                            contentStyle={{ borderRadius: '12px', border: 'none', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)' }}
                          />
                          <Legend />
                          <ReferenceLine y={0} stroke="#ef4444" strokeDasharray="3 3" />
                          <Line type="monotone" name="Lợi Nhuận Ngày" dataKey="profit" stroke="#10b981" strokeWidth={3} dot={{ r: 4, strokeWidth: 2 }} activeDot={{ r: 6 }} />
                        </LineChart>
                      </ResponsiveContainer>
                    </div>
                  </div>
"""

content = content.replace('</div>\n                    </div>\n                  </div>\n                </div>\n              </div>\n            </section>', chart_ui + '                </div>\n              </div>\n            </section>')

with open('src/App.tsx', 'w') as f:
    f.write(content)
