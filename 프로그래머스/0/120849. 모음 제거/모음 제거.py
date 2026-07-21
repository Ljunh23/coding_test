def solution(my_string):
    answer = ''
    vowel = 'aeiou'
    for x in my_string:
        if x not in vowel:
            answer += x
            
    return answer