import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Replace all closing fragments at the wrong place
content = content.replace('      </div>\n    </>\n      {/* Mobile Menu Overlay */}', '      </div>\n      {/* Mobile Menu Overlay */}')

# Make sure we don't have multiple </>\n  );\n}
content = content.replace('      )}\n    </div>\n  );\n}', '      )}\n    </div>\n    </>\n  );\n}')

# Just in case we already replaced the bottom one
if content.endswith('    </>\n    </>\n  );\n}'):
    content = content.replace('    </>\n    </>\n  );\n}', '    </>\n  );\n}')

with open('src/App.tsx', 'w') as f:
    f.write(content)
