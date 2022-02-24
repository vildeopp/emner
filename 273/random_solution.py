import read_data as x
import random 

data = x.read_problem()

#this is not feasible
def random_sol():
    route = random.sample(range(1, data['calls']+1), data['calls']) #deciding the route
    rand_index = random.sample(range(1, data['calls']), data['vehicles']-1) #for placing the change of cars

    for i in rand_index:
        route.insert(i, 0)

    #adding the calls twice (pick up then delivery)
    route_pd = []
    for n in route: 
        if n == 0:
            route_pd.append(n)
            continue
        route_pd.append(n)
        route_pd.append(n)

    return route_pd

def new_random_sol():
    avail_calls = [x for x in range(1,data['calls']+1)]
    avail_vehicles = data['vehicles']
    count = 0
    routes = []
    while len(avail_calls) != 0 :
        route = []
        count += 1
        if not avail_calls:
            break
        if count > data['vehicles']:
            for c in avail_calls:
                avail_calls.remove(c)
                route.append(c), route.append(c)
            routes.append(route)
            break
        else:
            rnd = random.randrange(0, data['calls'])
            for _ in range(rnd):
                if not avail_calls:
                    break
                call = random.choice(avail_calls)
                avail_calls.remove(call)
                route.append(call)
                route.append(call)
            routes.append(route)
    return combine_routes(routes)

def combine_routes(routes):
    list = []
    for r in routes:
        if routes.index(r)+1 == len(routes):
            list = list + r
        else:
            list = list + r
            list.append(0)

    return list



#to make a random route where only the dummy vehicle is used
def random_dummy_route():
    route = random.sample(range(1, data['calls']+1), data['calls'])
    full_route = route + route
    for _ in range(data['vehicles']):
        full_route.insert(0,0)

    return full_route







