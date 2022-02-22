import random as rnd
import feasibility_check as f
import cost_calculation as c
import read_data as r
from operators import basic as b

p = r.read_problem()

def local_search(init_sol:list):
    best_sol = init_sol
    best_objective = c.f(p, init_sol)
    num_vehicles = p['vehicles']
    for i in range(1000):
        choice = rnd.choice([1,2,3])
        if choice == 1:
            current = b.one_reinsert(best_sol, num_vehicles)
        elif choice == 2:
            current = b.two_exchange(best_sol, num_vehicles)
        else:
            current = b.three_exchange(best_sol, num_vehicles)
        if f.feasibility(p, current) and c.total_cost_cal(p,current)< best_objective:
            best_sol = current
            best_objective = c.total_cost_cal(p, current)

    return best_sol

