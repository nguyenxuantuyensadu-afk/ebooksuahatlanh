import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

new_dl = """  const downloadRecipe = async (recipeId: string, recipeName: string) => {
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
  };"""

old_dl_pattern = re.compile(r'  const downloadRecipe = async \(.*?\) => \{.*?\n  \};\n', re.DOTALL)
content = old_dl_pattern.sub(new_dl + '\n', content)

with open('src/App.tsx', 'w') as f:
    f.write(content)
