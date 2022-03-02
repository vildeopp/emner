
def split_routes(route): 
    routes = []
    vehicle = []
    count = 0
    for call in route:  
        if call == 0: 
            routes.append(vehicle) #adds vehicle to route 
            count += 1 
            vehicle = [] #changes vehicle
            continue
        vehicle.append(call) #adds call to vehicle
    routes.append(vehicle) #adds the last vehicle to the route
    return routes

def full_route(routes, data):
    route = []
    for i in range(len(routes)):
        if i == data['n_vehicles']:
            route = route + routes[i]
        else:
            route = route + routes[i]
            route.append(0)
    return route
