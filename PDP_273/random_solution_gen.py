import random
def random_sol(data):
    route = random.sample(range(1, data['n_calls'] + 1), data['n_calls'])  # deciding the route
    rand_index = random.sample(range(1, data['n_calls']), data['n_vehicles'] )  # for placing the change of cars

    for i in rand_index:
        route.insert(i, 0)

    # adding the calls twice (pick up then delivery)
    route_pd = []
    for n in route:
        if n == 0:
            route_pd.append(n)
            continue
        route_pd.append(n)
        route_pd.append(n)

    return route_pd


def new_random_sol(data):
    avail_calls = [x for x in range(1, data['n_calls'] + 1)]
    avail_vehicles = int(data['n_vehicles'])
    count = 0
    routes = []
    while len(avail_calls) != 0:
        route = []
        count += 1
        if not avail_calls:
            break
        if count > avail_vehicles:
            for c in avail_calls:
                route.append(c), route.append(c)
            routes.append(route)
            break
        else:
            rnd = random.randrange(0, data['n_calls'])
            for _ in range(rnd):
                if not avail_calls:
                    break
                call = random.choice(avail_calls)
                avail_calls.remove(call)
                route.append(call)
                route.append(call)
            routes.append(route)

    diff = avail_vehicles - count
    print("org", routes)
    for _ in range(diff):
        routes.append([])
    print("new", routes)
    return full_route(routes)

def full_route(routes):
    route = []
    for r in routes:
        route += r
        route.append(0)
        print("index", routes.index(r))
    return route

def combine_routes(routes):
    route = []
    for r in routes:
        if not r and routes.index(r) != len(routes):
            route.append(0)
            continue
        if routes.index(r) == len(routes):
            route = route + r
        else:
            route = route + r
            route.append(0)

    return route