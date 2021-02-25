from index import ipt, dlv, otpt, pyt
from typing import *

file_a = './a_example'
file_b = './b_little_bit_of_everything.in'
file_c = './c_many_ingredients.in'
file_d = './d_many_pizzas.in'
file_e = './e_many_teams.in'

@pyt(file_d)
def solnone(obj: ipt) -> otpt:
    deliveries: List[dlv] = [] 
    unavail_pz: Set[int] = set()
    max_tm: int = 4
    tms: Dict[int:int] = obj.tms.copy()
    tot_pz = obj.total_pz
    total_ingredients: Set[str] = set()

    while max_tm > 0:
        if tot_pz >= 4 and tms[4] > 0:
            max_tm = 4
        elif tot_pz >= 3 and tms[3] > 0:
            max_tm = 3
        elif tot_pz >= 2 and tms[2] > 0:
            max_tm = 2
        else:
            max_tm = -1

        
        if max_tm < 0:
            break

        tms[max_tm] -= 1

        
        curr_pizza: List[int] = []
        curr_ingredients: Set[str] = set()
        while len(curr_pizza) < max_tm: 
            best_pizza_id = -1
            best_pizza = set()
            max_ingredients = -1

            
            for id_pizza, pizza in enumerate(obj.pz):
                
                if id_pizza in unavail_pz:
                    continue

                
                diff_ingredients: int = len(pizza.difference(curr_ingredients))
                if diff_ingredients > max_ingredients:
                    best_pizza_id = id_pizza
                    best_pizza = pizza
                    max_ingredients = diff_ingredients

            
            tot_pz -= 1
            unavail_pz.add(best_pizza_id)
            curr_pizza.append(best_pizza_id)
            curr_ingredients = curr_ingredients.union(best_pizza)
            total_ingredients = total_ingredients.union(best_pizza)

        d: dlv = dlv(len(curr_pizza), curr_pizza)
        deliveries.append(d)

    return otpt(deliveries)

