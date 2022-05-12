from collections import Counter

from route_operators import split_routes, full_route
import random as rnd
import numpy as np

"""
takes one element and reinserts it from one vehicle to another or inside the route of the same vehicle
"""


def reinsert(init_sol, data):
    rand_v1 = rnd.randrange(0, data['n_vehicles'] + 1)
    rand_v2 = rnd.randrange(0, data['n_vehicles'] + 1)
    routes = split_routes(init_sol)

    # want to look for vehicles that are able to reinsert elements (have calls)
    for _ in range(10):
        if not routes[rand_v1]:
            rand_v1 = rnd.randrange(0, data['n_vehicles'] + 1)
            rand_v2 = rnd.randrange(0, data['n_vehicles'] + 1)
        else:
            break

    if rand_v1 == rand_v2:

        route = routes[rand_v1]

        if not route:  # the list is empty
            return full_route(routes, data)
        else:
            if len(route) > 2:
                elem = rnd.choice(route)
                route.remove(elem)
                new_indx = rnd.randrange(0, len(route) - 1)
                route.insert(new_indx, elem)
                routes[rand_v1] = route
            else:
                return full_route(routes, data)

    else:
        route1 = routes[rand_v1]
        route2 = routes[rand_v2]

        if not route1:  # the list is empty and therefore nothing to insert
            return full_route(routes, data)
        else:

            elem = rnd.choice(route1)
            # remove the two instances of the element
            route1.remove(elem)
            route1.remove(elem)
            if len(route2) > 2:
                rnd_indx1 = rnd.randrange(0, len(route2) - 1)
                route2.insert(rnd_indx1, elem)
                rnd_indx2 = rnd.randrange(0, len(route2) - 1)
                route2.insert(rnd_indx2, elem)
            else:
                route2.insert(0, elem)
                route2.insert(0, elem)

            routes[rand_v2] = route2

    return full_route(routes, data)


"""
Takes two elements either from the same vehicle or two vehicles and swaps two calls
"""


def two_exchange(init_sol, data):
    re_insertroute = init_sol

    routes = split_routes(re_insertroute)
    rand_v1 = rnd.randrange(0, data['n_vehicles'] + 1)
    rand_v2 = rnd.randrange(0, data['n_vehicles'] + 1)

    for _ in range(10):
        if not routes[rand_v1] or not routes[rand_v2]:
            rand_v1 = rnd.randrange(0, data['n_vehicles'] + 1)
            rand_v2 = rnd.randrange(0, data['n_vehicles'] + 1)
        else:
            break

    if rand_v1 == rand_v2:
        route = routes[rand_v1]
        if not route:
            return full_route(routes, data)
        else:
            if len(route) >= 4:
                elems = rnd.sample(route, 2)
                elem1, elem2 = elems[0], elems[1]
                if elem1 == elem2:
                    return full_route(routes, data)
                else:
                    for i, c in enumerate(route):
                        if c == elem1:
                            route[i] = elem2
                        elif c == elem2:
                            route[i] = elem1
                    routes[rand_v1] = route
            return full_route(routes, data)
    else:

        route1 = routes[rand_v1]
        route2 = routes[rand_v2]
        if not route1 or not route2:
            return full_route(routes, data)
        elem1 = rnd.choice(route1)
        elem2 = rnd.choice(route2)

        if len(route1) >= 2 and len(route2) >= 2:
            for i, c in enumerate(route1):
                if c == elem1:
                    route1[i] = elem2
            for i, c in enumerate(route2):
                if c == elem2:
                    route2[i] = elem1

        routes[rand_v1] = route1
        routes[rand_v2] = route2

    return full_route(routes, data)


"""
Chooses randomly number of vehicles and which vehciles to choose from and then exchanges three elements 
in the way: elem1 = elem3, elem2 = elem1, elem3 = elem2
"""


def three_exchange(init_sol, data):
    # to make sure that some of the calls in the dummy vehicle is added to the other cars
    routes = split_routes(init_sol)
    # choosing how many vehicles to exchange between 1,2,3, by choosing random index with reversal
    rand_routes = list(np.random.randint(low=data["n_vehicles"], size=3))

    route1 = routes[rand_routes[0]]
    route2 = routes[rand_routes[1]]
    route3 = routes[rand_routes[2]]

    for _ in range(10):
        if not route1 or not route2 or not route3:
            rand_routes = list(np.random.randint(low=data["n_vehicles"], size=3))
            route1 = routes[rand_routes[0]]
            route2 = routes[rand_routes[1]]
            route3 = routes[rand_routes[2]]
        else:
            break

    if not route1 or not route2 or not route3:
        return full_route(routes, data)

    elem1 = rnd.choice(route1)
    elem2 = rnd.choice(route2)
    elem3 = rnd.choice(route3)

    if elem1 == elem2 or elem2 == elem3 or elem1 == elem3:
        return full_route(routes, data)

    i1 = [i for i, el in enumerate(route1) if el == elem1]
    i2 = [i for i, el in enumerate(route2) if el == elem2]
    i3 = [i for i, el in enumerate(route3) if el == elem3]

    for i in range(2):
        route1[i1[i]] = elem3
        route2[i2[i]] = elem1
        route3[i3[i]] = elem2

    routes[rand_routes[0]] = route1
    routes[rand_routes[1]] = route2
    routes[rand_routes[2]] = route3

    solution = full_route(routes, data)
    return solution
