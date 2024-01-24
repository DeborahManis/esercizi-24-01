import numpy as np

li = [132, 2546, 895, 2356]
ar = np.array(li)
print(type(li), type(ar))

print(np.arange(-10, 10, 2))
print(np.linspace(0,100, 10))
print(ar.min())

mat = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]] # e' una matrice
elemento= mat  [2] [0] # vogliamo accedere alla 3 riga e al primo elemento
print(elemento)

# trasformiamo la lista in un array
mat = np.array(mat)
# accediamo ad un elemento
elemento = mat [2, 0]
print(elemento)
#Quante dimensioni ha il nuovo array? Come facciamo per accedere ai singoli elementi?
linear_data = np.array([x for x in range(27)])
reshaped_data = linear_data.reshape((3, 3, 3))
print(reshaped_data)
num_dimensioni = reshaped_data.ndim
print("Numero di dimensioni:", num_dimensioni)
elemento = reshaped_data [0, 1, 1]
print(elemento)
print(reshaped_data.shape)

# calcola la distanza
lunghezza_stuttura = 28.75
travetti = 15
distanza_travetti = lunghezza_stuttura / travetti
posizione = np.arange( 0, lunghezza_stuttura + 0.1, distanza_travetti)
print(posizione)

# 
matrice = [1, 1, 1, 1], [5, 1, 1, 1], [20, -4, 0, 42]
print(matrice)
matrice = np.array(matrice)

#
matrice2 = np.array([[10, 22, 21, 8, 9],[9, 42, 3, 18, 11], [5, 4, 30, 12, 29],[37, 31, 7, 2, 26],[8, 6, 4, 33, 1]])
min_valore = np.min(matrice2)
print (min_valore)
max_valore = np.max(matrice2)
print(max_valore)
risultato1 = (matrice2 - min_valore) / (max_valore - 2)
print(matrice2)
print(risultato1)

