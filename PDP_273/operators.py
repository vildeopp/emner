import copy
from posixpath import split
import random
import numpy as np

from route_operators import most_expensive_for_each_car, split_routes, full_route, \
    get_expense_of_not_transporting_calls, choose_call, choose_vehicle, choose_call_from_dummy, vehcile
from greedy_operators import insert_call
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
 

    if abs(len(shortest_route)- len(longest_route)) > problem['n_calls']/2 or not shortest_route: 
       
        call = random.choice(longest_route)
        if not shortest_route: 
            shortest_route.append(call)
            shortest_route.append(call)
            routes[shortest_v] = shortest_route
            routes[longest_v] = [x for x in longest_route if x != call]
            return full_route(routes, problem)
        else: 
            shortest_route.insert(random.randint(0, len(shortest_route)), call)
            shortest_route.insert(random.randint(0, len(shortest_route)), call)
            routes[shortest_v] = shortest_route
            routes[longest_v] = [x for x in longest_route if x != call]
            return full_route(routes, problem)
    else: 
       
        call1 = random.choice(longest_route)
        call2 = random.choice(shortest_route)
        
#        for i1, c1 in enumerate(shortest_route): 
#            if c1 == call2: 
#                shortest_route[i1] = call1
#        for i2, c2 in enumerate(longest_route): 
#            if c2 == call1: 
#                longest_route[i2] = call2
#
#       routes[longest_v] = longest_route
#        routes[shortest_v] = shortest_route
        sol1 = insert_call(solution, shortest_v, call1, problem)
        return insert_call(sol1, longest_v, call2, problem)

def remove_from_dummy(init_solution, problem):
    ratio = problem['n_calls']//problem['n_vehicles']
    routes = split_routes(init_solution)
    calls = random.choices([x for x in range(1, problem['n_calls']+1)], k=ratio)
    calls = list(set(calls))
    if not calls: 
        return solution

    solution = [x for x in init_solution if x not in calls]
    routes = split_routes(solution)

    routes = split_routes(solution)
    call = choose_call(problem['n_vehicles'],routes[-1], problem)
    
    for call in calls: 
        if not call: 
            return solution
        
        insert_vehicle = choose_vehicle(call, problem)

        if not routes[insert_vehicle-1]: 
            routes[insert_vehicle-1].append(call)
            routes[insert_vehicle-1].append(call)
            continue
       
        routes[insert_vehicle-1].insert(random.randrange(0, len(routes[insert_vehicle-1])), call)
        routes[insert_vehicle-1].insert(random.randrange(0, len(routes[insert_vehicle-1])), call)

    return full_route(routes, problem)

def try_for_best(init_solution, problem): 
    call = random.randint(1, problem['n_calls'])
    solution = [x for x in init_solution if x != call] #remove call
    
    vehicle = random.randint(0, problem['n_vehicles']-1)
    if vehicle == problem['n_vehicles']: 
        solution.append(call)
        solution.append(call)
        return  solution
    routes = split_routes(solution)
    vehicle_route = routes[vehicle]

    pos_solutions = []
    for posIdx in range(len(vehicle_route)-1): 
        new_routes = copy.deepcopy(routes)
        new_routes[vehicle].insert(posIdx, call)
        for posIdx2 in range(posIdx+1, len(vehicle_route)):
            new_routes[vehicle].insert(posIdx2, call)
            pos_solutions.append(full_route(new_routes, problem))

    cost = cost_function(init_solution, problem)
    best = init_solution
    for sol in pos_solutions: 
        f,c = feasibility_check(sol, problem)
        if f: 
            cost_sol = cost_function(sol, problem)
            if cost_sol < cost: 
                best = sol 
                cost = cost_sol
    
    return best


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
    """take a random number of calls and place it back in the dummy"""
    
    routes = split_routes(solution)[:-1]
    route_wo_dummy = full_route(routes, problem)
    pos_calls_to_move = [x for x in route_wo_dummy if x != 0]
    if not pos_calls_to_move: 
        return solution

    if len(set(pos_calls_to_move)) <= 1: 
        call = set(pos_calls_to_move).pop()
        tampered_solution = [x for x in solution if x != call]
        tampered_solution.append(call)
        tampered_solution.append(call)
        return tampered_solution
    else: 
        choose = random.randint(1, (len(set(pos_calls_to_move))+1//2))
        calls_to_move = random.sample(list(set(pos_calls_to_move)), k = choose)
        tampered_solution = [x for x in solution if x not in calls_to_move]
        for call in calls_to_move: 
            tampered_solution.insert(len(tampered_solution)+500, call)
            tampered_solution.insert(len(tampered_solution)+500, call)
        return tampered_solution

def move_to_next_vehicle(solution, problem): 
  
    call = random.randint(1, problem['n_calls'])
    routes = split_routes(solution)
    vehicle = [i for i in range(len(routes)) if call in routes[i]][0]
   
    
    routes[vehicle] = [x for x in routes[vehicle] if x != call]
    comp = problem['VesselCargo']

    pos_vehicles = [v for v in range(problem['n_vehicles']) if bool(comp[v][call-1]) and v != vehicle]
    if not pos_vehicles: 
        return solution

    vehicle_to_insert = random.choice(pos_vehicles)
    routes[vehicle_to_insert].insert(random.randint(0, len(routes[vehicle_to_insert])), call)
    routes[vehicle_to_insert].insert(random.randint(0, len(routes[vehicle_to_insert])), call)
   
    return full_route(routes, problem)

def shuffle_route(solution, problem): 
    routes = split_routes(solution)
    vehciles = [i for i in range(len(routes)) if len(routes[i]) > 2]
    random_vehicle = random.choice(vehciles)
    if random_vehicle == problem['n_vehicles']: 
        return solution
    route = routes[random_vehicle]
    if not route: 
        return solution
    
    shuffle_routes = []

    for _ in range(5): 
        random.shuffle(route)
        shuffle_routes.append(route)

    best = solution
    initial_cost = cost_function(solution,problem)

    for sol in shuffle_routes: 
        new_route = copy.deepcopy(routes)
        new_route[random_vehicle] = sol 
        full = full_route(new_route, problem)
        cost = cost_function(full, problem)
        if cost < initial_cost: 
            best = full 
            initial_cost = cost 

    return best
    

    
    







    