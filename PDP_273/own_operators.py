import random
import sys
from itertools import permutations
import copy

import numpy as np
from route_operators import split_routes, full_route, get_expense_of_not_transporting_calls, choose_call, choose_vehicle

from PDP_utils import cost_function, feasibility_check
from own_utils import cost_route
from operators import reinsert
from PDP_utils import cost_function, feasibility_check


def replace_vehicles_calls(solution, problem):
    routes = split_routes(solution)

    length = list(map(len, routes))

    vehicle_remove = length.index(max(length))
    remove = routes[vehicle_remove]
    vehicle = length.index(min(length))
    add = routes[vehicle]

    call = random.choice(remove)
    vesselCargo = problem['VesselCargo']
    pos_calls = remove
    if vesselCargo[vehicle, call - 1] == float(1):
        remove = [x for x in remove if x != call]
    else:
        for _ in range(10):  # tries to find valid call to put into smallest route
            call = random.choice(remove)
            if vesselCargo[vehicle, call - 1] == float(1):
                remove = [x for x in remove if x != call]
                break
            pos_calls = [x for x in pos_calls if x != call]  # removes the call if it is not possible to add it to vehicle
            if not pos_calls:
                return solution

    if len(add) < 2:
        add.append(call)
        add.append(call)
    else:
        add.insert(random.randrange(0, len(add)), call)
        add.insert(random.randrange(0, len(add)), call)

    routes[vehicle_remove] = remove
    routes[vehicle] = add

    return full_route(routes, problem)


def two_exchange_reinsert(solution, problem):
    """Measure the length of each route and takes the shortest and the longest, if the shortest have 0 calls
    takes one from the longest and adds to that vehicle. If both routes has more than one call
    do not include dummy pr. now"""

    solution = reinsert(solution, problem)
    routes = split_routes(solution)
    lengths = list(map(len, routes[0:problem['n_vehicles']]))

    max_len = max(lengths)
    min_len = min(lengths)

    v1 = lengths.index(max_len)
    v2 = lengths.index(min_len)

    if max_len == 0:
        return full_route(routes, problem)

    vesselCargo = problem['VesselCargo']

    #When to reinsert? -> when the smallest list is empty? (some kind of ratio between max and min length)
    if abs(max_len-min_len) > problem['n_calls']/2:
        v1_route = routes[v1]
        elem = random.choice(v1_route)
        for _ in range(10): #try 10 times to find å feasible call
            if bool(vesselCargo[v2, elem-1]):
                break
            else:
                elem = random.choice(v1_route)

        v1_route = [x for x in v1_route if x != elem]
        routes[v1] = v1_route
        v2_route = routes[v2]

        v2_route.append(elem)
        v2_route.append(elem)

        routes[v2] = v2_route
    else:

        v1_route = routes[v1]
        v2_route = routes[v2]

        if len(v1_route) > 2 and len(v2_route) > 2:
            elem1 = random.choice(v1_route)

            #looks for valid calls
            for _ in range(10):
                if bool(vesselCargo[v2, elem1-1]):
                    break
                else:
                    elem1 = random.choice(v1_route)

            elem2 = random.choice(v2_route)
            for _ in range(10):
                if bool(vesselCargo[v1, elem2-1]):
                    break
                else:
                    elem2 = random.choice(v2_route)

            if not bool(vesselCargo[v1, elem2-1]) or not bool(vesselCargo[v2,elem1-1]):
                return full_route(routes, problem)

            for i1, c1 in enumerate(v1_route):
                if c1 == elem1:
                    v1_route[i1] = elem2
            for i2, c2 in enumerate(v2_route):
                if c2 == elem2:
                    v2_route[i2] = elem1

            routes[v1] = v1_route
            routes[v2] = v2_route

    return full_route(routes, data = problem)


def try_for_best_dummy_insert(solution:list, problem:dict) -> list: 
    solutions = []

    get_expenses = get_expense_of_not_transporting_calls(problem)

    routes = split_routes(solution)
    dummy_route = routes[-1]

    #find most expensive call
    most_expensive = 0
    for call in get_expenses.keys(): 
        if call in dummy_route: 
            most_expensive = call 
            break
    
    if most_expensive == 0: 
        return solution

    for v in range(problem['n_vehicles']+1): 
        sol = insert_call_to_vehicle(solution, v, most_expensive, problem)
        f,c = feasibility_check(sol, problem)
        if f: 
            solutions.append(sol)
        
    
    best_solution = solution
    cost = cost_function(solution, problem)

    for sol in solutions: 
        cost_new = cost_function(sol, problem)
        if cost_new < cost: 
            return sol
    
    return best_solution

def insert_call_to_vehicle(init_solution:list, v_id:int, call:int, problem:dict) -> list: #removes the call from solution
    solution = [x for x in init_solution if x != call]
    routes = split_routes(solution)
    
    route = routes[v_id-1]

    if not route: 
        route.append(call)
        route.append(call)
        routes[v_id-1] = route
        return full_route(routes, problem)

    pos_solutions = []
    new_routes = copy.deepcopy(routes)
    cost = cost_function(init_solution, problem)

    if v_id-1 == problem['n_vehicles']:  #if the vehicle is dummy order has nothing to say for cost
        route.append(call)
        route.append(call)
        routes[-1] = route 
        return full_route(routes, problem)

    for pos_idx in range(len(route)): 
        new_new_routes = copy.deepcopy(new_routes)
        new_new_routes[v_id-1].insert(pos_idx, call)
        new_new_routes[v_id-1].insert(pos_idx+1, call)
        full_new_route = full_route(new_new_routes, problem)
        if full_new_route not in pos_solutions:
            f, c = feasibility_check(full_new_route, problem)
            cost_sol = cost_function(full_new_route, problem)
            if f and cost_sol < cost: 
                return full_new_route

    best_solution = init_solution
    cost = cost_function(init_solution, problem)

    for sol in pos_solutions: 
        new_cost = cost_function(sol, problem)
        if new_cost < cost: 
            return sol

    return best_solution
    
        
def try_for_best_for_each_vehicle(solution:list, problem:dict) -> list: 

    call = random.randrange(1, problem['n_calls']) 

    v = random.randrange(1, problem['n_vehicles']+1)
    pos_solution = insert_call_to_vehicle(solution, v, call, problem)
    cost = cost_function(solution, problem)
    cost_sol = cost_function(pos_solution, problem)
    if cost_sol < cost: 
        return pos_solution 

    return solution

    

    
    

 








