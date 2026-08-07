import { initializeApp } from 'firebase/app';
import { getAuth, signInAnonymously } from 'firebase/auth';

const firebaseConfig = {
  projectId: "gen-lang-client-0777757329",
  apiKey: "AIzaSyDlsOFERILkosKZ0yxS6DwvF78JwhhiutE",
  authDomain: "gen-lang-client-0777757329.firebaseapp.com"
};
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

async function test() {
  try {
    const cred = await signInAnonymously(auth);
    console.log("Anon UID:", cred.user.uid);
    process.exit(0);
  } catch (e) {
    console.error(e);
    process.exit(1);
  }
}
test();
