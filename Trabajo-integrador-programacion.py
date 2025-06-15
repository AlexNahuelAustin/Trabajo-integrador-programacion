class Nodo: # Se define la clase para representar cada área en el organigrama

    def __init__(self, policia):  # Cada nodo tiene su nombre (bombero, policía) y un diccionario de todos los bomberos
        self.policia = policia  # El nombre del nodo
        self.bomberos = {}  # Almacena nodos (Diccionario)

    def agregar_funcion_de_las_direcciones(self, nodo):  # Función para agregar nodos
        self.bomberos[nodo.policia] = nodo # Se usa el nombre del nodo como clave y se almacena

    def buscar_dependencia(self, destino, camino=None): # Función para buscar un nodo en el árbol y devolver el camino desde la raíz
        if camino is None:
            camino = [] # Se inicializa la lista de camino si no se ha proporcionado

        camino.append(self) # Se agrega el nodo actual al camino

        if self == destino:# Si el nodo actual es el nodo que estamos buscando, retorna el camino recorrido hasta ahora
            return camino
        
        # Ciclo for para recorrer las dependencias de bomberos (recursivamente)
        for bombero in self.bomberos.values(): # Se busca de manera recursiva en cada nodo, pasando el camino como una copia para no modificar la lista 
            camino_encontrado = bombero.buscar_dependencia(destino, camino[:])
            if camino_encontrado: #: Se encuentra el destino en la sub-rama
                return camino_encontrado # retorna el camino encontrado
        return None # Si no se encuentra el nodo buscado, retorna None 


    def calcular_grado_nodo(self): # Función para calcular el grado máximo del árbol
        return len(self.bomberos) # Retorna la cantidad de nodos


    # Función para calcular el grado máximo del árbol
    def calcular_grado_arbol(self):
        # Grado del árbol: máximo grado de todos los nodos
        grado_maximo = self.calcular_grado_nodo() # Se calcula el grado actual del nodo
        for bombero in self.bomberos.values(): # Se recorren todas las ramas y nodos
            grado_maximo = max(grado_maximo, bombero.calcular_grado_arbol())
        return grado_maximo # Se retorna el grado máximo encontrado

   # Función para calcular el peso del árbol
    def calcular_peso_arbol(self):
        peso = 1 # Se cuenta desde el nodo actual
        for bombero in self.bomberos.values(): # Se recorren todos los nodos hoja
            peso += bombero.calcular_peso_arbol() # Se suman los nodos de las subramas
        return peso # Retorna el total encontrado
    
    # Esta función genera e imprime una representación jerárquica del árbol
    def organigrama(self,indentado = 0): 
        salto_de_la_rama = "  " * indentado # Crea espacios que se usará para indentar y mejorar visualmente cada nivel del árbol
        print(f"{salto_de_la_rama} |--- {self.policia} ") # Imprime el nombre de la unidad con indentación y un formato de rama de árbol
        for depenecias in self.bomberos.values():
            depenecias.organigrama(indentado + 1) # llama recursivamente al método organigrama para cada dependencia
        
        

# Se crean todos los nodos que van a formar parte de nuestro árbol jerárquico (organigrama) 
bombero = Nodo("Policía Bombero")
direccion = Nodo("Dirección de Bomberos")
departamento_a = Nodo("DPTO. Coordinación Operativa")
departamento_b = Nodo("DPTO. Técnico Administrativo")
departamento_c = Nodo("DPTO. Unidades de Alto Riesgo e Interior")
division_a = Nodo("División Operacionales")
seccion_a = Nodo("Sección Central de Alarmas")
seccion_b = Nodo("División de Cuarteles")
seccion_c = Nodo("División de Servicios Técnicos")
division_b = Nodo("División de Investigación Siniestro")
division_c = Nodo("Grupo Especial de Salvamento")
brigada_a = Nodo("Brigada de Búsqueda y Rastreo")
brigada_b = Nodo("Brigada de Materiales Peligrosos")
departamento_d = Nodo("DPTO. Unidades de Alto Riesgo Interior")
seccion_d = Nodo("Sección Asesoramientos")
seccion_e = Nodo("Sección Inspecciones")
seccion_f = Nodo("Sección Proyectos")
seccion_g = Nodo("Sección Pericias")
seccion_h = Nodo("Sección Informes Técnicos")


