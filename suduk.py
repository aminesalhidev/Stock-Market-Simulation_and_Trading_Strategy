



# La griglia del Sudoku, dove 0 rappresenta una cella vuota
from treding import Azione


griglia = [ [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]]
 
 
 
 # Controllo
def valido(griglia, num, posizione):          
  
    # Verifica che il numero non sia già presente nella stessa riga
    for i in range(len(griglia[0])): 
        if griglia[posizione[0]][i] == num and posizione[1] != i:
            return False

    for i in range(len(griglia)):
        if griglia[i][posizione[1]] == num and posizione[0] != i: 
            return False

    quadrante_x = posizione[1] // 3 
    quadrante_y = posizione[0] // 3  

    # Verifica le celle d'intorno
    for i in range(quadrante_y * 3, quadrante_y * 3 + 3):  # righe
        for j in range(quadrante_x * 3, quadrante_x * 3 + 3):  # colonne
            if griglia[i][j] == num and (i, j) != posizione:  # quadrante
                return False

    return True  # Se tutte le condizioni sono soddisfatte, il numero è valido




# Funzione per stampare la griglia di Sudoku

def stampa_griglia(griglia):
    for i in range(len(griglia)):  
        if i % 3 == 0 and i != 0:  
            print("- - - - - - - - - - - - - ")
        for j in range(len(griglia[1])):  # le colonne
            if j % 3 == 0 and j != 0:  # Aggiunge una linea separatrice ogni 3 colonne
                print(" | ", end="")
            if j == 8:
                print(griglia[i][j])  # Stampa l'ultimo valore della riga
            else :
                print(str(griglia[i][j]) + " ", end="")  # Stampa il numero con uno spazio
 

# Funzione per trovare la prima cella vuota (con valore 0)
def trova_vuoto(griglia):    
    for i in range(len(griglia)):          
        for j in range(len(griglia[0])):  
            if griglia[i][j] == 0:  
                return (i, j)  
    return None  # Se non ci sono celle vuote, ritorna None
 
 
# Start Programming ()
def risolvi(griglia):
    trova = trova_vuoto(griglia)  
    if not trova:  
        return True # Soduk risolto.
    else:
        riga, colonna = trova 
    
    for i in range(1, 10): # contatore da 1 a 10
        if valido(griglia, i, (riga, colonna)):  #afuControllo
            griglia[riga][colonna] = i  # inserisco il in numero nella colonna
            if risolvi(griglia):  # richiama la funzione finche non risolve tutto il sudok.
                return True
            griglia[riga][colonna] = 0  
    return False  # Se nessun numero funziona, ritorna False


# Funzione principale
print("Stampa della griglia iniziale:")
stampa_griglia(griglia)  # Stampa la griglia iniziale


# Risolviamo il Sudoku
risolvi(griglia)
print("Abbiamo risolto la griglia Sudoku!")
print("Griglia risolta: ")
stampa_griglia(griglia)  # Stampa la griglia risolta
