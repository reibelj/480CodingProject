import numpy as np

#Modified Dijkstra's algorithm for our graph
def Dijkstra(graph,source,destination):


    #dist is for time and cost is for the total cost
    dist = {}
    previous = {}
    cost = {}

    #two separate dictionaries which get updated at the
    #end of each iteration and are solely used for the purposes
    #of priting optimal cost and time
    dist_disp = {}
    cost_disp = {}

    for city in graph.list_of_cities:
        dist[city.name] = float("Inf")
        previous[city.name] = None
        cost[city.name] = float("Inf")
        dist_disp[city.name] = float("Inf")
        cost_disp[city.name] = float("Inf")


    dist[source] = 0
    cost[source] = 0

    dist_disp[source]=0
    cost_disp[source] = 0

    visited = []

    #print cost

    while(len(visited) != len(graph.list_of_cities)):
        #find node with minimum time
        current = min(dist, key=dist.get)

        #get all neighbors
        neighbors_plane = graph.adjacencyListPlane.get(current)
        neighbors_bus = graph.adjacencyListBus.get(current)
        neighbors_train = graph.adjacencyListTrain.get(current)


        if neighbors_plane == None:
            neighbors_plane = []

        if neighbors_train == None:
            neighbors_train = []

        if neighbors_bus == None:
            neighbors_bus = []

        #perform Dijkstra's for all neighbors separately by transit type
        for i in range(0,len(neighbors_plane)):
            neighbor = neighbors_plane[i]

            if(neighbor[0] in visited):
                continue

            if((dist[current] + neighbor[1]) <= dist[neighbor[0]] and ((cost[current] + neighbor[2]) < cost[neighbor[0]])):

                dist[neighbor[0]] = dist[current] + neighbor[1]
                cost[neighbor[0]] = cost[current] + neighbor[2]
                previous[neighbor[0]] = [current,'p']
            elif((dist[current] + neighbor[1]) < dist[neighbor[0]] or ((cost[current] + neighbor[2]) < cost[neighbor[0]])):
                dist[neighbor[0]] = dist[current] + neighbor[1]
                cost[neighbor[0]] = cost[current] + neighbor[2]
                previous[neighbor[0]] = [current,'p']

        for i in range(0,len(neighbors_train)):
            neighbor = neighbors_train[i]

            if(neighbor[0] in visited):
                continue

            if((dist[current] + neighbor[1]) <= dist[neighbor[0]] and ((cost[current] + neighbor[2]) < cost[neighbor[0]]) ):

                #print("train")
                dist[neighbor[0]] = dist[current] + neighbor[1]
                cost[neighbor[0]] = cost[current] + neighbor[2]
                previous[neighbor[0]] = [current,'t']
            elif((dist[current] + neighbor[1]) < dist[neighbor[0]] or ((cost[current] + neighbor[2]) < cost[neighbor[0]]) ):
                dist[neighbor[0]] = dist[current] + neighbor[1]
                cost[neighbor[0]] = cost[current] + neighbor[2]
                previous[neighbor[0]] = [current,'t']

        for i in range(0,len(neighbors_bus)):
            neighbor = neighbors_bus[i]

            if(neighbor[0] in visited):
                continue

            if((dist[current] + neighbor[1]) <= dist[neighbor[0]] and ((cost[current] + neighbor[2]) < cost[neighbor[0]])):
                #print("bus")
                dist[neighbor[0]] = dist[current] + neighbor[1]
                cost[neighbor[0]] = cost[current] + neighbor[2]
                previous[neighbor[0]] = [current,'b']
            elif((dist[current] + neighbor[1]) < dist[neighbor[0]] or ((cost[current] + neighbor[2]) < cost[neighbor[0]])):
                dist[neighbor[0]] = dist[current] + neighbor[1]
                cost[neighbor[0]] = cost[current] + neighbor[2]
                previous[neighbor[0]] = [current,'b']

        visited.append(current)
        dist_disp.update(dist)
        cost_disp.update(cost)
        del dist[current]

    curr_c = destination
    #print previous
    route = []

    #print(cost)

    #print(previous)


    #route to destination
    while(curr_c != source):
        route.append(previous[curr_c])
        curr_c = previous[curr_c][0]

    route = list(reversed(route))

    route.append([destination,'f'])


    print("Optimal cost for reaching " + destination + " is $ "+ str(cost_disp[destination]))
    print("Optimal time for reaching " + destination + " is "+ str(dist_disp[destination]))


    return [route]



def find_all_paths_util(graph,source,destination,visited,path,all_paths,count):

    visited[source] = True

    path.append(source)
    #if destination found, append that path to the all_paths list
    if (source == destination):
        all_paths[0] +=path
        count[0]+=1

    else:
        #getting all neighbors and pooling them together
        neighbor_p = [i[0] for i in graph.adjacencyListPlane.get(source,[])]
        neighbor_b = [i[0] for i in graph.adjacencyListBus.get(source,[])]
        neighbor_t = [i[0] for i in graph.adjacencyListTrain.get(source,[])]

        all_neighbors = []

        for c in neighbor_p:
            if(not (c in all_neighbors)):
                all_neighbors.append(c)

        for c in neighbor_b:
            if(not (c in all_neighbors)):
                all_neighbors.append(c)

        for c in neighbor_t:
            if(not (c in all_neighbors)):
                all_neighbors.append(c)


        for n in all_neighbors:
            if(visited[n] == False):
                 find_all_paths_util(graph,n,destination,visited,path,all_paths,count)

    path.pop()
    visited[source] = False

