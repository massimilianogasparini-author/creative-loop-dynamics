"""
THERMODYNAMIC FILTER (Bit/Watt)
-------------------------------
Autore: Massimiliano Gasparini (ORCID: 0009-0004-4216-4852)
DOI: 10.5281/zenodo.19500843

Modulo per il calcolo della Densità Negentropica Specifica (V = N/P).
Agisce come Interruttore Passa-Alto per prevenire il Data Laundering e il 
conseguente Model Autophagy Disorder (MAD) nel dataset di addestramento.
"""

class ThermodynamicFilter:
    def __init__(self, threshold=1.0):
        """
        Inizializza il filtro con la soglia critica di Bit/Watt.
        """
        self.threshold = threshold

    @staticmethod
    def calculate_density(delta_n, power):
        """
        Calcola il Volume Informazionale Termodinamico.
        delta_n: Negentropia (Bit di Shannon-Brillouin)
        power: Potenza metabolica o elettrica spesa (Watt = Joule/secondo)
        """
        safe_power = max(power, 1e-9) # Evita divisioni per zero
        volume_thermodynamic = delta_n / safe_power
        return volume_thermodynamic

    def training_gate(self, delta_n, power):
        """
        L'Interruttore Passa-Alto. 
        Restituisce True (Ingestione Permessa) solo se il dato supera la soglia termodinamica.
        """
        v = self.calculate_density(delta_n, power)
        
        if v >= self.threshold:
            return True, v   # Dato validato per il ciclo di addestramento IA successivo
        else:
            return False, v  # Dato scartato (Rischio MAD rilevato)
