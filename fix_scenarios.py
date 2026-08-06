import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

target = """                <div className="p-8">
                  <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">"""

replacement = """                <div className="p-8">
                  <div className="mb-8 flex flex-wrap items-center gap-4 bg-stone-50 p-4 rounded-2xl border border-stone-200">
                    <span className="font-bold text-stone-700 text-sm">Giả lập kịch bản thực tế:</span>
                    <button 
                      onClick={() => {
                        setDailySales(100);
                        setCostPerBottle(3500);
                        setDailyOpsCost(80000);
                      }}
                      className="px-4 py-2 bg-emerald-100 text-emerald-800 hover:bg-emerald-200 rounded-xl text-sm font-bold transition-colors"
                    >
                      🚀 Bán đắt hàng (Tối ưu)
                    </button>
                    <button 
                      onClick={() => {
                        setDailySales(10);
                        setCostPerBottle(4200);
                        setDailyOpsCost(100000);
                      }}
                      className="px-4 py-2 bg-rose-100 text-rose-800 hover:bg-rose-200 rounded-xl text-sm font-bold transition-colors"
                    >
                      📉 Kinh doanh ế ẩm
                    </button>
                    <button 
                      onClick={() => {
                        setDailySales(50);
                        setCostPerBottle(3800);
                        setDailyOpsCost(100000);
                      }}
                      className="px-4 py-2 bg-stone-200 text-stone-700 hover:bg-stone-300 rounded-xl text-sm font-bold transition-colors"
                    >
                      🔄 Đặt lại mặc định
                    </button>
                  </div>
                  <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">"""

if target in content:
    content = content.replace(target, replacement)
    with open('src/App.tsx', 'w') as f:
        f.write(content)
    print("Success")
else:
    print("Not found")

