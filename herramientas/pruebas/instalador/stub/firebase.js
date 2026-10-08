// =====================================================
//  STUB DEL SDK DE FIRESTORE (para las pruebas del instalador)
//  Delega todo en window.__api, que la prueba reemplaza por una
//  base falsa en memoria.asi nadie toca Firebase de verdad.
// =====================================================
function api(){
  if(!window.__api) throw new Error("la prueba no definiio window.__api");
  return window.__api;
}
export function doc(db, ...p){ return api().doc(db, ...p); }
export function getDoc(ref){ return api().getDoc(ref); }
export function setDoc(ref, d){ return api().setDoc(ref, d); }
export function collection(db, n){ return api().collection(db, n); }
export function getDocs(col){ return api().getDocs(col); }
export function addDoc(col, d){ return api().addDoc(col, d); }
export function serverTimestamp(){ return api().serverTimestamp(); }