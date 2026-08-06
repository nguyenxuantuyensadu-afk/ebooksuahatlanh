import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

new_export = """  const exportActiveModuleToPDF = async () => {
    try {
      setIsDownloading(true);
      const element = document.getElementById(activeModuleId);
      if (!element) return;
      
      // Wait for any animations to finish
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
          return node.classList ? !node.classList.contains('print:hidden') : true;
        },
        style: {
          transform: 'none',
          boxShadow: 'none',
          width: `${width}px`,
          height: `${height}px`
        }
      });
      
      const pdf = new jsPDF({
        orientation: 'p',
        unit: 'px',
        format: 'a4'
      });
      
      const imgProps = pdf.getImageProperties(dataUrl);
      const pdfWidth = pdf.internal.pageSize.getWidth();
      const pdfHeight = (imgProps.height * pdfWidth) / imgProps.width;
      
      let heightLeft = pdfHeight;
      let position = 0;
      
      pdf.addImage(dataUrl, 'PNG', 0, position, pdfWidth, pdfHeight);
      heightLeft -= pdf.internal.pageSize.getHeight();
      
      while (heightLeft >= 0) {
        position = heightLeft - pdfHeight;
        pdf.addPage();
        pdf.addImage(dataUrl, 'PNG', 0, position, pdfWidth, pdfHeight);
        heightLeft -= pdf.internal.pageSize.getHeight();
      }
      
      const activeModule = courseData.modules.find(m => m.id === activeModuleId);
      const title = activeModule ? activeModule.title.replace(/[^a-zA-Z0-9 -]/g, '') : 'bai-hoc';
      
      pdf.save(`${title}.pdf`);
    } catch (err) {
      console.error('Error exporting PDF:', err);
    } finally {
      setIsDownloading(false);
    }
  };"""

old_export_pattern = re.compile(r'  const exportActiveModuleToPDF = async \(\) => \{.*?\n  \};\n', re.DOTALL)
content = old_export_pattern.sub(new_export + '\n', content)

with open('src/App.tsx', 'w') as f:
    f.write(content)
