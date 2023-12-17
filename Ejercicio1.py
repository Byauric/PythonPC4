
ruta_archivo = './archivo.txt'
with open(ruta_archivo, mode='r') as archivo:
    data = archivo.read()
    contador_la = data.lower().count('la')

print(f'La palabra "la" aparece {contador_la} veces en el archivo.')

nuevo_texto = input('Ingrese un texto para agregar al final del archivo: ')

with open(ruta_archivo, 'a') as archivo:
    archivo.write('\n' + nuevo_texto)

print('Texto agregado al final del archivo.')
