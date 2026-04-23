# CREATIVE LOOP DYNAMICS: Thermodynamic Homeostasis in Generative AI

**Autore:** Massimiliano Gasparini ([ORCID: 0009-0004-4216-4852](https://orcid.org/0009-0004-4216-4852))  
**Preprint Reference (Zenodo):** [DOI: 10.5281/zenodo.19500843](https://doi.org/10.5281/zenodo.19500843)

## 1. Executive Summary: The Model Autophagy Disorder (MAD)
Questo repository contiene l'implementazione matematica e le simulazioni in Python del framework **Creative Loop**. L'architettura dimostra formalmente che il degrado della varianza informazionale nei Large Language Models (LLM) ricorsivi non è un errore statistico transitorio, ma un collasso strutturale governato da una **Biforcazione Nodo-Sella**.

Il codice modella l'interazione tra informazione umana originale ($h$) e informazione sintetica ($s$) attraverso un sistema di equazioni differenziali accoppiate (Lotka-Volterra e Gompertz), dimostrando la necessità topologica di un "Walled Garden" crittografico per ripristinare l'omeostasi termodinamica tramite algoritmi di scoperta sparsa e filtraggio stocastico.

## 2. Mathematical Framework: Il Modello h-s
L'evoluzione dell'ecosistema informativo è governata dalle seguenti ODE:

* **Dinamica Umana (h):** $\frac{dh}{dt} = \alpha h\left(1 - \frac{h}{K_h}\right) - \beta hs + \phi$
* **Dinamica Sintetica (s):** $\frac{ds}{dt} = \gamma s \ln\left(\frac{K_s}{s}\right) - \lambda sh$

La stabilità del sistema dipende in modo critico dal mantenimento dell'iniezione esogena $\phi$ al di sopra della soglia di biforcazione analitica $\phi_{crit}$.

## 3. The Thermodynamic Engine: La Metrica Bit/Watt
Per operazionalizzare il controllo e prevenire l'ingestione di rumore sintetico (Data Laundering), il framework abbandona il "token" come unità di misura, introducendo la **Densità Negentropica Specifica ($V$)**:

$$V = \frac{\Delta N}{P}$$

Dove $\Delta N$ è la variazione di entropia di Shannon-Brillouin (novità irriducibile) e $P$ è la potenza metabolica o elettrica (Joule/secondo) spesa per la generazione. L'enorme asimmetria termodinamica tra i substrati permette la costruzione di un filtro passa-alto inespugnabile a protezione del database di addestramento.

## 4. Integrazione Algoritmica: SINDy + EKF
Il repository estende l'applicazione del framework SINDy (Sparse Identification of Nonlinear Dynamics) combinato con l'Extended Kalman Filter (EKF), come teorizzato da *Rosafalco et al. (2025)* per i sistemi meccanici biforcanti.
Nel contesto del Creative Loop, l'integrazione SINDy+EKF agisce come Demone di Maxwell:
1. **SINDy:** Identifica offline la cinematica sparsa delle popolazioni informative.
2. **EKF:** Aggiorna online i coefficienti del modello tramite assimilazione dati nel Walled Garden, tracciando in tempo reale il *Critical Slowing Down* della Matrice Jacobiana prima dell'innesco irreversibile dell'autofagia.

## 5. Struttura del Repository
* `/diagrams/`: Script Python per la generazione dei ritratti di fase, delle dinamiche vettoriali e del diagramma di biforcazione Nodo-Sella.
* `/simulations/`: Simulatori numerici delle dinamiche termodinamiche del Creative Loop e logica dell'interruttore passa-alto (Filtro Bit/Watt).

## 6. Riferimenti Bibliografici Principali
1. **Gasparini, M. (2026).** *CREATIVE LOOP: Dinamiche di Replicazione Informazionale e Stabilità nei Sistemi Generativi Ricorsivi.* Zenodo. DOI: 10.5281/zenodo.19500843.
2. **Rosafalco, L., Conti, P., Manzoni, A., Mariani, S., Frangi, A. (2025).** *Online learning in bifurcating dynamic systems via SINDy and Kalman filtering.* Nonlinear Dyn 113, 14201–14221. DOI: 10.1007/s11071-025-11029-y.

## Copyright e Licenza
© 2026 Massimiliano Gasparini. Rilasciato sotto licenza [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/). Tutti i diritti riservati sull'impianto teorico e le topologie di simulazione.
