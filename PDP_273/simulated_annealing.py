import PDP_utils as pdp
import random as rnd
import math 
from display import print_sol
from statistics import mean

def simulated_annealing(init_sol, problem, operator): 
    Tf = 0.1 #final temperature 
    incumbent = init_sol 
    inc_objective = pdp.cost_function(incumbent, problem)
    best_solution = init_sol 
    best_objective = pdp.cost_function(best_solution, problem)

    delta = [] #store the feasible deltas

    sum_objectives = pdp.cost_function(init_sol, problem) #sum of objectives to calculate average objective
    #"warm-up"
    print("simulated annealing starting")
    for _ in range(100):
        new_solution = operator(incumbent, problem)
        new_objective = pdp.cost_function(new_solution, problem)
        delta_E = new_objective - inc_objective
        feasible, c = pdp.feasibility_check(new_solution, problem)
        sum_objectives += new_objective
        if feasible and delta_E < 0: #if the new solution is feasible and the incumbent objective is larger than the objective of the new solution
            incumbent = new_solution
            inc_objective = new_objective
            if inc_objective < best_objective: 
                best_solution = incumbent
                best_objective = inc_objective
        elif feasible: 
            rand = rnd.random() #returns a floating point between 0 and 1 
            if rand < 0.8: 
                incumbent = new_solution
                inc_objective = new_objective
            
            delta.append(delta_E) #adds delta E to the deltas
        
    delta_avg = mean(delta)
    t_null = (-delta_avg)/math.log(0.8)
    alpha = pow(Tf/t_null, 1/9900)
    t = t_null 

    for _ in range(9900): 
        new_solution = operator(incumbent, problem)
        new_objective = pdp.cost_function(new_solution, problem)
        delta_E = new_objective - inc_objective
        feasible, c = pdp.feasibility_check(new_solution, problem)
        sum_objectives += new_objective
        if feasible and delta_E < 0: 
            incumbent = new_solution
            inc_objective = new_objective
            if inc_objective < best_objective: 
                best_solution = incumbent
                best_objective = inc_objective
            elif feasible: 
                rand = rnd.random()
                p = math.pow(math.e, (-delta_E/ t))
                if rand < p: 
                    incumbent = new_solution
                    inc_objective = new_objective
            t = alpha * t 
    print("end of simulated annealing")
    avg_objectives = sum_objectives/1000

    return best_solution, best_objective, feasible, avg_objectives

    

  
    


  