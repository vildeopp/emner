import random
import sys
from itertools import permutations

import numpy as np
from route_operators import split_routes, full_route, get_expense_of_not_transporting_call
from PDP_utils import cost_function, feasibility_check
from own_utils import cost_route
from operators import reinsert


def allocate_dummy_call(solution: list, problem: dict) -> list:
    """
    Allocates one call in the dummy vehicle to the first valid vehicle
    """
    routes = split_routes(solution)
    dummy = routes[-1]
    if not dummy:
        return solution

    elem = random.choice(dummy)
    new_dummy = [x for x in dummy if x != elem]
    routes[-1] = new_dummy

    vesselCargo = problem['VesselCargo']
    vehcile = 0
    insert_route = []
    for i, calls in enumerate(vesselCargo):
        if calls[elem - 1] == float(1):
            insert_route = routes[i]
            vehcile = i
            break

    insert_route.append(elem)
    insert_route.append(elem)

    routes[vehcile] = insert_route
    return full_route(routes, data=problem)


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
            pos_calls = [x for x in pos_calls if
                         x != call]  # removes the call if it is not possible to add it to vehicle
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


def rearrange_vehicles_calls(solution, problem):
    """
    takes a random vehicle in route and rearranges the calls in its route, if there are more than two different calls (4 elements in the list)
    """

    routes = split_routes(solution)

    vehicle = random.randrange(0, problem['n_vehicles'] - 1)
    route = routes[vehicle]
    if not route or len(route) < 4:
        for _ in range(10):
            vehicle = random.randrange(0, problem['n_vehicles'] - 1)
            route = routes[vehicle]
            if len(route) >= 4:
                break

    random.shuffle(route)
    routes[vehicle] = route
    if feasibility_check(full_route(routes, data=problem), problem):
        return full_route(routes, data=problem)
    else:
        for _ in range(20):
            random.shuffle(route)
            if feasibility_check(route, problem):
                routes[vehicle] = route
                break

    return full_route(routes, data=problem)


def insert_most_expensive_from_dummy(solution, problem):
    routes = split_routes(solution)
    if len(routes) == problem['n_vehicles']:
        return solution

    dummy_route = routes[-1]
    if not dummy_route:
        return solution

    dummy_route.sort()  # sort the dummy route so that the indices in the list below match the calls in the dummy route
    expenses = [get_expense_of_not_transporting_call(x, problem) for x in set(dummy_route)]

    most_expensive = dummy_route[expenses.index(max(expenses))]
    if most_expensive == 0:
        return solution

    dummy_route = [x for x in dummy_route if x != most_expensive]
    routes[-1] = dummy_route

    vesselCargo = problem['VesselCargo']

    for v in range(problem['n_vehicles']):
        if bool(vesselCargo[v, most_expensive - 1]):
            insert_route = routes[v]
            if len(insert_route) < 2:
                insert_route.append(most_expensive)
                insert_route.append(most_expensive)
            else:
                idx1 = random.randrange(len(insert_route))
                insert_route.insert(idx1, most_expensive)
                insert_route.insert(idx1 + 1, most_expensive)

            routes[v] = insert_route
            break

    return full_route(routes, problem)


def find_cheapest_transport(call, problem):
    """Use this method to insert pickup and delivery right after each other"""
    calls = [call, call]
    cargo = problem['VesselCargo']

    cheapest = sys.maxsize
    vehicle = 0

    for v in range(problem['n_vehicles']):
        if cargo[v, call - 1] == float(1):
            if cost_route(calls, v, problem) < cheapest:
                cheapest = cost_route(calls, v, problem)
                vehicle = v
        else:
            continue

    return vehicle + 1

def two_exchange_reinsert(solution, problem):

    solution = reinsert(solution, problem)
    routes = split_routes(solution)
    lengths = list(map(len, routes[0:problem['n_vehicles']]))

    v1 = lengths.index(max(lengths))
    v2 = lengths.index(min(lengths))

    if v2 == 0:
        return full_route(routes, problem)

    vesselCargo = problem['VesselCargo']

    #When to reinsert? -> when the smallest list is empty? (some kind of ratio between max and min length)
    if not routes[v2]:
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

    #else find the cheapest car to exchange the calls with ?






