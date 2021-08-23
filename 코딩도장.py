# 일치하는 아이디 찾기
# input_id = input("아이디를 입력하세요:\n")
# def login(_id):
#     members = ['baul', 'father', 'mother', 'brother','sister']
#     for member in members:
#         if member == _id:
#             return True
#     return False
# if login(input_id):
#     print("안녕하세요. %s님" %input_id)
# else:
#     print("일치하는 회원이 없습니다.")

# num = [-1, 1, 3, -2, 2]
# num2, num3 = [], []
# for num1 in num:
#     if num1 <= 0:
#         num2.append(num1)
#     else:
#         num3.append(num1)
# result = num2+ num3
# print("예.",*num,"ans:",*result,end='.')



# 피보나치 수열 구하기
# n= int(input("숫자를 입력:"))
# a=0;b=1
# print('0', end='')
# while b<=n:
#     print(', %d'%b, end='')
#     a,b = b,a+b

# num = int(input("첫번째 수를 입력 : "))
# num2 = int(input("두번째 수를 입력 : "))
# num_1 = num % 10 
# num_2 = num2 % 10
# if num_1 < num_2:
#     print("내림이 발생합니다.")
# else:
#     print("내림이 발생하지 않습니다.")