---
layout: post
title: 선형배열
category: data structures and algorithms
permalink: /algorithms/:year/:month/:day/:title/
tags: [algorithms, 선형배열, data-structure]
comments: true
---

# 배열
같은 종류의 데이터가 줄지어 늘어서 있는것. 파이썬에서 리스트로 제공됨. 원소들을 순서대로 늘어놓은 것. 


# 리스트(배열) 연산
1. 원소 덧붙이기 O(1)
2. 원소 꺼내기  O(1)
3. 원소 삽입하기 (선형시간) O(N)
4. 원소 삭제하기 (선형시간) O(N)
5. 원소 탐색하기 (선형시간) O(N)

```python
#1 원소 덧붙이기
L=['BOB', 'CAT','SPAM']
L.append('new')
print("결과:", L)

#2 원소 꺼내기
L.pop()
print("결과:", L)

#3 원소 삽입하기
L= [20,30,50,60]
L.insert(3,65) #3번 인덱스에 65삽입
                #3번 인덱스를 4번으로 밀어넣음
                #4번 값을 5번으로 밀어넣음 점점 뒤로 밀려서 완성
                #3번에 삽입
#4 원소 삭제하기
del(L[2])#2번 인덱스 찾기
                #3번 인덱스를 2번으로 밀어넣음
                #4번 값을 3번으로 밀어넣음 점점 뒤로 밀려서 완성
                #마지막 인덱스 삽입 
                # 즉 복사해서 앞으로 떙기고 마지막 원소 삭제

#5 원소 탐색하기
L=['BOB', 'CAT','SPAM']
L.index('SPAM')
```

# 연습문제
```python
# 정렬된 리스트에 주어진 원소 삽입
def solution(L,x):
    L.append(x)
    L.sort()
    return L

# 리스트에서 원소 찾기
def solution(L,x):
    ind = []
    for i in range(len(L)):
        if L[i] == x:
            ind.append(i)
    if len(ind)==0:
        return [-1]
    return ind
```