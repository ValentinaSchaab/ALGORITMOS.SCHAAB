from tree import BinaryTree
from queue_ import Queue

# Datos de Pokémons
pokemons = [
    {
        "nombre": "Pikachu",
        "numero": 25,
        "tipo": ["Electrico"],
        "debilidades": ["Tierra"],
        "mega_evolucion": False,
        "gigamax": True
    },
    {
        "nombre": "Charizard",
        "numero": 6,
        "tipo": ["Fuego", "Volador"],
        "debilidades": ["Agua", "Eléctrico", "Roca"],
        "mega_evolucion": True,
        "gigamax": True
    },
    {
        "nombre": "Bulbasaur",
        "numero": 1,
        "tipo": ["Planta", "Veneno"],
        "debilidades": ["Fuego", "Hielo", "Volador", "Psiquico"],
        "mega_evolucion": False,
        "gigamax": False
    },
    {
        "nombre": "Mewtwo",
        "numero": 150,
        "tipo": ["Psiquico"],
        "debilidades": ["Bicho", "Fantasma", "Siniestro"],
        "mega_evolucion": True,
        "gigamax": False
    },
    {
        "nombre": "Gyarados",
        "numero": 130,
        "tipo": ["Agua", "Volador"],
        "debilidades": ["Electrico", "Roca"],
        "mega_evolucion": True,
        "gigamax": False
    },
    {
        "nombre": "Gengar",
        "numero": 94,
        "tipo": ["Fantasma", "Veneno"],
        "debilidades": ["Tierra", "Psiquico", "Fantasma", "Siniestro"],
        "mega_evolucion": True,
        "gigamax": True
    },
    {
        "nombre": "Lucario",
        "numero": 448,
        "tipo": ["Lucha", "Acero"],
        "debilidades": ["Fuego", "Lucha", "Tierra"],
        "mega_evolucion": True,
        "gigamax": False
    },
    {
        "nombre": "Eevee",
        "numero": 133,
        "tipo": ["Normal"],
        "debilidades": ["Lucha"],
        "mega_evolucion": False,
        "gigamax": True
    },
    {
        "nombre": "Dragonite",
        "numero": 149,
        "tipo": ["Dragon", "Volador"],
        "debilidades": ["Hielo", "Roca", "Dragon", "Hada"],
        "mega_evolucion": False,
        "gigamax": False
    },
    {
        "nombre": "Alakazam",
        "numero": 65,
        "tipo": ["Psiquico"],
        "debilidades": ["Bicho", "Fantasma", "Siniestro"],
        "mega_evolucion": True,
        "gigamax": False
    },
    {
        "nombre": "Garchomp",
        "numero": 445,
        "tipo": ["Dragon", "Tierra"],
        "debilidades": ["Hielo", "Dragon", "Hada"],
        "mega_evolucion": True,
        "gigamax": False
    },
    {
        "nombre": "Lapras",
        "numero": 131,
        "tipo": ["Agua", "Hielo"],
        "debilidades": ["Electrico", "Planta", "Lucha", "Roca"],
        "mega_evolucion": False,
        "gigamax": True
    },
    {
        "nombre": "Snorlax",
        "numero": 143,
        "tipo": ["Normal"],
        "debilidades": ["Lucha"],
        "mega_evolucion": False,
        "gigamax": True
    },
    {
        "nombre": "Tyranitar",
        "numero": 248,
        "tipo": ["Roca", "Siniestro"],
        "debilidades": ["Lucha", "Tierra", "Bicho", "Acero", "Agua", "Planta", "Hada"],
        "mega_evolucion": True,
        "gigamax": False
    },
    {
        "nombre": "Blastoise",
        "numero": 9,
        "tipo": ["Agua"],
        "debilidades": ["Electrico", "Planta"],
        "mega_evolucion": True,
        "gigamax": True
    },
    {
        "nombre": "Venusaur",
        "numero": 3,
        "tipo": ["Planta", "Veneno"],
        "debilidades": ["Fuego", "Hielo", "Volador", "Psiquico"],
        "mega_evolucion": True,
        "gigamax": True
    },
    {
        "nombre": "Jolteon",
        "numero": 135,
        "tipo": ["Electrico"],
        "debilidades": ["Tierra"],
        "mega_evolucion": False,
        "gigamax": False
    },
    {
        "nombre": "Lycanroc",
        "numero": 745,
        "tipo": ["Roca"],
        "debilidades": ["Agua", "Planta", "Lucha", "Tierra", "Acero"],
        "mega_evolucion": False,
        "gigamax": False
    },
    {
        "nombre": "Tyrantrum",
        "numero": 697,
        "tipo": ["Roca", "Dragon"],
        "debilidades": ["Hielo", "Lucha", "Acero", "Tierra", "Dragón", "Hada"],
        "mega_evolucion": False,
        "gigamax": False
    }
]

