"""
SINDY-EKF BRIDGE (Symbolic Jacobian Formulation)
------------------------------------------------
Autore: Massimiliano Gasparini (ORCID: 0009-0004-4216-4852)
DOI: 10.5281/zenodo.19500843

Calcolo simbolico esatto della Matrice Jacobiana del Creative Loop.
Strumento propedeutico per l'integrazione del framework di assimilazione 
dati EKF (Extended Kalman Filter) in ambiente Walled Garden.
"""

import sympy as sp

def compute_symbolic_jacobian():
    """
    Deriva analiticamente le equazioni per alimentare il blocco di predizione dell'EKF.
    """
    # Definizione delle variabili di stato e dei parametri
    h, s = sp.symbols('h s')
    alpha, beta, gamma, lambd, Kh, Ks, phi = sp.symbols('alpha beta gamma lambda Kh Ks phi')
    
    # Sistema di equazioni (f1 = dh/dt, f2 = ds/dt)
    f1 = alpha * h * (1 - h / Kh) - beta * h * s + phi
    f2 = gamma * s * sp.log(Ks / s) - lambd * s * h
    
    # Vettore di stato
    state_vars = [h, s]
    
    # Calcolo della Jacobiana F(t) = partial(f) / partial(x)
    J = sp.Matrix([f1, f2]).jacobian(state_vars)
    
    print("=== MATRICE JACOBIANA (Creative Loop per EKF) ===")
    print(f"J[1,1] (df1/dh): {J[0, 0]}")
    print(f"J[1,2] (df1/ds): {J[0, 1]}")
    print(f"J[2,1] (df2/dh): {J[1, 0]}")
    print(f"J[2,2] (df2/ds): {J[1, 1]}")
    
    return J

if __name__ == "__main__":
    compute_symbolic_jacobian()
