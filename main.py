from busqueda import Busqueda
from laberinto import cv2

mapa = cv2.imread('laberinto.png', 1)
bus = Busqueda(mapa)

''' title = 'Busqueda en Amplitud'
[resultado,costo] = bus.busquedaAmplitud() '''

''' title = 'Busqueda en Profundidad'
[resultado,costo] = bus.busquedaProfundidad() '''

title = 'Busqueda Primero el Mejor'
[resultado,costo] = bus.primero_el_mejor()

''' title = 'Busqueda A estrella'
[resultado,costo] = bus.a_estrella() '''

costo_str = 'Costo del camino: ' + str(costo) 

# redimensionar la imagen
scale_percent = 200
width = int(resultado.shape[1] * scale_percent / 100)
height = int(resultado.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(resultado, dim, interpolation = cv2.INTER_AREA)

resized = cv2.putText(resized, costo_str ,(368,374), cv2.FONT_HERSHEY_PLAIN, 
                      1, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow(title,resized)
cv2.waitKey(0)
cv2.destroyAllWindows()