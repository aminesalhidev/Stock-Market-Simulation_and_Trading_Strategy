# Simulazione del Mercato Azionario e Strategia di Trading

Questo repository contiene una semplice implementazione di una simulazione del mercato azionario con una strategia di trading basata sulle fluttuazioni dei prezzi delle azioni. L'obiettivo è simulare gli aggiornamenti dei prezzi delle azioni, generare segnali di trading e testare una strategia di trading di base.

## Caratteristiche

### Classe Azione

La classe `Azione` rappresenta un'azione e include:

- **Attributi**:
  - `nome`: Il nome dell'azione (es. "Apple").
  - `simbolo`: Il simbolo dell'azione (es. "AAPL").
  - `price`: Il prezzo attuale dell'azione.

- **Metodi**:
  - `Aggiorna_prezzo()`: Aggiorna casualmente il prezzo dell'azione a intervalli regolari per simulare le fluttuazioni del mercato.
  - `Variazione_percentuale()`: Tramite una formula avremo il prezzo in % in base all'aumento della Azione o al suo decremento.

### Funzioni

1. **crea_azioni(numero_azioni)**: Consente la creazione la creazione de
2. **mostea_azioni(azioni)**: Mostra le azioni e i prezzi correnti di tutte le azioni nel mercato.
3. **segnale_acquisto(azioni)**: Restituisce `True` se il prezzo dell'azione è aumentato di una certa percentuale dall'ultimo aggiornamento, indicando un segnale di acquisto.
4. **segnale_vendita(Azioni)**: Restituisce `True` se il prezzo dell'azione è aumentato , tramite il controllo condizionale noi andiamo a vendere solamente se l' `azione.prezzo > prezzo.acquisto` in caso fosse `True` si procede alla vendita dell'azione.
5. **simula_strategia_trading(azioni, saldo_iniziale=100, giorni=2)**: Simula il trading per il numero di giorni specificato utilizzando i segnali di acquisto e vendita. Monitora il portafoglio e il saldo durante la simulazione e restituisce i risultati finali.

## Installazione

Per iniziare, clona questo repository e naviga nella cartella del progetto.

```bash
git clone https://github.com/aminesalhidev/Stock-Market-Simulation_and_Trading_Strategy
cd Stock-Market-Simulation_and_Trading_Strategy
