---
layout: post
title: 정렬과 탐색
category: data structures and algorithms
permalink: /algorithms/:year/:month/:day/:title/
tags: [algorithms, sorting, searching, 선형배열, data-structure]
comments: true
---

# 배열 - 정렬과 탐색
같은 종류의 데이터가 줄지어 늘어서 있는것. 파이썬에서 리스트로 제공됨. 원소들을 순서대로 늘어놓은 것. 


# python 리스트의 정렬
- sorted() : 내장함수(built-in fuction),정렬된 새로운 리스트를 얻어냄
- sort() :리스트의 메서드, 해당 리스트를 정렬함

```python
L = [3,5,1,2,4,68,85]
L2 = sorted(L)
print (L2) 
>>>> [1,2,3,4,5,68,85]
print (L)
>>>> [3,5,1,2,4,68,85]
L.sort()
print (L) 
>>>> [1,2,3,4,5,68,85]

L = ['abcd','xyz','spam']
sorted(L, key = lambda x:len(x))
>>>> ['xyz','abcd','spam']
L = ['spam','abcd','xyz']
>>>> ['xyz','spam','abcd']

L=[{'name':'john', 'score':83},{'name':'Paul', 'score':92}]
>>> L.sort(key=lambda x: x['score'], reverse=True)
[{'name': 'Paul', 'score': 92}, {'name': 'john', 'score': 83}]
```

# 탐색 알고리즘(1) - 선형탐색
- 순차적으로 하나씩 비교하여 찾아냄(모든 요소를 비교해서 찾기 때문에 선형 시간이 걸리 ) o(n)
- 배열의 길이에 비례하는 시간이 걸리므로, 끝일 경우 모든 리스트를 뒤져봐야함 

```python
def linear_search(L,x):
    i = 0
    while i < len(L) and L[i] !=x:
        i +=1
        if i <len(L):
            return i
        else: 
            return -1

>>> S = [3, 8, 2, 7, 6, 10, 9]
>>> linear_search(S, 6)
>>> 4 
```


# 탐색 알고리즘(2) - 이진탐색
- 탐색하려는 리스트가 이미 정렬되어 있는 경우 사용가능
- divde and conquer 이용 o(log n)

# 연습문제 - 이진탐색 구현
```python 

def solution(L,x):
    lower = 0
    upper = len(L)-1
    idx = -1
    while lower <= upper:
        middle = (lower+upper)//2
        if L[middle] == x:
            idx = middle
            break
        elif L[middle] < x:
            lower = middle + 1
        else:
            upper = middle -1
        return x

```