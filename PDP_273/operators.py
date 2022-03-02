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

    if rand_v1 == rand_v2:
        route = routes[rand_v1]
        if route is None:  # the list is empty
            return routes
        else:
            if len(route) > 2:
                elem = rnd.choice(route)
                route = route.remove(elem)
                new_indx = rnd.randrange(0, len(route) - 1)
                route[new_indx] = elem
                routes[rand_v1] = route
            else:
                return routes

    else:
        route1 = routes[rand_v1]
        route2 = routes[rand_v2]
        if not route1:  # the list is empty and therefore nothing to insert
            return routes
        else:
            elem = rnd.choice(route1)
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


def two_exchange(init_sol, data):
    routes = split_routes(init_sol)

    rand_v1 = rnd.randrange(0, data['n_vehicles'] + 1)
    rand_v2 = rnd.randrange(0, data['n_vehicles'] + 1)

    if rand_v1 == rand_v2:
        print("like", rand_v1, rand_v2)
        route = routes[rand_v1]
        if not route:
            print(route)
            return routes
        else:
            if len(routes) >= 4:
                elems = rnd.sample(route, 2)
                elem1, elem2 = elems[0], elems[1]
                print("elements", elem1, elem2)
                if elem1 == elem2:
                    return routes
                else:
                    indx1 = route.index(elem1)
                    indx2 = route.index(elem2)
                    route[indx1] = elem2
                    route[indx2] = elem1
                    print("changed", route)
                    routes[rand_v1] = route
    else:
        print("ikke like", rand_v1, rand_v2)
        route1 = routes[rand_v1]
        route2 = routes[rand_v2]
        if not route1 or not route2:
            print("en er tom ")
            return routes
        elem1 = rnd.choice(route1)
        elem2 = rnd.choice(route2)
        print("elements", elem1, elem2)

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


def three_exhcange(init_sol, data):
    routes = split_routes(init_sol)
    # choosing how many vehicles to exchange between 1,2,3
    rand_routes = list(np.random.randint(low=data["n_vehicles"], size=3))
    print(rand_routes)
    route1 = routes[rand_routes[0]]
    route2 = routes[rand_routes[1]]
    route3 = routes[rand_routes[2]]

    if not route1 or not route2 or not route3:
        print("one or more lists are empty")
        return routes

    elem1 = rnd.choice(route1)
    elem2 = rnd.choice(route2)
    elem3 = rnd.choice(route3)
    print("old", route1, route2, route3)
    print("elements", elem1, elem2, elem3)
    if elem1 == elem2 or elem2 == elem3 or elem1 == elem3:  # checks if the elements are equal
        return routes

    for i, c in enumerate(route1):
        if c == elem1:
            route1[i] = elem3
    for i2, c2 in enumerate(route2):
        if c2 == elem2:
            route2[i2] = elem1
    for i3, c3 in enumerate(route3):
        if c3 == elem3:
            route3[i3] = elem2
    print("new", route1, route2, route3)
    routes[rand_routes[0]] = route1
    routes[rand_routes[1]] = route2
    routes[rand_routes[2]] = route3

    return full_route(routes, data)