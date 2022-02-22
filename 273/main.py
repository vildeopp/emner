from feasibility_check import feasibility
import random_solution as rnd
import random_init as init

def main(): 
    init_solution = rnd.random_dummy_route()
    init.random_solution_initializer(init_solution, 10)


if __name__ == '__main__': 
    main()