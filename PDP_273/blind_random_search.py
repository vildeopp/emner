import PDP_utils as pdp
import random_solution_gen as rnd

def blind_search(init_sol, problem):
    best = init_sol
    best_objective = pdp.cost_function(init_sol, problem)

    for _ in range(1000):
        new_sol = rnd.new_random_sol(problem)
        new_objective = pdp.cost_function(new_sol, problem)
        feasible, c = pdp.feasibility_check(new_sol, problem)
        if (new_objective < best_objective) and feasible:
            best = new_sol
            best_objective = new_objective

    return best, best_objective