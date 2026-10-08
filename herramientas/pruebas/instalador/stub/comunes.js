// =====================================================
//  STUBS de modulos compartidos (acceso, taquilla, invitado)
//  Para probar las pantallas reales sin licenses ni tienda.
// =====================================================

// acceso.js
export function miProyecto(){ return "stub"; }
export function appTaq(){ return { __db: true }; }
export function leerLicencias(){ return {}; }
export function guardarLicencia(){}
export function quitarLicencia(){}
export async function tengoAcceso(){ return window.__conAcceso === true; }
export async function oficialesAprobados(){ return []; }
export function escucharItem(){ return () => {}; }

// taquilla.js
export async function verificarCodigo(){ return null; }
export async function verificarFirma(){ return null; }
export const TAQUILLA_FIREBASE = { projectId: "stub" };

// invitado.js
export async function publicarInvitacion(){ return {}; }
export async function retirarInvitacion(){ return {}; }
export async function pausarInvitacion(){ return {}; }