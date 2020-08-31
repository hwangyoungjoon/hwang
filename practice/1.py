# def solution(n, costs):
#     answer = 0
#     costs.sort(key = lambda x:x[2]) #비용에 따라서 오름차순으로 정렬 이렇게 함으로써 앞으로의 과정에서 연결되느냐가 중요함. 
#     visited = [0]*n
#     visited[0] = 1
#     while sum(visited) !=n: #섬이 연결되지 않으면 계속 반복
#         for cost in costs:
#             start,end,c = cost
#             if visited[start] or visited[end]: #둘중 하나라도 값이 1이면 그 섬이 나왔던 거임
#                 if visited[start] and visited[end]: # 두섬이 연결되어 있다면
#                     continue
#                 else:
#                     visited[start] = 1
#                     visited[end] = 1
#                     answer += c
#                     break
#     return answer

    

# n= 4
# cost = [[0,1,1], [0,2,2], [1,2,5],[1,3,1], [2,3,8] ]

# print(solution(n, cost))

def solution(N,number):
    S = [0,{N}]
    for i in range(2,9):
        case_set = {int(str(N)*i)}
        for i_half in range(1,i//2+1):
            for x in S[i_half]:
                print(S[i_half])
                for y in S[i-i_half]:
                    print(S[i-i_half])
                    case_set.add(x+y)
                    case_set.add(x-y)
                    case_set.add(y-x)
                    case_set.add(x*y)
                    if x != 0:
                        case_set.add(y//x)
                    if y != 0:
                        case_set.add(x//y)
        if number in case_set:
            return i
        S.append(case_set)
    return -1

print(solution(2,11))
                    