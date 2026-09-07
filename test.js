const code = `
        <button 
          onClick={() => setActiveTab('locks')}
          className={\`flex items-center gap-2 px-6 py-3 rounded-xl font-bold transition-all \${
            activeTab === 'locks' ? 'bg-stone-900 text-white shadow-md' : 'bg-stone-100 text-stone-600 hover:bg-stone-200'
          }\`}
        >
          <Lock size={18} /> Khoá Nội Dung
        </button>
`
