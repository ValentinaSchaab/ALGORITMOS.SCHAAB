from graph import Graph

# Creo grafo no dirigido
star_wars = Graph(is_directed=False)

# Datos de personajes con episodios
personajes_info = {
    "Luke Skywalker": [4, 5, 6, 7, 8],
    "Darth Vader": [3, 4, 5, 6],
    "Yoda": [1, 2, 3, 5, 6, 8, 9],
    "Boba Fett": [2, 5, 6],
    "C-3PO": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Leia": [4, 5, 6, 7, 8, 9],
    "Rey": [7, 8, 9],
    "Kylo Ren": [7, 8, 9],
    "Chewbacca": [3, 4, 5, 6, 7],
    "Han Solo": [4, 5, 6, 7],
    "R2-D2": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "BB-8": [7, 8, 9]
}

# Diccionario para guardar info extra
info_extra = {}

print("Star Wars - apariciones")

# Cargo los vértices
for nombre, episodios in personajes_info.items():
    star_wars.insert_vertex(nombre)
    info_extra[nombre] = episodios
    print(f" {nombre:<20} aparece en {len(episodios)} episodios")

print(f"\n{len(personajes_info)} personajes cargados en ell grafo.\n")

# Inserto las aristas (conexiones entre personajes) El peso representa cuántos episodios compartieron.

# Conexiones de Luke Skywalker
star_wars.insert_edge("Luke Skywalker", "Leia", 5)
star_wars.insert_edge("Luke Skywalker", "Han Solo", 4)
star_wars.insert_edge("Luke Skywalker", "Darth Vader", 3)
star_wars.insert_edge("Luke Skywalker", "Chewbacca", 4)
star_wars.insert_edge("Luke Skywalker", "C-3PO", 5)
star_wars.insert_edge("Luke Skywalker", "R2-D2", 5)
star_wars.insert_edge("Luke Skywalker", "Yoda", 2)
star_wars.insert_edge("Luke Skywalker", "Boba Fett", 1)

# Conexiones de Darth Vader
star_wars.insert_edge("Darth Vader", "Leia", 3)
star_wars.insert_edge("Darth Vader", "C-3PO", 3)
star_wars.insert_edge("Darth Vader", "R2-D2", 3)
star_wars.insert_edge("Darth Vader", "Boba Fett", 2)
star_wars.insert_edge("Darth Vader", "Chewbacca", 2)
star_wars.insert_edge("Darth Vader", "Yoda", 2)
star_wars.insert_edge("Darth Vader", "Han Solo", 2)

# Conexiones de Yoda
star_wars.insert_edge("Yoda", "C-3PO", 6)
star_wars.insert_edge("Yoda", "R2-D2", 6)
star_wars.insert_edge("Yoda", "Leia", 4)
star_wars.insert_edge("Yoda", "Rey", 2)
star_wars.insert_edge("Yoda", "Chewbacca", 3)

# Conexiones de C-3PO y R2-D2
star_wars.insert_edge("C-3PO", "R2-D2", 9)
star_wars.insert_edge("C-3PO", "Leia", 6)
star_wars.insert_edge("C-3PO", "Han Solo", 4)
star_wars.insert_edge("C-3PO", "Chewbacca", 5)
star_wars.insert_edge("C-3PO", "Rey", 3)
star_wars.insert_edge("C-3PO", "BB-8", 3)
star_wars.insert_edge("C-3PO", "Kylo Ren", 2)

# Conexiones de R2-D2
star_wars.insert_edge("R2-D2", "Leia", 6)
star_wars.insert_edge("R2-D2", "Han Solo", 4)
star_wars.insert_edge("R2-D2", "Chewbacca", 5)
star_wars.insert_edge("R2-D2", "Rey", 3)
star_wars.insert_edge("R2-D2", "BB-8", 3)
star_wars.insert_edge("R2-D2", "Boba Fett", 2)

# Conexiones de Leia
star_wars.insert_edge("Leia", "Han Solo", 4)
star_wars.insert_edge("Leia", "Chewbacca", 4)
star_wars.insert_edge("Leia", "Rey", 3)
star_wars.insert_edge("Leia", "Kylo Ren", 3)
star_wars.insert_edge("Leia", "BB-8", 3)

