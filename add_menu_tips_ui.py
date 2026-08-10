import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

old_block = """              )}

              {course.modules[2].menuStrategy && ("""

new_block = """              )}

              {course.modules[2].menuTips && (
                <div className="mb-10 bg-rose-50/50 rounded-[2rem] p-8 md:p-10 border border-rose-100">
                  <h4 className="font-bold text-2xl text-rose-900 mb-8 flex items-center gap-3">
                    <span className="w-2.5 h-2.5 rounded-full bg-rose-500"></span>
                    {course.modules[2].menuTips.title}
                  </h4>
                  <div className="grid md:grid-cols-2 gap-6">
                    {course.modules[2].menuTips.tips.map((tip: any, idx: number) => (
                      <div key={idx} className="bg-white p-6 rounded-2xl border border-rose-100 shadow-sm transition-transform hover:-translate-y-1">
                        <div className="flex items-center gap-3 mb-3">
                          <div className="w-8 h-8 rounded-full bg-rose-100 text-rose-600 flex items-center justify-center shrink-0 font-black text-sm">
                            {idx + 1}
                          </div>
                          <h5 className="font-bold text-stone-900 text-lg">{tip.title}</h5>
                        </div>
                        <p className="text-stone-600 font-medium leading-relaxed pl-11">{tip.content}</p>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {course.modules[2].menuStrategy && ("""

content = content.replace(old_block, new_block)

with open('src/App.tsx', 'w') as f:
    f.write(content)
