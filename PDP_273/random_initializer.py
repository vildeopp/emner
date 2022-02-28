import sys 
import PDP_utils as pdp
import datetime
import blind_random_search
import display 

def random_init(init_sol, iterations, problem): 
    print("starting random search")
    
    objective = pdp.cost_function(init_sol, problem)
    solution = init_sol 
    best_runtime = sys.maxsize
    sum_objectives = 0
    for _ in range(iterations): 
        iteration_start = datetime.datetime.now()
        new_solution = blind_random_search.blind_search(init_sol, problem)
        new_objective = pdp.cost_function(new_solution, problem)
        sum_objectives += new_objective
        if pdp.feasibility_check(new_solution) and new_objective < objective: 
            solution = new_solution
            objective = new_objective
        
        iteration_end = datetime.datetime.now()
        total_runtime = (iteration_end - iteration_start).total_seconds()
        if total_runtime < best_runtime: 
            best_runtime = total_runtime

        display.print_sol(sum_objectives/iterations, objective, best_runtime, solution, pdp.feasibility_check(solution))
