import { initializeApp } from 'firebase/app';
import { getFirestore, doc, setDoc } from 'firebase/firestore';
import fs from 'fs';

const firebaseConfig = {
  projectId: "gen-lang-client-0777757329",
  apiKey: "AIzaSyDlsOFERILkosKZ0yxS6DwvF78JwhhiutE",
  authDomain: "gen-lang-client-0777757329.firebaseapp.com"
};
const app = initializeApp(firebaseConfig);
const db = getFirestore(app, "ai-studio-giotrnhsahtthcch-576d790a-aead-4cc7-8fd0-328f7c23fb0a");

async function seed() {
  try {
    // Initial users
    await setDoc(doc(db, "users", "admin"), {
      username: "admin",
      password: "123", // Insecure but fine for prototype
      role: "admin",
      createdAt: new Date().toISOString()
    });
    console.log("Admin seeded.");

    await setDoc(doc(db, "users", "student"), {
      username: "student",
      password: "123",
      role: "student",
      createdAt: new Date().toISOString()
    });
    console.log("Student seeded.");
    process.exit(0);
  } catch (e) {
    console.error(e);
    process.exit(1);
  }
}
seed();
