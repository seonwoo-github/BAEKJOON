# Question
'''
 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
'''

# Input
num = input()

# Answer
def solution(num):
    num = int(num)
    
    for i in range(num+1):
        print(i)

solution(num)