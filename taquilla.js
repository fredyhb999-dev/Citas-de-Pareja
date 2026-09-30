// Taquilla (proyecto aparte, llaves públicas por diseño).
// Reglas: solo solicitudes (r/w) y packs (lectura).
export const TAQUILLA_FIREBASE = {
  "apiKey": "AIzaSyBIBF_RdDt1G-9PFZzTTfjd8xlIghCXZ1M",
  "authDomain": "taquilla-juegos.firebaseapp.com",
  "projectId": "taquilla-juegos",
  "storageBucket": "taquilla-juegos.firebasestorage.app",
  "messagingSenderId": "840449503241",
  "appId": "1:840449503241:web:41d3ac26d196721ef2c8d8"
};

// Llave PÚBLICA del autorizador: verifica, no firma (no sirve para falsificar).
export const TAQUILLA_PUBLICA = {"kty": "EC", "crv": "P-256", "x": "zE7aeZa_M1EgTnCN84jpu2F4uPqizYyW9e4Xd5yfLwM", "y": "NJJUiutYY3hVkV3tqlyvCXN7F6Pv8Kymq1qTZTyM47I", "ext": true};

function b64u(bytes){
  let s = '';
  bytes.forEach(b=>{ s += String.fromCharCode(b); });
  return btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}
function deB64u(t){
  t = t.replace(/-/g, '+').replace(/_/g, '/');
  while(t.length % 4) t += '=';
  const s = atob(t);
  const b = new Uint8Array(s.length);
  for(let i = 0; i < s.length; i++) b[i] = s.charCodeAt(i);
  return b;
}
async function clavePublica(){
  return crypto.subtle.importKey('jwk', TAQUILLA_PUBLICA,
    { name: 'ECDSA', namedCurve: 'P-256' }, false, ['verify']);
}
/** Verifica un código. Regresa payload {para,item,vence} o null. */
export async function verificarCodigo(codigo){
  try{
    const partes = String(codigo || '').trim().split('.');
    if(partes.length !== 2) return null;
    const datos = new TextEncoder().encode(partes[0]);
    const firma = deB64u(partes[1]);
    const key = await clavePublica();
    const ok = await crypto.subtle.verify({ name: 'ECDSA', hash: 'SHA-256' }, key, firma, datos);
    if(!ok) return null;
    const pay = JSON.parse(new TextDecoder().decode(deB64u(partes[0])));
    if(!pay || !pay.para || !pay.item) return null;
    if(pay.vence && Date.now() > pay.vence) return null;
    return pay;
  }catch(e){ return null; }
}
/** Firma un acceso (solo autorizador, con su privada guardada). */
export async function firmarAcceso(privJwk, para, item, vence){
  const pay = { para, item, vence: vence || null };
  const base = b64u(new TextEncoder().encode(JSON.stringify(pay)));
  const key = await crypto.subtle.importKey('jwk', privJwk,
    { name: 'ECDSA', namedCurve: 'P-256' }, false, ['sign']);
  const firma = new Uint8Array(await crypto.subtle.sign(
    { name: 'ECDSA', hash: 'SHA-256' }, key, new TextEncoder().encode(base)));
  return base + '.' + b64u(firma);
}
