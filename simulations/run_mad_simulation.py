"""
SIMULAZIONE COMPARATIVA: Open Web (MAD) vs Sandbox Crittografica (Creative Loop)
-------------------------------------------------------------------------------
Autore: Massimiliano Gasparini (ORCID: 0009-0004-4216-4852)

Questo script richiama il motore cinematico e dimostra l'efficacia del
filtro termodinamico. Genera due scenari:
1. Open Web: Nessun filtro, inquinamento tossico, collasso.
2. Sandbox: Filtro termodinamico attivo, inquinamento abbattuto, omeostasi.
"""

import sys
import os
import matplotlib.pyplot as plt

# Aggiunge la cartella 'src' al path per poter importare il motore
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from engine import CreativeLoopEngine

def run_comparative_simulation():
    # SCENARIO 1: OPEN WEB (Collasso MAD)
    # Alta tossicità (beta), alta velocità IA (gamma), nessuna restrizione
    open_web_engine = CreativeLoopEngine(
        alpha=0.05, beta=0.05, gamma=2.0, lambd=0.01, Kh=100.0, Ks=100.0, phi=0.5
    )
    t_web, sol_web = open_web_engine.simulate(h_init=10.0, s_init=5.0, t_max=100)
    h_web, s_web = sol_web[:, 0], sol_web[:, 1]

    # SCENARIO 2: SANDBOX TERMODINAMICA
    # Filtro Bit/Watt attivo: Tossicità quasi nulla (beta), IA relegata a Kh bassi, umano domina
    sandbox_engine = CreativeLoopEngine(
        alpha=0.05, beta=0.0005, gamma=1.5, lambd=0.01, Kh=500.0, Ks=5.0, phi=0.5
    )
    t_box, sol_box = sandbox_engine.simulate(h_init=10.0, s_init=0.1, t_max=100)
    h_box, s_box = sol_box[:, 0], sol_box[:, 1]

    # Renderizzazione del Confronto
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle('Test di Validazione Architetturale: Creative Loop vs MAD', fontsize=16, fontweight='bold')

    # Grafico 1: Open Web
    ax1.plot(t_web, h_web, color='#000080', linewidth=2.5, label='Informazione Umana (h)')
    ax1.plot(t_web, s_web, color='#B22222', linewidth=2.5, label='Informazione Sintetica (s)')
    ax1.set_title('Scenario A: Open Web (Nessun Filtro Termodinamico)')
    ax1.set_xlabel('Tempo')
    ax1.set_ylabel('Volume Informazionale')
    ax1.axhline(y=0, color='black', linewidth=1)
    ax1.fill_between(t_web, 0, 100, color='red', alpha=0.05, label='Autofagia MAD Irreversibile')
    ax1.legend()
    ax1.grid(True, linestyle=':', alpha=0.7)

    # Grafico 2: Sandbox
    ax2.plot(t_box, h_box, color='#000080', linewidth=2.5, label='Densità Umana (h) [Bit/Watt]')
    ax2.plot(t_box, s_box, color='#B22222', linewidth=2.5, label='Densità Sintetica (s) [Bit/Watt]')
    ax2.set_title('Scenario B: Walled Garden (Filtro Bit/Watt Attivo)')
    ax2.set_xlabel('Tempo')
    ax2.set_ylabel('Densità Termodinamica')
    ax2.fill_between(t_box, 0, 500, color='green', alpha=0.05, label='Omeostasi Simbiotica')
    ax2.legend()
    ax2.grid(True, linestyle=':', alpha=0.7)

    plt.tight_layout()
    plt.savefig('confronto_termodinamico.png', dpi=300)
    print("Simulazione completata. Grafico di confronto generato.")

if __name__ == "__main__":
    run_comparative_simulation()