def find_all_paths(graph,source,destination,time_constraint,budget):
    visited = {}

    for city in graph.list_of_cities:
        visited[city.name]  = False


    path = []

    count= [0]
    all_paths_temp = [[]]
    find_all_paths_util(graph,source,destination,visited,path,all_paths_temp,count)


    #arranging all paths as separate lists inside of a list
    all_paths_np = np.array(all_paths_temp[0])


    indices = np.where(all_paths_np == destination)[0]

    all_paths = []
    start = 0
    for ii in indices:
        all_paths.append(all_paths_temp[0][start:(ii+1)])
        start = ii+1

    #perform optimization and return paths satisfied by user constraints
    return arrange_all_paths_by_transit_type(graph,all_paths,destination,time_constraint,budget)

    #return path_with_transit

def arrange_all_paths_by_transit_type(graph,all_paths,destination,time_constraint,budget):
    path_with_transit = []
    for path in all_paths:

        flag_path_exists =True
        current_path = []
        city_count = 0
        time_taken = 0
        cost = 0
        for city in path:

            #getting neighbors and finding time and cost taken by taking a par-
            #ticular transit type to that neighbor

            if(city == destination):
                current_path.append([destination,'f'])
                break
            plane = graph.adjacencyListPlane.get(city)
            train = graph.adjacencyListTrain.get(city)
            bus = graph.adjacencyListBus.get(city)

            #to check if that mode of transit exists

            flag_planeExists = False
            flag_trainExists = False
            flag_busExists = False

            #if doesn't exist, time taken and cost is inf

            temp_cost_train = float("inf")
            temp_cost_plane = float("inf")
            temp_cost_bus = float("inf")

            temp_time_train = float("inf")
            temp_time_plane = float("inf")
            temp_time_bus = float("inf")

            #current_city_transit = [city]


            if(not(plane == None)):
                neighbor = [x[0] for x in plane]
                if(path[city_count+1] in neighbor):
                    index = neighbor.index(path[city_count+1])

                    temp_time_taken = time_taken + plane[index][1]
                    temp_cost = cost + plane[index][2]

                    if(temp_time_taken <= time_constraint and temp_cost <= budget):
                        temp_time_plane = temp_time_taken
                        temp_cost_plane = temp_cost
                        flag_planeExists = True
                            #current_path.append((city,'p'))
                        #current_city_transit.append('p')

            if(not(train == None)):
                neighbor = [x[0] for x in train]
                if(path[city_count+1] in neighbor):
                    index = neighbor.index(path[city_count+1])

                    temp_time_taken = time_taken + train[index][1]
                    temp_cost = cost + train[index][2]

                    if(temp_time_taken <= time_constraint and temp_cost <= budget):
                        temp_time_train = temp_time_taken
                        temp_cost_train = temp_cost
                        flag_trainExists = True

                        #current_path.append((city,'t'))
                        #current_city_transit.append('t')


            if(not(bus == None)):
                neighbor = [x[0] for x in bus]
                if(path[city_count+1] in neighbor):
                    index = neighbor.index(path[city_count+1])

                    temp_time_taken = time_taken + bus[index][1]
                    temp_cost = cost + bus[index][2]

                    if(temp_time_taken <= time_constraint and temp_cost <= budget):
                        temp_time_bus = temp_time_taken
                        temp_cost_bus = temp_cost
                        flag_busExists = True

                        #current_path.append((city,'b'))
                        #current_city_transit.append('b')



            if(flag_busExists or flag_trainExists or flag_planeExists):
                #find most optimal medium of transit

                current_city_transit = [city]
                city_count += 1
                transit_list = ['b','t','p']
                cost_list = [temp_cost_bus , temp_cost_train ,temp_cost_plane]
                time_taken_list = [temp_time_bus , temp_time_train , temp_cost_plane]

                cheapest_i = cost_list.index(min(cost_list))
                fastest_i = time_taken_list.index(min(time_taken_list))

                cheapest_trans = transit_list[cheapest_i]
                fastest_trans = transit_list[fastest_i]
                #if cheapest transit and fastest transit are same, choose that
                if(cheapest_trans == fastest_trans):
                    cost = cost_list[cheapest_i]
                    time_taken = time_taken_list[fastest_i]
                    current_city_transit.append(cheapest_trans)
                else:
                    #choose fastest transit available if they're not the same
                    cost = cost_list[fastest_i]
                    time_taken = time_taken_list[fastest_i]
                    current_city_transit.append(fastest_trans)

                current_path.append(current_city_transit)

            else:
                flag_path_exists = False
                break

        if(flag_path_exists):
            path_with_transit.append(current_path)

    if (len(path_with_transit) == 0):
        print("No paths found with given budget and time!!!!")

    return path_with_transit
