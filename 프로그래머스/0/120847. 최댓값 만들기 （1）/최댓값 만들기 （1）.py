def solution(numbers):
    l = len(numbers)
    answer = numbers[0] * numbers[1]
    for i in range(l):
        for j in range(i+1, l):
            if answer < numbers[i] * numbers[j]:
                answer = numbers[i] * numbers[j]
    return answer