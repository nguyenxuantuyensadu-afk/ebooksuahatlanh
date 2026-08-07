with open('src/App.tsx', 'r') as f:
    content = f.read()

# I will just remove that one `    </>\n`
content = content.replace('      </div>\n    </>\n      {/* Mobile', '      </div>\n      {/* Mobile')
content = content.replace('      )}\n    </div>\n  );\n}', '      )}\n    </div>\n    </>\n  );\n}')

with open('src/App.tsx', 'w') as f:
    f.write(content)
