import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add import Login
if "import Login from" not in content:
    content = content.replace('import { CheckCircle2', 'import Login from "./components/Login";\nimport { CheckCircle2')

# Add isAuthenticated state
if "const [isAuthenticated, setIsAuthenticated]" not in content:
    content = content.replace('export default function App() {\n', 'export default function App() {\n  const [isAuthenticated, setIsAuthenticated] = useState(false);\n')

# Check if not authenticated
return_auth_code = """
  if (!isAuthenticated) {
    return <Login onLogin={() => setIsAuthenticated(true)} />;
  }

  return (
"""
if "!isAuthenticated" not in content:
    content = content.replace('  return (\n    <div className="min-h-screen', return_auth_code + '    <div className="min-h-screen')

with open('src/App.tsx', 'w') as f:
    f.write(content)

print("Auth added to App.tsx")
