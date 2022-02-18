from feasibility_check import feasibility
import random_solution as rnd
import random_init as init

def main(): 
    solution = rnd.random_sol()
    init.random_solution_initializer(solution, 10)


if __name__ == '__main__': 
    main()