import random

class Azione:
    
    def __init__(self, nome, simbolo, prezzo):  

        self.nome = nome
        self.simbolo = simbolo
        self.prezzo = prezzo
        self.prezzo_precedente = prezzo
        
    def aggiorna_prezzo(self):
        self.prezzo_precedente = self.prezzo
        self.prezzo = round(self.prezzo * random.uniform(0.9, 1.1), 2)
        
    def variazione_percentuale(self):
        return round(((self.prezzo - self.prezzo_precedente) / self.prezzo_precedente) * 100, 2)
    
    @staticmethod  
    
    def crea_azione(numero_azioni):
        
        azioni = []
        
        for i in range(numero_azioni):
            nome = f"Azione_{i + 1}"
            simbolo = f"Simbolo_{i + 1}"
            prezzo = round(random.uniform(10, 100), 2)
            azioni.append(Azione(nome, simbolo, prezzo))
        return azioni

    def mostra_mercato_azioni(azioni):
        print("Mercato Azionario Italiano: ")
        for azione in azioni:  
            print(f"{azione.nome} ({azione.simbolo}): {azione.prezzo} Euro")


    def segnale_acquisto(self):
        if self.variazione_percentuale() >= 5:
            print(f"Segnale di Acquisto per : {self.nome} ({self.simbolo}) a {self.prezzo} EUR")
            return True
        return False


    def segnale_vendita(self):
        if self.variazione_percentuale() <= -5:
            print(f"Segnale di Vendita per : {self.nome} ({self.simbolo}) a {self.prezzo} EUR")
            return True
        return False


# Funzione per simulare la strategia di trading
def simula_strategia_trading(azioni, saldo_iniziale, giorni):
    saldo = saldo_iniziale
    portafoglio = {}
    
    for giorno in range(1, giorni + 1):
        print(f"\nGiorno {giorno}:")
        for azione in azioni:
            azione.aggiorna_prezzo()  # Aggiorna il prezzo
            print(f"{azione.nome}: {azione.prezzo} EUR ({azione.variazione_percentuale()}%)")
            
            # Verifica segnale di acquisto
            if azione.segnale_acquisto():  # Chiamata corretta tramite l'istanza di azione
                if saldo >= azione.prezzo:
                    saldo -= azione.prezzo
                    portafoglio[azione.nome] = portafoglio.get(azione.nome, 0) + 1
                    print(f"Comprata 1 azione di {azione.nome} a {azione.prezzo} EUR")
            
           
            # Verifica segnale di vendita
            elif azione.segnale_vendita():  # Chiamata corretta tramite l'istanza di azione
                if portafoglio.get(azione.nome, 0) > 0:
                    saldo += azione.prezzo
                    portafoglio[azione.nome] -= 1
                    print(f"Venduta 1 azione di {azione.nome} a {azione.prezzo} EUR")
        
     
        # Stampa il portafoglio alla fine di ogni giorno
        print("\nPortafoglio attuale:")
        for nome_azione, quantita in portafoglio.items():
            print(f"{nome_azione}: {quantita} azioni")
        print(f"Saldo rimanente: {saldo} EUR")
        
    return saldo, portafoglio


# Creazione delle azioni
azioni = Azione.crea_azione(2)
mostra_mercato_azioni(azioni)

# Simuliamo la strategia di trading
saldo_iniziale = 1000  
giorni = 2 # Numero di giorni per la simulazione
saldo_finale, portafoglio_finale = simula_strategia_trading(azioni, saldo_iniziale, giorni)

print("\nSimulazione terminata:")
print(f"Saldo finale: {saldo_finale} EURO")
for nome_azione, quantita in portafoglio_finale.items():
    print(f"{nome_azione}: {quantita} azioni")
