def check(result):
    for x,y,arc in result:
        if arc ==0:#기둥 경우
            if y == 0 or (x-1,y,1) in result or (x,y,1) in result or (x,y-1,0) in result:
                continue
            else: 
                return False
        elif arc ==1:# 보인 경우
            if ((x-1,y,1) in result and (x+1,y,1) in result) or (x,y-1,0) in result or (x+1,y-1,0) in result:
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    result = set()
    for a in build_frame:
        x,y,arc,how = a
        if how == 1:
            result.add((x,y,arc))
            is_valid = check(result)
            if is_valid:
                continue
            else:
                result.remove(((x,y,arc))
        else:
            if (x,y,arc) in result:
                result.remove((x,y,arc))
                is_valid = check(result)
                if is_valid:
                    continue
                else:
                    result.add((x,y,arc))
                              
    result = [list(i) for i in result]
                              
    return sorted(result, key = lambda x: ([0],x[1],x[2]))

print(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])