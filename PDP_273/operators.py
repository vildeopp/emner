import copy
import random
import numpy as np
from route_operators import most_expensive_for_each_car, split_routes, full_route, \
    get_expense_of_not_transporting_calls, choose_call, choose_vehicle, choose_call_from_dummy, vehcile

from PDP_utils import cost_function, feasibility_check
from own_utils import cost_route
from basic_operators import reinsert
from PDP_utils import cost_function, feasibility_check


def insert_two_exchange(solution: list, problem:list) -> list: 

    routes = split_routes(solution)
    lengths = list(map(len,routes))
    longest_v = lengths.index(max(lengths))
    shortest_v = lengths.index(min(lengths))

    longest_route = routes[longest_v]
    shortest_route = routes[shortest_v]
 

    if abs(len(shortest_route)- len(longest_route)) > problem['n_calls']/2: 
       
        call = choose_call(longest_v, longest_route, problem)
        shortest_route.append(call)
        shortest_route.append(call)
        routes[shortest_v] = shortest_route
        routes[longest_v] = [x for x in longest_route if x != call]
        return full_route(routes, problem)
    else: 
        
        call1 = choose_call(longest_v, longest_route, problem)
        call2 = choose_call(shortest_v, shortest_route, problem)

        for i1, c1 in enumerate(shortest_route): 
            if c1 == call2: 
                shortest_route[i1] = call1
        for i2, c2 in enumerate(longest_route): 
            if c2 == call1: 
                longest_route[i2] = call2

        routes[longest_v] = longest_route
        routes[shortest_v] = shortest_route

        return full_route(routes, problem)

def remove_from_dummy(solution, problem): 
    routes = split_routes(solution)
    call = choose_call(problem['n_vehicles'],routes[-1], problem)
    
    if not call: 
        return solution
    
    insert_vehicle = choose_vehicle(call, problem)
    solution = [x for x in solution if x != call]
    routes = split_routes(solution)

    if not routes[insert_vehicle-1]: 
        routes[insert_vehicle-1].append(call)
        routes[insert_vehicle-1].append(call)
        return full_route(routes, problem)

    routes[insert_vehicle-1].insert(random.randrange(0, len(routes[insert_vehicle-1])), call)
    routes[insert_vehicle-1].insert(random.randrange(0, len(routes[insert_vehicle-1])), call)

    return full_route(routes, problem)

def try_for_best(init_solution, problem): 
    calls = most_expensive_for_each_car(init_solution, problem)
    call = random.choice(list(calls.keys()))
    solution = [x for x in init_solution if x != call] #remove call
    
    vehicle = choose_vehicle(call, problem)
    routes = split_routes(solution)
    vehicle_route = routes[vehicle]

    pos_solutions = []

    for posIdx in range(len(vehicle_route)): 
        new_routes = routes
        new_routes[vehicle-1].insert(posIdx, call)
        new_routes[vehicle-1].insert(posIdx+1, call)
        pos_solutions.append(full_route(new_routes, problem))

    cost = cost_function(init_solution, problem)
    for sol in pos_solutions: 
        f,c = feasibility_check(sol, problem)
        if f: 
            if cost_function(sol,problem) < cost: 
                return sol 
    
    return init_solution


def remove_k_calls(initial, problem): 

    routes = split_routes(initial)
    lengths = list(map(len, routes))
   
    longest_route = routes[lengths.index(max(lengths))]
    if longest_route == 1: 
        return initial 

    k = random.randint(1, len(set(longest_route))+1)

    chosen_calls = list(set(random.choices(list(set(longest_route)), k=k)))
    solution_wo_calls = [x for x in initial if x not in chosen_calls]
    routes_wo_calls = split_routes(solution_wo_calls)
    for call in chosen_calls: 
        copy_route = copy.deepcopy(routes_wo_calls)
        route, v = vehcile(call, full_route(routes_wo_calls, problem), problem)
        copy_route[v] = route 
        routes_wo_calls = copy_route
    return full_route(routes_wo_calls, problem)

def escape(solution, problem): 
    """take a random call and place it back in the dummy"""

    calls = problem['n_calls']

    random_call = random.randint(1, calls)
    tampered_solution = [x for x in solution if x != random_call]
    tampered_solution.insert(len(tampered_solution)+500, random_call)
    tampered_solution.insert(len(tampered_solution)+500, random_call)

    return tampered_solution


    
    







    