from PDP_utils import read_problem

data = read_problem()

def random_solution():
    calls = [x for x in range(1, data['n_calls'])]
    return calls

print(random_solution())