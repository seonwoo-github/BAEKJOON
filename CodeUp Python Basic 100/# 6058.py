# Question
'''
2개의 정수값이 입력될 때,
그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.
'''

# Input
a, b = input().split(' ')

# Answer
def solution(a, b):
    a = int(a)
    b = int(b)
    
    if a and b == int(0):
        pirnt('True')
    else:
        print('False')
        
solution(a, b)