from feasibility_check import feasibility
import random_solution as rnd
import random_init as init
from search_algorithms import local_search

def main(): 
    init_solution = rnd.random_sol()
    #init.random_solution_initializer(init_solution, 10)
    local_search.local_search(init_solution)


if __name__ == '__main__': 
    main()