class Nodo: # Se defino la clase para reprentar cada area en el organigrama

    def __init__(self, policia): # Cada nodo tiene su nombre (bombero, policia) y un diccionario de todos los bomberos
        self.policia = policia # El nombre del nodo
        self.bomberos = {}  # Almacena nodos (Diccionario)

    def agregar_funcion_de_las_direcciones(self, nodo):  # Funcion para agregar nodos
        self.bomberos[nodo.policia] = nodo # Se usa el nombre del nodo como clave y se almancena

    def buscar_dependencia(self, destino, camino=None): # Funcion para buscar un nodo en el arbol y devolver el camino desde la raiz
        if camino is None:
            camino = [] # Se inicializa la lista de camino si no se ah proporcionado

        camino.append(self) # Se agrega el nodo actual al camino

        if self == destino: # SI el nodo actual es el nodo que estamos buscando retorna al camino recorrido hasta ahora
            return camino
        # Ciclo For para recorrer las dependencias de bomberos (recursivamente)
        for bombero in self.bomberos.values(): # Se busca de manera recursiva en cada nodo, pasando el camino como una copia para no modificar la lista 
            camino_encontrado = bombero.buscar_dependencia(destino, camino[:])
            if camino_encontrado: # Se encuentra el destino en la sub rama
                return camino_encontrado # retorna el comino encontrado

        return None # Si no se encuentra el nodo buscardo, retorna en None

    def calcular_grado_nodo(self): # Funcion para calcular el grado maximo del arbol
        return len(self.bomberos) # Retorna la cantidad de nodos


    # funcion para calcular el grado maximo del arbol 
    def calcular_grado_arbol(self):
        # Grado del árbol: máximo grado de todos los nodos
        grado_maximo = self.calcular_grado_nodo() # Se calcula el grado actual del nodo
        for bombero in self.bomberos.values(): # Se recorren todas las ramas y nodos
            grado_maximo = max(grado_maximo, bombero.calcular_grado_arbol())
        return grado_maximo # Se retorna el grado maximo encontrado

    # Funcion para calcular el peso del arbol
    def calcular_peso_arbol(self):
        peso = 1 # Se cuenta desde el nodo actual
        for bombero in self.bomberos.values(): # Se recorren todos los nodos hoja
            peso += bombero.calcular_peso_arbol() # Se suman los nodos de las subramas
        return peso # Retorna el total encontrado
    
    def organigrama(self,indentado = 0):
        salto_de_la_rama = "  " * indentado  
        print(f"{salto_de_la_rama} |--- {self.policia} ")
        for depenecias in self.bomberos.values():
            depenecias.organigrama(indentado + 1)
        