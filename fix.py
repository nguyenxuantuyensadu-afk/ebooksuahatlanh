with open('src/App.tsx', 'r') as f:
    content = f.read()

bad = """                  </button>
                  </div>
                </div>

                <div className="flex flex-wrap items-center gap-2 pt-3 border-t border-stone-100">"""

good = """                  </button>
                </div>
              </div>

              <div className="mb-8 relative flex flex-wrap items-center gap-2 pt-3 print:hidden">"""

content = content.replace(bad, good)

# also remove the extra </div> before {/* Group Tabs */}
bad_end = """                  ))}
                </div>
              </div>

              {/* Group Tabs */}"""

good_end = """                  ))}
                </div>
              </div>

              {/* Group Tabs */}"""

with open('src/App.tsx', 'w') as f:
    f.write(content)
