import route as r
import read_data as read

problem = read.read_problem()

def time_feasability(solution: list, vehicle: int):
    #the info from problem reading
    vehicle_info = problem['vehicle_info'].get(vehicle)
    calls_info = problem['call_info']
    travel_time = problem['travel_cost']
    node_info = problem['node_time_cost']

    route_calls = r.get_vehicle_calls(solution, vehicle) # the route represented as calls
    route_nodes = r.call_to_nodes(problem, route_calls) #route represented as nodes

    if not route_nodes:
        #print("no nodes in car's route")
        return True

    start_node = vehicle_info[0]
    dest_node = route_nodes.pop(0) #first element of the list

    time_used = vehicle_info[1] #adds the start time to the vehicle as the inital time
    picked_up = [] #the calls that are picked up, but not yet delivered
    for i, calls in enumerate(route_calls):
        c_info = calls_info.get(calls)

        if i == 0:
            key = (vehicle, start_node, dest_node)
            time_used += travel_time.get(key)[0]

        start_node = dest_node
        try:
            dest_node = route_nodes.pop(0)
        except IndexError as e:
            dest_node = None
        try:
            key = (vehicle, start_node, dest_node)
            time_used += travel_time.get(key)[0]
        except TypeError as e:
            break

        if dest_node is None: #if at the end of the route breaks the loop
            break

        key = (vehicle, calls)

        if calls not in picked_up and dest_node is not None:
            picked_up.append(calls)
            lw_tm_wd = c_info[4] #lower timewindow
            up_tm_wd = c_info[5] #upper timewindow

            if time_used < lw_tm_wd:
                #print("lower window for pickup")
                wait = lw_tm_wd - time_used
                time_used += wait
            if time_used > up_tm_wd:
                #print("upper window for pickup")
                return False

            time_used += node_info.get(key)[0]
        else:
            picked_up.remove(calls)
            lw_tm_wd = c_info[6] #lower timewindow
            up_tm_wd = c_info[7] #upper timewindow
            if time_used < lw_tm_wd:
                #print("lower window for delivery")
                wait = lw_tm_wd - time_used
                time_used += wait
            if time_used > up_tm_wd:
                #print("upper window for delivery")
                return False
            time_used += node_info.get(key)[2]

    return time_used, True




