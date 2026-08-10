import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

target_audience_ui = """
              <div className="mb-10 bg-amber-50/50 rounded-[2rem] p-8 md:p-10 border border-amber-100">
                <h4 className="font-bold text-2xl text-amber-900 mb-8 flex items-center gap-3">
                  <span className="w-2.5 h-2.5 rounded-full bg-amber-500"></span>
                  {course.modules[2].targetAudience?.title || 'Xác định khách hàng mục tiêu'}
                </h4>
                <div className="grid md:grid-cols-2 gap-6">
                  {course.modules[2].targetAudience?.groups.map((group: any, idx: number) => (
                    <div key={idx} className="bg-white p-6 rounded-2xl border border-amber-100 shadow-sm flex flex-col gap-3 transition-transform hover:-translate-y-1">
                      <div className="flex items-center gap-3">
                         <div className="w-8 h-8 rounded-full bg-amber-100 text-amber-600 flex items-center justify-center shrink-0 font-black text-sm">
                           {idx + 1}
                         </div>
                         <h5 className="font-bold text-stone-900 text-lg">{group.name}</h5>
                      </div>
                      <p className="text-stone-600 font-medium leading-relaxed pl-11">{group.description}</p>
                    </div>
                  ))}
                </div>
              </div>

              <div className="bg-white rounded-[2rem] shadow-sm border border-stone-200 overflow-hidden">"""

content = content.replace(
    '              <div className="bg-white rounded-[2rem] shadow-sm border border-stone-200 overflow-hidden">',
    target_audience_ui,
    1 # replace only the first occurrence in the file, though we should be careful. Let's make sure it's the right one.
)

with open('src/App.tsx', 'w') as f:
    f.write(content)
