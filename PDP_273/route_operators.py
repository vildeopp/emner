import copy
import random

from PDP_utils import feasibility_check, cost_function


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
            

def get_expense_of_not_transporting_calls( problem: dict) -> dict:
    expenses = {}
    cargo = problem['Cargo']
    for c in range(problem["n_calls"]):
        expenses[c+1] = cargo[c][3]
    return dict(sorted(expenses.items(), key = lambda item: item[1], reverse=True))

def choose_call_to_insert(expenses: dict): 
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
    costs = find_cheapest_transport()

    p = random.uniform(0,1)
    if p < 0.8: 
        return list(costs.keys())[0]
    elif 0.8 < p < 0.9: 
        return list(costs.keys())[0]
    else: 
        return random.choice(list(costs.keys()))


def cost_of_calls_vehicle(v_route: list, v_id: int, problem: dict) -> dict: 
    """ Chosen the cost to be the port cost of the call and the transport cost 
    from pickup to delivery if they are rigth after eachother, if the vehicle is dummy return the costs of not transporting"""

    call_info = problem['Cargo']
    port_cost = problem['PortCost']
    travel_cost = problem['TravelCost']

    if v_id == problem['n_vehicles']: 
        return get_expense_of_not_transporting_calls(problem)

    costs = {}

    for c in set(v_route):
        pickup_node = int(call_info[c][0])
        delivery_node = int(call_info[c][1])

        travel_cost_pd = travel_cost[v_id-1, pickup_node-1, delivery_node-1]
        cost_pickup_delivery = port_cost[v_id, c]
        cost_sum = sum([travel_cost_pd, cost_pickup_delivery])

        costs[c] = cost_sum
    
    return dict(sorted(costs.items(), key = lambda item: item[1], reverse=True))

def choose_call(v_id:int, v_route: list, problem: dict) -> dict: 
    """Makes sure that the most expensive call isn't allways chosen"""
    costs = cost_of_calls_vehicle(v_route, v_id, problem)
    print("costs", costs)

    p = random.uniform(0,1)
    if len(v_route) > 4: 
        print("more than two calls in route")
        if p < 0.7: 
            print("most expensive")
            return list(costs.keys())[0]
        elif 0.7 < p < 0.9: 
            print("second most expensive")
            return list(costs.keys())[1]
        else: 
            print("random choice")
            return random.choice(list(costs.keys()))
    else: 
        print("not more than two calls in route")
        return list(costs.keys())[0]
    
