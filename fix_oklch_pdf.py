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
      
      const elementsToRender: HTMLElement[] = [];
      for (const group of pageBlocks) {
          if (group.length === 0) continue;
          if (group.length === 1) {
              elementsToRender.push(group[0] as HTMLElement);
          } else {
              const wrapper = document.createElement('div');
              wrapper.style.display = 'flex';
              wrapper.style.flexDirection = 'column';
              wrapper.style.gap = '24px';
              
              const firstEl = group[0];
              firstEl.parentNode?.insertBefore(wrapper, firstEl);
              for (const el of group) {
                  wrapper.appendChild(el);
              }
              wrapper.dataset.isTempWrapper = "true";
              elementsToRender.push(wrapper);
          }
      }
      
      const pdfWidth = pdf.internal.pageSize.getWidth();
      const pdfHeight = pdf.internal.pageSize.getHeight();
      const margin = 15;
      
      let isFirstPage = true;
      
      for (let i = 0; i < elementsToRender.length; i++) {
          const el = elementsToRender[i];
          
          if (el.offsetHeight === 0) continue;
          
          const dataUrl = await toPng(el, {
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
          const maxHeight = pdfHeight - (margin * 2);
          
          let renderWidth = maxWidth;
          let renderHeight = (imgProps.height * renderWidth) / imgProps.width;
          
          if (renderHeight > maxHeight) {
              renderHeight = maxHeight;
              renderWidth = (imgProps.width * renderHeight) / imgProps.height;
          }
          
          if (!isFirstPage) {
              pdf.addPage();
          }
          
          const x = margin + (maxWidth - renderWidth) / 2;
          const y = margin;
          
          pdf.addImage(dataUrl, 'PNG', x, y, renderWidth, renderHeight);
          isFirstPage = false;
      }
      
      for (const el of elementsToRender) {
          if (el.dataset.isTempWrapper === "true") {
              const parent = el.parentNode;
              if (parent) {
                  while (el.firstChild) {
                      parent.insertBefore(el.firstChild, el);
                  }
                  parent.removeChild(el);
              }
          }
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
