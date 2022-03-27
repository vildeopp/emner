from route_operators import split_routes, full_route


def valid(solution, vesselCargo, num_vehicles):
    vehicle = 1
    for call in solution: 
        
        if call == 0: 
            vehicle += 1 
            if vehicle == num_vehicles: 
                break
            continue
        valid_calls = vesselCargo[vehicle-1]
        if valid_calls[call-1] != 1: 
            return False
    
    return True






