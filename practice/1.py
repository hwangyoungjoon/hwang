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
def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])
    while True:
        remove_box = []
        for i in range(m-1):
            for j in range(n-1):
                if (board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]):

                        remove_box.append((i,j))
                        remove_box.append((i,j+1))
                        remove_box.append((i+1,j))
                        remove_box.append((i+1,j+1))



        remove_id = list(set(remove_box))
        if len(remove_id) == 0:
            break
        # print(remove_id)
        # print(remove_box)
        answer += len(remove_id)
        for idx in remove_id:
            i,j = idx
            print(i,j)
            board[i][j] = 0

        for i in range(n):
            for j in range(m-1,0,-1):
                if board[j][i] == 0:
                    start = j-1
                    value = '0'
                    while(start > -1):
                        if board[start][i] != 0:
                            value = board[start][i]
                            break
                        start -= 1
                    if value != '0':
                        board[j][i] = value
                        board[start][i] = '0'
                    else:
                        break
                    
    return answer
                
    
            
    
print(solution(4,5,	["CCBDE", "AAADE", "AAABF", "CCBBF"]))