# N = int(input("수를 입력 : "))
# if N % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# N = int(input("수를 입력 : "))
# for i in range(1, N+1):
#     if i % 2 == 0:
#         print(i, "= 짝수")
#     else:
#         print(i, "= 홀수")

# a = []
# b = []
# N = int(input("수를 입력 : "))
# for i in range(1, N+1):
#     if i % 2 == 0:
#         a.append(i)
#     else:
#         b.append(i)
# print("짝수 :",sum(a))
# print("홀수 :",sum(b))

# N = int(input("수를 입력 : "))

# for i in range(1, N+1):
#     if i % 2 == 0:
#         print(i, "짝수")
#     else:
#         print(i, "홀수")

# li = []
# N = int(input("수를 입력 : "))
# li.append(N)
# print(li)

# li = []
# N = int(input("수를 입력 : "))
# for i in range(1, N+1):
#     li.append(i)
# print(li)

# li = []
# N = int(input("수를 입력 : "))
# for i in range(1, N+1):
#     if i % 2 == 1:
#         li.append(i)
# print(li)

# N = int(input("수를 입력 : "))
# if N % 3 == 0:
#     print(N,": 3의 배수입니다.")
# else:
#     print(N,": 3의 배수가 아닙니다.")

# N = int(input("수를 입력 : "))

# if N % 4 == 0:
#     print("당번: D")
# elif N % 4 == 1:
#     print("당번: A")
# elif N % 4 == 2:
#     print("당번: B")
# else:
#     print("당번: C")

# N = int(input("입력: "))

# for i in range(1, N+1):
#     if i % 4 == 0:
#         print(i,"일 당번: D")
#     elif i % 4 == 1:
#         print(i,"일 당번: A")
#     elif i % 4 == 2:
#         print(i,"일 당번: B")
#     else:
#         print(i,"일 당번: C")

# N = int(input())
# result = 0
# for i in range(1, 10):
#     result = N * i
#     print(N,'*',i,'=',result)

# N = int(input())
# for i in range(N):
#     N1, N2 = input().split()
#     N1 = int(N1)
#     N2 = int(N2)
#     print(N1 + N2)

# li = []
# N = int(input())
# for i in range(1, N+1):
#     li.append(i)
# print(sum(li))

# li = []
# N = int(input())
# for i in range(1, N+1):
#     li.append(i)
# li.reverse()
# for j in li:
#     print(j)

# N=int(input())
# for i in range(1,N+1):
#     print(N)
#     N -= 1

# N = int(input())
# for i in range(1,N+1):
#     N1, N2 = input().split()
#     N1 = int(N1)
#     N2 = int(N2)
#     result = N1 + N2
#     print("Case #%d: %d + %d = %d"% (i, N1, N2, result))

# N = int(input())
# for i in range(1,N+1):
#     N -= 1
#     print(N * ' ' + i * '*')

# N1, N2 = input().split()
# N1 = int(N1)
# N2 = int(N2)
# N3 = input().split()
# for i in N3:
#     i = int(i)
#     if i < N2:
#         print(i,end=' ')

# for i in range(2,10):
#     print(i,'단 출력')
#     for j in range(1,10):
#         print(f"{i} x {j} = {i*j}")
#    
#     print()

# for k in range(2,10):
#     print(k,'단 출력',end='\t')
# print()
# for i in range(1,10):
#     for j in range(2,10):
#         print(f"{j} x {i} = {j*i}", end = '\t')
#     print()

# 1~N까지 수 입력
# 각각의 수의 짝수개수 구한 다음 변수담기
# 1~N 범위가 바뀔때마다 변수는 초기화 (외반복문)
# 1 1
# 2 12 1개
# 3 123 1개
# N = int(input())
# for k in range(1, N+1):
#     li = []
#     for i in range(1,k+1):
#         if i % 2 == 0:
#             li.append(i)
#     print(i,len(li))

# li = []
# for i in range(1,3):
#     n = int(input('수학:')) 
#     n1 = int(input('국어:')) 
#     n2 = int(input('영어:')) 
#     avg = (n+n1+n2) // 3
#     li.append(avg)
# for j in li:
#     if j < 70:
#         continue
#     elif 70 <= j <80:
#         print("100만원")
#     elif 80 <= j < 85:
#         print("150만원")

# i = 2 
# while i < 10:
#     j = 1
#     while j <10:
#         print(f"{i} x {j} = {i * j}")
#         j += 1
#     i+=1

# i = int(input("수 입력 : "))
# j = 1
# while j < 10:
#     print(f"{i} x {j} = {i*j}")
#     j += 1

# N = int(input())
# for i in range(1,N+1):
#     su = 0
#     for j in range(1,i+1):
#         if j % 2 == 0:
#             su += 1
#     print(i, su)

# 3~N 까지 수를 i에 넣는다.
# 3~N각각의 수를 j에 넣는다
# j를 i로 나눈후 
# su는 외반복문에 적용(초기화)
#  4 1234 123 
#  5 12345 1

# N = int(input("수를 입력 : "))
# for i in range(3,N+1):
#     li = []
#     for j in range(1,i+1):
#         if i % j ==0:
#             li.append(j)
#     print(i,li)

# 6 = 1+2+3
# 28 = 1+2+4+7+14 
# 완전수
# 1 1
# 2 12
# 3 123
# 4 1234
# 5 12345
# 6 123456
# N = int(input("수 입력 : "))

# for i in range(1, N+1):
#     li = []
#     for j in range(1, i):
#         if i % j == 0:
#             li.append(j)
#     if sum(li) == i:
#         print(i,"는 절댓값")
#  10 입력 
# 3 4 5 6 7 8 9 10
# 소수는 3 5 7 9 
# N = int(input("수 입력 : "))
# for i in range(1,N+1):
#     li = []
#     for j in range(1, i+1):
#         if i % j ==0:
#             li.append(j)
# 5! = 1*2*3*4*5 = 120

# N = int(input("수를 입력 : "))
# for i in range(1,N+1):
#     gop = 1
#     for j in range(1,i+1):
#         gop *= j
#     print(i,gop)
# for i in range(2,10):
#     for j in range(1, 10):
#         print(i,j,i*j,end='\t')
#         print()
