import random as rnd
import feasibility_check as f
import cost_calculation as c
import read_data as r
from operators import basic as b


p = r.read_problem()

def local_search(init_sol:list):
    best_sol = init_sol
    best_objective = c.total_cost_cal(p, init_sol)
    num_vehicles = p['vehicles']
    print(num_vehicles)
    for _ in range(1000):
        choice = rnd.choice([1,2,3])
        if choice == 1:
            current = b.one_reinsert(best_sol, num_vehicles)
            print("insert")
        elif choice == 2:
            current = b.two_exchange(best_sol, num_vehicles)
            print("two exchange")
        else:
            current = b.three_exchange(best_sol, num_vehicles)
            print("three exchange")
        print("current", current)
        if f.feasibility(p, current) and c.total_cost_cal(p,current)< best_objective:
            best_sol = current
            best_objective = c.total_cost_cal(p, current)

    print("initial", init_sol)
    print("best objective", best_objective)
    print("best solution", best_sol)

    return best_sol

