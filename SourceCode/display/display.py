#HONOR CODE: This work is ours unless cited.
from __future__ import print_function

def display_all_paths(path_list,destination):

    path_count = 0

    for path in path_list:

        print("ROUTE {} [plotted at map{}.html]".format(path_count,path_count))
        print('---------------------------------------')

        city_count = 0
        for city in path:
            if(city_count < (len(path) - 1)):
                for i in range(1,len(city)):
                    transit = None
                    if(city[i] == 'b'):
                        transit = "bus"
                    elif(city[i] == 't'):
                        transit = "train"
                    else:
                        transit = "plane"
                    print("Take {} from {} to {}".format(transit,city[0],path[city_count+1][0]))
            else:
                print("You have reached {}!!".format(destination))
            city_count+=1

        path_count += 1
    pass


