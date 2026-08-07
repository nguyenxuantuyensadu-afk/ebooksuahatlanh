import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

target = """          <AnimatePresence mode="wait">
            <motion.div
              key={activeModuleId}
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              transition={{ duration: 0.3 }}
              className="space-y-12"
            >"""

replacement = """          {currentUser?.role !== 'admin' && !(currentUser?.unlockedModules || []).includes(activeModuleId) ? (
            <div className="flex flex-col items-center justify-center py-20 px-4 text-center">
              <div className="w-20 h-20 bg-stone-100 text-stone-400 rounded-full flex items-center justify-center mb-6">
                <Lock size={40} />
              </div>
              <h3 className="text-2xl font-black text-stone-900 mb-2">Module Này Bị Khóa</h3>
              <p className="text-stone-500 font-medium max-w-md mx-auto">
                Bạn chưa được cấp quyền truy cập vào phần nội dung này. Vui lòng liên hệ quản trị viên để được hỗ trợ mở khóa.
              </p>
            </div>
          ) : (
          <AnimatePresence mode="wait">
            <motion.div
              key={activeModuleId}
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              transition={{ duration: 0.3 }}
              className="space-y-12"
            >"""

content = content.replace(target, replacement)

target2 = """          </motion.div>
        </AnimatePresence>
          
          {/* Footer */}"""

replacement2 = """          </motion.div>
        </AnimatePresence>
          )}
          
          {/* Footer */}"""

content = content.replace(target2, replacement2)

with open('src/App.tsx', 'w') as f:
    f.write(content)
print("done")
