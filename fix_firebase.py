import re

with open('src/lib/firebase.ts', 'r') as f:
    content = f.read()

content = content.replace(
    "import { getFirestore } from 'firebase/firestore';",
    "import { getFirestore, initializeFirestore } from 'firebase/firestore';"
)

content = content.replace(
    'export const db = getFirestore(app, "ai-studio-giotrnhsahtthcch-576d790a-aead-4cc7-8fd0-328f7c23fb0a");',
    'export const db = initializeFirestore(app, { experimentalForceLongPolling: true }, "ai-studio-giotrnhsahtthcch-576d790a-aead-4cc7-8fd0-328f7c23fb0a");'
)

with open('src/lib/firebase.ts', 'w') as f:
    f.write(content)
