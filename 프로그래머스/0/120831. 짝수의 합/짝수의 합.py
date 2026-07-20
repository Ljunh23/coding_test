def solution(n):
    answer = 0
    if n <=1:
        answer = 0
    else:
        for i in range(2, n+1, 2):
            answer += i
    return answer