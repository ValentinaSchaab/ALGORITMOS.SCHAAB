from graph import Graph

g = Graph(is_directed=False)

vertices = {
    "Switch 1": "switch",
    "Switch 2": "switch",
    "Router 1": "router",
    "Router 2": "router",
    "Router 3": "router",
    "Ubuntu": "pc",
    "Fedora": "pc",
    "Manjaro": "pc",
    "Parrot": "pc",
    "Mint": "pc",
    "Guarani": "servidor",
    "Red Hat": "notebook",
    "Arch": "notebook",
    "MongoDB": "servidor",
    "Impresora": "impresora",
    "Debian": "notebook"
}

# insertar vértices 
for nombre, tipo in vertices.items():
    g.insert_vertex(nombre)
    pos = g.search(nombre, "value")  # devuelve la posición real del vértice
    g[pos].other_values = tipo       # asigno el tipo

# ARISTAS (una sola porque NO es dirigido) 
aristas = [
    ("Switch 1", "Debian", 17),
    ("Switch 1", "Ubuntu", 18),
    ("Switch 1", "Impresora", 22),
    ("Switch 1", "Mint", 80),
    ("Switch 1", "Router 1", 29),
    ("Router 1","Router 2", 37),
    ("Router 1","Router 3", 43),
    ("Router 2","Red Hat", 25),
    ("Router 2","Guarani", 9),
    ("Router 2","Router 3", 50),
    ("Router 3","Switch 2", 61),
    ("Switch 2","Manjaro", 40),
    ("Switch 2","Parrot", 12),
    ("Switch 2","MongoDB", 5),
    ("Switch 2","Arch", 56),
    ("Switch 2","Fedora", 3),
]

# agregamos aristas 
for origen, destino, peso in aristas:
    g.insert_edge(origen, destino, peso)

# mostrar que cargó todo bien 
print("\nVértices cargados en el grafo:\n")
for v in g:
    print(f"Nombre: {v.value}  |  Tipo: {v.other_values}")

# punto b. barrido por amplitud y profundidad de notebook
print("BARRIDOS DFS y BFS")

notebooks = ["Red Hat", "Debian", "Arch"]

for nb in notebooks:
    print(f"\nDFS desde {nb}:")
    g.deep_sweep(nb)

    print(f"\nBFS desde {nb}:")
    g.amplitude_sweep(nb)

# punto c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro, Red Hat, Fedora hasta la impresora.
def camino_mas_corto(grafo, origen, destino):
    stack = grafo.dijkstra(origen)

    # Convertimos el stack en una lista
    resultados = []
    while stack.size() > 0:
        resultados.append(stack.pop())

    # Buscamos el destino
    nodo_actual = None
    for nodo in resultados:
        if nodo[0] == destino:
            nodo_actual = nodo
            break

    if nodo_actual is None:
        return None, None

    # Reconstruir camino usando los "padres"
    camino = []
    while nodo_actual is not None:
        camino.append(nodo_actual[0])
        padre = nodo_actual[2]
        nodo_actual = next((x for x in resultados if x[0] == padre), None)

    camino.reverse()
    costo = next(x[1] for x in resultados if x[0] == destino)

    return camino, costo

print("caminos mas cortos a impresora:")

equipos = ["Manjaro", "Red Hat", "Fedora"]

for pc in equipos:
    camino, costo = camino_mas_corto(g, pc, "Impresora")
    print(f"Desde {pc}:")
    print(" → ".join(camino))
    print(f"Costo total: {costo}\n")


# punto  d. encontrar el árbol de expansión mínima;
def mst_kruskal(aristas):
    # Ordena por peso (ascendente)
    aristas = sorted(aristas, key=lambda x: x[2])
    
    parent = {}
    rank = {}

    # Find con compresión de caminos
    def find(n):
        if parent[n] != n:
            parent[n] = find(parent[n])
        return parent[n]

    # Union por rango
    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra != rb:
            if rank[ra] > rank[rb]:
                parent[rb] = ra
            elif rank[ra] < rank[rb]:
                parent[ra] = rb
            else:
                parent[rb] = ra
                rank[ra] += 1
            return True
        return False

    # Inicializar conjuntos
    for a, b, w in aristas:
        if a not in parent:
            parent[a] = a
            rank[a] = 0
        if b not in parent:
            parent[b] = b
            rank[b] = 0

    mst = []
    total = 0

    # Procesar
    for a, b, w in aristas:
        if union(a, b):
            mst.append((a, b, w))
            total += w

    return mst, total

mst, peso_total = mst_kruskal(aristas)

print("Árbol de expansión mínima:")
for a, b, w in mst:
    print(f"{a} - {b} : {w}")

print(f"Peso total: {peso_total}")


# punto e.
def camino_mas_corto_a_guarani(grafo):
    pcs = ["Ubuntu", "Fedora", "Manjaro", "Parrot", "Mint"]
    destino = "Guarani"
    mejor_origen = None
    mejor_peso = float("inf")

    for pc in pcs:
        ruta = grafo.dijkstra(pc)

        costo = None
        # recorrer el stack sacando elementos
        while ruta.size() > 0:
            nodo = ruta.pop()
            nombre = nodo[0]
            peso = nodo[1]
            if nombre == destino:
                costo = peso
                break

        if costo is not None and costo < mejor_peso:
            mejor_peso = costo
            mejor_origen = pc

    return mejor_origen, mejor_peso

origen, peso = camino_mas_corto_a_guarani(g)
print("La PC con el camino más corto a Guarani es:", origen)
print("Costo:", peso)

# punto f.  indicar desde que computadora del switch 01 es el camino más corto al servidor “MongoDB”
def camino_mas_corto_a_mongodb(grafo):
    pcs_switch1 = ["Ubuntu", "Mint"]  # solo las PCs del Switch 1
    destino = "MongoDB"

    mejor_origen = None
    mejor_peso = float("inf")

    for pc in pcs_switch1:
        ruta = grafo.dijkstra(pc)

        costo = None
        # leer la ruta desde el stack
        while ruta.size() > 0:
            nodo = ruta.pop()
            nombre = nodo[0]
            peso = nodo[1]

            if nombre == destino:
                costo = peso
                break

        if costo is not None and costo < mejor_peso:
            mejor_peso = costo
            mejor_origen = pc

    return mejor_origen, mejor_peso

origen, peso = camino_mas_corto_a_mongodb(g)
print("La PC del Switch 1 con el camino más corto a MongoDB es:", origen)
print("Costo:", peso)

# punto g. 
# eliminar arista vieja
g.delete_edge("Switch 1", "Impresora", "value")

# agregar arista nueva
g.insert_edge("Router 2", "Impresora", 22)

# barridos del punto b
print("\n--- Barrido en profundidad desde Red Hat ---")
g.deep_sweep("Red Hat")

print("\n--- Barrido por amplitud desde Red Hat ---")
g.amplitude_sweep("Red Hat")


print("\n--- Barrido en profundidad desde Debian ---")
g.deep_sweep("Debian")

print("\n--- Barrido por amplitud desde Debian ---")
g.amplitude_sweep("Debian")


print("\n--- Barrido en profundidad desde Arch ---")
g.deep_sweep("Arch")

print("\n--- Barrido por amplitud desde Arch ---")
g.amplitude_sweep("Arch")
