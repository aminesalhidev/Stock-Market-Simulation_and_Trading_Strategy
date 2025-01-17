# Simulazione del Mercato Azionario e Strategia di Trading

Questo repository contiene una semplice implementazione di una simulazione del mercato azionario con una strategia di trading basata sulle fluttuazioni dei prezzi delle azioni. L'obiettivo è simulare gli aggiornamenti dei prezzi delle azioni, generare segnali di trading e testare una strategia di trading di base.

## Caratteristiche

### Classe Stock

La classe `Stock` rappresenta un'azione e include:

- **Attributi**:
  - `name`: Il nome dell'azione (es. "Apple").
  - `symbol`: Il simbolo dell'azione (es. "AAPL").
  - `price`: Il prezzo attuale dell'azione.

- **Metodi**:
  - `updatePrice()`: Aggiorna casualmente il prezzo dell'azione a intervalli regolari per simulare le fluttuazioni del mercato.

### Funzioni

1. **createStocks(num_stocks)**: Crea `num_stocks` istanze della classe `Stock` con nomi, simboli e prezzi iniziali casuali.
2. **displayStockMarket(stocks)**: Mostra i prezzi correnti di tutte le azioni nel mercato.
3. **buySignal(stock)**: Restituisce `True` se il prezzo dell'azione è aumentato di una certa percentuale dall'ultimo aggiornamento, indicando un segnale di acquisto.
4. **sellSignal(stock)**: Restituisce `True` se il prezzo dell'azione è diminuito di una certa percentuale dall'ultimo aggiornamento, indicando un segnale di vendita.
5. **testTradingStrategy(stocks, initial_balance, num_days)**: Simula il trading per il numero di giorni specificato utilizzando i segnali di acquisto e vendita. Monitora il portafoglio e il saldo durante la simulazione e restituisce i risultati finali.

## Installazione

Per iniziare, clona questo repository e naviga nella cartella del progetto.

```bash
git clone https://github.com/aminesalhidev/Stock-Market-Simulation_and_Trading_Strategy
cd Stock-Market-Simulation_and_Trading_Strategy
