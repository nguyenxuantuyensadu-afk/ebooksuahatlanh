import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

old_ui = """                <div className="mt-10">
                  <h4 className="text-xl font-bold text-stone-900 mb-2">{course.modules[2].menuStrategy.title}</h4>"""

new_ui = """              {course.modules[2].sampleMenus && (
                <div className="mt-10">
                  <h4 className="font-bold text-2xl text-stone-900 mb-6 flex items-center gap-2">
                    <span className="w-2 h-2 rounded-full bg-emerald-500"></span>
                    Menu Gợi Ý Theo Nhóm Khách Hàng
                  </h4>
                  <div className="grid md:grid-cols-2 gap-6 mb-10">
                    {course.modules[2].sampleMenus.map((menu: any, idx: number) => (
                      <div key={idx} className="bg-white rounded-2xl border border-stone-200 shadow-sm overflow-hidden flex flex-col">
                        <div className="bg-stone-900 px-6 py-4">
                          <h5 className="font-bold text-white text-lg tracking-wide">{menu.groupName}</h5>
                          <p className="text-stone-300 text-sm mt-1">{menu.description}</p>
                        </div>
                        <div className="p-0 flex-grow">
                          <ul className="divide-y divide-stone-100">
                            {menu.items.map((item: any, iIdx: number) => (
                              <li key={iIdx} className="flex justify-between items-center px-6 py-4 hover:bg-stone-50 transition-colors">
                                <span className="font-bold text-stone-800">{item.name}</span>
                                <span className="font-bold text-emerald-600 bg-emerald-50 px-3 py-1 rounded-lg text-sm">{item.price}</span>
                              </li>
                            ))}
                          </ul>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

                <div className="mt-10">
                  <h4 className="text-xl font-bold text-stone-900 mb-2">{course.modules[2].menuStrategy.title}</h4>"""

content = content.replace(old_ui, new_ui)

with open('src/App.tsx', 'w') as f:
    f.write(content)