# punto 1. arboles con indice nombre, numero y tipo.

# Creo los tres árboles 
arbol_por_nombre = BinaryTree()
arbol_por_numero = BinaryTree()
arbol_por_tipo = BinaryTree()

# Cargo pokemons en los tres árboles
for pokemon in pokemons:

    # Árbol por nombre (clave = nombre)
    arbol_por_nombre.insert(pokemon["nombre"], pokemon)

    # Árbol por número (clave = número)
    arbol_por_numero.insert(pokemon["numero"], pokemon)

    # Árbol por tipo (clave = tipo del pokemon)
    for tipo in pokemon["tipo"]:
        
        nodo_tipo = arbol_por_tipo.search(tipo)

        if nodo_tipo is None:
            # si no existe el tipo, creo el nodo con una lista
            arbol_por_tipo.insert(tipo, [pokemon])
        else:
            # si ya existe agrego el pokemon a esa lista
            nodo_tipo.other_values.append(pokemon)

# punto 2. datos de pokemones a partir de su numero.
def mostrar_por_numero(numero):
    nodo = arbol_por_numero.search(numero)

    if nodo is None:
        print("No existe un Pokémon con ese número.")
    else:
        pokemon = nodo.other_values
        print("Nombre:", pokemon["nombre"])
        print("Número:", pokemon["numero"])
        print("Tipo:", pokemon["tipo"])
        print("Debilidades:", pokemon["debilidades"])
        print("Mega evolución:", pokemon["mega_evolucion"])
        print("Gigamax:", pokemon["gigamax"])

print("Búsqueda por número")
numero = int(input("Ingresá el número del Pokémon a buscar: "))
mostrar_por_numero(numero)

print("---------------------------------------")

# punto 2. datos de pokemones a partir de su nombre por proximidad.

def nombre_proximidad(arbol, texto):
    def __buscar(root, texto):
        if root is not None:
            nombre = root.value.lower()
            texto = texto.lower()

            if nombre.startswith(texto) or texto in nombre:
                pokemon = root.other_values
                print("Nombre:", pokemon["nombre"])
                print("Número:", pokemon["numero"])
                print("Tipo:", pokemon["tipo"])
                print("Debilidades:", pokemon["debilidades"])
                print("Mega evolución:", pokemon["mega_evolucion"])
                print("Gigamax:", pokemon["gigamax"])

            __buscar(root.left, texto)
            __buscar(root.right, texto)

    if arbol.root is None:
        print("El árbol está vacío.")
    else:
        __buscar(arbol.root, texto)

print("Buscamos nombre por proximidad")
texto = input("Ingresá parte del nombre a buscar: ")
nombre_proximidad(arbol_por_nombre, texto)

print("---------------------------------------")

# punto 3. mostrar todos los nombres de pokemons de un determinado tipo.
def mostrar_por_tipo(tipo):
    nodo = arbol_por_tipo.search(tipo)

    if nodo is None:
        print("No hay Pokémons del tipo ", tipo)
        return
    
    print("Pokémons del tipo: ", tipo)
    for pokemon in nodo.other_values:
        print(pokemon["nombre"])

tipo = input("Ingresá el tipo de Pokémon a buscar: ")
mostrar_por_tipo(tipo)

print("---------------------------------------")

