// =====================================================
//  STUB DEL SDK DE FIREBASE (para probar las PANTALLAS reales)
//  Las pantallas (actividades, accesorios, agenda, Guiadas,
//  Encuentros) se cargan tal cual, con su DOM de verdad, pero
//  apuntando a una base falsa en memoria (window.__api).
//  Lo demas devuelve cosas inertes.
// =====================================================
function api(){ return window.__api; }

export function initializeApp(cfg){ return { __app: true, cfg }; }
export function getApp(){ return { __app: true }; }
export function getFirestore(app){ return { __db: true }; }

export function doc(db, ...p){ return api().doc(db, ...p); }
export function collection(db, n){ return api().collection(db, n); }
export function getDoc(ref){ return api().getDoc(ref); }
export function setDoc(ref, d){ return api().setDoc(ref, d); }
export function getDocs(col){ return api().getDocs(col); }
export function addDoc(col, d){ return api().addDoc(col, d); }
export function deleteDoc(ref){ return api().deleteDoc(ref); }
export function serverTimestamp(){ return api().serverTimestamp(); }

export async function updateDoc(){}
export function onSnapshot(){ return () => {}; }
export function query(...a){ return { __q: a }; }
export function where(...a){ return { __w: a }; }
export function orderBy(...a){ return { __o: a }; }
export function runTransaction(){ return async fn => fn(); }
export function getAuth(){ return { __auth: true }; }
export function GoogleAuthProvider(){ return { __p: true }; }
export async function signInWithPopup(){ return { user: {} }; }
export function onAuthStateChanged(){ return () => {}; }