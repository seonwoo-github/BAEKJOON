# Question
'''
정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
'''

# Input
num = input()

# Answer
def solution(num):
    num = int(num)
    for i in range(1,num+1):
        print(num-i)

solution(num)