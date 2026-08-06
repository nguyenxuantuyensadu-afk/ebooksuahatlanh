import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

calculator_code = """
              <div className="mt-10 bg-white rounded-[2rem] shadow-sm border border-stone-200 overflow-hidden">
                <div className="bg-stone-900 px-8 py-5">
                  <h4 className="font-bold text-white text-lg tracking-wide">
                    Công Cụ Tính Lợi Nhuận Dự Kiến
                  </h4>
                </div>
                <div className="p-8">
                  <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
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
                  </div>
                  
                  <div className="bg-emerald-50 rounded-[1.5rem] p-6 md:p-8">
                    <h5 className="font-bold text-emerald-900 mb-6 text-lg">Kết quả dự tính:</h5>
                    <div className="grid md:grid-cols-2 gap-8">
                      <div className="space-y-4">
                        <div className="flex justify-between items-center">
                          <span className="text-emerald-700 font-medium">Doanh thu/ngày:</span>
                          <span className="font-bold text-stone-900 text-lg">{(dailySales * sellingPrice).toLocaleString()} đ</span>
                        </div>
                        <div className="flex justify-between items-center">
                          <span className="text-emerald-700 font-medium">Chi phí NVL/ngày:</span>
                          <span className="font-bold text-rose-600 text-lg">-{(dailySales * costPerBottle).toLocaleString()} đ</span>
                        </div>
                        <div className="flex justify-between items-center">
                          <span className="text-emerald-700 font-medium">Chi phí vận hành/ngày:</span>
                          <span className="font-bold text-rose-600 text-lg">-{(dailyOpsCost).toLocaleString()} đ</span>
                        </div>
                        <div className="w-full h-px bg-emerald-200/60 my-2"></div>
                        <div className="flex justify-between items-center">
                          <span className="text-emerald-900 font-bold text-lg">Lợi nhuận ròng/ngày:</span>
                          <span className={`font-black text-2xl ${((dailySales * sellingPrice) - (dailySales * costPerBottle) - dailyOpsCost) >= 0 ? 'text-emerald-700' : 'text-rose-600'}`}>
                            {((dailySales * sellingPrice) - (dailySales * costPerBottle) - dailyOpsCost).toLocaleString()} đ
                          </span>
                        </div>
                      </div>
                      
                      <div className="space-y-4 border-t md:border-t-0 md:border-l border-emerald-200/50 pt-6 md:pt-0 md:pl-8">
                        <div className="flex justify-between items-center">
                          <span className="text-emerald-700 font-medium">Doanh thu/tháng (30 ngày):</span>
                          <span className="font-bold text-stone-900 text-lg">{(dailySales * sellingPrice * 30).toLocaleString()} đ</span>
                        </div>
                        <div className="w-full h-px bg-emerald-200/60 my-2"></div>
                        <div className="flex justify-between items-center">
                          <span className="text-emerald-900 font-bold text-lg">Lợi nhuận/tháng (30 ngày):</span>
                          <span className={`font-black text-2xl ${((dailySales * sellingPrice) - (dailySales * costPerBottle) - dailyOpsCost) >= 0 ? 'text-emerald-700' : 'text-rose-600'}`}>
                            {(((dailySales * sellingPrice) - (dailySales * costPerBottle) - dailyOpsCost) * 30).toLocaleString()} đ
                          </span>
                        </div>
                        <div className="mt-6 bg-white/60 p-4 rounded-xl border border-emerald-100">
                           <div className="text-sm font-bold text-emerald-800 mb-1">Tỷ suất lợi nhuận ròng:</div>
                           <div className="text-xl font-black text-emerald-600">
                             {dailySales * sellingPrice > 0 ? (((dailySales * sellingPrice - dailySales * costPerBottle - dailyOpsCost) / (dailySales * sellingPrice)) * 100).toFixed(1) : 0}%
                           </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
"""

target = """                    </tfoot>
                  </table>
                </div>
              </div>"""

content = content.replace(target, target + calculator_code)

with open('src/App.tsx', 'w') as f:
    f.write(content)

