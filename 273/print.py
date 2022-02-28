


def print_sol(avg_obj, best_obj, init_obj, runtime, best_sol, feasible): 
    impr = round(((init_obj - best_obj)/init_obj)*100, 3) 

    print(f"average objective: {round(avg_obj, 3)}")
    print(f"best objective: {best_obj}")
    print(f"Improvement: {impr}")
    print("-"*25)
    print(f"runtime: {runtime}")
    print("-"*25)
    print(f"Best solution: {best_sol}")
    print(f"feasible: {feasible}")
    