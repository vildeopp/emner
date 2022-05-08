import copy
import random
import sys

from PDP_utils import feasibility_check, cost_function
from own_utils import cost_route


def split_routes(route):
    routes = []
    vehicle = []
    count = 0
    for call in route:
        if call == 0:
            routes.append(vehicle)  # adds vehicle to route
            count += 1
            vehicle = []  # changes vehicle
            continue
        vehicle.append(call)  # adds call to vehicle
    routes.append(vehicle)  # adds the last vehicle to the route
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

def get_routes_with_zero(solution): 
    routes = []
    vehicle = []
    for call in solution: 
        if call == 0: 
            vehicle.append(call)
            routes.append(vehicle)
            vehicle = []
            continue
        vehicle.append(call)
    routes.append(vehicle)
    return routes
            

def get_expense_of_not_transporting_calls(problem) -> dict:
    expenses = {}
    cargo = problem['Cargo']
    for c in range(problem["n_calls"]):
        expenses[c+1] = cargo[c][3]
    return dict(sorted(expenses.items(), key = lambda item: item[1], reverse=True))

def choose_call_from_dummy(problem): 
    expenses = get_expense_of_not_transporting_calls(problem)
    p = random.uniform(0,1)

    if p < 0.7: 
        return list(expenses.keys())[0]
    elif 0.7 < p < 0.2: 
        return list(expenses.keys())[1]
    elif 0.9 < p < 0.95: 
        return list(expenses.keys())[2]
    else: 
        return random.choice(list(expenses.keys())[2:])


def find_cheapest_transport(call:int, problem: dict) -> dict: 
    """ Finds the expenses of transporting a call for each vehicle and 
    returns a dict of the expenses sorted from lowest to highest """

    num_vehicles = problem['n_vehicles']
    call_info = problem['Cargo']
    port_cost = problem['PortCost']
    travel_cost = problem['TravelCost']
    vessel_cargo = problem['VesselCargo']

    pickup_node = int(call_info[call-1][0])
    delivery_node = int(call_info[call-1][1])
    
    #the sum of pickup cost driving to delivery node from pickup node and delivery cost
    costs = {}
    for vehicle in range(num_vehicles): 
        if not bool(vessel_cargo[vehicle, call-1]): 
            continue
        else: 
            travel_cost_pd = travel_cost[vehicle,pickup_node-1,delivery_node-1]
            cost_pickup_delivery = port_cost[vehicle, call-1]
            cost_sum = sum([travel_cost_pd, cost_pickup_delivery])
            costs[vehicle] = cost_sum

    costs[num_vehicles] = problem['Cargo'][call-1,3]

    return dict(sorted(costs.items(), key = lambda item: item[1], reverse=False))


def choose_vehicle(call:int, problem: dict) -> int: 
    """Makes sure that the cheapest vehicle to insert into isn't allways chosen"""
    costs = find_cheapest_transport(call, problem)
    return list(costs.keys())[0]

def vehcile(call: int, solution_wo_call: list, problem: dict) -> tuple: 
    num_vehicles = problem["n_vehicles"]
    vesselcomp = problem["VesselCargo"]
    split = split_routes(solution_wo_call)
    car = 0
    vehicles = []
    for route in split:
        car += 1
        if car-1 == num_vehicles: 
            break
        if not bool(vesselcomp[car-1, call-1]):
            vehicles.append(([], sys.maxsize)) 
            continue
        
        if not route:
            n_route = copy.deepcopy(route)
            n_route.append(call)
            n_route.append(call) 
            cost = cost_route(n_route,car, problem)
            vehicles.append([n_route, cost])

        else: 
            routes = []
            for pos_i in range(len(route)):
                new_new_route = copy.deepcopy(route)
                new_new_route.insert(pos_i, call)
                new_new_route.insert(pos_i+1, call)
                routes.append(new_new_route)

            costs = list(map(lambda p: cost_route(p, car, problem), routes))
            indx_cheapest = costs.index(min(costs))
            vehicles.append((routes[indx_cheapest], min(costs)))
    
    #print("cars", vehicles)
    
    prices = [p for r,p in vehicles]
    #print("price", prices)
    cheap = prices.index(min(prices))
    return (vehicles[cheap][0], cheap)


def cost_of_calls_vehicle(v_route: list, v_id: int, problem: dict) -> dict: 
    """ Chosen the cost to be the port cost of the call and the transport cost 
    from pickup to delivery if they are rigth after eachother, if the vehicle is dummy return the costs of not transporting"""

    call_info = problem['Cargo']
    port_cost = problem['PortCost']
    travel_cost = problem['TravelCost']
    cargo = problem['Cargo']

    if not v_route: 
        return None
    
    v_id = v_id
    costs = {}
    if v_id == problem['n_vehicles']: 
        for c in set(v_route): 
            costs[c] = cargo[c-1]
        return costs
   
    for c in set(v_route):
        pickup_node = int(call_info[c-1][0])
        delivery_node = int(call_info[c-1][1])

        travel_cost_pd = travel_cost[v_id-1, pickup_node-1, delivery_node-1]
        cost_pickup_delivery = port_cost[v_id-1, c-1]
        cost_sum = sum([travel_cost_pd, cost_pickup_delivery])

        costs[c] = cost_sum
    
    return dict(sorted(costs.items(), key = lambda item: item[1], reverse=True))

def choose_call(v_id:int, v_route: list, problem: dict) -> int: 
    """Makes sure that the most expensive call isn't allways chosen"""
    costs = cost_of_calls_vehicle(v_route, v_id, problem)
    if not v_route: 
        return None
    p = random.uniform(0,1)
    if len(v_route) > 4: 
        if p < 0.7: 
            return list(costs.keys())[0]
        elif 0.7 < p < 0.9: 
            return list(costs.keys())[1]
        else: 
            return random.choice(list(costs.keys()))
    else: 
        return list(costs.keys())[0]

def most_expensive_for_each_car(solution, problem): 
    most_expensive = {}
    routes = split_routes(solution)
    for v in range(problem['n_vehicles']+1):  #including dummy
        costs = cost_of_calls_vehicle(routes[v], v, problem)
        if not costs: 
            continue
        most_expensive[v+1] = list(costs.keys())[0]

    return most_expensive

    
