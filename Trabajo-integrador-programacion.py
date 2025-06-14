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


    # Funcion para calcular el grado maximo del arbol 
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
    
    # Esta funcion genera e imprime una reprensetacion jerargica del arbol 
    def organigrama(self,indentado = 0): 
        salto_de_la_rama = "  " * indentado # Crea espacios que se usara para identar y mejorar visualmetne cada nivel del arbol  
        print(f"{salto_de_la_rama} |--- {self.policia} ") # Imprime el nombre de la unidad con identacion y un formato de rama de arbol
        for depenecias in self.bomberos.values():
            depenecias.organigrama(indentado + 1) # llama recursivamente al metodo organigrama para cada dependencia 
        
        

# Se crean todos los nodos que van a formar parte de nuestro arbol jerargico(organigrama) 
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


# Agregamos y conectados la Raiz con las ramas, y las ramas con las hojas, armando asi nuestro arbol jerargico 
# Se conecta la raiz con la Direccion Bomberos
bombero.agregar_funcion_de_las_direcciones(direccion)
# Se conectan los departamentos que depende de la Direccion Bomberos
direccion.agregar_funcion_de_las_direcciones(departamento_a)
direccion.agregar_funcion_de_las_direcciones(departamento_b)
direccion.agregar_funcion_de_las_direcciones(departamento_c)
# Se conectan las Subdependencias que depende del Derpartamento Coordinacion operativa
departamento_a.agregar_funcion_de_las_direcciones(division_a)
departamento_a.agregar_funcion_de_las_direcciones(seccion_a)
departamento_a.agregar_funcion_de_las_direcciones(seccion_b)
# Subdependencias del departamento Tecnico Administrativo
departamento_b.agregar_funcion_de_las_direcciones(seccion_c)
departamento_b.agregar_funcion_de_las_direcciones(division_b)
#Subdependencias del DUAR (departamento de unidades de alto riesgo)
departamento_c.agregar_funcion_de_las_direcciones(division_c)
departamento_c.agregar_funcion_de_las_direcciones(brigada_a)
departamento_c.agregar_funcion_de_las_direcciones(brigada_b)
departamento_c.agregar_funcion_de_las_direcciones(departamento_d)
# Subdivisiones del servicio tecnico
seccion_c.agregar_funcion_de_las_direcciones(seccion_d)
seccion_c.agregar_funcion_de_las_direcciones(seccion_e)
seccion_c.agregar_funcion_de_las_direcciones(seccion_f)
# Subdivisiones de la division de investigacion siniestrales
division_b.agregar_funcion_de_las_direcciones(seccion_g)
division_b.agregar_funcion_de_las_direcciones(seccion_h)


# -------- IMPRESIONES --------
print("\nDependencias de los  bomberos:")  # Imprime las dependencias desde la Raiz
for nodo in bombero.bomberos.values(): # 
    print(" >", nodo.policia) # 

print("\nDependencias de la Dirección de Bomberos:") # Imprime los nodos de la Direccion bomberos
for nodo in direccion.bomberos.values():# 
    print("  >", nodo.policia) # 

print("\nDependencias del DPTO. Coordinación Operativa:") # Imprime los nodos del Dpto, coordinacion operativa
for nodo in departamento_a.bomberos.values():
    print(" >", nodo.policia) #

print("\nSubfunciones de Investigación Siniestro:") # Imprime los nodo de Investigaciones Siniestrales
for nodo in division_b.bomberos.values():
    print(" >", nodo.policia) # 


# -------- CALCULAR GRADO Y PESO --------
grado = bombero.calcular_grado_arbol()
peso = bombero.calcular_peso_arbol()

print(f"\nEl grado maximo del árbol es: {grado}") # Imprimimos el Grado del arbol
print(f"El peso del árbol es igual a: {peso}")# Imprimimos el Peso del arbol


# -------- BUSCAR CAMINO HASTA UN NODO --------
camino = bombero.buscar_dependencia(seccion_h)  # Buscamos el recorrido del nodo_r

# -------- IMPRIME EL RECORRIDO --------
print("\nCamino jerárquico hasta 'Sección Informes Técnicos':")

for paso in camino:
    print(" >", paso.policia)

# -------- IMPRIME EL ORGANIGRAMA --------
print("\nEl organigrama de la direccion de bomberos es: ")
bombero.organigrama()