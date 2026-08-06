import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add import
if "import html2pdf" not in content:
    content = content.replace("import { jsPDF } from 'jspdf';", "import { jsPDF } from 'jspdf';\n// @ts-ignore\nimport html2pdf from 'html2pdf.js';")

new_func = """const exportActiveModuleToPDF = async () => {
    try {
      setIsDownloading(true);
      
      // Select the main content container
      // If we want to export all modules, we would need to render them all.
      // Assuming we export the active module:
      const element = document.getElementById(activeModuleId);
      if (!element) return;
      
      // Wait for any animations
      await new Promise(resolve => setTimeout(resolve, 350));
      
      const activeModule = courseData.modules.find(m => m.id === activeModuleId);
      const title = activeModule ? activeModule.title.replace(/[^a-zA-Z0-9 -]/g, '') : 'bai-hoc';
      
      const opt = {
        margin:       [15, 10, 15, 10], // top, left, bottom, right in mm
        filename:     `${title}.pdf`,
        image:        { type: 'jpeg', quality: 0.98 },
        html2canvas:  { scale: 2, useCORS: true, logging: false },
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
