import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

new_func = """const exportActiveModuleToPDF = async () => {
    try {
      setIsDownloading(true);
      
      const element = document.getElementById(activeModuleId);
      if (!element) return;
      
      await new Promise(resolve => setTimeout(resolve, 350));
      
      const activeModule = courseData.modules.find(m => m.id === activeModuleId);
      const title = activeModule ? activeModule.title.replace(/[^a-zA-Z0-9 -]/g, '') : 'bai-hoc';
      
      // Dynamic import to avoid Vite build/SSR issues
      const html2pdfModule = await import('html2pdf.js');
      const html2pdf = html2pdfModule.default || html2pdfModule;
      
      const opt = {
        margin:       [15, 10, 15, 10], 
        filename:     `${title}.pdf`,
        image:        { type: 'jpeg', quality: 0.98 },
        html2canvas:  { 
          scale: 2, 
          useCORS: true, 
          logging: false,
          ignoreElements: (node) => {
            return node.classList && node.classList.contains('print:hidden');
          }
        },
        jsPDF:        { unit: 'mm', format: 'a4', orientation: 'landscape' },
        pagebreak:    { mode: ['css', 'legacy'] }
      };
      
      await html2pdf().set(opt).from(element).save();
      
    } catch (err) {
      console.error('Error exporting PDF:', err);
    } finally {
      setIsDownloading(false);
    }
  };"""

pattern = re.compile(r'const exportActiveModuleToPDF = async \(\) => \{.*?\n  \};\n', re.DOTALL)
content = pattern.sub(new_func + '\n', content)

with open('src/App.tsx', 'w') as f:
    f.write(content)
