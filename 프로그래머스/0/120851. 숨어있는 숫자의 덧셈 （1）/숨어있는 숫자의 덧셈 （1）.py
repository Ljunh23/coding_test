def solution(my_string):
    answer = 0
    sum = ""
    for i in range(10):
        sum += str(i)
    for num in my_string:
        if num in sum:
            answer += int(num)
    return answer