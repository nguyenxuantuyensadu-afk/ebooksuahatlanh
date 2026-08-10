import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add a new state for the selected milk type
content = content.replace(
    'const [difficultyFilter, setDifficultyFilter] = useState<string | null>(null);',
    'const [difficultyFilter, setDifficultyFilter] = useState<string | null>(null);\n  const [selectedMilkType, setSelectedMilkType] = useState<string>("Sữa bắp, sữa bí đỏ (nhóm củ quả bùi)");'
)

old_ui = """                                    <tr key={idx} className="hover:bg-stone-50 transition-colors">
                                      <td className="py-3 px-6 font-bold text-stone-800">{item.name}</td>
                                      <td className="py-3 px-6 font-medium text-stone-600">{item.type}</td>
                                      <td className="py-3 px-6 text-sm text-stone-700">{item.prepTip}</td>
                                      <td className="py-3 px-6 font-black text-pink-600 text-right">{item.calories}</td>
                                    </tr>
                                  ))}
                               </tbody>
                             </table>
                           </div>
                        </div>

                      </div>
                    </div>
                  </section>
                )}"""

new_ui = """                                    <tr key={idx} className="hover:bg-stone-50 transition-colors">
                                      <td className="py-3 px-6 font-bold text-stone-800">{item.name}</td>
                                      <td className="py-3 px-6 font-medium text-stone-600">{item.type}</td>
                                      <td className="py-3 px-6 text-sm text-stone-700">{item.prepTip}</td>
                                      <td className="py-3 px-6 font-black text-pink-600 text-right">{item.calories}</td>
                                    </tr>
                                  ))}
                               </tbody>
                             </table>
                           </div>
                        </div>

                        {course.modules[0].sweetenerSuggestions && (
                          <div className="mt-8 bg-pink-50/50 p-6 md:p-8 rounded-[1.5rem] border border-pink-100">
                            <h5 className="font-bold text-xl text-pink-900 mb-6 flex items-center gap-2">
                              <Sparkles size={20} className="text-pink-500" />
                              Gợi ý nguyên liệu tạo ngọt theo loại sữa
                            </h5>
                            
                            <div className="flex flex-col md:flex-row gap-6 items-start">
                              <div className="w-full md:w-1/3">
                                <label className="block text-sm font-bold text-stone-700 mb-2">Chọn nhóm sữa hạt:</label>
                                <select 
                                  value={selectedMilkType}
                                  onChange={(e) => setSelectedMilkType(e.target.value)}
                                  className="w-full px-4 py-3 rounded-xl border border-stone-200 bg-white shadow-sm focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-transparent transition-all font-medium text-stone-700"
                                >
                                  {course.modules[0].sweetenerSuggestions.map((sug: any, idx: number) => (
                                    <option key={idx} value={sug.milkType}>{sug.milkType}</option>
                                  ))}
                                </select>
                              </div>
                              
                              <div className="w-full md:w-2/3">
                                {course.modules[0].sweetenerSuggestions
                                  .filter((sug: any) => sug.milkType === selectedMilkType)
                                  .map((sug: any, idx: number) => (
                                    <div key={idx} className="bg-white p-6 rounded-xl border border-pink-100 shadow-sm animate-in fade-in slide-in-from-bottom-2 duration-300">
                                      <div className="flex items-center gap-3 mb-3">
                                        <div className="w-10 h-10 rounded-full bg-pink-100 flex items-center justify-center shrink-0">
                                          <CheckCircle2 size={20} className="text-pink-600" />
                                        </div>
                                        <div>
                                          <p className="text-xs uppercase tracking-wider font-bold text-pink-500 mb-0.5">Khuyên dùng</p>
                                          <p className="font-black text-lg text-stone-900">{sug.recommended}</p>
                                        </div>
                                      </div>
                                      <div className="pl-13">
                                        <p className="text-stone-600 font-medium leading-relaxed">{sug.reason}</p>
                                      </div>
                                    </div>
                                  ))}
                              </div>
                            </div>
                          </div>
                        )}

                      </div>
                    </div>
                  </section>
                )}"""

content = content.replace(old_ui, new_ui)

with open('src/App.tsx', 'w') as f:
    f.write(content)
