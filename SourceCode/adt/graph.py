#HONOR CODE: This work is ours unless cited
from __future__ import print_function
from node import Node
import os

# Graph data structure
class Graph(object):
    __instance__ = None

    #Contains graphs based on transit type
    def __init__(self):
        self.adjacencyListPlane = {}
        self.adjacencyListBus = {}
        self.adjacencyListTrain = {}

        self.list_of_cities = []

    def __add__node__to__transit__graph__(self,node,dest,time_taken,cost,transit_adjacency_list):
        neighbors = []
        if node.name in transit_adjacency_list:
            neighbors = transit_adjacency_list[node.name]
            neighbors.append((dest.lower(),time_taken,cost))
        else:
            neighbors.append((dest.lower(),time_taken,cost))

        transit_adjacency_list[node.name] = neighbors
        pass

    def __add__node__to__graph__(self,node,dest,time_taken,cost):
        if(node.coordinates == None or node.transit_type == None or
                node.name == None):
            raise Exception("Node does not have sufficient data! Exiting...")
        else:
            if(node.transit_type == 't'):
                self.__add__node__to__transit__graph__(node,dest,time_taken,cost,self.adjacencyListTrain)
            elif(node.transit_type == 'b'):
                self.__add__node__to__transit__graph__(node,dest,time_taken,cost,self.adjacencyListBus)
            elif(node.transit_type == 'p'):
                self.__add__node__to__transit__graph__(node,dest,time_taken,cost,self.adjacencyListPlane)
            else:
                raise Exception("Node transit type is unidentified!! Exiting...")


    #Data needs to be present in a folder with files b.dat, p.dat, and t.dat
    def __read__data__file__(self,f,transit_type):
        if(not os.path.exists(f)):
            print("{} datafile not found".format(transit_type))
            return


        data_file = open(f,'r')


        for line in data_file.readlines():
            l = line.rstrip()
            params = l.split(',')
            #print(params)
            source = str(params[0]).upper()
            destination = str(params[1]).upper()
            latitude_source = float(params[2])
            longitude_source = float(params[3])
            coordinates_source = (longitude_source,latitude_source)

            latitude_destination = float(params[4])
            longitude_destination = float(params[5])
            coordinates_destination = (longitude_destination, latitude_destination)


            time_taken = float(params[6])
            cost = float(params[7])

            node_source = Node(source,coordinates_source,transit_type)
            node_destination = Node(destination,coordinates_destination,transit_type)
            if (not (node_source in self.list_of_cities)):
                self.list_of_cities.append(node_source)

            if (not (node_destination in self.list_of_cities)):
                self.list_of_cities.append(node_destination)

            self.__add__node__to__graph__(node_source,destination,time_taken,cost)
            self.__add__node__to__graph__(node_destination,source,time_taken,cost)



    #Default data dir is just 'data'
    def makeGraphFromData(self,data_dir='../data'):
        data_dir_exists = os.path.exists(data_dir)
        if (not data_dir_exists):
            raise Exception("data directory is unrecognized!!! Exiting...")
        else:
            f_t = "{}/t.dat".format(data_dir)
            f_b = "{}/b.dat".format(data_dir)
            f_p = "{}/p.dat".format(data_dir)

            self.__read__data__file__(f_t,'t')
            self.__read__data__file__(f_b,'b')
            self.__read__data__file__(f_p,'p')





