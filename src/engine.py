"""
CREATIVE LOOP ENGINE
--------------------
Autore: Massimiliano Gasparini (ORCID: 0009-0004-4216-4852)
DOI: 10.5281/zenodo.19500843

Modulo per l'integrazione numerica delle equazioni differenziali ordinarie (ODE) 
che governano le dinamiche informazionali h-s (Lotka-Volterra e Gompertz).
"""

import numpy as np
from scipy.integrate import odeint

class CreativeLoopEngine:
    def __init__(self, alpha=0.05, beta=0.0005, gamma=1.5, lambd=0.01, Kh=500.0, Ks=5.0, phi=0.5):
        """
        Inizializza i parametri termodinamici del Walled Garden.
        """
        self.alpha = alpha   # Rigenerazione Umana
        self.beta = beta     # Interferenza Autòfaga (Tossicità)
        self.gamma = gamma   # Efficienza Replicativa Sintetica
        self.lambd = lambd   # Inibizione da RLHF Umano
        self.Kh = Kh         # Capacità Portante Umana
        self.Ks = Ks         # Capacità Portante Sintetica
        self.phi = phi       # Iniezione di Omeostasi (Lavoro)

    def system_equations(self, y, t):
        """
        Definisce il sistema di ODE accoppiate.
        """
        h, s = y
        s_safe = max(s, 1e-9) # Prevenzione divergenza logaritmica
        
        # Dinamica dell'Informazione Umana
        dh_dt = self.alpha * h * (1 - h / self.Kh) - self.beta * h * s + self.phi
        
        # Dinamica dell'Informazione Sintetica
        ds_dt = self.gamma * s * np.log(self.Ks / s_safe) - self.lambd * s * h
        
        return [dh_dt, ds_dt]

    def simulate(self, h_init, s_init, time_steps=2000, t_max=150):
        """
        Esegue l'integrazione numerica nel dominio del tempo.
        Restituisce il vettore temporale e la matrice dei risultati [h, s].
        """
        t = np.linspace(0, t_max, time_steps)
        y0 = [h_init, s_init]
        sol = odeint(self.system_equations, y0, t)
        return t, sol
