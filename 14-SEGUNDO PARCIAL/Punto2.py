from grafo import Graph

# 2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los
# algoritmos necesarios para resolver las siguientes tareas:

# a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
# cantidad de episodios en los que aparecieron juntos ambos personajes que se
# relacionan;

# b) hallar el árbol de expansión minino y determinar si contiene a Yoda;

# c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son.

# d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda,
# Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.

grafo = Graph(dirigido=False)

personajes = ["Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO", "Leia",
              "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"]

for personaje in personajes:
    grafo.insert_vertice(personaje)

grafo.insert_arista("Luke Skywalker", "Darth Vader", 4)
grafo.insert_arista("Luke Skywalker", "Leia", 5)
grafo.insert_arista("Luke Skywalker", "Yoda", 3)
grafo.insert_arista("Luke Skywalker", "Han Solo", 4)
grafo.insert_arista("Luke Skywalker", "C-3PO", 5)
grafo.insert_arista("Luke Skywalker", "R2-D2", 5)
grafo.insert_arista("Darth Vader", "Leia", 2)
grafo.insert_arista("Darth Vader", "Yoda", 1)
grafo.insert_arista("Darth Vader", "Boba Fett", 2)
grafo.insert_arista("Leia", "Han Solo", 5)
grafo.insert_arista("Leia", "C-3PO", 5)
grafo.insert_arista("Leia", "R2-D2", 5)
grafo.insert_arista("Han Solo", "Chewbacca", 6)
grafo.insert_arista("Han Solo", "C-3PO", 4)
grafo.insert_arista("Han Solo", "R2-D2", 4)
grafo.insert_arista("C-3PO", "R2-D2", 6)
grafo.insert_arista("Yoda", "Chewbacca", 2)
grafo.insert_arista("Yoda", "Rey", 1)
grafo.insert_arista("Rey", "Kylo Ren", 3)
grafo.insert_arista("Rey", "BB-8", 3)
grafo.insert_arista("Kylo Ren", "BB-8", 1)
grafo.insert_arista("Kylo Ren", "Darth Vader", 1)
grafo.insert_arista("Chewbacca", "R2-D2", 3)
grafo.insert_arista("Chewbacca", "Leia", 4)

# b) hallar el árbol de expansión minino y determinar si contiene a Yoda;

arbol_expansion_minima = grafo.kruskal("Yoda")
print("El arbol de expansion minima es:")
print("")
print(arbol_expansion_minima)
print("")

for pj in arbol_expansion_minima:
    if "Yoda" in pj:
        print(f"Yoda está en el árbol de expansión mínima")
        break

print("-------------------------------------------------")

# c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son.
print("Punto C")
personajes_episodeos = 0
comparten = None

for nodo in grafo.elements:
    for aristas in nodo['aristas']:
        if aristas['peso'] > personajes_episodeos:
            personajes_episodeos = aristas['peso']
            comparten = (nodo['value'], aristas['value'])

print(
    f"Los personajes que comparten episodeos son {comparten} y comparten {personajes_episodeos} episodeos")
# print("Máximo número de episodios compartidos:", personajes_episodeos)
# print("")
# print("Personajes que los comparten:", comparten)
# print("")
print("------------------------------------------------")
