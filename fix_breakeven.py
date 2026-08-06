import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

target = """                        <div className="mt-6 bg-white/60 p-4 rounded-xl border border-emerald-100">
                           <div className="text-sm font-bold text-emerald-800 mb-1">Tỷ suất lợi nhuận ròng:</div>
                           <div className="text-xl font-black text-emerald-600">
                             {dailySales * sellingPrice > 0 ? (((dailySales * sellingPrice - dailySales * costPerBottle - dailyOpsCost) / (dailySales * sellingPrice)) * 100).toFixed(1) : 0}%
                           </div>
                        </div>"""

replacement = """                        <div className="mt-6 grid grid-cols-2 gap-4">
                          <div className="bg-white/60 p-4 rounded-xl border border-emerald-100">
                             <div className="text-sm font-bold text-emerald-800 mb-1">Tỷ suất LN ròng:</div>
                             <div className="text-xl font-black text-emerald-600">
                               {dailySales * sellingPrice > 0 ? (((dailySales * sellingPrice - dailySales * costPerBottle - dailyOpsCost) / (dailySales * sellingPrice)) * 100).toFixed(1) : 0}%
                             </div>
                          </div>
                          <div className="bg-white/60 p-4 rounded-xl border border-emerald-100">
                             <div className="text-sm font-bold text-emerald-800 mb-1">Điểm hòa vốn/ngày:</div>
                             <div className="text-xl font-black text-emerald-600">
                               {(sellingPrice - costPerBottle) > 0 ? Math.ceil(dailyOpsCost / (sellingPrice - costPerBottle)) : 0} chai
                             </div>
                          </div>
                        </div>"""

if target in content:
    content = content.replace(target, replacement)
    with open('src/App.tsx', 'w') as f:
        f.write(content)
    print("Success")
else:
    print("Not found")

