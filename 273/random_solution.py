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

#to make a random route where only the dummy vehicle is used
def random_dummy_route():
    route = random.sample(range(1, data['calls']+1), data['calls'])
    full_route = route + route
    for _ in range(data['vehicles']):
        full_route.insert(0,0)

    return full_route







