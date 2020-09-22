from collections import defaultdict
from itertools import combinations
from operator import itemgetter

def solution(orders, course):
    valid_combi = []
    
    count_orders = defaultdict(list)
    for id, foods in enumerate(orders):
        for menu in foods:
            count_orders[menu].append(id+1)
    # print(count_orders)
    for key,value_food in count_orders.items():
        # print(count_orders[key])
        if len(count_orders[key]) >= 2:
            # print(idx)
            valid_combi.append(key)

    combi_food = defaultdict(int)
    for i in course:
        n_food = combinations(valid_combi,i)
        for k in n_food:
            combi_food["".join(sorted(k))] =0

    # print(combi_food)

    for foods,cnt in combi_food.items():
        for order in orders:
            # print(set(foods))
            valid_combi2 = list(set(foods) & set(order))
            # print(valid_combi)
            valid_combi2 = "".join(sorted(valid_combi2))
            if len(valid_combi2) >=2 and (len(valid_combi2) == len(foods)):

                combi_food[valid_combi2] += 1 
            # print(valid_combi)
    
    possible_chain = [(k,v) for k,v in combi_food.items() if v>=2]
    # print(possible_chain)
    real_bucket = []
    for cnt in course:
        bucket =[]
        for i,v in possible_chain:
            if len(i) == cnt:
                bucket.append((i,v))
                
        if len(bucket) == 0:
            continue
        max = sorted(bucket, key =lambda x:x[1],reverse=True)[0][1]
        for k in bucket:
            if k[1] == max:
                real_bucket.append(k[0])

        # print(bucket)
        answer = sorted(sorted(real_bucket),key=itemgetter(0))
    return answer


print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))