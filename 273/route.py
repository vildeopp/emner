
def call_to_nodes(problem, calls): 
    call_info = problem['call_info']
    pickup = []
    route = []
    for c in calls: 
        if c == 0: 
            route.append(0)
            continue 
        call = call_info.get(c)
        if c not in pickup: 
            pickup.append(c)
            route.append(call[0])
        else: 
            route.append(call[1])
    return route

def get_vehiclecalls_aslist(calls:list):
    vehicle_calls = []
    all_calls = []
    for c in calls:
        if c == 0:
            all_calls.append(vehicle_calls)
            vehicle_calls = []
            continue
        vehicle_calls.append(c)
    all_calls.append(vehicle_calls)
    return all_calls

def get_vehicle_calls(calls:list, vehicle: int):
    return get_vehiclecalls_aslist(calls)[vehicle-1]

def get_vehiclesroutes_aslist(route):
    vehicle_route = []
    all_routes = []
    for node in route: 
        if node == 0: 
            all_routes.append(vehicle_route)
            vehicle_route = []
            continue
        vehicle_route.append(node)
    return all_routes


