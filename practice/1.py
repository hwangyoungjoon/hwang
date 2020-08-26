def solution(citations):
    answer = 0
    max_h = max(citations)
    if max_h ==0:
        return 0

    for i in range(max_h):
        citation_h = [c for c in citations if c-i>=0]
         
        if len(citation_h) <i:
            return i-1


citation =[0,0,0,9]
a= solution(citation)
print(a)