import { initializeApp } from 'firebase/app';
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword } from 'firebase/auth';
import { getFirestore, doc, setDoc } from 'firebase/firestore';

const firebaseConfig = {
  projectId: "gen-lang-client-0777757329",
  apiKey: "AIzaSyDlsOFERILkosKZ0yxS6DwvF78JwhhiutE",
  authDomain: "gen-lang-client-0777757329.firebaseapp.com"
};
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app, "ai-studio-giotrnhsahtthcch-576d790a-aead-4cc7-8fd0-328f7c23fb0a");

async function bootstrap() {
  try {
    let cred;
    try {
        cred = await createUserWithEmailAndPassword(auth, "admin@example.com", "admin123");
    } catch(e) {
        cred = await signInWithEmailAndPassword(auth, "admin@example.com", "admin123");
    }
    console.log("Admin UID:", cred.user.uid);
    await setDoc(doc(db, "users", cred.user.uid), {
        email: "admin@example.com",
        role: "admin"
    });
    console.log("Admin doc written.");
    process.exit(0);
  } catch (e) {
    console.error(e);
    process.exit(1);
  }
}
bootstrap();
