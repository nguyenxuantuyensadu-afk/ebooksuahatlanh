import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Fix the JSX conditional closing
content = content.replace("        )}\n        </main>", "        </>)}\n        </main>")

# Also we need to wrap the second part of the conditional in a Fragment
content = content.replace("""        {showAdmin ? (
          <AdminDashboard onClose={() => setShowAdmin(false)} />
        ) : (""", """        {showAdmin ? (
          <AdminDashboard onClose={() => setShowAdmin(false)} />
        ) : (<>""")

with open('src/App.tsx', 'w') as f:
    f.write(content)

print("Fixed syntax")
