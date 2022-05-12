import random
import copy
from turtle import pos

import numpy as np
from route_operators import split_routes, full_route, get_expense_of_not_transporting_calls, \
    choose_call, choose_vehicle, choose_call_from_dummy

from PDP_utils import cost_function, feasibility_check
from own_utils import cost_route
from basic_operators import reinsert
from PDP_utils import cost_function, feasibility_check


def replace_vehicles_calls(solution, problem):
    routes = split_routes(solution)

    length = list(map(len, routes))

    vehicle_remove = length.index(max(length))
    remove = routes[vehicle_remove]
    vehicle = length.index(min(length))
    add = routes[vehicle]

    call = choose_call(vehicle_remove, remove, problem)
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
        elem = choose_call(v1, v1_route, problem)
        sol = insert_call(solution, v1, elem, problem)
        return sol
    else:
        v1_route = routes[v1]
        v2_route = routes[v2]
        if len(v1_route) > 2 and len(v2_route) > 2:
            elem1 = choose_call(v1, v1_route, problem)
            elem2 = choose_call(v2, v2_route, problem)

            sol1 = insert_call(solution, v1, elem2, problem)
            end_sol = insert_call(sol1, v2, elem1, problem)
            return end_sol

    return full_route(routes, data = problem)


def try_for_best_dummy_insert(solution:list, problem:dict) -> list: 
    most_expensive = random.randint(1, problem['n_calls'])

    if most_expensive == 0: 
        return solution

    vessel_comp = problem['VesselCargo']
    vehicles = [v for v in range(problem['n_vehicles']) if bool(vessel_comp[v, most_expensive-1])]
    vehicle_to_insert = random.sample(vehicles, k=1).pop()
    sol = insert_call(solution, vehicle_to_insert+1, most_expensive, problem)
    return sol

def insert_call_to_vehicle(init_solution:list, v_id:int, call:int, problem:dict) -> list: #removes the call from solution
    solution = [x for x in init_solution if x != call]
    routes = split_routes(solution)
    
    route = routes[v_id-1]

    vessel_comp = problem['VesselCargo']
    if not bool(vessel_comp[v_id-1, call-1]): 
        return init_solution

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
        new_new_routes = copy.deepcopy(routes)
        new_new_routes[v_id-1].insert(pos_idx, call)
        f1, c1 = feasibility_check(full_route(new_new_routes,problem), problem)
        if c1 == "Time window exceeded at call": 
            break 
        else:
            new_new_routes[v_id-1].insert(pos_idx+1, call)
            full_new_route = full_route(new_new_routes, problem)
            if full_new_route not in pos_solutions:
                cost_sol = cost_function(full_new_route, problem)
                if cost_sol < cost: 
                    return full_new_route
            else: 
                continue
  

def try_for_best(solution:list, problem:dict) -> list: 

    call = random.randrange(1, problem['n_calls']) 

    v = choose_vehicle(call, problem)
    pos_solution = insert_call(solution, v, call, problem)
    return pos_solution

def insert_call(init_solution:list, v_id:int, call:int, problem:dict) -> list: 
    if call == 0: 
        return init_solution
    solution_wo_call = [x for x in init_solution if x != call]
    routes = split_routes(solution_wo_call)

    route = routes[v_id-1]
    if not route: 
        route.append(call)
        route.append(call)
        routes[v_id-1] = route
        return full_route(routes, problem)

    solutions = {}
    for idx1 in range(len(route)-1): 
        new_routes = copy.deepcopy(routes)

        new_routes[v_id-1].insert(idx1, call)

        f1, c1 = feasibility_check(full_route(new_routes,problem), problem)
        if c1 == "Time window exceeded at call": 
            break 
        else:
            for idx2 in range(idx1+1, len(route)): 
                new_new_routes = copy.deepcopy(new_routes)
                new_new_routes[v_id-1].insert(idx2, call)
                new_full_route = full_route(new_new_routes, problem)
                f, c = feasibility_check(new_full_route, problem)
                #print(new_full_route, c)
                if f: 
                    new_cost = cost_function(new_full_route, problem)
                    solutions[new_cost] = new_full_route 

    best_cost = cost_function(init_solution, problem)
    best = init_solution
    for cost, r in solutions.items(): 
        if cost < best_cost: 
            best = r 
            best_cost = cost

 
    return best 



    
    

 








