import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

new_export = """  const exportActiveModuleToPDF = async () => {
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
        
        if (typeof className === 'string' && className.match(/(space-y-\\d+|grid\\b)/)) {
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
  };"""

pattern = re.compile(r'  const exportActiveModuleToPDF = async \(\) => \{.*?\n  \};\n', re.DOTALL)
match = pattern.search(content)
if match:
    old_str = match.group(0)
    content = content.replace(old_str, new_export + '\n')
else:
    print("Not found!")

with open('src/App.tsx', 'w') as f:
    f.write(content)
