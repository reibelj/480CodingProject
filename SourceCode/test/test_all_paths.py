from adt.graph import Graph
from algorithm.algorithms import *
from plot.plot import *
from display.display import *

map_of_cities = Graph()
map_of_cities.makeGraphFromData('data')

#path = Dijkstra(map_of_cities,'mead','harr')
path = find_all_paths(map_of_cities,'mead','nyc',8,250)
print path


display_all_paths(path,'nyc')

#mod_path = get_distinct_paths(path,'pitt')
#print mod_path
#plot(map_of_cities,path,'nyc')

#print(map_of_cities.adjacencyListTrain)
#print(map_of_cities.adjacencyListPlane)
#print(map_of_cities.adjacencyListBus)
#names_of_cities = [x.name for x in map_of_cities.list_of_cities]
#print(names_of_cities)
