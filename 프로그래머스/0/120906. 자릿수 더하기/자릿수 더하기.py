def solution(n):
    answer = 0
    num_str = str(n)
    for x in num_str:
        answer += int(x)
    return answer