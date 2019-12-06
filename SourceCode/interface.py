# import all data structures and algorithms
from adt.graph import Graph
from algorithm.algorithms import *
from plot.plot import *
from display.display import *

def main():
    whichType = int(input("Do you want to find optimal travel path? (1) or all travel paths? (2)\n"))
    print(" Destination options include: Buffalo, Erie, Harrisburgh, Meadville, NewYorkCity,  Pittsburgh,  Philadelphia, StateCollege, and WashingtonDC ")
    if(whichType == 1):
        source = str(input("Enter source (Starting Destination): "))
        destination = str(input("Enter destination (Ending Destination): "))

        map_of_cities = Graph()
        map_of_cities.makeGraphFromData('data')

        path_shortest = Dijkstra(map_of_cities,source.lower(),destination.lower())

        print("Here are the travel instructions for the optimal path \n\n")

        display_all_paths(path_shortest,destination.lower())

        plot(map_of_cities,path_shortest,destination.lower())
    elif(whichType == 2):


        budget = float(input("Enter a budget in $: "))

        time_taken = float(input("Enter the time taken in hours: "))

        source = str(input("Enter source : "))

        destination = str(input("Enter destination: "))

        map_of_cities = Graph()
        map_of_cities.makeGraphFromData('data')

        paths = find_all_paths(map_of_cities,source.lower(),destination.lower(), time_taken, budget)

        plot(map_of_cities,paths,destination.lower())

        print("Here are the travel instructions")

        display_all_paths(paths,destination.lower())
    else:
        print("WRONG OPTION!")

if __name__ == '__main__':
    main()
