import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Adding the sweeteners UI code
sweeteners_ui = """
                    <div>
                      <h4 className="font-bold text-xl text-stone-900 mb-6 flex items-center gap-2">
                        <span className="w-2 h-2 rounded-full bg-pink-500"></span>
                        Các nguyên liệu tạo ngọt tốt cho sức khỏe
                      </h4>
                      <div className="bg-stone-50 border border-stone-200 rounded-[1.5rem] p-6 md:p-8">
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-8">
                          {course.modules[0].sweeteners?.map((item: any, idx: number) => (
                            <div key={idx} className="bg-white p-4 rounded-xl border border-stone-200 shadow-sm flex flex-col gap-2">
                              <div className="flex justify-between items-start">
                                <h5 className="font-bold text-stone-900">{item.name}</h5>
                                <span className="px-2 py-1 bg-pink-50 text-pink-700 text-[10px] font-bold rounded-lg uppercase tracking-wider">{item.type}</span>
                              </div>
                              <p className="text-sm text-stone-600 font-medium">{item.note}</p>
                              <div className="mt-auto pt-3 border-t border-stone-100 flex items-center gap-2">
                                <span className="text-xs text-stone-500 font-bold uppercase tracking-wider">Năng lượng (10g):</span>
                                <span className="text-sm font-black text-pink-600">{item.calories} kcal</span>
                              </div>
                            </div>
                          ))}
                        </div>
                        
                        <div className="bg-white rounded-2xl overflow-hidden border border-stone-200 shadow-sm">
                           <div className="bg-stone-900 px-6 py-4">
                              <h5 className="font-bold text-white tracking-wide">Bảng so sánh năng lượng (trên 10g)</h5>
                           </div>
                           <div className="overflow-x-auto">
                             <table className="w-full text-left border-collapse min-w-[600px]">
                               <thead>
                                 <tr className="bg-stone-50 border-b border-stone-200">
                                   <th className="py-4 px-6 text-xs uppercase tracking-widest font-bold text-stone-500">Nguyên liệu</th>
                                   <th className="py-4 px-6 text-xs uppercase tracking-widest font-bold text-stone-500">Phân loại</th>
                                   <th className="py-4 px-6 text-xs uppercase tracking-widest font-bold text-stone-500 text-right">Năng lượng (kcal)</th>
                                 </tr>
                               </thead>
                               <tbody className="divide-y divide-stone-100">
                                  {course.modules[0].sweeteners?.map((item: any, idx: number) => (
                                    <tr key={idx} className="hover:bg-stone-50 transition-colors">
                                      <td className="py-3 px-6 font-bold text-stone-800">{item.name}</td>
                                      <td className="py-3 px-6 font-medium text-stone-600">{item.type}</td>
                                      <td className="py-3 px-6 font-black text-pink-600 text-right">{item.calories}</td>
                                    </tr>
                                  ))}
                               </tbody>
                             </table>
                           </div>
                        </div>
                      </div>
                    </div>

                    <div>
                      <h4 className="font-bold text-xl text-stone-900 mb-6 flex items-center gap-2">
                        <span className="w-2 h-2 rounded-full bg-indigo-500"></span>
                        Quy Trình Nấu Sữa 7 Bước
                      </h4>"""

content = content.replace("""                    <div>
                      <h4 className="font-bold text-xl text-stone-900 mb-6 flex items-center gap-2">
                        <span className="w-2 h-2 rounded-full bg-indigo-500"></span>
                        Quy Trình Nấu Sữa 7 Bước
                      </h4>""", sweeteners_ui)

with open('src/App.tsx', 'w') as f:
    f.write(content)
