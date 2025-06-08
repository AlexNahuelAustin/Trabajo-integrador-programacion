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
    
    # Esta funcion genera e imprime una reprensetacion jerargica del arbol 
    def organigrama(self,indentado = 0): 
        salto_de_la_rama = "  " * indentado # Crea un str de espacios que se usara para identar y mejorar visualmetne cada nivel del arbol  
        print(f"{salto_de_la_rama} |--- {self.policia} ") # imprime el nombre de la unidad con identacion y un formato de rama de arbol
        for depenecias in self.bomberos.values():
            depenecias.organigrama(indentado + 1) # llama recursivamente al metodo organigrama para cada dependencia 
        
        
    

# Se crean todos los nodos que van a formar parte de nuestro arbol jerargico(organigrama) 
raiz = Nodo("Policía Bombero")
nodo_a = Nodo("Dirección de Bomberos")
nodo_b = Nodo("DPTO. Coordinación Operativa")
nodo_c = Nodo("DPTO. Técnico Administrativo")
nodo_d = Nodo("DPTO. Unidades de Alto Riesgo e Interior")
nodo_e = Nodo("División Operacionales")
nodo_f = Nodo("Sección Central de Alarmas")
nodo_g = Nodo("División de Cuarteles")
nodo_h = Nodo("División de Servicios Técnicos")
nodo_i = Nodo("División de Investigación Siniestro")
nodo_j = Nodo("Grupo Especial de Salvamento")
nodo_k = Nodo("Brigada de Búsqueda y Rastreo")
nodo_n = Nodo("Brigada de Materiales Peligrosos")
nodo_m = Nodo("DPTO. Unidades de Alto Riesgo Interior")
nodo_s1 = Nodo("Sección Asesoramientos")
nodo_s2 = Nodo("Sección Inspecciones")
nodo_s3 = Nodo("Sección Proyectos")
nodo_q = Nodo("Sección Pericias")
nodo_r = Nodo("Sección Informes Técnicos")

# Agregamos y conectados la Raiz con las ramas, y las ramas con las hojas, armando asi nuestro arbol jerargico 
# Se conecta la raiz con la Direccion Bomberos
raiz.agregar_funcion_de_las_direcciones(nodo_a)
# Se conectan los departamentos que depende de la Direccion Bomberos
nodo_a.agregar_funcion_de_las_direcciones(nodo_b)
nodo_a.agregar_funcion_de_las_direcciones(nodo_c)
nodo_a.agregar_funcion_de_las_direcciones(nodo_d)
# Se conectan las Subdependencias que depende del Derpartamento Coordinacion operativa
nodo_b.agregar_funcion_de_las_direcciones(nodo_e)
nodo_b.agregar_funcion_de_las_direcciones(nodo_f)
nodo_b.agregar_funcion_de_las_direcciones(nodo_g)
# Subdependencias del departamento Tecnico Administrativo
nodo_c.agregar_funcion_de_las_direcciones(nodo_h)
nodo_c.agregar_funcion_de_las_direcciones(nodo_i)
#Subdependencias del DUAR (departamento de unidades de alto riesgo)
nodo_d.agregar_funcion_de_las_direcciones(nodo_j)
nodo_d.agregar_funcion_de_las_direcciones(nodo_k)
nodo_d.agregar_funcion_de_las_direcciones(nodo_n)
nodo_d.agregar_funcion_de_las_direcciones(nodo_m)
# Subdivisiones del servicio tecnico
nodo_h.agregar_funcion_de_las_direcciones(nodo_s1)
nodo_h.agregar_funcion_de_las_direcciones(nodo_s2)
nodo_h.agregar_funcion_de_las_direcciones(nodo_s3)
# Subdivisiones de la division de investigacion siniestrales
nodo_i.agregar_funcion_de_las_direcciones(nodo_q)
nodo_i.agregar_funcion_de_las_direcciones(nodo_r)


# -------- IMPRESIONES --------
print("\nDependencias de los  bomberos:")  # Imprimi las dependencias desde la Raiz

for nodo in raiz.bomberos.values(): # 
    print(" >", nodo.policia) # 

print("\nDependencias de la Dirección de Bomberos:") # Imprime los nodos de la Direccion bomberos
for nodo in nodo_a.bomberos.values():# 
    print("  >", nodo.policia) # 

print("\nDependencias del DPTO. Coordinación Operativa:") # Imprime los nodos del Dpto, coordinacion operativa
for nodo in nodo_b.bomberos.values():
    print(" >", nodo.policia) #

print("\nSubfunciones de Investigación Siniestro:") # Imprime los nodo de Investigaciones Siniestrales
for nodo in nodo_i.bomberos.values():
    print(" >", nodo.policia) # 


# -------- CALCULAR GRADO Y PESO --------
grado = raiz.calcular_grado_arbol()
peso = raiz.calcular_peso_arbol()

print(f"\nEl grado del árbol es: {grado}") # Imprimimos el Grado del arbol
print(f"El peso del árbol es igual a: {peso}")# Imprimimos el Peso del arbol


# -------- BUSCAR CAMINO HASTA UN NODO --------
camino = raiz.buscar_dependencia(nodo_r)  # Buscamos el recorrido del nodo_r

#Imprime el camino encontrado en caso que exista
print("\nCamino jerárquico hasta 'Sección Informes Técnicos':")

for paso in camino:
    print(" >", paso.policia)
    
#impime el organigrama
raiz.organigrama()