import random as rnd
from route import get_vehiclecalls_aslist, get_full_route

def one_reinsert(solution, num_vehicles):
    calls = get_vehiclecalls_aslist(solution)
    if num_vehicles > 1:
        rand = rnd.randrange(1, num_vehicles)
        reinsert_list = calls[rand]
    else:
        reinsert_list = calls[0]

    if len(reinsert_list) <= 1:
        return solution
    else:
        elem = rnd.choice(reinsert_list)
        reinsert_list.remove(elem)
        rand_index = rnd.randrange(0, len(reinsert_list))
        reinsert_list.insert(rand_index, elem)
    print(reinsert_list)
    calls[rand] = reinsert_list
    return get_full_route(calls)

def two_exchange(solution, num_vehicles):

    calls = get_vehiclecalls_aslist(solution)
    if num_vehicles > 1:
        rand = rnd.randrange(1,num_vehicles)
        two_exchange_list = calls[rand]
    else:
        two_exchange_list = calls[0]

    if len(two_exchange_list) <= 2:
        return solution
    else:
        change_elem = rnd.sample(two_exchange_list, 2)
        elem1, elem2 = change_elem[0], change_elem[1]
        if elem1 == elem2:
            print("equal elements in two exchange")
            return solution
        index1, index2 = two_exchange_list.index(elem1), two_exchange_list.index(elem2)
        two_exchange_list[index1], two_exchange_list[index2] = elem2, elem1
    print(two_exchange_list)
    calls[rand] = two_exchange_list
    return get_full_route(calls)


def three_exchange(solution, num_vehicles):
    routes = get_vehiclecalls_aslist(solution)

    if num_vehicles > 1:
        vehicle = rnd.randrange(1, num_vehicles)
        three_exchange_list = routes[vehicle]
    else:
        three_exchange_list = routes[0]

    if len(three_exchange_list) <= 3:
        return solution
    else:
        change_elems = rnd.sample(three_exchange_list,3)
        elem1, elem2, elem3 = change_elems[0], change_elems[1], change_elems[2]
        if elem1 == elem2 or elem2 == elem3 or elem1 == elem3:
            print("equal elements in three exchange")
            return solution
        index1, index2, index3 = three_exchange_list.index(elem1), three_exchange_list.index(elem2), three_exchange_list.index(elem3)
        three_exchange_list[index1], three_exchange_list[index2], three_exchange_list[index3] = elem3, elem1, elem2
    print(three_exchange_list)
    routes[vehicle] = three_exchange_list
    return get_full_route(routes)