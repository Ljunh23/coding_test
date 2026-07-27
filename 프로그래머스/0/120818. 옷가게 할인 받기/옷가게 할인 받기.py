def solution(price):
    answer = 0
    a = 100000
    b = 300000
    c = 500000
    if price >= c:
        answer = price * (80/100)
    elif price >= b:
        answer = price * (90/100)
    elif price >= a:
        answer = price * (95/100)
    else:
        answer = price
    return int(answer)