# punto 4. listado en orden ascendente por número.
def lista_ascendente_por_numero(arbol):
    def __in_order(root):
        if root is not None:
            __in_order(root.left)
            p = root.other_values
            print(f"N° {p['numero']} - {p['nombre']}")
            __in_order(root.right)

    if arbol.root is None:
        print("Árbol vacío")
    else:
        __in_order(arbol.root)

lista_ascendente_por_numero(arbol_por_numero)

print("---------------------------------------")

# punto 4. listado en orden ascendente por nombre de Pokémon.
def lista_ascendente_por_nombre(arbol):
    def __in_order(root):
        if root is not None:
            __in_order(root.left)
            p = root.other_values
            print(f"{p['nombre']} - N° {p['numero']}")
            __in_order(root.right)

    if arbol.root is None:
        print("Árbol vacío.")
    else:
        __in_order(arbol.root)

lista_ascendente_por_nombre(arbol_por_nombre)

print("---------------------------------------")

# punto 4. listado por nivel por nombre.
def listado_por_nivel(arbol):
    if arbol.root is None:
        print("el arbol esta vacío")
        return

    cola = Queue()
    cola.arrive(arbol.root)
    cola.arrive(None)   # separa de niveles

    nivel = 0
    print("Nivel:", nivel)

    while cola.size() > 0:
        nodo = cola.attention()

        if nodo is None:
            # Fin de un nivel
            if cola.size() > 0:
                nivel += 1
                print("Nivel:", nivel)
                cola.arrive(None)
            continue

        p = nodo.other_values
        print(f"  {p['nombre']} - N° {p['numero']} - Tipo {p['tipo']}")

        if nodo.left:
            cola.arrive(nodo.left)
        if nodo.right:
            cola.arrive(nodo.right)


listado_por_nivel(arbol_por_nombre)

print("---------------------------------------")

# punto 5. mostrar todos los pokemons que son debiles frente a..
# veo los tipos
def tipos_referencia(arbol):
    j = arbol.search("Jolteon").other_values
    l = arbol.search("Lycanroc").other_values
    t = arbol.search("Tyrantrum").other_values

    return j["tipo"] + l["tipo"] + t["tipo"]   # lista simple

# recorro el arbol completo
def recorrer(nodo, lista):
    if nodo is not None:
        recorrer(nodo.left, lista)
        lista.append(nodo.other_values)
        recorrer(nodo.right, lista)

#mostrar q son debiles a esos tipos
def mostrar_debiles(arbol):
    tipos = tipos_referencia(arbol)   # lista como ["Electrico", "Roca", "Dragon"]

    todos = []
    recorrer(arbol.root, todos)

    print("Pokémons débiles a Jolteon, Lycanroc y Tyrantrum:")

    for p in todos:
        # si alguno de sus tipos está dentro de sus debilidades
        for t in tipos:
            if t in p["debilidades"]:
                print(p["nombre"])
                break

mostrar_debiles(arbol_por_nombre)

print("---------------------------------------")

# punto 6. todos los tipos de pokemons y cuantos hay de cada tipo.
def mostrar_cantidad_por_tipo(arbol):
    def _in_order(root):
        if root is not None:
            _in_order(root.left)
            tipo = root.value
            cantidad = len(root.other_values)
            print(f"{tipo}: {cantidad}")
            _in_order(root.right)

    if arbol.root is not None:
        _in_order(arbol.root)


mostrar_cantidad_por_tipo(arbol_por_tipo)

print("---------------------------------------")

def contar_por_caracteristica(arbol, caracteristica):
    def _contar(root):
        if root is None:
            return 0
        suma = 1 if root.other_values[caracteristica] else 0
        return suma + _contar(root.left) + _contar(root.right)
    return _contar(arbol.root)

#punto 7.cuantos pokemons tienen megaevolucion.
print("Pokémons con megaevolución:", contar_por_caracteristica(arbol_por_nombre, "mega_evolucion"))
#punto 8.cuantos pokemons tiene forma gigamax.
print("Pokémons con gigamax:", contar_por_caracteristica(arbol_por_nombre, "gigamax"))
