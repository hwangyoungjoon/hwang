def solution(tickets):
    tic_dic = dict()
    for s,a in tickets:
        tic_dic[s] = tic_dic.get(s,[]) + [a]
    for k in tic_dic.keys():
        tic_dic[k].sort(reverse=True)
    
    stack = ["ICN"]
    visit = []
    while len(stack) > 0:
        top = stack[-1]
        if len(tic_dic.get(top,[])) == 0: ##this node will be not visited
            visit.append(stack.pop())
        else:
            stack.append(tic_dic[top].pop())

    return visit[::-1]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	))
