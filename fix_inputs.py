import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

target = """                  <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
                    <div>
                      <label className="block text-sm font-bold text-stone-700 mb-2">Số chai bán/ngày</label>
                      <input 
                        type="number" 
                        value={dailySales} 
                        onChange={(e) => setDailySales(Number(e.target.value) || 0)}
                        className="w-full px-4 py-3 bg-stone-50 border border-stone-200 rounded-xl font-medium text-stone-900 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:bg-white transition-all"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-bold text-stone-700 mb-2">Giá bán/chai (VNĐ)</label>
                      <input 
                        type="number" 
                        value={sellingPrice} 
                        onChange={(e) => setSellingPrice(Number(e.target.value) || 0)}
                        className="w-full px-4 py-3 bg-stone-50 border border-stone-200 rounded-xl font-medium text-stone-900 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:bg-white transition-all"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-bold text-stone-700 mb-2">Giá vốn NVL/chai (VNĐ)</label>
                      <input 
                        type="number" 
                        value={costPerBottle} 
                        onChange={(e) => setCostPerBottle(Number(e.target.value) || 0)}
                        className="w-full px-4 py-3 bg-stone-50 border border-stone-200 rounded-xl font-medium text-stone-900 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:bg-white transition-all"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-bold text-stone-700 mb-2">Chi phí vận hành/ngày (VNĐ)</label>
                      <input 
                        type="number" 
                        value={dailyOpsCost} 
                        onChange={(e) => setDailyOpsCost(Number(e.target.value) || 0)}
                        className="w-full px-4 py-3 bg-stone-50 border border-stone-200 rounded-xl font-medium text-stone-900 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:bg-white transition-all"
                      />
                    </div>
                  </div>"""

replacement = """                  <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
                    <div className="bg-stone-50 p-4 rounded-xl border border-stone-200">
                      <div className="flex justify-between items-center mb-3">
                        <label className="block text-sm font-bold text-stone-700">Số chai bán/ngày</label>
                        <span className="text-sm font-black text-emerald-600 bg-emerald-100 px-2 py-1 rounded-md">{dailySales}</span>
                      </div>
                      <input 
                        type="range" 
                        min="0"
                        max="300"
                        step="1"
                        value={dailySales} 
                        onChange={(e) => setDailySales(Number(e.target.value) || 0)}
                        className="w-full h-2 bg-stone-200 rounded-lg appearance-none cursor-pointer accent-emerald-500"
                      />
                    </div>
                    <div className="bg-stone-50 p-4 rounded-xl border border-stone-200">
                      <div className="flex justify-between items-center mb-3">
                        <label className="block text-sm font-bold text-stone-700">Giá bán/chai</label>
                        <span className="text-sm font-black text-emerald-600 bg-emerald-100 px-2 py-1 rounded-md">{(sellingPrice/1000).toLocaleString()}k</span>
                      </div>
                      <input 
                        type="range" 
                        min="5000"
                        max="50000"
                        step="1000"
                        value={sellingPrice} 
                        onChange={(e) => setSellingPrice(Number(e.target.value) || 0)}
                        className="w-full h-2 bg-stone-200 rounded-lg appearance-none cursor-pointer accent-emerald-500"
                      />
                    </div>
                    <div className="bg-stone-50 p-4 rounded-xl border border-stone-200">
                      <div className="flex justify-between items-center mb-3">
                        <label className="block text-sm font-bold text-stone-700">Giá vốn NVL</label>
                        <span className="text-sm font-black text-emerald-600 bg-emerald-100 px-2 py-1 rounded-md">{(costPerBottle/1000).toLocaleString()}k</span>
                      </div>
                      <input 
                        type="range"
                        min="1000"
                        max="20000"
                        step="500"
                        value={costPerBottle} 
                        onChange={(e) => setCostPerBottle(Number(e.target.value) || 0)}
                        className="w-full h-2 bg-stone-200 rounded-lg appearance-none cursor-pointer accent-emerald-500"
                      />
                    </div>
                    <div className="bg-stone-50 p-4 rounded-xl border border-stone-200">
                      <div className="flex justify-between items-center mb-3">
                        <label className="block text-sm font-bold text-stone-700">CP vận hành/ngày</label>
                        <span className="text-sm font-black text-emerald-600 bg-emerald-100 px-2 py-1 rounded-md">{(dailyOpsCost/1000).toLocaleString()}k</span>
                      </div>
                      <input 
                        type="range" 
                        min="0"
                        max="500000"
                        step="10000"
                        value={dailyOpsCost} 
                        onChange={(e) => setDailyOpsCost(Number(e.target.value) || 0)}
                        className="w-full h-2 bg-stone-200 rounded-lg appearance-none cursor-pointer accent-emerald-500"
                      />
                    </div>
                  </div>"""

if target in content:
    content = content.replace(target, replacement)
    with open('src/App.tsx', 'w') as f:
        f.write(content)
    print("Success")
else:
    print("Not found")

