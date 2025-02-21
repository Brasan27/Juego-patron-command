#RECEPTOR
#es nuestro tablero de juego con 5 valores: dimensiones, posición y aspecto (G o P)
#tamaño 9x9, posición (4, 4) y aspecto G
juego = [9, 9, 4, 4, 'G']

#COMANDOS
#para subir disminuimos la fila en una unidad (posición mínima 0)
def subir(juego):
	juego[2] = juego[2]-1 if juego[2] > 0 else 0

#para bajar aumentamos la fila en una unidad (posición máxima es dimensión máxima)
def bajar(juego):
	juego[2] = juego[2]+1 if juego[2] < juego[0] - 1 else juego[0] - 1

#para ir a la izquierda disminuimos la columna en una unidad (posición mínima 0)
def izquierda(juego):
	juego[3] = juego[3]-1 if juego[3] > 0 else 0

#para ir a la derecha aumentamos la columna en una unidad (posición máxima es dimensión máxima)
def derecha(juego):
	juego[3] = juego[3]+1 if juego[3] < juego[1] - 1  else juego[1] - 1

def cambiar_aspecto(juego):
	juego[4] = 'P' if juego[4] == 'G' else 'G'

#guardamos el estado del juego en un fichero para recuperarlo cuando queramos
def guardar(juego):
	with open('juego.txt','w') as fichero:
		for elemento in juego:
			fichero.write(str(elemento))
			fichero.write('\n')

#cargamos el juego guardado en fichero
def cargar(juego):
	with open('juego.txt', 'r') as fichero:
		leido = fichero.readlines()
	for i in range(0,4):
		juego[i] = int(leido[i][:-1])
	juego[4] = leido[4][:-1]

#ubicamos los comandos en un diccionario para acceder a ellos cómodamente
comandos = {'S':subir,
				'B':bajar,
				'I':izquierda,
				'D':derecha,
				'A':cambiar_aspecto,
				'G':guardar,
				'C':cargar}

#INVOCADOR
#en este caso es una función que recibe el comando a ejecutar y lo ejecuta
def controlador(comando, juego):
	comando(juego)
 
 #añadimos una funcione que dibuje el estado de juego por pantalla
def dibujar_juego(juego):
	print(' * Estado del juego:', juego)
	print()
	for fila in range(0, juego[0]):
		for columna in range(0, juego[1]):
			if fila == juego[2] and columna == juego[3]:
				print(' '+juego[4], end='')
			else:
				print(' ·', end='')
		print()
	print()


#función para la selección del comando
def solicitar_comando():
    print('Esperando entrada del usuario...')
    valor = input('Introduzca un comando '+str(list(comandos.keys()))+' (otro para terminar): ')
    return comandos[valor] if valor in comandos.keys() else None


while True:
    print("Iterando...")
    dibujar_juego(juego)
    comando = solicitar_comando()
    if not comando:
        break
    controlador(comando, juego)
