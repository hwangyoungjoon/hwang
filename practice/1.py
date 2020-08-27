

def solution(people, limit):
    
    answer = 0
    people.sort(reverse=True)
    start = 0
    end = len(people) - 1
    while start < end:
        if people[start]+people[end] <=limit:
            end -= 1

        start += 1
    return 0

people= [70, 50, 80, 50]
limit = 100
solution(people, limit)