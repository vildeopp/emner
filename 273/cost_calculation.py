import route as r

def total_cost_cal(problem, solution): 

    #gets the routes as nodes and seperated for each vehicle
    full_route = r.call_to_nodes(problem, solution)
    vehicles_routes = r.get_vehiclesroutes_aslist(full_route)
    total_cost = 0

    travel_cost = problem['travel_cost']
    node_cost = problem['node_time_cost']

    curr_vehicle = 0

    for vehicle_route in vehicles_routes: 
        curr_vehicle += 1
        if curr_vehicle > problem['vehicles']: 
            break
        if not vehicle_route: 
            continue
        
        vehicle_info = problem["vehicle_info"].get(curr_vehicle)
        curr_node = vehicle_info[0] #start with vehicle home node
        for i in range(len(vehicle_route)): 
            #calculates the travelcost between nodes 
            key = (curr_vehicle, curr_node, vehicle_route[0]) 
            total_cost += travel_cost[key][1] #adds to the travel cost
            try:
                curr_node = vehicle_route.pop(0) #removes head of the list
            except IndexError as e: 
                curr_node = -1

    #need to calculate the cost to pick up and deliver from nodes
        calls_pickedup = []
        
        for call_index in range(len(solution)): 
            if solution[call_index] == 0: 
                continue
            key = (curr_vehicle, solution[call_index])
            if solution[call_index] not in calls_pickedup: 
                calls_pickedup.append(solution[call_index])
                pickup_cost = node_cost.get(key)[1]
                total_cost += pickup_cost
            else:
                delivery_cost = node_cost.get(key)[3]
                total_cost += delivery_cost

    #Dummy vehicle
    dummy_cost = 0 # the cost of not transporting a call
    call_info = problem['call_info']
    dummy_transport = solution[::-1]
    dummy_pickup = []
    for calls in dummy_transport: 
        if calls == 0: 
            break
        if calls not in dummy_pickup: 
            dummy_pickup.append(calls)
        
    for p in dummy_pickup: 
        dummy_cost += call_info.get(p)[3]
    
    total_cost += dummy_cost
    return total_cost



        


