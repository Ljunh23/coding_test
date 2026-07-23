def solution(sides):
    answer = 0
    sides.sort()
    total = sum(sides[:2])
    if total > sides[2]:
        answer = 1
    else:
        answer = 2
    return answer