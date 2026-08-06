import { Plus, Trash2, CheckCircle2, ChevronRight, Menu, X, Search, ChevronDown, ChevronUp, Printer, Download } from "lucide-react";
import React, { useState } from "react";
import { motion, AnimatePresence } from "motion/react";
import { courseData } from "./data";
import { toPng } from 'html-to-image';
import { jsPDF } from 'jspdf';

export default function App() {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [activeModuleId, setActiveModuleId] = useState(courseData.modules[0].id);
  const [recipeSearch, setRecipeSearch] = useState("");
  const [showOnlyEasy, setShowOnlyEasy] = useState(false);
  const [activeGroupIdx, setActiveGroupIdx] = useState(0);
  const [expandedRecipeId, setExpandedRecipeId] = useState<string | null>(null);
  const [isDownloading, setIsDownloading] = useState(false);
  const [sweetenerPrefs, setSweetenerPrefs] = useState<Record<string, 'sugar' | 'milk'>>({});
  const [recipeMultiplier, setRecipeMultiplier] = useState(1);
  
  interface CostRow {
    id: string;
    name: string;
    usage: number;
    buyQuantity: number;
    buyPrice: number;
    unit: string;
  }
  
  const [costYield, setCostYield] = useState<number>(10);
  const [detailedCostRows, setDetailedCostRows] = useState<CostRow[]>([
    { id: '1', name: 'Bắp nếp tươi', usage: 600, buyQuantity: 1000, buyPrice: 15000, unit: 'g' },
    { id: '2', name: 'Đường phèn hạt nhỏ', usage: 150, buyQuantity: 1000, buyPrice: 30000, unit: 'g' },
    { id: '3', name: 'Sữa đặc', usage: 50, buyQuantity: 1000, buyPrice: 60000, unit: 'ml' },
    { id: '4', name: 'Chai PET + Nắp', usage: 10, buyQuantity: 10, buyPrice: 12000, unit: 'bộ' },
    { id: '5', name: 'Tem nhãn decal', usage: 10, buyQuantity: 10, buyPrice: 6000, unit: 'bộ' },
    { id: '6', name: 'Điện, nước, khấu hao', usage: 1, buyQuantity: 1, buyPrice: 3500, unit: 'mẻ' }
  ]);

  const updateCostRow = (id: string, field: keyof CostRow, value: any) => {
    setDetailedCostRows(rows => rows.map(r => r.id === id ? { ...r, [field]: value } : r));
  };

  const removeCostRow = (id: string) => {
    setDetailedCostRows(rows => rows.filter(r => r.id !== id));
  };
  
  const totalDetailedCost = detailedCostRows.reduce((acc, r) => acc + (r.usage / (r.buyQuantity || 1)) * r.buyPrice, 0);
  
  const [dailySales, setDailySales] = useState<number>(50);
  const [sellingPrice, setSellingPrice] = useState<number>(15000);
  const [costPerBottle, setCostPerBottle] = useState<number>(3800);
  const [dailyOpsCost, setDailyOpsCost] = useState<number>(100000);

  const exportActiveModuleToPDF = async () => {
    try {
      setIsDownloading(true);
      
      const element = document.getElementById(activeModuleId);
      if (!element) return;
      
      await new Promise(resolve => setTimeout(resolve, 350));
      
      const activeModule = courseData.modules.find(m => m.id === activeModuleId);
      const title = activeModule ? activeModule.title.replace(/[^a-zA-Z0-9 -]/g, '') : 'bai-hoc';
      
      const pdf = new jsPDF({
        orientation: 'p',
        unit: 'mm',
        format: 'a4'
      });
      
      const pageBlocks: Element[][] = [];
      const children = Array.from(element.children);
      let currentGroup: Element[] = [];
      
      for (let i = 0; i < children.length; i++) {
        const child = children[i];
        const className = child.className || '';
        
        if (typeof className === 'string' && className.match(/(space-y-\d+|grid\b)/)) {
            if (currentGroup.length > 0) {
                pageBlocks.push(currentGroup);
                currentGroup = [];
            }
            const subChildren = Array.from(child.children);
            for (const sub of subChildren) {
                pageBlocks.push([sub]);
            }
        } else {
            currentGroup.push(child);
        }
      }
      if (currentGroup.length > 0) {
          pageBlocks.push(currentGroup);
      }
      
      const pdfWidth = pdf.internal.pageSize.getWidth();
      const pdfHeight = pdf.internal.pageSize.getHeight();
      const margin = 15;
      
      let isFirstPage = true;
      
      for (let i = 0; i < pageBlocks.length; i++) {
          const group = pageBlocks[i];
          if (group.length === 0) continue;
          
          if (!isFirstPage) {
              pdf.addPage();
          }
          
          let currentY = margin;
          
          for (const el of group) {
              if (el.offsetHeight === 0) continue;
              
              const dataUrl = await toPng(el as HTMLElement, {
                  quality: 1,
                  pixelRatio: 2,
                  backgroundColor: '#ffffff',
                  filter: (node) => {
                      return (node as HTMLElement).classList ? !(node as HTMLElement).classList.contains('print:hidden') : true;
                  },
                  style: {
                      transform: 'none',
                      boxShadow: 'none',
                  }
              });
              
              const imgProps = pdf.getImageProperties(dataUrl);
              const maxWidth = pdfWidth - (margin * 2);
              
              let renderWidth = maxWidth;
              let renderHeight = (imgProps.height * renderWidth) / imgProps.width;
              
              // Scale down if it exceeds the page height
              if (currentY + renderHeight > pdfHeight - margin) {
                  const availableHeight = pdfHeight - margin - currentY;
                  // If it's the first element on the page and it's too tall, just scale it
                  if (currentY === margin) {
                      renderHeight = availableHeight;
                      renderWidth = (imgProps.width * renderHeight) / imgProps.height;
                  } else {
                      // It doesn't fit on this page, add a new page
                      pdf.addPage();
                      currentY = margin;
                      // Recalculate if it still exceeds full page height
                      if (renderHeight > pdfHeight - margin * 2) {
                          renderHeight = pdfHeight - margin * 2;
                          renderWidth = (imgProps.width * renderHeight) / imgProps.height;
                      }
                  }
              }
              
              const x = margin + (maxWidth - renderWidth) / 2;
              pdf.addImage(dataUrl, 'PNG', x, currentY, renderWidth, renderHeight);
              currentY += renderHeight + 5; // 5mm gap
          }
          isFirstPage = false;
      }
      
      pdf.save(`${title}.pdf`);
      
    } catch (err) {
      console.error('Error exporting PDF:', err);
      alert('Có lỗi xảy ra khi xuất PDF. Vui lòng thử lại.');
    } finally {
      setIsDownloading(false);
    }
  };

  const downloadRecipe = async (recipeId: string, recipeName: string) => {
    try {
      setIsDownloading(true);
      const element = document.getElementById(`recipe-card-${recipeId}`);
      if (!element) return;
      
      await new Promise(resolve => setTimeout(resolve, 350));
      
      const width = element.scrollWidth;
      const height = element.scrollHeight;
      
      const dataUrl = await toPng(element, {
        quality: 1,
        pixelRatio: 2,
        backgroundColor: '#ffffff',
        width: width,
        height: height,
        filter: (node) => {
          return node.classList ? !node.classList.contains('download-section') : true;
        },
        style: {
          transform: 'none',
          boxShadow: 'none',
          border: 'none',
          width: `${width}px`,
          height: `${height}px`
        }
      });
      
      const link = document.createElement('a');
      link.download = `cong-thuc-${recipeName.toLowerCase().replace(/[^a-zA-Z0-9]/g, '-')}.png`;
      link.href = dataUrl;
      link.click();
    } catch (err) {
      console.error('Error downloading recipe:', err);
    } finally {
      setIsDownloading(false);
    }
  };

  const getDifficulty = (prepTip: string) => {
    const tip = prepTip.toLowerCase();
    if (tip.includes("hấp") || tip.includes("luộc") || tip.includes("nấu chín kỹ") || tip.includes("ngâm 8h") || tip.includes("ngâm 12h") || tip.includes("hầm") || tip.includes("nấu nhừ")) return "Advanced";
    if (tip.includes("không cần nấu") || tip.includes("xay sống") || tip.includes("nước ấm") || tip.includes("không ngâm") || tip.includes("nhanh")) return "Easy";
    return "Medium";
  };

  const NutritionIcon = courseData.modules[0].icon;
  const MenuIcon = courseData.modules[2].icon;
  const EquipmentIcon = courseData.modules[1].icon;
  const CostingIcon = courseData.modules[3].icon;
  const OperationsIcon = courseData.modules[4].icon;
  const MarketingIcon = courseData.modules[5].icon;
  const RecipesIcon = courseData.modules[6].icon;

  return (
    <div className="min-h-screen bg-[#f8f7f5] print:bg-white font-sans text-stone-900 selection:bg-amber-200">
      {/* Mobile Header */}
      <header className="print:hidden lg:hidden sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-stone-200 px-5 py-4 flex justify-between items-center shadow-sm">
        <h1 className="font-bold text-lg text-stone-900 truncate tracking-tight">Giáo Trình Sữa Hạt</h1>
        <button onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)} className="p-2 text-stone-600 hover:bg-stone-100 rounded-xl transition-colors">
          {isMobileMenuOpen ? <X size={20} /> : <Menu size={20} />}
        </button>
      </header>

      <div className="flex max-w-[1400px] mx-auto print:max-w-none print:w-full print:block">
        {/* Sidebar Navigation */}
        <aside
          className={`print:hidden ${
            isMobileMenuOpen ? "translate-x-0" : "-translate-x-full"
          } lg:translate-x-0 fixed lg:sticky top-0 lg:top-0 h-screen w-72 bg-[#f8f7f5] border-r border-stone-200 p-6 overflow-y-auto transition-transform duration-300 z-40`}
        >
          <div className="hidden lg:block mb-10">
            <h1 className="font-black text-[1.75rem] tracking-tight text-stone-900 leading-[1.1]">
              Kinh Doanh <br />
              <span className="text-amber-700">Sữa Hạt</span>
            </h1>
            <p className="text-sm font-semibold text-stone-500 mt-2 tracking-wide uppercase">Thực Chiến Take-away</p>
          </div>

          <nav className="space-y-1.5">
            <p className="text-[11px] font-bold text-stone-400 uppercase tracking-widest mb-4 mt-8 lg:mt-0">Mục lục khóa học</p>
            {courseData.modules.map((module) => {
              const Icon = module.icon;
              const isActive = activeModuleId === module.id;
              return (
                <button
                  key={module.id}
                  onClick={() => {
                    setActiveModuleId(module.id);
                    setIsMobileMenuOpen(false);
                  }}
                  className={`w-full flex items-center gap-3.5 px-4 py-3 text-left text-sm font-semibold rounded-xl transition-all duration-200 group ${
                    isActive
                      ? "bg-white text-amber-700 shadow-sm border border-stone-200/60"
                      : "text-stone-600 hover:bg-white hover:text-stone-900 border border-transparent"
                  }`}
                >
                  <Icon size={18} className={`transition-colors ${isActive ? "text-amber-600" : "text-stone-400 group-hover:text-stone-600"}`} />
                  <span className="flex-1 truncate">{module.title}</span>
                  <ChevronRight size={14} className={`transition-all ${isActive ? "opacity-100 text-amber-600 translate-x-0" : "opacity-0 -translate-x-2 group-hover:opacity-100 text-stone-300 group-hover:translate-x-0"}`} />
                </button>
              );
            })}
          </nav>

          <div className="mt-12 p-5 bg-white rounded-2xl border border-stone-200 shadow-sm">
            <div className="w-10 h-10 rounded-full bg-amber-50 flex items-center justify-center mb-3">
               <CheckCircle2 size={20} className="text-amber-600" />
            </div>
            <p className="text-xs text-stone-500 font-medium leading-relaxed">
              Tài liệu độc quyền thiết kế cho mô hình quầy và xe đẩy nhỏ lẻ.
            </p>
          </div>
        </aside>

        {/* Main Content */}
        <main className="flex-1 px-5 py-8 lg:px-16 lg:py-16 max-w-5xl w-full mx-auto bg-white min-h-screen border-l border-stone-100 shadow-[0_0_40px_rgba(0,0,0,0.02)] print:border-none print:shadow-none print:m-0 print:p-0 print:max-w-none print:w-full">
          {/* Hero Section */}
          <div className="mb-14 pb-10 border-b border-stone-100 print:hidden">
            <div className="inline-flex items-center px-3.5 py-1.5 rounded-full bg-stone-100 text-stone-800 text-[11px] font-bold uppercase tracking-widest mb-6">
              Module Cốt Lõi
            </div>
            <h2 className="text-4xl lg:text-[3.5rem] font-black text-stone-900 tracking-tight leading-[1.05] mb-6">
              {courseData.title}
            </h2>
            <p className="text-2xl font-bold text-amber-700 mb-5 tracking-tight">{courseData.subtitle}</p>
            <p className="text-lg text-stone-600 leading-relaxed max-w-3xl">
              {courseData.description}
            </p>
          </div>

          <AnimatePresence mode="wait">
            <motion.div
              key={activeModuleId}
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              transition={{ duration: 0.3 }}
              className="space-y-12"
            >
              {/* Section 0: Nutrition */}
              {activeModuleId === 'nutrition' && (
                <section id="nutrition">
                  <div className="flex flex-wrap items-center justify-between gap-4 mb-6">
                    <div className="flex items-center gap-4">
                      <div className="p-3.5 bg-green-100 text-green-700 rounded-2xl shadow-sm">
                        <NutritionIcon size={24} />
                      </div>
                      <h3 className="text-[1.75rem] font-bold text-stone-900 tracking-tight">{courseData.modules[0].title}</h3>
                    </div>
                    <button onClick={exportActiveModuleToPDF} className="print:hidden flex items-center gap-2 px-4 py-2.5 bg-rose-50 text-rose-600 hover:bg-rose-100 rounded-xl text-sm font-bold transition-colors"><Download size={16} />Xuất PDF slide</button>
                  </div>
                  <p className="text-stone-600 mb-10 text-[1.1rem] leading-relaxed max-w-4xl">{courseData.modules[0].description}</p>
                  
                  <div className="space-y-10">
                    <div>
                      <h4 className="font-bold text-xl text-stone-900 mb-6 flex items-center gap-2">
                        <span className="w-2 h-2 rounded-full bg-blue-500"></span>
                        Tháp Cân Bằng Dinh Dưỡng
                      </h4>
                      <div className="bg-stone-50 border border-stone-200 rounded-[1.5rem] p-6 md:p-8 flex flex-col items-center gap-3">
                        {courseData.modules[0].nutritionalPyramid?.map((item: any, idx: number) => (
                          <div 
                            key={idx} 
                            className={`flex flex-col sm:flex-row items-center justify-between p-4 rounded-xl border-2 ${item.color} ${item.width} min-w-[280px] shadow-sm transition-transform hover:scale-[1.02]`}
                          >
                            <div className="flex flex-col sm:flex-row items-center gap-2 sm:gap-4 text-center sm:text-left">
                              <span className="font-black text-lg opacity-70">Tầng {item.level}</span>
                              <div className="hidden sm:block w-px h-8 bg-current opacity-20"></div>
                              <div>
                                <h5 className="font-bold text-[15px]">{item.name}</h5>
                                <p className="text-xs font-medium opacity-80 mt-1">{item.description}</p>
                              </div>
                            </div>
                            <span className="font-black text-xl mt-2 sm:mt-0">{item.percentage}</span>
                          </div>
                        ))}
                      </div>
                    </div>

                    <div>
                      <h4 className="font-bold text-xl text-stone-900 mb-6 flex items-center gap-2">
                        <span className="w-2 h-2 rounded-full bg-green-500"></span>
                        Phân Loại Hạt Cơ Bản
                      </h4>
                      <div className="grid md:grid-cols-3 gap-6">
                        {courseData.modules[0].nutritionData?.map((item: any, idx: number) => (
                          <div key={idx} className="bg-stone-50 border border-stone-200 rounded-[1.5rem] p-6 hover:shadow-md transition-shadow">
                            <h5 className="font-bold text-stone-800 text-lg mb-3 leading-tight">{item.group}</h5>
                            <p className="text-sm font-medium text-stone-600 mb-4 bg-white p-3 rounded-xl border border-stone-100">{item.examples}</p>
                            <div className="space-y-4">
                              <div>
                                <p className="text-[10px] uppercase font-bold text-stone-400 mb-1 tracking-wider">Vai trò</p>
                                <p className="text-sm text-stone-700 font-medium leading-relaxed">{item.role}</p>
                              </div>
                              <div className="pt-4 border-t border-stone-200">
                                <p className="text-[10px] uppercase font-bold text-stone-400 mb-1 tracking-wider">Ngâm hạt</p>
                                <p className="text-sm text-amber-700 font-bold leading-relaxed">{item.soakTime}</p>
                              </div>
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>

                    <div className="bg-amber-50 rounded-[2rem] p-8 md:p-10 border border-amber-100">
                      <h4 className="font-bold text-xl text-amber-900 mb-6 flex items-center gap-2">
                        <span className="w-2 h-2 rounded-full bg-amber-500"></span>
                        Nguyên Tắc Ngâm Hạt Quan Trọng
                      </h4>
                      <div className="grid md:grid-cols-2 gap-4">
                        {courseData.modules[0].soakingRules?.map((rule: string, idx: number) => (
                          <div key={idx} className="bg-white p-5 rounded-2xl border border-amber-100/50 flex gap-4 items-start shadow-sm">
                            <div className="w-8 h-8 rounded-full bg-amber-100 text-amber-600 flex items-center justify-center shrink-0 font-bold text-sm">
                              {idx + 1}
                            </div>
                            <p className="text-sm font-medium text-stone-700 leading-relaxed pt-1.5">{rule}</p>
                          </div>
                        ))}
                      </div>
                    </div>

                    <div>
                      <h4 className="font-bold text-xl text-stone-900 mb-6 flex items-center gap-2">
                        <span className="w-2 h-2 rounded-full bg-teal-500"></span>
                        Thời Gian Ngâm Cho Từng Loại Hạt
                      </h4>
                      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-6">
                        {courseData.modules[0].specificSoakTimes?.map((item: any, idx: number) => (
                          <div key={idx} className="flex flex-col items-center group">
                            <div className="w-24 h-24 sm:w-28 sm:h-28 rounded-full border-[6px] border-teal-100 bg-white shadow-sm flex flex-col items-center justify-center transition-all group-hover:border-teal-300 group-hover:-translate-y-1 relative">
                              <span className="font-black text-teal-700 text-xl sm:text-2xl">{item.time}</span>
                            </div>
                            <span className="mt-4 font-bold text-stone-800 text-[15px]">{item.name}</span>
                            <span className="text-xs font-medium text-stone-500 mt-1">{item.note}</span>
                          </div>
                        ))}
                      </div>
                    </div>

                    <div>
                      <h4 className="font-bold text-xl text-stone-900 mb-6 flex items-center gap-2">
                        <span className="w-2 h-2 rounded-full bg-indigo-500"></span>
                        Quy Trình Nấu Sữa 7 Bước
                      </h4>
                      <div className="flex flex-col gap-4 relative before:absolute before:inset-0 before:ml-6 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-indigo-200 before:to-transparent">
                        {courseData.modules[0].brewingSteps?.map((step: any, idx: number) => (
                          <div key={idx} className={`relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active`}>
                            
                            <div className="flex items-center justify-center w-12 h-12 rounded-full border-4 border-white bg-indigo-100 text-indigo-600 shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 font-black z-10">
                              {step.step}
                            </div>
                            
                            <div className="w-[calc(100%-4rem)] md:w-[calc(50%-3rem)] bg-white p-5 rounded-2xl border border-stone-200 shadow-sm transition-transform hover:-translate-y-1">
                              <h5 className="font-bold text-stone-800 text-lg mb-2 text-indigo-900">{step.name}</h5>
                              <p className="text-sm font-medium text-stone-600 leading-relaxed">{step.description}</p>
                            </div>

                          </div>
                        ))}
                      </div>
                    </div>

                    <div className="bg-gradient-to-br from-violet-50 to-fuchsia-50 rounded-[2rem] p-8 md:p-10 border border-violet-100">
                      <div className="mb-8">
                        <h4 className="font-bold text-2xl text-violet-900 mb-3 flex items-center gap-3">
                          <span className="w-2.5 h-2.5 rounded-full bg-violet-500"></span>
                          Công Thức Phối Sữa Hạt Tiêu Chuẩn
                        </h4>
                        <p className="text-violet-800 font-medium opacity-90">{courseData.modules[0].mixingFormulas?.description}</p>
                      </div>

                      <div className="grid md:grid-cols-2 gap-8 mb-8">
                        <div className="bg-white rounded-[1.5rem] p-6 shadow-sm border border-violet-100/50">
                          <div className="inline-block px-3 py-1 bg-violet-100 text-violet-700 rounded-lg text-sm font-bold mb-4">
                            {courseData.modules[0].mixingFormulas?.twoTypes.title}
                          </div>
                          <div className="text-xl font-black text-stone-800 mb-6 bg-stone-50 p-4 rounded-xl border border-stone-100 text-center">
                            {courseData.modules[0].mixingFormulas?.twoTypes.ratio}
                          </div>
                          <ul className="space-y-3">
                            {courseData.modules[0].mixingFormulas?.twoTypes.examples.map((ex: string, idx: number) => (
                              <li key={idx} className="flex items-start gap-3">
                                <span className="text-violet-400 mt-1">✓</span>
                                <span className="text-sm font-medium text-stone-700">{ex}</span>
                              </li>
                            ))}
                          </ul>
                        </div>

                        <div className="bg-white rounded-[1.5rem] p-6 shadow-sm border border-fuchsia-100/50">
                          <div className="inline-block px-3 py-1 bg-fuchsia-100 text-fuchsia-700 rounded-lg text-sm font-bold mb-4">
                            {courseData.modules[0].mixingFormulas?.threeTypes.title}
                          </div>
                          <div className="text-xl font-black text-stone-800 mb-6 bg-stone-50 p-4 rounded-xl border border-stone-100 text-center">
                            {courseData.modules[0].mixingFormulas?.threeTypes.ratio}
                          </div>
                          <ul className="space-y-3">
                            {courseData.modules[0].mixingFormulas?.threeTypes.examples.map((ex: string, idx: number) => (
                              <li key={idx} className="flex items-start gap-3">
                                <span className="text-fuchsia-400 mt-1">✓</span>
                                <span className="text-sm font-medium text-stone-700">{ex}</span>
                              </li>
                            ))}
                          </ul>
                        </div>
                      </div>

                      <div className="bg-white/60 backdrop-blur-sm rounded-2xl p-6 border border-violet-100">
                        <h5 className="font-bold text-violet-900 mb-4 text-sm uppercase tracking-wider">Nguyên Tắc Vàng</h5>
                        <div className="grid gap-3">
                          {courseData.modules[0].mixingFormulas?.goldenRules.map((rule: string, idx: number) => (
                            <div key={idx} className="flex gap-3 items-center">
                              <div className="w-1.5 h-1.5 rounded-full bg-violet-400 shrink-0"></div>
                              <p className="text-sm font-medium text-stone-700">{rule}</p>
                            </div>
                          ))}
                        </div>
                      </div>
                    </div>
                  </div>
                </section>
              )}

              {/* Section 1: Menu */}
              {activeModuleId === 'menu' && (
                <section id="menu">
              <div className="flex flex-wrap items-center justify-between gap-4 mb-6">
                    <div className="flex items-center gap-4">
                <div className="p-3.5 bg-amber-100 text-amber-700 rounded-2xl shadow-sm">
                  <MenuIcon size={24} />
                </div>
                <h3 className="text-[1.75rem] font-bold text-stone-900 tracking-tight">{courseData.modules[2].title}</h3>
              </div>
                <button onClick={exportActiveModuleToPDF} className="print:hidden flex items-center gap-2 px-4 py-2.5 bg-rose-50 text-rose-600 hover:bg-rose-100 rounded-xl text-sm font-bold transition-colors"><Download size={16} />Xuất PDF slide</button>
            </div>
              <p className="text-stone-600 mb-10 text-[1.1rem] leading-relaxed max-w-4xl">{courseData.modules[2].description}</p>

              <div className="bg-white rounded-[2rem] shadow-sm border border-stone-200 overflow-hidden">
                <div className="overflow-x-auto">
                  <table className="w-full text-left border-collapse">
                    <thead>
                      <tr className="bg-stone-50/80 border-b border-stone-200">
                        <th className="py-5 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500 whitespace-nowrap">Tên Món</th>
                        <th className="py-5 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500 whitespace-nowrap">Giá Bán</th>
                        <th className="py-5 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500 min-w-[200px]">Đặc Điểm</th>
                        <th className="py-5 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500 min-w-[300px]">Lý Do Đưa Vào Menu</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-stone-100">
                      {courseData.modules[2].menuItems?.map((item, idx) => (
                        <tr key={idx} className="hover:bg-stone-50 transition-colors group">
                          <td className="py-5 px-6 font-bold text-stone-800 whitespace-nowrap">{item.name}</td>
                          <td className="py-5 px-6">
                            <span className="inline-flex px-3 py-1.5 rounded-lg bg-green-50 text-green-700 text-sm font-bold border border-green-100">
                              {item.price}
                            </span>
                          </td>
                          <td className="py-5 px-6 text-sm font-medium text-stone-600 leading-relaxed group-hover:text-stone-900 transition-colors">{item.features}</td>
                          <td className="py-5 px-6 text-sm font-medium text-stone-600 leading-relaxed">{item.reason}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
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
              )}
            </section>
          )}

          {/* Section 2: Equipment */}
          {activeModuleId === 'equipment' && (
            <section id="equipment">
              <div className="flex flex-wrap items-center justify-between gap-4 mb-6">
                    <div className="flex items-center gap-4">
                <div className="p-3.5 bg-sky-100 text-sky-700 rounded-2xl shadow-sm">
                  <EquipmentIcon size={24} />
                </div>
                <h3 className="text-[1.75rem] font-bold text-stone-900 tracking-tight">{courseData.modules[1].title}</h3>
              </div>
                <button onClick={exportActiveModuleToPDF} className="print:hidden flex items-center gap-2 px-4 py-2.5 bg-rose-50 text-rose-600 hover:bg-rose-100 rounded-xl text-sm font-bold transition-colors"><Download size={16} />Xuất PDF slide</button>
            </div>
              <p className="text-stone-600 mb-10 text-[1.1rem] leading-relaxed max-w-4xl">{courseData.modules[1].description}</p>

              <div className="grid md:grid-cols-2 gap-6">
                {courseData.modules[1].equipmentCategories?.map((category, idx) => (
                  <div key={idx} className="bg-white p-8 rounded-[2rem] shadow-sm border border-stone-200 hover:shadow-md transition-shadow">
                    <h4 className="font-bold text-xl text-stone-900 mb-6 pb-4 border-b border-stone-100">
                      {category.name}
                    </h4>
                    <ul className="space-y-5">
                      {category.items.map((item, itemIdx) => (
                        <li key={itemIdx} className="flex gap-4 items-start group">
                          <div className="mt-1 bg-green-50 rounded-full p-1 group-hover:bg-green-100 transition-colors shrink-0">
                             <CheckCircle2 size={16} className="text-green-600" />
                          </div>
                          <div>
                            <p className="font-bold text-stone-800">{item.name}</p>
                            <p className="text-sm font-medium text-stone-500 mt-1.5 leading-relaxed">{item.desc}</p>
                          </div>
                        </li>
                      ))}
                    </ul>
                  </div>
                ))}
              </div>
            </section>
          )}

          {/* Section 3: Costing */}
          {activeModuleId === 'costing' && (
            <section id="costing">
              <div className="flex flex-wrap items-center justify-between gap-4 mb-6">
                    <div className="flex items-center gap-4">
                <div className="p-3.5 bg-emerald-100 text-emerald-700 rounded-2xl shadow-sm">
                  <CostingIcon size={24} />
                </div>
                <h3 className="text-[1.75rem] font-bold text-stone-900 tracking-tight">{courseData.modules[3].title}</h3>
              </div>
                <button onClick={exportActiveModuleToPDF} className="print:hidden flex items-center gap-2 px-4 py-2.5 bg-rose-50 text-rose-600 hover:bg-rose-100 rounded-xl text-sm font-bold transition-colors"><Download size={16} />Xuất PDF slide</button>
            </div>
              
              <div className="bg-stone-50 p-8 rounded-[2rem] border border-stone-200 mb-10">
                <h4 className="font-bold text-lg mb-5 text-stone-900 flex items-center gap-2">
                   <span className="w-2 h-2 rounded-full bg-emerald-500"></span>
                   Nguyên Tắc Tính Giá Vốn:
                </h4>
                <ul className="space-y-4">
                  {courseData.modules[3].costExplanation?.map((exp, idx) => (
                    <li key={idx} className="flex gap-4 text-stone-700 font-medium text-[1.05rem] items-start">
                      <span className="w-6 h-6 rounded-full bg-white border border-stone-200 flex items-center justify-center shrink-0 text-xs font-bold text-stone-400 mt-0.5">{idx + 1}</span>
                      <span className="leading-relaxed">{exp}</span>
                    </li>
                  ))}
                </ul>
              </div>

              <div className="bg-white rounded-[2rem] shadow-sm border border-stone-200 overflow-hidden">
                <div className="bg-stone-900 px-8 py-5">
                  <h4 className="font-bold text-white text-lg tracking-wide">
                    Bảng tính mẫu: {courseData.modules[3].costTableData?.recipe}
                  </h4>
                </div>
                <div className="overflow-x-auto">
                  <table className="w-full text-left border-collapse">
                    <thead>
                      <tr className="bg-stone-50/80 border-b border-stone-200">
                        <th className="py-5 px-8 text-[11px] uppercase tracking-widest font-bold text-stone-500">Thành phần</th>
                        <th className="py-5 px-8 text-[11px] uppercase tracking-widest font-bold text-stone-500 text-right">Định lượng</th>
                        <th className="py-5 px-8 text-[11px] uppercase tracking-widest font-bold text-stone-500 text-right">Đơn giá</th>
                        <th className="py-5 px-8 text-[11px] uppercase tracking-widest font-bold text-stone-500 text-right">Thành tiền</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-stone-100">
                      {courseData.modules[3].costTableData?.rows.map((row, idx) => (
                        <tr key={idx} className="hover:bg-stone-50 transition-colors">
                          <td className="py-4 px-8 font-bold text-stone-800">{row.item}</td>
                          <td className="py-4 px-8 text-right font-medium text-stone-600">{row.quantity}</td>
                          <td className="py-4 px-8 text-right font-medium text-stone-500 text-sm">{row.unitCost}</td>
                          <td className="py-4 px-8 text-right font-bold text-stone-900">{row.total}</td>
                        </tr>
                      ))}
                    </tbody>
                    <tfoot className="bg-stone-50 border-t border-stone-200">
                      <tr>
                        <td colSpan={3} className="py-5 px-8 font-bold text-right text-stone-600 uppercase text-xs tracking-wider">Tổng Chi Phí Mẻ:</td>
                        <td className="py-5 px-8 font-black text-right text-stone-900 text-xl">
                          {courseData.modules[3].costTableData?.summary.totalCost}
                        </td>
                      </tr>
                      <tr>
                        <td colSpan={3} className="py-3 px-8 font-bold text-right text-stone-500 uppercase text-xs tracking-wider">Thành phẩm thu được:</td>
                        <td className="py-3 px-8 font-bold text-right text-stone-800">
                          {courseData.modules[3].costTableData?.summary.yield}
                        </td>
                      </tr>
                      <tr>
                        <td colSpan={3} className="py-3 px-8 font-bold text-right text-stone-600 uppercase text-xs tracking-wider">Giá Vốn (Cost) / 1 Chai:</td>
                        <td className="py-3 px-8 font-black text-right text-rose-600 text-xl">
                          {courseData.modules[3].costTableData?.summary.costPerBottle}
                        </td>
                      </tr>
                      <tr className="bg-emerald-50/50">
                        <td colSpan={3} className="py-6 px-8 font-bold text-right text-emerald-800 border-t border-emerald-100 uppercase text-xs tracking-wider">Giá Bán Đề Xuất:</td>
                        <td className="py-6 px-8 font-black text-right text-emerald-700 text-2xl border-t border-emerald-100">
                          {courseData.modules[3].costTableData?.summary.sellingPrice}
                        </td>
                      </tr>
                      <tr>
                        <td colSpan={3} className="py-4 px-8 font-bold text-right text-stone-500 uppercase text-xs tracking-wider">Biên lợi nhuận gộp:</td>
                        <td className="py-4 px-8 font-bold text-right text-stone-800">
                          {courseData.modules[3].costTableData?.summary.profitMargin}
                        </td>
                      </tr>
                    </tfoot>
                  </table>
                </div>
              </div>
              <div className="mt-10 bg-white rounded-[2rem] shadow-sm border border-stone-200 overflow-hidden">
                <div className="bg-stone-900 px-8 py-5 flex flex-wrap justify-between items-center gap-4">
                  <h4 className="font-bold text-white text-lg tracking-wide">
                    Bảng Tính Giá Vốn Chi Tiết (Tương Tác)
                  </h4>
                  <button 
                    onClick={() => setDetailedCostRows([...detailedCostRows, { id: Date.now().toString(), name: 'Nguyên liệu mới', usage: 100, buyQuantity: 1000, buyPrice: 0, unit: 'g' }])} 
                    className="print:hidden px-4 py-2 bg-emerald-500 hover:bg-emerald-600 text-white text-sm font-bold rounded-xl transition-colors flex items-center gap-2"
                  >
                    <Plus size={16} /> Thêm dòng
                  </button>
                </div>
                <div className="overflow-x-auto">
                  <table className="w-full text-left border-collapse min-w-[800px]">
                    <thead>
                      <tr className="bg-stone-50/80 border-b border-stone-200">
                        <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500 w-1/3">Tên Chi Phí</th>
                        <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500">Đ.Lượng dùng</th>
                        <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500">Quy cách mua</th>
                        <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500">Giá mua (VNĐ)</th>
                        <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500 text-right">Thành tiền</th>
                        <th className="py-4 px-6 text-[11px] uppercase tracking-widest font-bold text-stone-500 text-center print:hidden">Xóa</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-stone-100">
                      {detailedCostRows.map(row => (
                        <tr key={row.id} className="hover:bg-stone-50 transition-colors">
                          <td className="py-3 px-6">
                            <input type="text" value={row.name} onChange={e => updateCostRow(row.id, 'name', e.target.value)} className="w-full bg-transparent font-bold text-stone-800 focus:outline-none focus:border-emerald-500 border-b border-transparent hover:border-stone-200 px-1 py-1" />
                          </td>
                          <td className="py-3 px-6 flex items-center gap-2">
                            <input type="number" value={row.usage || ''} onChange={e => updateCostRow(row.id, 'usage', Number(e.target.value))} className="w-20 bg-stone-100 rounded-lg text-right font-medium text-stone-800 focus:outline-none focus:ring-1 focus:ring-emerald-500 px-2 py-1.5" />
                            <input type="text" value={row.unit} onChange={e => updateCostRow(row.id, 'unit', e.target.value)} className="w-12 bg-transparent text-sm text-stone-500 focus:outline-none" />
                          </td>
                          <td className="py-3 px-6 flex items-center gap-2">
                            <input type="number" value={row.buyQuantity || ''} onChange={e => updateCostRow(row.id, 'buyQuantity', Number(e.target.value))} className="w-20 bg-stone-100 rounded-lg text-right font-medium text-stone-800 focus:outline-none focus:ring-1 focus:ring-emerald-500 px-2 py-1.5" />
                            <span className="text-sm text-stone-500">{row.unit}</span>
                          </td>
                          <td className="py-3 px-6">
                            <input type="number" value={row.buyPrice || ''} onChange={e => updateCostRow(row.id, 'buyPrice', Number(e.target.value))} className="w-28 bg-stone-100 rounded-lg text-right font-medium text-stone-800 focus:outline-none focus:ring-1 focus:ring-emerald-500 px-2 py-1.5" />
                          </td>
                          <td className="py-3 px-6 text-right font-bold text-stone-900">
                            {((row.usage / (row.buyQuantity || 1)) * row.buyPrice).toLocaleString()}đ
                          </td>
                          <td className="py-3 px-6 text-center print:hidden">
                            <button onClick={() => removeCostRow(row.id)} className="p-2 text-stone-400 hover:text-rose-500 hover:bg-rose-50 rounded-lg transition-colors">
                              <Trash2 size={16} />
                            </button>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                    <tfoot className="bg-emerald-50/50 border-t border-emerald-100">
                      <tr>
                        <td colSpan={4} className="py-4 px-6 font-bold text-right text-stone-600 uppercase text-xs tracking-wider">Tổng Chi Phí Mẻ:</td>
                        <td className="py-4 px-6 font-black text-right text-stone-900 text-lg">
                          {totalDetailedCost.toLocaleString()}đ
                        </td>
                        <td className="print:hidden"></td>
                      </tr>
                      <tr>
                        <td colSpan={4} className="py-4 px-6 font-bold text-right text-stone-600 uppercase text-xs tracking-wider flex items-center justify-end gap-3">
                          Thành phẩm thu được:
                          <div className="flex items-center gap-2">
                            <input type="number" value={costYield} onChange={e => setCostYield(Number(e.target.value) || 1)} className="w-16 bg-white border border-emerald-200 rounded-lg text-center font-bold text-emerald-800 focus:outline-none focus:ring-2 focus:ring-emerald-500 px-2 py-1" />
                            <span className="text-emerald-800 lowercase">chai</span>
                          </div>
                        </td>
                        <td className="py-4 px-6 font-bold text-right text-stone-900">
                        </td>
                        <td className="print:hidden"></td>
                      </tr>
                      <tr className="bg-emerald-100/50">
                        <td colSpan={4} className="py-5 px-6 font-bold text-right text-emerald-800 border-t border-emerald-200 uppercase text-xs tracking-wider">Giá Vốn (Cost) / 1 Chai:</td>
                        <td className="py-5 px-6 font-black text-right text-rose-600 text-xl border-t border-emerald-200">
                          {(totalDetailedCost / (costYield || 1)).toLocaleString(undefined, { maximumFractionDigits: 0 })}đ
                        </td>
                        <td className="print:hidden border-t border-emerald-200"></td>
                      </tr>
                    </tfoot>
                  </table>
                </div>
              </div>

              <div className="mt-10 bg-white rounded-[2rem] shadow-sm border border-stone-200 overflow-hidden">
                <div className="bg-stone-900 px-8 py-5">
                  <h4 className="font-bold text-white text-lg tracking-wide">
                    Công Cụ Tính Lợi Nhuận Dự Kiến
                  </h4>
                </div>
                <div className="p-8">
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
                  <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
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
                        <div className="mt-6 grid grid-cols-2 gap-4">
                          <div className="bg-white/60 p-4 rounded-xl border border-emerald-100">
                             <div className="text-sm font-bold text-emerald-800 mb-1">Tỷ suất LN ròng:</div>
                             <div className="text-xl font-black text-emerald-600">
                               {dailySales * sellingPrice > 0 ? (((dailySales * sellingPrice - dailySales * costPerBottle - dailyOpsCost) / (dailySales * sellingPrice)) * 100).toFixed(1) : 0}%
                             </div>
                          </div>
                          <div className="bg-white/60 p-4 rounded-xl border border-emerald-100">
                             <div className="text-sm font-bold text-emerald-800 mb-1">Điểm hòa vốn/ngày:</div>
                             <div className="text-xl font-black text-emerald-600">
                               {(sellingPrice - costPerBottle) > 0 ? Math.ceil(dailyOpsCost / (sellingPrice - costPerBottle)) : 0} chai
                             </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

            </section>
          )}

          {/* Section 4: Operations & Tech */}
          {activeModuleId === 'operations' && (
            <section id="operations">
              <div className="flex flex-wrap items-center justify-between gap-4 mb-6">
                    <div className="flex items-center gap-4">
                <div className="p-3.5 bg-indigo-100 text-indigo-700 rounded-2xl shadow-sm">
                  <OperationsIcon size={24} />
                </div>
                <h3 className="text-[1.75rem] font-bold text-stone-900 tracking-tight">{courseData.modules[4].title}</h3>
              </div>
                <button onClick={exportActiveModuleToPDF} className="print:hidden flex items-center gap-2 px-4 py-2.5 bg-rose-50 text-rose-600 hover:bg-rose-100 rounded-xl text-sm font-bold transition-colors"><Download size={16} />Xuất PDF slide</button>
            </div>
              <p className="text-stone-600 mb-10 text-[1.1rem] leading-relaxed max-w-4xl">{courseData.modules[4].description}</p>

              <div className="space-y-10">
                <div className="bg-white p-8 rounded-[2rem] shadow-sm border border-stone-200">
                  <h4 className="font-bold text-2xl text-stone-900 mb-8 flex items-center gap-3">
                    <span className="w-1.5 h-7 bg-indigo-500 rounded-full inline-block"></span>
                    Quy Trình Chuẩn Bị (SOP) Đầu Ngày
                  </h4>
                  <div className="relative border-l-2 border-stone-100 ml-5 space-y-10 pb-4">
                    {courseData.modules[4].sopSteps?.map((step, idx) => (
                      <div key={idx} className="relative pl-10">
                        <span className="absolute -left-[11px] top-1.5 w-5 h-5 rounded-full bg-white border-4 border-indigo-500 shadow-sm"></span>
                        <div className="inline-block px-3 py-1 bg-indigo-50 text-indigo-700 font-bold text-xs rounded-lg mb-2">{step.time}</div>
                        <p className="text-stone-700 font-medium leading-relaxed">{step.task}</p>
                      </div>
                    ))}
                  </div>
                </div>

                <div className="grid md:grid-cols-2 gap-6">
                  {courseData.modules[4].techTips?.map((tip, idx) => (
                    <div key={idx} className="bg-stone-900 p-8 rounded-[2rem] shadow-sm text-white">
                      <h5 className="font-bold text-xl mb-4 leading-tight">{tip.title}</h5>
                      <p className="text-stone-400 font-medium leading-relaxed">{tip.desc}</p>
                    </div>
                  ))}
                </div>
              </div>
            </section>
          )}

          {/* Section 5: Marketing & TikTok */}
          {activeModuleId === 'marketing' && (
            <section id="marketing">
              <div className="flex flex-wrap items-center justify-between gap-4 mb-6">
                    <div className="flex items-center gap-4">
                <div className="p-3.5 bg-rose-100 text-rose-700 rounded-2xl shadow-sm">
                  <MarketingIcon size={24} />
                </div>
                <h3 className="text-[1.75rem] font-bold text-stone-900 tracking-tight">{courseData.modules[5].title}</h3>
              </div>
                <button onClick={exportActiveModuleToPDF} className="print:hidden flex items-center gap-2 px-4 py-2.5 bg-rose-50 text-rose-600 hover:bg-rose-100 rounded-xl text-sm font-bold transition-colors"><Download size={16} />Xuất PDF slide</button>
            </div>
              <p className="text-stone-600 mb-10 text-[1.1rem] leading-relaxed max-w-4xl">{courseData.modules[5].description}</p>

              <div className="space-y-10">
                {/* Concepts */}
                <div className="grid md:grid-cols-3 gap-6">
                  {courseData.modules[5].concepts?.map((concept, idx) => (
                    <div key={idx} className="bg-white p-8 rounded-[2rem] shadow-sm border border-stone-200 hover:border-rose-200 transition-colors">
                      <div className="w-12 h-12 rounded-full bg-rose-50 flex items-center justify-center mb-5 text-rose-600 font-black text-xl">
                        {idx + 1}
                      </div>
                      <h4 className="font-bold text-xl text-stone-900 mb-3">{concept.name}</h4>
                      <p className="text-[0.95rem] font-medium text-stone-500 leading-relaxed">{concept.desc}</p>
                    </div>
                  ))}
                </div>

                {/* Content Funnel */}
                <div className="bg-stone-900 p-10 rounded-[2rem] shadow-sm text-white">
                  <h4 className="font-bold text-2xl mb-8">Phễu Nội Dung (Content Funnel)</h4>
                  <div className="grid md:grid-cols-3 gap-6">
                    {courseData.modules[5].contentFunnel?.map((item, idx) => (
                      <div key={idx} className="bg-[#242424] rounded-2xl p-6 border border-stone-800">
                        <div className="text-rose-400 font-black text-3xl mb-3 tracking-tight">{item.percentage}</div>
                        <h5 className="font-bold text-lg mb-3 text-stone-100">{item.type}</h5>
                        <p className="text-sm font-medium text-stone-400 leading-relaxed">{item.desc}</p>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Shooting Guidelines */}
                <div className="bg-white p-8 rounded-[2rem] shadow-sm border border-stone-200">
                  <h4 className="font-bold text-2xl text-stone-900 mb-8 border-b border-stone-100 pb-5">
                    Kỹ Thuật Quay Dựng Cơ Bản Bằng Điện Thoại
                  </h4>
                  <div className="grid sm:grid-cols-2 gap-8">
                    {courseData.modules[5].shootingGuidelines?.map((guide, idx) => (
                      <div key={idx} className="flex gap-4">
                        <div className="mt-1 bg-rose-50 rounded-full p-1.5 shrink-0">
                           <CheckCircle2 className="text-rose-600" size={18} />
                        </div>
                        <div>
                          <h5 className="font-bold text-stone-900 mb-2">{guide.title}</h5>
                          <p className="text-[0.95rem] font-medium text-stone-500 leading-relaxed">{guide.desc}</p>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Perfect Video Blueprint */}
                <div className="bg-[#fff5f5] p-8 lg:p-10 rounded-[2rem] border border-rose-100 shadow-sm">
                  <h4 className="font-bold text-2xl text-rose-900 mb-8 tracking-tight">
                    {courseData.modules[5].perfectVideoBlueprint?.title}
                  </h4>
                  <div className="space-y-4">
                    {courseData.modules[5].perfectVideoBlueprint?.steps.map((step, idx) => (
                      <div key={idx} className="bg-white p-6 rounded-2xl shadow-sm border border-rose-100/50 flex flex-col md:flex-row gap-5 items-center">
                        <div className="md:w-1/3 shrink-0 w-full">
                          <span className="inline-block px-3.5 py-1.5 bg-rose-100 text-rose-900 font-black uppercase tracking-widest text-[10px] rounded-lg mb-3">
                            {step.time}
                          </span>
                          <p className="font-bold text-stone-800">{step.action}</p>
                        </div>
                        <div className="md:w-2/3 md:border-l-2 md:border-stone-100 md:pl-8 w-full">
                          <p className="text-[1.05rem] font-medium text-stone-600 italic">"{step.audio}"</p>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Local SEO */}
                <div className="bg-white p-8 rounded-[2rem] shadow-sm border border-stone-200">
                  <h4 className="font-bold text-2xl text-stone-900 mb-8">Tối Ưu Phân Phối Địa Phương (Local SEO)</h4>
                  <ul className="space-y-6">
                    {courseData.modules[5].localSEO?.map((seo, idx) => (
                      <li key={idx} className="flex gap-5 items-start">
                        <div className="w-10 h-10 rounded-xl bg-stone-100 flex items-center justify-center font-black text-stone-700 shrink-0">
                          {idx + 1}
                        </div>
                        <div className="pt-1.5">
                          <h5 className="font-bold text-stone-900 mb-2">{seo.title}</h5>
                          <p className="text-[0.95rem] font-medium text-stone-500 leading-relaxed">{seo.desc}</p>
                        </div>
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            </section>
          )}

          {/* Section 6: Recipes Dictionary */}
          {activeModuleId === 'recipes' && (
            <section id="recipes" className="print:m-0 print:p-0">
              <div className="flex flex-wrap items-center justify-between gap-4 mb-6 print:hidden">
                <div className="flex items-center gap-4">
                  <div className="p-3.5 bg-teal-100 text-teal-700 rounded-2xl shadow-sm">
                    <RecipesIcon size={24} />
                  </div>
                  <h3 className="text-[1.75rem] font-bold text-stone-900 tracking-tight">{courseData.modules[6].title}</h3>
                </div>
                <button onClick={exportActiveModuleToPDF} className="print:hidden flex items-center gap-2 px-4 py-2.5 bg-rose-50 text-rose-600 hover:bg-rose-100 rounded-xl text-sm font-bold transition-colors"><Download size={16} />Xuất PDF slide</button>
              </div>
              <p className="text-stone-600 mb-10 text-[1.1rem] leading-relaxed max-w-4xl print:hidden">{courseData.modules[6].description}</p>

              <div className="mb-8 relative flex flex-col md:flex-row gap-4 print:hidden">
                <div className="relative flex-1">
                  <div className="absolute inset-y-0 left-0 pl-5 flex items-center pointer-events-none">
                    <Search className="h-5 w-5 text-stone-400" />
                  </div>
                  <input
                    type="text"
                    placeholder="Tìm kiếm công thức, tên món hoặc công dụng..."
                    value={recipeSearch}
                    onChange={(e) => setRecipeSearch(e.target.value)}
                    className="w-full pl-12 pr-6 py-4 bg-stone-50 border border-stone-200 rounded-2xl focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all font-medium text-stone-900 placeholder:text-stone-400 shadow-sm"
                  />
                </div>
                <button 
                  onClick={() => setShowOnlyEasy(!showOnlyEasy)}
                  className={`px-8 py-4 rounded-2xl font-bold transition-all border whitespace-nowrap shadow-sm flex items-center gap-2 justify-center ${showOnlyEasy ? 'bg-teal-600 text-white border-teal-600' : 'bg-white text-stone-600 border-stone-200 hover:border-teal-200 hover:bg-teal-50'}`}
                >
                  {showOnlyEasy ? (
                    <>
                      <CheckCircle2 size={20} className="text-teal-200" />
                      Đang lọc: Easy
                    </>
                  ) : (
                    'Chỉ hiện món Easy'
                  )}
                </button>
              </div>

              {/* Group Tabs */}
              {!recipeSearch && !showOnlyEasy && (
                <div className="flex flex-wrap gap-2 mb-8 print:hidden">
                  {courseData.modules[6].recipeGroups?.map((group, idx) => (
                    <button
                      key={idx}
                      onClick={() => setActiveGroupIdx(idx)}
                      className={`px-5 py-2.5 rounded-xl text-[13px] font-bold transition-all border whitespace-nowrap ${
                        activeGroupIdx === idx
                          ? 'bg-[#13352c] text-white border-[#13352c] shadow-md'
                          : 'bg-white text-stone-600 border-stone-200 hover:border-teal-200 hover:bg-teal-50'
                      }`}
                    >
                      {group.groupName}
                    </button>
                  ))}
                </div>
              )}

              {/* Active Group Description */}
              {!recipeSearch && !showOnlyEasy && courseData.modules[6].recipeGroups && (
                <div className="mb-6 p-4 bg-teal-50 rounded-xl border border-teal-100 print:hidden">
                  <p className="text-teal-800 text-sm font-medium">
                    {courseData.modules[6].recipeGroups[activeGroupIdx].groupDesc}
                  </p>
                </div>
              )}

              {/* Recipes Grid */}
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-3 gap-6 mb-10 print:flex print:flex-col print:gap-0 print:mb-0">
                {courseData.modules[6].recipeGroups?.flatMap((group, idx) => {
                  const searchLower = recipeSearch.toLowerCase();
                  const matchGroup = group.groupName.toLowerCase().includes(searchLower) || group.groupDesc.toLowerCase().includes(searchLower);
                  
                  // If not searching, only show active group
                  if (!recipeSearch && !showOnlyEasy && idx !== activeGroupIdx) {
                    return [];
                  }

                  const filteredRecipes = group.recipes.filter(recipe => {
                    const searchMatch = matchGroup || 
                      recipe.name.toLowerCase().includes(searchLower) ||
                      recipe.usage.toLowerCase().includes(searchLower) ||
                      recipe.recipe.toLowerCase().includes(searchLower) ||
                      recipe.prepTip.toLowerCase().includes(searchLower);
                    
                    if (showOnlyEasy) {
                      return searchMatch && getDifficulty(recipe.prepTip) === "Easy";
                    }
                    return searchMatch;
                  });

                  return filteredRecipes.map((recipe, rIdx) => {
                    const diff = getDifficulty(recipe.prepTip);
                    const recipeId = `${idx}-${rIdx}`;
                    const isExpanded = expandedRecipeId === recipeId;
                    const sweetener = sweetenerPrefs[recipeId] || 'sugar';

                    return (
                      <div 
                        id={`recipe-card-${recipeId}`}
                        key={recipeId} 
                        className={`bg-white rounded-[2rem] p-6 transition-all flex flex-col group overflow-hidden ${
                          isExpanded 
                            ? 'col-span-1 md:col-span-2 lg:col-span-2 xl:col-span-3 border border-teal-500 shadow-md ring-4 ring-teal-50 h-auto cursor-default print:block print:border-none print:shadow-none print:ring-0 print:p-0' 
                            : 'col-span-1 border border-stone-200 hover:shadow-lg hover:-translate-y-1 hover:border-teal-300 h-full shadow-sm cursor-pointer print:hidden'
                        }`}
                      >
                        <div 
                          className="flex justify-between items-start mb-4 gap-3 cursor-pointer print:mb-6"
                          onClick={() => { setExpandedRecipeId(isExpanded ? null : recipeId); setRecipeMultiplier(1); }}
                        >
                          <h4 className="font-bold text-stone-900 text-lg leading-tight print:text-2xl">
                            {rIdx + 1}. {recipe.name}
                          </h4>
                          <span className={`px-2.5 py-1 text-[10px] uppercase tracking-wider font-bold rounded-md border shrink-0 print:border-stone-300 print:text-stone-700 ${
                            diff === 'Easy' ? 'bg-green-50 text-green-700 border-green-200' :
                            diff === 'Medium' ? 'bg-amber-50 text-amber-700 border-amber-200' :
                            'bg-rose-50 text-rose-700 border-rose-200'
                          }`}>
                            {diff}
                          </span>
                        </div>
                        
                        {(recipeSearch || showOnlyEasy) && (
                          <div className="mb-4">
                            <span className="inline-block px-2.5 py-1 bg-stone-100 text-stone-600 text-[10px] font-bold uppercase tracking-widest rounded-lg">
                              {group.groupName}
                            </span>
                          </div>
                        )}

                        <AnimatePresence initial={false} mode="wait">
                          {!isExpanded ? (
                            <motion.div
                              key="collapsed"
                              initial={{ height: 0, opacity: 0 }}
                              animate={{ height: "auto", opacity: 1 }}
                              exit={{ height: 0, opacity: 0 }}
                              transition={{ duration: 0.2 }}
                              className="flex-1 flex flex-col gap-4 overflow-hidden"
                            >
                              <div className="bg-stone-50 p-4 rounded-2xl border border-stone-100">
                                <p className="text-xs font-bold text-stone-400 uppercase tracking-widest mb-2">Công thức</p>
                                <p className="text-sm font-bold text-stone-800 leading-relaxed line-clamp-2">{recipe.recipe}</p>
                                <p className="text-amber-700 text-sm font-bold mt-1.5 flex items-center gap-1.5">
                                  <span className="w-1 h-1 rounded-full bg-amber-500"></span>
                                  {sweetener === 'sugar' ? '+ Đường phèn' : '+ Sữa đặc'}
                                </p>
                              </div>
                              
                              <div>
                                <p className="text-xs font-bold text-stone-400 uppercase tracking-widest mb-1.5">Công dụng</p>
                                <p className="text-sm font-medium text-stone-600 leading-relaxed group-hover:text-stone-800 transition-colors line-clamp-2">{recipe.usage}</p>
                              </div>
                              
                              <div className="mt-auto pt-4 border-t border-stone-100">
                                <p className="text-xs font-bold text-stone-400 uppercase tracking-widest mb-1.5">Mẹo sơ chế</p>
                                <p className="text-sm font-medium text-stone-500 italic line-clamp-1">"{recipe.prepTip}"</p>
                              </div>
                            </motion.div>
                          ) : (
                            <motion.div
                              key="expanded"
                              initial={{ height: 0, opacity: 0 }}
                              animate={{ height: "auto", opacity: 1 }}
                              exit={{ height: 0, opacity: 0 }}
                              transition={{ duration: 0.3 }}
                              className="overflow-hidden"
                            >
                              <div className="download-section flex justify-end pt-4 pb-2 border-t border-stone-100 mt-2 print:hidden">
                                <button 
                                  onClick={(e) => {
                                    e.stopPropagation();
                                    downloadRecipe(recipeId, recipe.name);
                                  }}
                                  disabled={isDownloading}
                                  className="flex items-center gap-2 px-4 py-2 bg-stone-100 hover:bg-stone-200 text-stone-700 rounded-xl text-sm font-bold transition-colors disabled:opacity-50"
                                >
                                  <Download size={16} />
                                  {isDownloading ? 'Đang Tải...' : 'Tải Công Thức'}
                                </button>
                              </div>
                              <div className="grid grid-cols-1 md:grid-cols-3 gap-6 pt-4 border-t border-stone-100">
                                <section>
                                  <h4 className="font-bold text-sm text-stone-900 mb-3 flex items-center gap-2">
                                    <span className="w-1.5 h-1.5 rounded-full bg-teal-500"></span>
                                    Nguyên liệu (Gram/ml)
                                  </h4>
                                  <div className="bg-teal-50/50 p-4 rounded-2xl border border-teal-100 h-full">
                                    <div className="mb-4 flex items-center justify-between print:hidden">
                                      <span className="text-xs font-bold text-teal-800 uppercase tracking-wider">Khẩu phần (Lít)</span>
                                      <div className="flex items-center gap-1 bg-white rounded-lg border border-teal-200 p-0.5 shadow-sm">
                                        <button 
                                          onClick={(e) => { e.stopPropagation(); setRecipeMultiplier(prev => Math.max(0.5, prev - 0.5)); }} 
                                          className="download-section w-7 h-7 flex justify-center items-center rounded hover:bg-teal-50 text-teal-700 font-bold"
                                        >-</button>
                                        <span className="w-10 text-center text-sm font-bold text-teal-900">{recipeMultiplier}L</span>
                                        <button 
                                          onClick={(e) => { e.stopPropagation(); setRecipeMultiplier(prev => prev + 0.5); }} 
                                          className="download-section w-7 h-7 flex justify-center items-center rounded hover:bg-teal-50 text-teal-700 font-bold"
                                        >+</button>
                                      </div>
                                    </div>
                                    <p className="text-sm font-bold text-teal-900 leading-relaxed">
                                      {recipe.recipe.replace(/(\d+(?:\.\d+)?)(\s*)(g|ml|lít|trái|quả)/gi, (match, num, space, unit) => {
                                        const val = parseFloat(num) * recipeMultiplier;
                                        // format to remove trailing .0 if integer
                                        const displayVal = val % 1 === 0 ? val : val.toFixed(1);
                                        return `${displayVal}${space}${unit}`;
                                      })}
                                    </p>
                                    <div className="mt-3 pt-3 border-t border-teal-100/50">
                                      <p className="text-xs font-bold text-teal-800 mb-2">Chất tạo ngọt (chọn 1)</p>
                                      <div className="flex gap-2 download-section">
                                        <button 
                                          onClick={(e) => { e.stopPropagation(); setSweetenerPrefs(prev => ({...prev, [recipeId]: 'sugar'})); }}
                                          className={`flex-1 py-1.5 px-2 rounded-lg border text-[11px] font-bold transition-colors ${sweetener === 'sugar' ? 'bg-amber-100 border-amber-300 text-amber-800' : 'bg-white border-teal-200 text-teal-700 hover:bg-teal-50'}`}
                                        >
                                          Đường phèn
                                        </button>
                                        <button 
                                          onClick={(e) => { e.stopPropagation(); setSweetenerPrefs(prev => ({...prev, [recipeId]: 'milk'})); }}
                                          className={`flex-1 py-1.5 px-2 rounded-lg border text-[11px] font-bold transition-colors ${sweetener === 'milk' ? 'bg-amber-100 border-amber-300 text-amber-800' : 'bg-white border-teal-200 text-teal-700 hover:bg-teal-50'}`}
                                        >
                                          Sữa đặc
                                        </button>
                                      </div>
                                      <p className="text-amber-700 text-xs font-bold mt-2 flex items-center gap-1.5">
                                        <span className="w-1 h-1 rounded-full bg-amber-500"></span>
                                        {sweetener === 'sugar' ? '+ Đường phèn (khoảng 10-20g/chai)' : '+ Sữa đặc (khoảng 15-25ml/chai)'}
                                      </p>
                                    </div>
                                  </div>
                                </section>
                                
                                <section>
                                  <h4 className="font-bold text-sm text-stone-900 mb-3 flex items-center gap-2">
                                    <span className="w-1.5 h-1.5 rounded-full bg-indigo-500"></span>
                                    Hướng dẫn chi tiết
                                  </h4>
                                  <div className="space-y-3 bg-stone-50 p-4 rounded-2xl border border-stone-100 h-full">
                                    <div className="flex gap-3">
                                      <div className="w-6 h-6 rounded-full bg-indigo-50 text-indigo-700 font-black text-xs flex items-center justify-center shrink-0">1</div>
                                      <div>
                                        <p className="font-bold text-stone-800 text-sm mb-0.5">Sơ chế</p>
                                        <p className="text-xs font-medium text-stone-600 leading-relaxed">{recipe.prepTip}</p>
                                      </div>
                                    </div>
                                    <div className="flex gap-3">
                                      <div className="w-6 h-6 rounded-full bg-indigo-50 text-indigo-700 font-black text-xs flex items-center justify-center shrink-0">2</div>
                                      <div>
                                        <p className="font-bold text-stone-800 text-sm mb-0.5">Xay & Nấu</p>
                                        <p className="text-xs font-medium text-stone-600 leading-relaxed">
                                          {diff === 'Easy' 
                                            ? 'Cho nguyên liệu vào máy xay công nghiệp cùng nước ấm, xay tốc độ cao 2-3 phút đến khi nhuyễn mịn.'
                                            : 'Hấp/luộc chín nguyên liệu. Cho vào máy xay công nghiệp cùng nước ấm, xay tốc độ cao 2-3 phút đến khi nhuyễn mịn.'}
                                        </p>
                                      </div>
                                    </div>
                                    <div className="flex gap-3">
                                      <div className="w-6 h-6 rounded-full bg-indigo-50 text-indigo-700 font-black text-xs flex items-center justify-center shrink-0">3</div>
                                      <div>
                                        <p className="font-bold text-stone-800 text-sm mb-0.5">Hoàn thiện</p>
                                        <p className="text-xs font-medium text-stone-600 leading-relaxed">Rót ra chai, bảo quản tủ lạnh.</p>
                                      </div>
                                    </div>
                                  </div>
                                </section>
                                
                                <div className="flex flex-col gap-6">
                                  <section>
                                    <h4 className="font-bold text-sm text-stone-900 mb-3 flex items-center gap-2">
                                      <span className="w-1.5 h-1.5 rounded-full bg-amber-500"></span>
                                      Dụng cụ
                                    </h4>
                                    <div className="flex flex-wrap gap-2">
                                      <span className="px-2.5 py-1 bg-stone-50 border border-stone-200 rounded-lg text-xs font-medium text-stone-700">Máy xay công nghiệp</span>
                                      <span className="px-2.5 py-1 bg-stone-50 border border-stone-200 rounded-lg text-xs font-medium text-stone-700">Cân tiểu ly</span>
                                      <span className="px-2.5 py-1 bg-stone-50 border border-stone-200 rounded-lg text-xs font-medium text-stone-700">Chai 330ml</span>
                                      {diff !== 'Easy' && (
                                        <span className="px-2.5 py-1 bg-stone-50 border border-stone-200 rounded-lg text-xs font-medium text-stone-700">Rây lọc</span>
                                      )}
                                    </div>
                                  </section>
                                  
                                  <section>
                                    <h4 className="font-bold text-sm text-stone-900 mb-3 flex items-center gap-2">
                                      <span className="w-1.5 h-1.5 rounded-full bg-rose-500"></span>
                                      Dinh dưỡng
                                    </h4>
                                    <div className="bg-rose-50/50 p-4 rounded-2xl border border-rose-100">
                                      <p className="text-xs font-medium text-stone-700 leading-relaxed">{recipe.usage}</p>
                                      <div className="mt-3 pt-3 border-t border-rose-100/50 flex items-center gap-3">
                                        <div className="flex-1">
                                          <p className="text-[9px] uppercase font-bold text-stone-400 mb-0.5">Năng lượng</p>
                                          <p className="font-bold text-stone-800 text-xs">~150-250 kcal</p>
                                        </div>
                                        <div className="w-px h-6 bg-rose-200/50"></div>
                                        <div className="flex-1">
                                          <p className="text-[9px] uppercase font-bold text-stone-400 mb-0.5">Hạn dùng</p>
                                          <p className="font-bold text-stone-800 text-xs">2 - 3 ngày</p>
                                        </div>
                                      </div>
                                    </div>
                                  </section>
                                </div>
                              </div>
                            </motion.div>
                          )}
                        </AnimatePresence>
                      </div>
                    );
                  });
                })}
              </div>
            </section>
          )}

          {/* Section 7: Troubleshooting */}
          {activeModuleId === 'troubleshooting' && (() => {
            const TroubleshootingIcon = courseData.modules[7].icon;
            return (
            <section id="troubleshooting">
              <div className="flex flex-wrap items-center justify-between gap-4 mb-6">
                    <div className="flex items-center gap-4">
                <div className="p-3.5 bg-rose-100 text-rose-700 rounded-2xl shadow-sm">
                  <TroubleshootingIcon size={24} />
                </div>
                <h3 className="text-[1.75rem] font-bold text-stone-900 tracking-tight">{courseData.modules[7].title}</h3>
              </div>
                <button onClick={exportActiveModuleToPDF} className="print:hidden flex items-center gap-2 px-4 py-2.5 bg-rose-50 text-rose-600 hover:bg-rose-100 rounded-xl text-sm font-bold transition-colors"><Download size={16} />Xuất PDF slide</button>
            </div>
              <p className="text-stone-600 mb-10 text-[1.1rem] leading-relaxed max-w-4xl">{courseData.modules[7].description}</p>

              <div className="space-y-6">
                {courseData.modules[7].issues?.map((issue: any, idx: number) => (
                  <div key={idx} className="bg-white p-6 md:p-8 rounded-[2rem] shadow-sm border border-stone-200">
                    <h4 className="font-bold text-xl text-stone-900 mb-6 flex items-center gap-3">
                      <div className="w-8 h-8 rounded-full bg-rose-50 text-rose-600 flex items-center justify-center shrink-0 font-black text-sm">
                        {idx + 1}
                      </div>
                      {issue.name}
                    </h4>
                    <div className="grid md:grid-cols-2 gap-6 md:gap-10">
                      <div className="bg-stone-50 p-6 rounded-2xl border border-stone-100 relative">
                        <div className="absolute -top-3 -left-3 w-8 h-8 rounded-full bg-stone-200 text-stone-600 flex items-center justify-center font-bold text-xs">
                          Lý do
                        </div>
                        <h5 className="font-bold text-stone-800 mb-3 ml-2">Nguyên nhân</h5>
                        <p className="text-sm font-medium text-stone-600 leading-relaxed ml-2">{issue.cause}</p>
                      </div>
                      <div className="bg-teal-50/50 p-6 rounded-2xl border border-teal-100 relative">
                        <div className="absolute -top-3 -left-3 w-8 h-8 rounded-full bg-teal-200 text-teal-800 flex items-center justify-center font-bold text-xs">
                          Mẹo
                        </div>
                        <h5 className="font-bold text-teal-900 mb-3 ml-2">Cách khắc phục</h5>
                        <p className="text-sm font-medium text-teal-800 leading-relaxed ml-2">{issue.solution}</p>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </section>
            );
          })()}
          </motion.div>
        </AnimatePresence>
          
          {/* Footer */}
          <footer className="mt-24 pt-8 border-t border-stone-200 text-center">
            <p className="text-sm text-stone-500 font-medium">
              Thiết kế dành riêng cho Học Viên Khởi Nghiệp - Mô hình Take-away Thực Chiến
            </p>
          </footer>
        </main>
      </div>

      {/* Mobile Menu Overlay */}
      {isMobileMenuOpen && (
        <div 
          className="fixed inset-0 bg-stone-900/20 backdrop-blur-sm z-30 lg:hidden"
          onClick={() => setIsMobileMenuOpen(false)}
        />
      )}

    </div>
  );
}