# Conexiones de Han Solo y Chewbacca
star_wars.insert_edge("Han Solo", "Chewbacca", 4)
star_wars.insert_edge("Han Solo", "Boba Fett", 2)

# Conexiones de Rey
star_wars.insert_edge("Rey", "Kylo Ren", 3)
star_wars.insert_edge("Rey", "BB-8", 3)
star_wars.insert_edge("Rey", "Chewbacca", 2)

# Conexiones de Kylo Ren
star_wars.insert_edge("Kylo Ren", "BB-8", 3)
star_wars.insert_edge("Kylo Ren", "Chewbacca", 2)

# Conexiones adicionales
star_wars.insert_edge("Chewbacca", "BB-8", 2)
star_wars.insert_edge("Chewbacca", "Boba Fett", 1)

print("---------------------------------------")

# punto 2. arbol de expansión mínimo desde C-3PO, Yoda y Leia
print("arbol de expansion minima (KRUSKAL)")

vertices_mst = ["C-3PO", "Yoda", "Leia"]

for personaje in vertices_mst:
    print(f"Árbol de expansión mínima desde {personaje}")
    resultado_mst = star_wars.kruskal(personaje)
    print(f"   {resultado_mst}\n")

print("---------------------------------------")

# punto 3. Número máximo de episodios compartidos entre dos personajes
print("maximo de episodios compartidos\n")

def hallar_maximo_episodios(grafo):
    peso_maximo = 0
    parejas_maximas = []

    for nodo in grafo:
        for conexion in nodo.edges:
            # Evitar duplicados A-B y B-A
            if nodo.value < conexion.value:
                if conexion.weight > peso_maximo:
                    peso_maximo = conexion.weight
                    parejas_maximas = [(nodo.value, conexion.value)]
                elif conexion.weight == peso_maximo:
                    parejas_maximas.append((nodo.value, conexion.value))

    print("número máximo de episodios compartidos:", peso_maximo)
    print("Parejas de personajes:\n")
    for p1, p2 in parejas_maximas:
        print(f"  {p1} - {p2}")

hallar_maximo_episodios(star_wars)

print("---------------------------------------")

# punto 4. Listado de personajes cargados
print("personajes cargados\nLista de personajes:\n")

contador = 1
for nombre, episodios in personajes_info.items():
    eps_str = ", ".join(map(str, episodios))
    print(f"   {contador:2d}. {nombre:<18} | Episodios: [{eps_str}]")
    contador += 1

print("---------------------------------------")

# punto 5. Camino más corto usando Dijkstra
print("camino mas corto (DIJKSTRA)\n")

def calcular_camino_corto(grafo, inicio, fin):
    
    pila = grafo.dijkstra(inicio)
    encontrado = False

    while pila.size() > 0:
        nodo = pila.pop()
        if nodo[0] == fin:
            print(f"Camino encontrado de '{inicio}' a '{fin}, con peso total: {nodo[1]} episodios\n")
            encontrado = True
            break

    if not encontrado:
        print(f"No existe un camino entre '{inicio}' y '{fin}'\n")

calcular_camino_corto(star_wars, "C-3PO", "R2-D2")
calcular_camino_corto(star_wars, "Yoda", "Darth Vader")

print("---------------------------------------")

# punto 6. personajes que aparecieron en los 9 episodios
print("personajes en todos los episodios\n")

def buscar_personajes_completos(grafo, info_extra):
    encontrados = []

    for nodo in grafo:
        eps = info_extra[nodo.value]
        if len(eps) == 9:
            encontrados.append((nodo.value, eps))

    print("Personajes que aparecen en los 9 episodios:\n")
    if not encontrados:
        print("No hay personajes que aparezcan en todos los episodios.")
    else:
        for nombre, eps in encontrados:
            eps_str = ", ".join(map(str, eps))
            print(f" {nombre}")
            print(f"   Episodios: [{eps_str}]\n")

buscar_personajes_completos(star_wars, info_extra)
