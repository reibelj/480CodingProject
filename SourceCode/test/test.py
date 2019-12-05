#Test case that handles generalized testing of the graph
from adt.graph import Graph

map_of_cities = Graph()
map_of_cities.makeGraphFromData('data')

print(map_of_cities.adjacencyListTrain)
print(map_of_cities.adjacencyListPlane)
print(map_of_cities.adjacencyListBus)
names_of_cities = [x.name for x in map_of_cities.list_of_cities]
print(names_of_cities)
