# "연도.월.일"을 입력 받아 "일-월-연도" 순서로 바꿔 출력해보자.

# 양식에 맞게 input을 받아온다.
y,m,d = input().split('.')

# answer
print(d + '-' + m + '-' + y)