#HONOR CODE: This work is ours unless cited

def plot(graph,path_list,destination):
    mod_path = []
    for path in path_list:
        cur_path = []
        for i in range(0,len(path)):
            if(not (path[i][0] in cur_path)):
                cur_path.append(path[i][0])

        mod_path.append(cur_path)
    #print("here")
    count = 0
    for path in mod_path:
        longitude_list = []
        latitude_list = []
        for city in path:
            node = None
            for i in range(0,len(graph.list_of_cities)):
                if(city == graph.list_of_cities[i].name):
                    node = graph.list_of_cities[i]
                    break

            coordinates  = node.coordinates
            longitude_list.append(coordinates[0])
            latitude_list.append(coordinates[1])

        print (longitude_list,latitude_list)
