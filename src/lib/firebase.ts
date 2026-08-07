import { initializeApp, getApp, getApps } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore, initializeFirestore } from 'firebase/firestore';

const firebaseConfig = {
  projectId: "gen-lang-client-0777757329",
  appId: "1:987395005216:web:f1c88594d06d9493b41545",
  apiKey: "AIzaSyDlsOFERILkosKZ0yxS6DwvF78JwhhiutE",
  authDomain: "gen-lang-client-0777757329.firebaseapp.com",
  storageBucket: "gen-lang-client-0777757329.firebasestorage.app",
  messagingSenderId: "987395005216",
  measurementId: ""
};

// Initialize Firebase
const app = !getApps().length ? initializeApp(firebaseConfig) : getApp();

export const auth = getAuth(app);
export const db = initializeFirestore(app, { experimentalForceLongPolling: true }, "ai-studio-giotrnhsahtthcch-576d790a-aead-4cc7-8fd0-328f7c23fb0a");

// Secondary app for creating users without logging out
export const secondaryApp = initializeApp(firebaseConfig, "Secondary");
export const secondaryAuth = getAuth(secondaryApp);
