from collections import deque
from copy import deepcopy
from laberinto import Laberinto

class Busqueda(Laberinto):
    def __init__(self, mapa):
        super().__init__(mapa)
   
    def manhattan_heuristica(self, posicion):
        y = abs(posicion[0] - self.meta[0])
        x = abs(posicion[1] - self.meta[1])
        return y + x

    def costo_camino(self,padre, recorrido):
        costo = 1
        i = padre
        while recorrido[i][0] != self.inicio:
            i = recorrido[i][1]
            costo += 1
        return costo

    def manhattan_heuristica(self, posicion):
        y = abs(posicion[0] - self.meta[0])
        x = abs(posicion[1] - self.meta[1])
        return y + x
    
    def a_estrella(self):
        visitados = []
        cola_de_prioridad = []
        recorrido = []
        copia_inicio = deepcopy(self.inicio)
    
        visitados.append(copia_inicio) #[nodo]
        cola_de_prioridad.append([copia_inicio, None, 0]) #[nodo, padre, heuristica]

        while len(cola_de_prioridad) > 0: 
            nuevaPos = cola_de_prioridad.pop(0)
            recorrido.append(nuevaPos)

            if self.revisar(nuevaPos[0]):
                return self.recorrido_inv(recorrido)

            adyacentes = []
            for direccion in self.movimientos:
                ady = self.mover(direccion,deepcopy(nuevaPos[0]))
                if ady != False:
                    adyacentes.append(ady)

            for ady in adyacentes:
                if ady not in visitados:
                    visitados.append(ady)
                    n = self.costo_camino(len(recorrido)-1, recorrido)
                    h = self.manhattan_heuristica(ady)
                    f =  h + n
                    cola_de_prioridad.append([ady, len(recorrido)-1, f])

            cola_de_prioridad = sorted(cola_de_prioridad, key=lambda cola:cola[2])
    
    def primero_el_mejor(self):
        visitados = []
        cola_de_prioridad = []
        recorrido = []
        copia_inicio = deepcopy(self.inicio)
    
        visitados.append(copia_inicio) #[nodo]
        cola_de_prioridad.append([copia_inicio, None, 0]) #[nodo, padre, heuristica]

        while len(cola_de_prioridad) > 0: 
            nuevaPos = cola_de_prioridad.pop(0)
            recorrido.append(nuevaPos)

            if self.revisar(nuevaPos[0]):
                return self.recorrido_inv(recorrido)

            adyacentes = []
            for direccion in self.movimientos:
                ady = self.mover(direccion,deepcopy(nuevaPos[0]))
                if ady != False:
                    adyacentes.append(ady)

            for ady in adyacentes:
                if ady not in visitados:
                    visitados.append(ady)
                    h =  self.manhattan_heuristica(ady)
                    cola_de_prioridad.append([ady, len(recorrido)-1, h])

            cola_de_prioridad = sorted(cola_de_prioridad, key=lambda cola:cola[2])
    
    def busquedaProfundidad(self):
        visitados = []
        pila = deque()
        recorrido = []
        copia_inicio = deepcopy(self.inicio)

        visitados.append(copia_inicio) #[nodo]
        pila.append([copia_inicio, None]) #[nodo, padre]

        while len(pila) > 0:
            nuevaPos = pila.pop()
            recorrido.append(nuevaPos)

            if self.revisar(nuevaPos[0]):
                return self.recorrido_inv(recorrido)

            #lista de posiciones posibles del siguiente movimiento
            adyacentes = []
            for direccion in self.movimientos:
                ady = self.mover(direccion,deepcopy(nuevaPos[0]))
                if ady != False:
                    adyacentes.append([ady, len(recorrido)-1])

            for adyacente in adyacentes:
                if adyacente[0] not in visitados:
                    visitados.append(adyacente[0])
                    pila.append(adyacente)
    
    def busquedaAmplitud(self):
        visitados = []
        cola = deque()
        recorrido = []
        copia_inicio = deepcopy(self.inicio)
    
        visitados.append(copia_inicio) #[nodo]
        cola.append([copia_inicio, None]) #[nodo, padre]

        while len(cola) > 0: 
            nuevaPos = cola.popleft()
            recorrido.append(nuevaPos)

            if self.revisar(nuevaPos[0]):
                return self.recorrido_inv(recorrido)

            adyacentes = []
            for direccion in self.movimientos:
                ady = self.mover(direccion,deepcopy(nuevaPos[0]))
                if ady != False:
                    adyacentes.append([ady, len(recorrido)-1])

            for adyacente in adyacentes:
                if adyacente[0] not in visitados:
                    visitados.append(adyacente[0])
                    cola.append(adyacente)