
import random_init as rnd_init
import random_solution as rnd

def main():
    init_sol = rnd.random_dummy_route()
    rnd_init.random_solution_initializer(init_sol, 10)

if __name__ == '__main__':
    main()