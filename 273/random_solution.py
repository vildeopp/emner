import read_data as x
import random 

data = x.read_problem()

#this is not feasible
def random_sol():
    route = random.sample(range(1, data['calls']+1), data['calls'])

    rand_index = random.sample(range(1, data['calls']), data['vehicles'])
    for i in rand_index: 
        route.insert(i, 0)

    route_pd = []
    for n in route: 
        if n == 0:
            route_pd.append(n)
            continue
        route_pd.append(n)
        route_pd.append(n)

    return route_pd

def problem_used(): 
    return data




