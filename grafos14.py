from graph import Graph

g = Graph(is_directed=False)

# vertices
ambientes = [
    "cocina", "comedor", "cochera", "quincho",
    "baño 1", "baño 2", "habitacion 1", "habitacion 2",
    "sala de estar", "terraza", "patio"
]

for a in ambientes:
    g.insert_vertex(a)

# Vvertices con aristas

# sala de estar 
g.insert_edge("sala de estar", "cocina", 4)
g.insert_edge("sala de estar", "comedor", 3)
g.insert_edge("sala de estar", "habitacion 1", 6)
g.insert_edge("sala de estar", "baño 1", 5)
g.insert_edge("sala de estar", "terraza", 7)

# cocina  
g.insert_edge("cocina", "terraza", 10)
g.insert_edge("cocina", "comedor", 3)
g.insert_edge("cocina", "habitacion 1", 6)
g.insert_edge("cocina", "baño 1", 5)

# comedor 
g.insert_edge("comedor", "terraza", 10)

# cochera 
g.insert_edge("cochera", "quincho", 2)
g.insert_edge("cochera", "habitacion 2", 6)
g.insert_edge("cochera", "baño 2", 1)

# quincho
g.insert_edge("quincho", "baño 2", 1)
g.insert_edge("quincho", "habitacion 2", 6)

# baño 1
g.insert_edge("baño 1", "habitacion 1", 6)

# baño 2 
g.insert_edge("baño 2", "habitacion 2", 6)
g.insert_edge("baño 2", "patio", 5)


# habitacion 1 
g.insert_edge("habitacion 1", "patio", 5)

# habitacion 2 
g.insert_edge("habitacion 2", "patio", 5)

# terraza (3) sala de estar - cocina - comedor

# patio (3) baño 2 - habitacion 1 - habitacion 2

# mostramos
g.show()

# punto c
print("arbol de expansion minima (KRUSKAL)")
mst_raw = g.kruskal("cocina")   # podés usar cualquier ambiente como origen
print("MST:", mst_raw)

# Calcular la suma total de metros 
total = 0
# el formato que devuelve kruskal es: "a-b-peso;a-b-peso;..."
aristas = mst_raw.split(";")

for a in aristas:
    if a.strip() == "":
        continue
    partes = a.split("-")
    peso = int(partes[-1])   # el peso siempre es lo último
    total += peso

print("Metros totales: ", total)

# punto d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de red se necesitan
def obtener_camino(dijkstra_stack, destino):
    # Pasar stack a lista
    info = []
    while dijkstra_stack.size() > 0:
        info.append(dijkstra_stack.pop())

    # Buscar el destino
    for nodo, dist, pred in info:
        if nodo == destino:
            distancia_final = dist
            actual = nodo
            break

    # Reconstruir el camino
    camino = [actual]
    while True:
        for nodo, dist, pred in info:
            if nodo == actual:
                if pred is None:
                    camino.reverse()
                    return camino, distancia_final
                camino.append(pred)
                actual = pred
                break

print("Camino mas corto:")

resultado = g.dijkstra("habitacion 1")

camino, metros = obtener_camino(resultado, "sala de estar")

print("Camino:", " -> ".join(camino))
print("Metros necesarios:", metros)
