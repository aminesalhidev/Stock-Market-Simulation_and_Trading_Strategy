import random

class Azione:
    
    def __init__(self, nome, simbolo, prezzo):
        
        # self viene usato all'interno di una classe nei metodi di istanza per la creazione di un oggetto
        self.nome = nome
        self.simbolo = simbolo
        self.prezzo = prezzo
        self.prezzo_precedente = prezzo
    

    def aggiorna_prezzo(self):
        
        """
        funzione che Aggiorna Il Prezzo dell'azione in modo casualmente.
        """
        self.prezzo_precedente = self.prezzo
        self.prezzo = round(self.prezzo * random.uniform(0.9, 1.1), 2)

    def variazione_percentuale(self):
        
        """
        Calcola la variazione percentuale del prezzo rispetto all'aggiornamento precedente.
        """
        return round(((self.prezzo - self.prezzo_precedente) / self.prezzo_precedente) * 100, 2)


# ci fu la creazione di una funzione di nome :
def crea_azioni(numero_azioni):
    
    azioni = []  # ci fu la creazione di una lista.
    for i in range(numero_azioni):
        nome = f"Azione_{i + 1}"
        simbolo = f"SYM{i + 1}"
        prezzo = round(random.uniform(10, 100), 2)
        azioni.append(Azione(nome, simbolo, prezzo)) # aggiugi i seguenti dati.
    return azioni


def mostra_mercato_azioni(azioni):
    print("Mostrazione delle azioni del mercato :" )
    for azione in azioni:
        print(f"{azione.nome} ({azione.simbolo}): {azione.prezzo} EURO")


def segnale_acquisto(azione):
    
    if azione.variazione_percentuale() >= 5:
        print(f"Segnale di acquisto: il prezzo di {azione.nome} è aumentato del 5% o più.")   
        return True # True Pass
    return False


def segnale_vendita(azione, prezzo_acquisto): 
    if azione.prezzo > prezzo_acquisto:
        print(f"Segnale di vendita: il prezzo di {azione.nome} è superiore al prezzo di acquisto ({azione.prezzo} > {prezzo_acquisto}).")
        return True
    else:
        print(f"Non vendo {azione.nome}: il prezzo attuale ({azione.prezzo}) è inferiore o uguale al prezzo di acquisto ({prezzo_acquisto}).")
    return False


def simula_strategia_trading(azioni, saldo_iniziale, giorni):
    
    saldo = saldo_iniziale
    portafoglio = {}  
    prezzi_acquisto = {}  
   
    for giorno in range(1, giorni + 1):
        print(f"\nGiorno {giorno}:")  
          
        for azione in azioni:
            azione.aggiorna_prezzo()
            print(f"{azione.nome}: {azione.prezzo} EUR ({azione.variazione_percentuale()}%)")

           #rcf
            if segnale_acquisto(azione): 
                
                if saldo >= azione.prezzo: # cds
                    saldo -= azione.prezzo #sds
                    portafoglio[azione.nome] = portafoglio.get(azione.nome, 0) + 1  
                  
                   
                    if azione.nome in prezzi_acquisto:                              
                            # Aggiorna il prezzo medio di acquisto 50 (seconda volta)
                            totale_speso = prezzi_acquisto[azione.nome] * (portafoglio[azione.nome] - 1) + azione.prezzo
                            prezzi_acquisto[azione.nome] = totale_speso / portafoglio[azione.nome]
                   
                    else: 
                        # PASS
                        prezzi_acquisto[azione.nome] = azione.prezzo
                        print(f"Comprata 1 azione di {azione.nome} al prezzo di: {azione.prezzo} Di Euro")
                        print("Il saldo e stato sottratto ed ora sta a : ", saldo, "EURO")
                           
                        
            elif azione.nome in portafoglio and portafoglio[azione.nome] > 0:                   
               if segnale_vendita(azione, prezzi_acquisto[azione.nome]):            
                    # Vendi un'azione
                    saldo += azione.prezzo
                    # quando vendo un'azione
                    portafoglio[azione.nome] -= 1
                    print(f"Venduta 1 azione di {azione.nome} a {azione.prezzo} EUR") 
                    
                    # Rimuovi dal portafoglio se non ne restano più
                    if portafoglio[azione.nome] == 0:
                        del prezzi_acquisto[azione.nome]
                        

    print("\n--- Strategia di Trading Completata ---")
    print(f"Saldo finale: {saldo:.2f} EUR")
    
    print("Portafoglio finale:")
    for nome, quantita in portafoglio.items():
        if quantita > 0:
            print(f"{nome}: {quantita} azioni (prezzo medio di acquisto: {prezzi_acquisto[nome]:.2f} EUR)")


# Esempio di utilizzo
azioni = crea_azioni(1) 
mostra_mercato_azioni(azioni)
simula_strategia_trading(azioni, saldo_iniziale=100, giorni=2)
