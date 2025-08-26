numeros={
    0:  [1, 1, 1, 1, 1, 1, 0],
    1:  [0, 1, 1, 0, 0, 0, 0],
    2:  [1, 1, 1, 0, 1, 0, 1],
    3:  [1, 1, 1, 1, 0, 0, 1],
    4:  [0, 1, 1, 0, 0, 1, 1],
    5:  [1, 1, 1, 1, 0, 1, 1],
    6:  [1, 0, 1, 1, 1, 1, 1],
    7:  [1, 0, 1, 0, 0, 1, 1],
    8:  [1, 1, 1, 1, 1, 1, 1],
    9:  [1, 1, 1, 0, 0, 1, 1],   
}
for numero in numeros:
    datos = numeros[numero]
    print(f"Numero {numero} = A={datos[0]} B={datos[1]} C={datos[2]} D={datos[3]} E={datos[4]} F={datos[5]} G={datos[6]}  ")
