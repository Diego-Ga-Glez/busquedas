from random import shuffle
import cv2

class Laberinto:
    def __init__(self,mapa):
        self.mapa = mapa
        self.inicio = (185,12)
        self.meta = (21,277)
        
        self.arriba = (-1, 0)
        self.abajo = (1, 0)
        self.izq = (0, -1)
        self.der = (0, 1)
        self.movimientos = [self.arriba, self.abajo, self.der, self.izq]
        shuffle(self.movimientos)

    def mover(self,direccion, posicion):
        #Se suma la posición actual con la direccion para la nueva posición
        # [y,x]
        nuevaPos = (posicion[0] + direccion[1],posicion[1] + direccion[0])
        
        #Posición no valida
        if (self.mapa[nuevaPos[0]][nuevaPos[1]] == [0,0,0]).all():
                return False

        return nuevaPos

    def revisar(self, posicion):
        if posicion == self.meta:
            return True     
        return False

    def recorrido_inv(self,recorrido):
        i = -1
        costo = 0
        while recorrido[i][0] != self.inicio:
            aux = recorrido[i][0]
            self.mapa = cv2.circle(self.mapa,(aux[1],aux[0]),radius=0,color=(255, 0, 0),thickness=1)
            costo +=1
            i = recorrido[i][1]

        return [self.mapa,costo]