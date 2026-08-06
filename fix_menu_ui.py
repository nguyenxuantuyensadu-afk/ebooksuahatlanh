import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

target = """                  </table>
                </div>
              </div>"""

replacement = """                  </table>
                </div>
              </div>

              {courseData.modules[2].menuStrategy && (
                <div className="mt-10">
                  <h4 className="text-xl font-bold text-stone-900 mb-2">{courseData.modules[2].menuStrategy.title}</h4>
                  <p className="text-stone-600 mb-6">{courseData.modules[2].menuStrategy.description}</p>
                  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                    {courseData.modules[2].menuStrategy.strategies.map((strategy: any, idx: number) => (
                      <div key={idx} className="bg-white rounded-2xl p-6 border border-stone-200 shadow-sm relative overflow-hidden flex flex-col h-full">
                        <div className="absolute top-0 left-0 w-full h-1 bg-amber-500"></div>
                        <div className="flex justify-between items-start mb-4">
                          <h5 className="font-bold text-stone-800 text-lg leading-tight">{strategy.name}</h5>
                          <span className="bg-amber-100 text-amber-800 text-xs font-black px-2.5 py-1 rounded-lg ml-2 shrink-0">{strategy.percentage}</span>
                        </div>
                        <div className="mb-4 flex-grow">
                          <p className="text-sm font-bold text-stone-700 mb-1">Vai trò:</p>
                          <p className="text-sm text-stone-600 leading-relaxed">{strategy.role}</p>
                        </div>
                        <div className="mt-auto">
                          <div className="bg-stone-50 p-3 rounded-xl border border-stone-100">
                            <p className="text-xs font-bold text-stone-500 mb-1">Mức giá:</p>
                            <p className="text-sm font-bold text-emerald-700 mb-2">{strategy.priceLevel}</p>
                            <p className="text-xs font-bold text-stone-500 mb-1">Ví dụ:</p>
                            <p className="text-sm font-medium text-stone-800">{strategy.examples}</p>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}"""

if target in content and "menuStrategy" not in content:
    # Need to make sure we replace the right one, the one inside section id="menu"
    content = content.replace(target, replacement, 1)
    with open('src/App.tsx', 'w') as f:
        f.write(content)
    print("Added menu strategy UI to App.tsx")
else:
    print("Target not found or already added")
