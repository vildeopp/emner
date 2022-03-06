
import random_solution_gen as rnd
import random_initializer as rnd_init
import PDP_utils as pdp
import operators as o
import localsearch as local
import simulated_annealing as sim 
import simulated_annealing_init as s

file1 = "data/Call_7_Vehicle_3.txt"
file2 = "data/Call_18_Vehicle_5.txt"
file3 = "data/Call_35_Vehicle_7.txt"
file4 = "data/Call_80_Vehicle_20.txt"
file5 = "data/Call_130_Vehicle_40.txt"
file6 = "data/Call_300_Vehicle_90.txt"

def main():
    problem = pdp.load_problem(file1)
    #init = rnd.random_dummy_route(problem)
    init = rnd.new_random_sol(problem)
    init2 = rnd.random_dummy_route(problem)
    #print("init", init)
    #print("Reinserted", o.reinsert(init, problem))
    #print("two exchange: ", o.two_exchange(init2, problem))
    #print("three exchange: ", o.three_exhcange(init, problem))
    #for _ in range(10): 
    #    local.local_search(init, problem, o.two_exchange)
    #print(sim.simulated_annealing(init2, problem, o.reinsert))
    s.intitalizer(init2, problem, 10)

if __name__ == '__main__':
    main()