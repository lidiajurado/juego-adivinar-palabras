#JUEGO REALIZADO POR ÁNGELA TRENAS Y LIDIA JURADO
import random

#Definición de listas
lista=["koala","perro","gallo","zorro","cerdo","burro","yegua","raton","cabra","oveja","mosca","piojo",
       "gamba","pollo","tigre","panda","llama","cebra","pulpo","huron"]

palabra = random.choice(lista)

#Bucle principal
print("¡Bienvenido al juego de adivinar animales con cinco letras!")
print("Debes de escoger una de estas palabras:")
print ("¡Mucha suerte!")
print(lista)
ganar = False
for i in range(1,6):
    intento = input("Di un animal con cinco letras:")
    if (palabra== intento):
      ganar = True
      break
    else:
      print("Te quedan " + str(5 - i) + " intentos, sigue intentándolo")
    
#Fin del juego  
if ganar == True:
  print("Enhorabuena,¡has ganado!")
else:
  print("Has perdido,inténtalo de nuevo")
  print("La palabra era:" + (palabra))

