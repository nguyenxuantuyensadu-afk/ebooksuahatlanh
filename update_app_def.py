import re

with open('src/App.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

definition_ui = """                  <p className="text-stone-600 mb-10 text-[1.1rem] leading-relaxed max-w-4xl">{course.modules[0].description}</p>
                  
                  {course.modules[0].definition && (
                    <div className="mb-10 bg-indigo-50/50 rounded-[2rem] border border-indigo-100 p-8">
                      <h4 className="font-bold text-2xl text-indigo-900 mb-6 flex items-center gap-2">
                        <span className="w-2 h-2 rounded-full bg-indigo-500"></span>
                        {course.modules[0].definition.title}
                      </h4>
                      <div className="space-y-4">
                        {course.modules[0].definition.content.map((paragraph: string, idx: number) => (
                          <p key={idx} className="text-indigo-800/80 leading-relaxed font-medium">
                            {paragraph}
                          </p>
                        ))}
                      </div>
                    </div>
                  )}

                  <div className="space-y-10">
                    <div>
                      <h4 className="font-bold text-xl text-stone-900 mb-6 flex items-center gap-2">"""

content = content.replace('                  <p className="text-stone-600 mb-10 text-[1.1rem] leading-relaxed max-w-4xl">{course.modules[0].description}</p>\n                  \n                  <div className="space-y-10">\n                    <div>\n                      <h4 className="font-bold text-xl text-stone-900 mb-6 flex items-center gap-2">', definition_ui)

with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated App.tsx to include definition")
