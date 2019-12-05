# Test case that determines correctness of the implementation of Dijkstras algorithm.
from adt.graph import Graph
from algorithm.algorithms import *
from display.display import *
map_of_cities = Graph()
map_of_cities.makeGraphFromData('data')

path = Dijkstra(map_of_cities,'mead','nyc')

print path

display_all_paths(path,'nyc')
