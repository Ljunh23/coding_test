def solution(n):
    answer = 0
    x = n ** (1/2)
    if x > int(x):
        answer = 2
    elif x == int(x):
        answer = 1
    return answer