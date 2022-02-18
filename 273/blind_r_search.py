import random_solution as rnd
import feasibility_check as feas
import cost_calculation as f

p = rnd.problem_used()
def blind_random_search(init_sol: list): 

    best_sol = init_sol
    best_objective = f.total_cost_cal(p, best_sol)
    for i in range(1000): 
        current_sol = rnd.random_sol()
        if feas.feasibility(p,current_sol) and f.total_cost_cal(p, current_sol) < best_objective:
            best_sol = current_sol
            best_objective = f.total_cost_cal(p, current_sol)
    
    return best_sol, best_objective
        

