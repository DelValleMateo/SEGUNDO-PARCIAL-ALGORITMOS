from AVL import ARBOLAVL

# 1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
# de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
# tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
# a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
# mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
# caracteres–;
# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
# además un listado por nivel por nombre;
# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
# f) Determina cuantos Pokémons hay de tipo eléctrico y acero. 2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los

pokemons = [
    {'nombre': 'Bulbasaur', 'numero': 1, 'tipos': [
        'Planta', 'Veneno'], 'generacion': 1},
    {'nombre': 'Charmander', 'numero': 4, 'tipos': ['Fuego'], 'generacion': 1},
    {'nombre': 'Squirtle', 'numero': 7, 'tipos': ['Agua'], 'generacion': 1},
    {'nombre': 'Jolteon', 'numero': 135,
        'tipos': ['Eléctrico'], 'generacion': 1},
    {'nombre': 'Lycanroc', 'numero': 745, 'tipos': ['Roca'], 'generacion': 7},
    {'nombre': 'Tyrantrum', 'numero': 697, 'tipos': [
        'Roca', 'Dragón'], 'generacion': 6},
    {'nombre': 'Mateo', 'numero': 12, 'tipos': [
        'Acero', 'Dragón'], 'generacion': 1},
]

arbol_nombre = ARBOLAVL()
arbol_tipo = ARBOLAVL()
arbol_numero = ARBOLAVL()

for pokemon in pokemons:
    arbol_nombre.insert_node(pokemon['nombre'], other_value=pokemon)
    arbol_numero.insert_node(pokemon['numero'], other_value=pokemon)
    for tipo in pokemon["tipos"]:
        arbol_tipo.insert_node(pokemon['nombre'], other_value=pokemons)


# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
# mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
# caracteres

print("--------------------------------")
print("Punto B:")
buscar_bul = arbol_nombre.proximity_search("Bul")
resultado = []

if buscar_bul is not None:
    resultado.append(buscar_bul.other_value)
else:
    print("No se encontró ningún Pokémon que contanga 'Bul'")
print(resultado)

# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
print("--------------------------------")
print("Punto C:")
tipos_a_buscar = ["Agua", "Fuego", "Planta", "Eléctrico"]

for pokemon in pokemons:
    for tipo in pokemon["tipos"]:
        nodo_existente = arbol_tipo.search(tipo)
        if nodo_existente is not None:
            nodo_existente.other_value.append(pokemon)
        else:
            arbol_tipo.insert_node(tipo, other_value=[pokemon])

for tipo in tipos_a_buscar:
    print(f"Pokémon de tipo {tipo}:")
    nodo_tipo = arbol_tipo.search(tipo)
    if nodo_tipo is not None:
        for pokemon in nodo_tipo.other_value:
            print(pokemon['nombre'])
    else:
        print(f"No se encontraron Pokémon de tipo {tipo}")

# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
# además un listado por nivel por nombre;

print("--------------------------------")
print("Punto D:")


# en orden ascendente por número


def inorden_por_numero(nodo):
    if nodo is not None:
        inorden_por_numero(nodo.left)
        print(f"Número: {nodo.value}, Nombre: {nodo.other_value['nombre']}")
        inorden_por_numero(nodo.right)


print("Listado por número ascendente:")
inorden_por_numero(arbol_numero.root)


# en orden ascendente por nombre


def inorden_por_nombre(nodo):
    if nodo is not None:
        inorden_por_nombre(nodo.left)
        print(f"Nombre: {nodo.value}, Número: {nodo.other_value['numero']}")
        inorden_por_nombre(nodo.right)


print("\nListado por nombre ascendente:")
inorden_por_nombre(arbol_nombre.root)


print("\nListado por nivel de profundidad por nombre:")
arbol_nombre.by_level()

# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
print("--------------------------------")
print("Punto E:")

mostrar_jolteon = arbol_nombre.proximity_search("Jolteon")
info_jolteon = []

if mostrar_jolteon is not None:
    info_jolteon.append(mostrar_jolteon.other_value)
else:
    print("No se encontro a 'Jolteon'")
print(info_jolteon)

print("--------------------------------")

mostrar_lycanroc = arbol_nombre.proximity_search("Lycanroc")
info_lycanroc = []

if mostrar_lycanroc is not None:
    info_lycanroc.append(mostrar_lycanroc.other_value)
else:
    print("No se encontro a 'Lycanroc'")
print(info_lycanroc)

print("--------------------------------")

mostrar_tyrantrum = arbol_nombre.proximity_search("Tyrantrum")
info_tyrantrum = []

if mostrar_tyrantrum is not None:
    info_tyrantrum.append(mostrar_tyrantrum.other_value)
else:
    print("No se encontro a 'Tyrantrum'")
print(info_tyrantrum)

print("--------------------------------")

# f) Determina cuantos Pokémons hay de tipo eléctrico y acero. 2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los

print("")
print("Punto F")

contar_tipos = ["Eléctrico", "Acero"]

for tipo in contar_tipos:
    nodo_tipo = arbol_tipo.search(tipo)
    if nodo_tipo is not None:
        cantidad = len(nodo_tipo.other_value)
        print(f"Cantidad de Pokémon de tipo {tipo}: {cantidad}")
    else:
        print(f"No se encontraron Pokémon de tipo {tipo}")