# Agregamos y conectamos la Raíz con las ramas, y las ramas con las hojas, armando así nuestro árbol jerárquico
bombero.agregar_funcion_de_las_direcciones(direccion)
# Se conectan los departamentos que dependen de la Dirección de Bomberos
direccion.agregar_funcion_de_las_direcciones(departamento_a)
direccion.agregar_funcion_de_las_direcciones(departamento_b)
direccion.agregar_funcion_de_las_direcciones(departamento_c)

# Se conectan las Subdependencias que dependen del Departamento Coordinación Operativa
departamento_a.agregar_funcion_de_las_direcciones(division_a)
departamento_a.agregar_funcion_de_las_direcciones(seccion_a)
departamento_a.agregar_funcion_de_las_direcciones(seccion_b)

# Subdependencias del Departamento Técnico Administrativo
departamento_b.agregar_funcion_de_las_direcciones(seccion_c)
departamento_b.agregar_funcion_de_las_direcciones(division_b)

# Subdependencias del DUAR (Departamento de Unidades de Alto Riesgo)
departamento_c.agregar_funcion_de_las_direcciones(division_c)
departamento_c.agregar_funcion_de_las_direcciones(brigada_a)
departamento_c.agregar_funcion_de_las_direcciones(brigada_b)
departamento_c.agregar_funcion_de_las_direcciones(departamento_d)

# Subdivisiones del servicio técnico
seccion_c.agregar_funcion_de_las_direcciones(seccion_d)
seccion_c.agregar_funcion_de_las_direcciones(seccion_e)
seccion_c.agregar_funcion_de_las_direcciones(seccion_f)

# Subdivisiones de la División de Investigación Siniestrales
division_b.agregar_funcion_de_las_direcciones(seccion_g)
division_b.agregar_funcion_de_las_direcciones(seccion_h)


# -------- IMPRESIONES --------
print("\nDependencias de los  bomberos:")  # Imprime las dependencias desde la Raíz
for nodo in bombero.bomberos.values(): # 
    print(" >", nodo.policia) # 

print("\nDependencias de la Dirección de Bomberos:") # Imprime los nodos de la Dirección de Bomberos
for nodo in direccion.bomberos.values():# 
    print("  >", nodo.policia) # 

print("\nDependencias del DPTO. Coordinación Operativa:") # Imprime los nodos del Dpto. Coordinación Operativa
for nodo in departamento_a.bomberos.values():
    print(" >", nodo.policia) #

print("\nSubfunciones de Investigación Siniestro:") # Imprime los nodos de Investigaciones Siniestrales
for nodo in division_b.bomberos.values():
    print(" >", nodo.policia) # 


# -------- CALCULAR GRADO Y PESO --------
grado = bombero.calcular_grado_arbol()
peso = bombero.calcular_peso_arbol()

print(f"\nEl grado maximo del árbol es: {grado}") # Imprimimos el Grado del árbol
print(f"El peso del árbol es igual a: {peso}") # Imprimimos el Peso del árbol


# -------- BUSCAR CAMINO HASTA UN NODO --------
camino = bombero.buscar_dependencia(seccion_h)  # Buscamos el recorrido hasta el nodo 'seccion_h'

# -------- IMPRIME EL RECORRIDO --------
print("\nCamino jerárquico hasta 'Sección Informes Técnicos':")

for paso in camino:
    if camino: 
        print(" >", paso.policia)
    else:
        print("No se encontró la dependencia.")

# -------- IMPRIME EL ORGANIGRAMA --------
print("\nEl organigrama de la direccion de bomberos es: ")
bombero.organigrama()