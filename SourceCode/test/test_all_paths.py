# Test case to determine if all of the paths are determined correctly
from adt.graph import Graph
from algorithm.algorithms import *
from plot.plot import *
from display.display import *

map_of_cities = Graph()
map_of_cities.makeGraphFromData('data')

path = find_all_paths(map_of_cities,'mead','nyc',8,250)
print path


display_all_paths(path,'nyc')
