# # print문 실습
# name = '한바울'
# age = 24
# email = 'hbwhbw123@naver.com'
# hobby = '노래부르기'
# movie = '어바웃타임'
# singer = '김범수,전상근'
# print("나의 이름은", name, "입니다.", end = ' 그리고 ')
# print("내 나이는", age, "입니다.")
# print("내 이메일 주소는 ", email, "입니다.")
# print("내 취미는", hobby, "입니다.")
# print("내가 좋아하는 영화는", movie, "입니다.")
# print("내가 좋아하는 가수는", singer, "입니다.")

# type(자료형)
# 자료의 자료형을 반환
# print(type(2.3)) class 'float'
# print(type(1)) = class 'int'
# print(type("hello")) = class 'str'

# a = 10
# b = 3

# print(a+b) #더하기
# print(a-b) #빼기
# print(a*b) #곱하기
# print(a/b) #나누기
# print(a//b) #//는 몫
# print(a%b) #%는 나머지
# print(a**b) # **는 제곱


#변수 사칙연산 
# a = 20
# b = 5

# print("A 는 %d 입니다." %a)
# print("B 는 %d 입니다." %b)
# print()
# print("A + B =", a+b)
# print("A - B =", a-b)
# print("A x B =", a*b)
# print("A / B =", a/b)
# print("A // B =", a//b)
# print("A % B =", a%b)
# print("A ** B =", a**b)

#연산자 사용법
# a = 'Hello'
# b = 'World'
# print(a +' '+ b)
# print(a* 3)


# A = "대한독립"
# B = "만세"
# C = A +' '+B*3 + '~'*5

# print(C)

# a = 847 
# //, %
# 세자리 수에서 일의 자리를 뽑아내는 공식은 !!a??
# 십의자리 백의자리 뽑아내는 공식은 ??
# a = 847
# print(a//100) #백의자리
# print(a%100//10) #십의자리
# print(a%10) #일의자리


# 임의의 4자리수 시, 분, 초로 분리하는식
# EX) a = 3880    > 1시 4분 40 초  
# a = 3880
# hour = a // 60 //60
# min1 = a // 60 % 60
# sec = a % 60 
# print("%d시 %d분 %d초" % (hour, min1, sec) ) # 시간 분리하는 공식

# #테스트1
# a = 7850 #2시 10분 50초 
# hour = a // 60 //60
# min1 = a // 60 % 60
# sec = a % 60 
# print("%d시 %d분 %d초" % (hour, min1, sec) )

# print(type(1))

# 입력받아 더하기
# num = int(input("수를 입력하세요:"))
# num2 = int(input("수를 입력하세요:"))
# print("더한 값은:",num+num2)

# 자료형(자료)
# 자료의 형태를 자료형으로 바꿈 
#int , str, float 자료형은 자료의 맞게 사용할 수 있다.
# ex) int(1.2) => 1로 출력됩니다.
# A = input("입력 :")
# int(A) => int형으로 바뀌지 않는다.
# A = int(A) 로 해야 int 형으로 바뀐다. 
# 차라리 입력과 동시에 int로 바꾸면 좋다. 
# ex) A = int(input("입력 : "))


# 평균을 구하는 계산기
# math = int(input("수학점수를 입력하세요:"))
# kor = int(input("국어점수를 입력하세요:"))
# science = int(input("과학점수를 입력하세요:"))
# avg = (math+kor+science)/3
# print("평균은:%d점" % avg)


#사과가격 배가격 총금액 구하는 프로그램 
# 사과가격 = 3000
# 배가격 = 2000
# print('='*30)
# print('사과 가격:',사과가격)
# print('배가격:', 배가격)
# print('='* 30)

# apple= int(input("사과의 개수를 입력하세요:"))
# pear = int(input("배의 개수를 입력하세요:"))
# value = apple*사과가격 + pear*배가격
# print("총 금액은:%d원" %value)

# 총 시간을 입력받아 초로 변환시켜주는 프로그램
# print('×' * 50)
# print("시간을 입력 받아 총 몇초 인지 계산해주는 프로그램")
# print('×' * 50)
# 시 = int(input("몇시인가요?: "))
# print('×' * 50)
# 분 = int(input("몇분인가요?: "))
# print('×' * 50)
# 초 = int(input("몇초인가요?: "))
# print('×' * 50)
# 시_초 = 시 * 60 * 60
# 분_초 = 분 * 60
# 총합초 = 시_초 + 분_초 + 초
# print("총 %d초입니다."%총합초)
# print('×'*50)

# print('='*30)
# print('섭씨를 화씨로')
# print('='* 30)
# 섭씨 = float(input("섭씨온도를 입력해주세요:"))
# 화씨 = (섭씨 * 9/5) + 32
# print("섭씨온도 : ",섭씨)
# print("섭씨온도", 섭씨,"=> " "화씨는:", 화씨)

# print("="*30)
# print("화씨온도를 섭씨로")
# print('='* 30)
# 화씨 = float(input("화씨를 입력해주세요:"))
# 섭씨 = (화씨 - 32) * 5/9
# print("섭씨는:", 섭씨)

# bmi계산기
# 신장 = float(input("신장을 입력(m):"))
# 몸무게 = float(input("몸무게를 입력(kg):"))
# bmi = 몸무게 / (신장 ** 2)
# print("bmi는:", round(bmi,1))

# 세자리수 각자리구하기
# 세자리수 = int(input("세자리수를 입력하세요:"))
# print("백의자리는:",세자리수 // 100 )
# print("십의자리는:",세자리수 % 100 //10)
# print("일의자리는:",세자리수 %10)

# 시간구하기
# 총초 = int(input("총 sec를 입력해주세요:"))
# 시 = 총초//3600
# 분 = 총초 // 60 % 60
# 초 = 총초 % 60
# print("총 초 :", 총초)
# print("%d시간 %d분 %d초"% (시, 분, 초) )

# 삼각형_밑변 = float(input("삼각형의 밑변을 입력하세요(cm):"))
# 삼각형_높이 = float(input("삼각형의 높이를 입력하세요(cm):"))
# 삼각형_넓이 = (삼각형_밑변 * 삼각형_높이) /2
# print("삼각형의 넓이는:",round(삼각형_넓이,2),'cm^2')

# 원_반지름 = float(input("원의 반지름을 입력하세요(cm):"))
# 원주율 = 3.14
# 원_넓이 = (원_반지름 ** 2) * 원주율
# 원_둘레 = (원_반지름 * 2) * 원주율
# print("원의 둘레는:",round(원_둘레,2),"r""\n원의 넓이는:",round(원_넓이,2),'cm^2')

# if문 ~라면 , ~가 아니라면
# bool형 참,거짓을 나타내는 자료형
# bool형은 첫글자가 대문자여야 bool형이 인정된다.
# ex)Ture O ture X
# bool형이 Flase가 되는 경우는 숫자일때 0, 0.0 문자일때 ""아무것도 없을때 이다.
# 숫자, 문자열 Bool자리로 들어가게 되면 bool값으로 바뀌어서 해석된다.
# ex) if 1: => True , if 0: => Flase

# 논리연산자
# and : 둘다 True 일때만 True
# or : 하나라도 Ture이면 True 
# 산술 > 비교 > 논리 ( and > or)

# 비교연산자
# print(10 > 0)    #A > B    
# A가 크면 True 아니면 False 

# print(10 < 0)    #A < B    
# B가 크면 True 아니면 False 

# print(10 == 0)  #A == B  
# A와 B가 같으면 True 다르면 False

# print(10 != 0)   #A != B     
# A와 B가 다르면 True 같으면 False

# print(10 >= 0)   #A >= B   
# A가 B보다 크거나 같으면 True 
# 아니면 False

# 조건문 if
# if [Bool]: <- 콜론 중요! 
#....[종속문장] <-들여쓰기 중요!
# :콜론이 오면 다음문장은 무조건 종속문장! 
# 종속문장에 시작을 알림!
# 

# A = int(input("수 입력 : "))

# if 0<=A<10:
#     print(A, "한자리수 입력 !!")
# if 10<=A<100:
#     print(A, "두자리수 입력 !!")

# 수 = int(input("수를 입력 : "))
# if 수 > 0:
#     print(수,"는 양수")
# elif 수 == 0:
#     print(수)
# elif 수 < 0:
#     print(수,"는 음수")

# 한수 = int(input("수를 입력 : "))
# 두수 = int(input("수를 입력 : "))
# if 한수 < 두수:
#     print(두수,"더 큽니다.")
# elif 한수 > 두수:
#     print(한수,"더 큽니다.")
# elif 한수 == 두수:
#     print("둘이 같습니다.")

# num = int(input("수 입력 : "))
# if num % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# num = int(input("수 입력 : "))
# if num % 3 ==0:
#     print("3의 배수입니다!")
# else:
#     print("3의 배수가 아닙니다!")

# 현재 시간과 분을 입력받고, 30분전시간을 출력하는 프로그램!!
# 시 = int(input("몇 시 : "))
# 분 = int(input("몇 분 : "))
# 분 = 분 - 30
# if 분 < 0:
#     분 = 60+분
#     시 = 시-1
#     if 시 < 0:
#         시 = 24 + 시
# print("%d시 %d분" % (시,분))

# 합격을알려주는프로그램
# 국어 = int(input("국어점수를 입력하세요 : "))
# 수학 = int(input("수학점수를 입력하세요 : "))
# 평균 = (국어 + 수학) / 2
# if 평균 >= 80:
#     print("축하합니다! 합격입니다!\n오늘은치킨이닭")
# else:
#     print("아쉽습니다. 불합격입니다!")

# n분전시간을 알려주는 프로그램
# 시 = int(input("현재 몇 시입니까? : "))
# 분 = int(input("현재 몇 분입니까? : "))
# n분 = int(input("몇 분 전 시간을 알려드릴까요?: "))
# 분 = 분 - n분
# if 분 < 0:
#     분 = 60+분
#     시 = 시-1
#     if 시 < 0:
#         시 = 24 + 시
# print("%d시 %d분" % (시,분))

# 수1 = int(input("수를 입력:"))
# 수2 = int(input("수를 입력:"))
# 수1_올림발생 = 수1 % 10
# 수2_올림발생 = 수2 % 10
# if 수1_올림발생 + 수2_올림발생 < 10:
#     print("올림이 발생하지 않습니다.")
# elif 수1_올림발생 + 수2_올림발생 >= 10:
#     print("올림이 발생합니다.")
#
# 연산자를 입력받아 계산하기 
# 수1 = int(input("수를 입력하세요 : "))
# 수2 = int(input("수를 입력하세요 : "))
# 연산 = input("연산을 입력하세요 : ")

# if 연산 == "+":
#     print("%d 와 %d 의 합은" %( 수1, 수2), 수1+수2)

# if 연산 =="*" or 연산=="x" or 연산== "X":
#     print(수1*수2)

# if문 확장 
# elif == else if
# 여러 조건 중 위에서 True가 되었을 때 나머지 조건은 실행하지 않는다.
# ex) choice = 4 
# ex) 
# if choice == 1:
# ....print("1번") => choice가 해당하지 않아 실행되지 않는다.
# elif choice == 4:
# ....print("4번") => 4번 이후로 실행되지 않는다.
# elif choice == 5:
# ....print("5번") => 실행되지 않는다.
# else:
# ....print("그밖에")
# 만약 choice = 10 일 경우 if, elif 조건이 충족 되지 않기 때문에 else로 넘어가 else가 실행된다.
# if는 무조건 써줘야 한다. 왜냐하면 elif,else는 if의 확장이기 때문이다.
# if 다음에 바로 elif, if 다음에 바로 else 사용가능

# num = int(input("수를 입력:"))
# if num % 2 == 0:
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")


# 평균을 학점으로 변환하는 프로그램
# math = int(input("수학 점수:"))
# sci = int(input("과학 점수:"))
# avg = (math + sci) / 2
# if avg >= 90:
#     print("A")
# elif avg >= 80:
#     print("B")
# elif avg >= 70:
#     print("C")
# else:
#     print("D")

# 두 수와 연산자를 입력받고 사칙연산 결과를 출력하는 프로그램을 작성하세요.
# num   = int(input("첫번째 수를 입력하세요:"))
# num2  = int(input("두번째 수를 입력하세요:"))
# 연산자 = input("연산자를 입력하세요:")

# if 연산자 == "+":
#     print(num + num2)
# elif 연산자 == "-":
#     print(num - num2)
# elif 연산자 == "/":
#     print(num / num2)
# elif 연산자 == "*" or 연산자 == "X" or 연산자 == "x":
#     print(num * num2)
# else:
#     print("연산자가 이상해요.")

# 월을 입력받고, 계절을 출력하는 프로그램
# mon = int(input("월:"))
# if 3 <= mon < 6:
#     print("%d월은 봄입니다!" % mon)
# elif 6 <= mon <= 8:
#     print("%d월은 여름입니다!" % mon)
# elif 9 <= mon <= 10:
#     print("%d월은 가을입니다!" % mon)
# elif 1 <= mon <= 2 or 11<= mon <= 12:
#     print("%d월은 겨울입니다!" % mon)
# else:
#     print("입력이 바르지 않습니다.")

# 로그인 프로그램
# 아이디 = input("아이디 입력 : ")
# if 아이디 == "admin":
#     print("Hello Amdin")

#     패스워드 = input("패스워드 입력 : ")
#     if 패스워드 == "admin":
#         print("Login Success!!")
#     else:
#         print("Wrong password :(")
# else:
#     print("No User :(") 


# 수 = int(input("수 : "))
# if 수 < 0:
#     print("절대값은",-(수), "입니다.")
# else:
#     print("절대값은 %d 입니다." % 수)
# 물건을 사서 계산하는 프로그램
# print('='* 30)
# print("사과:3000원\n배:2000원")
# print('='* 30)

# 사과 = 3000
# 배 = 2000

# 사과_개수 = int(input("구입하실 사과의 개수를 입력하세요(개수):"))
# 배_개수 = int(input("구입하실 사과의 개수를 입력하세요(개수):"))
# 지갑 = int(input("지갑안에 있는 돈을 입력하세요(원):"))

# 사과_금액 = 사과 * 사과_개수
# 배_금액 = 배 * 배_개수
# 총금액 = 사과_금액 + 배_금액
# if 지갑 > 총금액:
#     print("구입하셨습니다. 잔돈은:%d원입니다." % (지갑- 총금액))
# elif 지갑 < 총금액:
#     print("구매가 불가능합니다. 돈이 %d원 더 필요합니다." % (총금액 -지갑))
# else:
#     print("구매를 완료했습니다. 잔돈 반환이 없습니다.")

# 3의배수 5의배수 15의배수 출력하는 프로그램
# A = int(input("수 입력:"))
# if A % 3 == 0 and not A % 15 == 0:
#     print("3의 배수입니다.")
# elif A % 5 == 0 and not A % 15 == 0:
#     print("5의 배수입니다.")
# elif A % 15 ==0:
#     print("15의 배수입니다.")
# 
# 커피자판기
# print('='*20)
# print("1. 아메리카노\n2. 카페라떼")
# print('='*20)
# 메뉴 = int(input("메뉴 선택 :"))
# print('='*20)
# print("1. ICE\n2. HOT")
# print('='*20)
# 온도 = int(input("온도 선택 :"))
# if 메뉴 == 2 and 온도 == 1:
#     print("아이스 카페라떼 선택")
# elif 메뉴 == 1 and 온도 == 2:
#     print("핫 아메리카노 선택")
# elif 메뉴 and 온도 == 2:
#     print("핫 카페라떼 선택")
# elif 메뉴 and 온도 == 1:
#     print("아이스 아메리카노 선택")
# 
# 거꾸로 뒤집었을때 더 높은 숫자
# A = int(input("3자리 수를 입력하세요:"))
# B = int(input("3자리 수를 입력하세요:"))
# #                  
# r_A = A % 10 * 100 + A % 100 // 10 * 10 + A // 100
# r_B = B % 10 * 100 + B % 100 // 10 * 10 + B // 100
# if r_A > r_B:
#     print("뒤집었을 때 더 큰수는", A)
# elif r_A < r_B:
#     print("뒤집었을 때 더 큰수는", B)
# else:
#     print("서로 값이 같습니다.")


# 년도입력시 띠 출력하는 프로그램
# 생년월일 = input("생년월일을 입력하세요(yyyymmdd):")

# 생년 = int(생년월일[0]+생년월일[1]+생년월일[2]+생년월일[3])

# if   생년 % 12 == 4:
#     print("자(쥐띠)")
# elif 생년 % 12 == 5:
#     print("축(소띠)")
# elif 생년 % 12 == 6:
#     print("인(호랑이띠)")
# elif 생년 % 12 == 7:
#     print("묘(토끼띠)")
# elif 생년 % 12 == 8:
#     print("진(용띠)")
# elif 생년 % 12 == 9:
#     print("사(뱀띠)")
# elif 생년 % 12 == 10:
#     print("오(말띠)")
# elif 생년 % 12 == 11:
#     print("미(양띠)")
# elif 생년 % 12 == 0:
#     print("신(원숭이띠)")
# elif 생년 % 12 == 1:
#     print("유(닭띠)")
# elif 생년 % 12 == 2:
#     print("술(개띠)")
# else:
#     print("해(돼지띠)")

# 청소당번 찾는 프로그램
# n일 = int(input("며칠째 당번을 찾으시나요?:"))
# if n일 % 4 == 1:
#     print("A")
# elif n일 % 4 == 2:
#     print("B")
# elif n일 % 4 == 3:
#     print("C")
# else:
#     print("D")


# n일을 입력받아 무슨 요일인지 출력해주는 프로그램
# print("오늘은 화요일입니다.")
# print("=" * 33)
# n일 = int(input("며칠 뒤 요일을 알고 싶으신가요?:"))
# print("="*33)
# if n일 % 7 == 0:
#     print("%d일 뒤 화요일입니다."% n일)
# elif n일 % 7 == 1:
#     print("%d일 뒤 수요일입니다."% n일)
# elif n일 % 7 == 2:
#     print("%d일 뒤 목요일입니다."% n일)
# elif n일 % 7 == 3:
#     print("%d일 뒤 금요일입니다."% n일)
# elif n일 % 7 == 4:
#     print("%d일 뒤 토요일입니다."% n일)
# elif n일 % 7 == 5:
#     print("%d일 뒤 일요일입니다."% n일)
# else:
#     print("%d일 뒤 월요일입니다."% n일)

# 사분면 구하기
# x = int(input("x의 값을 입력하세요:"))
# y = int(input("y의 값을 입력하세요"))

# if x > 0 and y > 0:
#     print("1")
# elif x < 0 and y > 0:
#     print("2")
# elif x < 0 and y < 0 :
#     print("3")
# elif x > 0 and y < 0 :
#     print("4")
# else:
#     print("사분면에 위치하지 않습니다.")

# A, B = input().split()
# A = int(A)
# B = int(B)
# if A > B:
#     print('>')
# elif A < B:
#     print('<')
# else:
#     print('==')

# 년도 = int(input("년도를 입력하세요:"))
# if 년도 % 4 == 0 and 년도 % 400 == 0 and 년도 % 100 == 0:
#     print("윤년 입니다.")
# elif 년도 % 4 == 0 and 년도 % 100 == 0 and not 년도 % 400 == 0:
#     print("평년 입니다.")
# elif 년도 % 4 == 0 or 년도 % 400 == 0:
#     print("윤년입니다.")
# else:
#     print("윤년,평년 이 아닙니다.")

# li = []
# while len(li) < 1000:
#     n = [int(input("리스트에 추가할 수 입력 : "))]
#     for num in n:
#         li.append(num)
#         print(li)

# li = []
# while len(li) < 1000:
#     n = [int(input("리스트에 추가할 수 입력 : "))]
#     for num in n:
#         if num % 2 ==1:
#             li.append(num)
#             print(li)

# n1 = int(input("수를 입력 : "))
# n2 = int(input("수를 입력 : "))
# n3 = int(input("수를 입력 : "))
# li = []
# li.append(n1)
# li.append(n2)
# li.append(n3)
# avg = sum(li)/len(li)
# print(round(avg,2))

#  반복문에는 for 과 while 이 있다.
#  for문은 반복횟수가 명확할 때 사용한다.
# ex) 60계치킨처럼~ 
# while은 반복횟수가 명확하지 않을때 사용한다.
# while은 게임, GUI 에 많이 사용한다.
# for 문은 프로그램에 주축이 된다. (중요함!)
# list(리스트)나 tuple(튜플)은 마지막에 ,(콤마)로 끝나도 상관이 없다!
# 인덱싱 (인덱스를 가지고 자료에 접근)
# 리스트, 튜플의 이름[index]
# 0부터 시작!
# ex)  0  1  2   3    4     5
# a = [1, 2, 3, 'a', 'c', True]  a[2] = '3'
# 리스트 자료형은 자료변경이 가능하다.
# 튜플 자료형은 자료변경이 불가능하다.
# 다루는 자료의 특성에 따라 맞는 자료형을 선택해서 사용!

# len(집합 자료형의 요소의 개수)
# sum(집합자료형의 모든 요소들의 합)

# a = [1, 2, 3, 4]
# n = int(input("수를 입력"))
# if n % 2 == 1:
#     a.append(n)
# print(a)

# iterable : 반복가능한개체
# str, list, tuple, set, dict 
# for [반복문에서 사용될 변수] in [iterable 자료형]:
# ....[종속문장]
# 반복 횟수 : 자료형의 크기 만큼 종속문장 실행
# 반복문에서 사용될 변수 : iterable 자료형 내 자료들
# ex)
# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
# 1 회 반복시 print(1)
# 2 회 반복시 print(2)
# .......
# 9 회 반복시 print(9) 

# for i in (1, 2, 3, 4, 5, 6, 7, 8, 9):
#     print(i)

# python-for : iterable 자료형 내 자료에 접근하기 위한 문법

# A = [1, 1.2, 1-2j, "Hello", "World", "Life","is","too",'short,','you need python!']
# for i in A:
#     print(i)

# range([start:0], stop, [step:1])
# start 부터 stop 전 까지의 리스트로 반환 
# (증감 : step), []는 생략가능 

# for i in range(11):
#     print(i)
# print('='*20)
# for i in range(30, 40):
#     print(i)
# print('='*20)
# for i in range(11, 17, 4):
#     print(i)
# print('='*20)

# for i in range(1, 1001):
#     print(i, end=',')
# 
# 
# N = int(input("수를 입력 : "))
# for i in range(1, N+1, -1):
#     print(i)

# A = int(input("수를 입력 : "))
# B = int(input("수를 입력 : "))
# if A < B:
#     for i in range(A+1, B):
#         print(i)

# else:
#     for i in range(A-1,B,-1):
#         print(i)

# num = 0
# N = int(input("수를 입력 : "))
# for i in range(1,N+1):
#     num += i 
# print(num)
#
#  su = 1
# N = int(input("수를 입력 : "))
# for i in range(1, N+1):
#     su *= i
# print(N, "!:", su)

# 홀 = []
# 짝 = []
# N = [int(input("수를 입력 : "))]
# for i in N:
#     if i % 2 == 0:
#         짝.append(i)
#         print("짝수:",짝)       
#     else:
#         홀.append(i)
#         print("홀수:", 홀)
#
# 홀 = []
# 짝 = []
# N = int(input("수를 입력 : "))
# for i in range(1, N+1):
#     if i % 2 == 0:
#         짝.append(i)
            
#     else:
#         홀.append(i)

# print("짝수:",짝)
# print("홀수:",홀)

# 홀 = []
# 짝 = []
# N = int(input("수를 입력 : "))
# for i in range(1, N+1):
#     if i % 2 == 0:
#         짝.append(i)
            
#     else:
#         홀.append(i)

# print("짝수:",sum(짝))
# print("홀수:",sum(홀))

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
#     print("3의배수")
# else:
#     print("3의배수가 아닙니다.")

# N = int(input("수를 입력 : "))
# for i in range(1,N+1):
#     if i % 3 == 0:
#         print("3의배수:", i)

# N= int(input("며칠 뒤 당번을 찾으시나요:"))
# if N % 4 == 1:
#     print("B가 당번입니다.")
# elif N % 4 == 2:
#     print("C가 당번입니다.")
# elif N % 4 == 3:
#     print("D가 당번입니다.")
# else:
#     print("A가 당번입니다.")

# N= int(input("며칠 뒤 당번을 찾으시나요:"))
# for i in range(N+1):
#     if i % 4 == 0:
#         if i == 0:
#             i = "오늘"
#         print("%s : A가 당번입니다." % i)
#     elif i % 4 == 1:
#         print(i,": B가 당번입니다.")
#     elif i % 4 == 2:
#         print(i,": C가 당번입니다.")
#     else:
#         print(i,": D가 당번입니다.")

# N = int(input("년도를 입력하세요:"))
# for 년도 in range(1, N+1):
#     if 년도 % 400 == 0
#         print(년도,"년은 윤년입니다.")
#     elif 년도 % 100 == 0
#         continue
#     elif 년도 % 4 == 0
#         print(년도, "년은 윤년입니다.")
#     else:
#         continue

# 시 = int(input("시간을 입력 : "))
# 분 = int(input("분을 입력 : "))
# n = int(input("몇분전으로 돌아갈까요"))
# 총_분= (시 * 60) + 분 - n
# N_시 = 총_분 // 60
# N_분 = 총_분 % 60
# print(N_시,"시",N_분,"분")

# 시 = int(input("시간을 입력 : "))
# 분 = int(input("분을 입력 : "))
# n = int(input("몇분후로 돌아갈까요"))
# 총_분= (시 * 60) + 분 + n
# N_시 = 총_분 // 60
# N_분 = 총_분 % 60
# print(N_시,"시",N_분,"분")

# N = int(input("며칠째 당번을 찾으시나요:"))
# if N % 12 == 1 or N % 12 ==2 or N % 12 ==3:
#     print("A가 당번입니다.")
# elif N % 12 == 4 or N % 12 ==5 or N % 12 ==6:
#     print("B가 당번입니다.")
# elif N % 12 == 7 or N % 12 ==8 or N % 12 ==9:
#     print("C가 당번입니다.")
# else:
#     print("D가 당번입니다.")

# N = int(input("수를 입력 : "))
# if N % 2 == 0:
#     print("짝수")
# else: 
#     print("홀수")

# 홀 = []
# 짝 = []
# N = int(input("수를 입력 : "))
# for i in range(1, N+1):
#     if i % 2 == 0:
#         짝.append(i)
#     else:
#         홀.append(i)

# print("짝수:",짝)
# print("홀수:",홀)

# 홀 = []
# 짝 = []
# N = int(input("수를 입력 : "))
# for i in range(1, N+1):
#     if i % 2 == 0:
#         짝.append(i)
#     else:
#         홀.append(i)

# print("짝수:",sum(짝))
# print("홀수:",sum(홀))



# 수를 입력받고 리스트에 추가하는 프로그램
# li = []
# N = int(input("수를 입력 : "))
# li.append(N)
# print(li)

# 1부터 N까지 리스트에 추가하는 프로그램
# li = []
# N = int(input("수를 입력 : "))
# for i in range(1, N+1):
#     li.append(i)
# print(li)

# 1부터 N까지의 홀수들을 리스트에 추가하는 프로그램
# li = []
# N = int(input("수를 입력 : "))
# for i in range(1, N+1):
#     if i % 2 == 1:
#         li.append(i)
# print(li)

# 수를 입력받고 3의 배수를 판별하는 프로그램
# N = int(input("수를 입력 : "))
# if N % 3 == 0:
#     print("3의 배수입니다.")
# else:
#     print("3의 배수가 아닙니다.")

# 3의배수를 구하는 프로그램
# N = int(input("수를 입력 : "))
# for i in range(1, N+1):
#     if i % 3 ==0:
#         print("3의배수:",i)

# N일뒤 당번 구하는 프로그램
# i = int(input("며칠 뒤 당번을 찾으시나요 : "))
# if i % 4 == 1:
#     print("A가 당번입니다.")
# elif i % 4 == 2:
#     print("B가 당번입니다.")
# elif i % 4 == 3:
#     print("C가 당번입니다.")
# else:
#     print("D가 당번입니다.")

# 오늘부터 N일까지 당번을 출력하는 프로그램
# N = int(input("며칠동안에 당번표를 출력해드릴까요 : "))
# for i in range(0, N+1):
#     if i % 4 == 0:
#         if i == 0:
#             i = "오늘"
#         print(i,"일 뒤 A 가 당번")
#     elif i % 4 == 1:
#         print(i,"일 뒤 B가 당번")    
#     elif i % 4 == 2:
#         print(i,"일 뒤 C가 당번")
#     else:
#         print(i,"일 뒤 D가 당번")

# 윤년을 구하는 프로그램
# N = int(input("년도를 입력하세요 : "))

# if N % 400 == 0:
#     print("윤년입니다.")
# elif N % 100 == 0:
#     print("윤년이 아닙니다.")
# elif N % 4 == 0:
#     print("윤년입니다.")
# else:
#     print("윤년이 아닙니다.")

# N을 입력받고 해당년도가 윤년인지 판단하는 프로그램
# N = [int(input("년도를 입력하세요 : "))]
# for i in N:
#     if i % 400 == 0:
#         print(i, "년은 윤년입니다.")
#     elif i % 100 == 0:
#         continue
#     elif i % 4 == 0:
#         print(i, "년은 윤년입니다.")
#     else:
#         continue

# 1~N년 중 윤년인 년도를 출력하는 프로그램
# N = int(input("년도를 입력하세요 : "))
# for i in range(1, N+1):
#     if i % 400 == 0:
#         print(i, "년은 윤년입니다.")
#     elif i % 100 == 0:
#         continue
#     elif i % 4 == 0:
#         print(i, "년은 윤년입니다.")
#     else:
#         continue





# 수를 입력받고 짝수,홀수를 판별하는 프로그램
# N = int(input("수를 입력 : "))
# if N % 2 == 0:
#     print("짝수 입니다.")
# else:
#     print("홀수 입니다.")

# 4개의 수를 입력받고, 짝수, 홀수를 판별하는 프로그램(1)
# for i in range(4):
#     N = int(input("수 입력 : "))
#     if N % 2 == 0:
#         print(N, "는 짝수")
#     else:
#         print(N, "는 홀수")

# 4개의 수를 입력받고, 짝수, 홀수를 판별하는 프로그램(2)
# li = []
# for i in range(4):
#     N = int(input("수 입력 : "))
#     li.append(N)
# for j in li:
#     if j % 2 == 0:
#         print(j, "는 짝수")
#     else:
#         print(j, "는 홀수")


# 받아올림 발생을 판별하는 프로그램
# A = int(input("수를 입력 : "))
# B = int(input("수를 입력 : "))
# A_1 = A % 10
# B_1 = B % 10
# if A_1 + B_1 >= 10:
#     print("받아올림이 발생합니다.")
# else:
#     print("받아올림이 발생하지 않습니다.")

# 5개의 두수(A,B)를 입력받고, 받아올림 발생을 판별하는 프로그램
# for i in range(5):
#     A = int(input("수를 입력 : "))
#     B = int(input("수를 입력 : "))
#     A_1 = A % 10
#     B_1 = B % 10
#     if A_1 + B_1 >= 10:
#         print("받아올림 발생")
#     else:
#         print("받아올림 발생하지 않음")

# 5개의 점수를 입력받고 평균을 구하는 프로그램
# sco = []
# for i in range(5):
#     n = int(input("점수를 입력 : "))
#     sco.append(n)
#     avg = sum(sco) / 5
# print(avg)

# 5개의 점수를 입력받고 평균보다 낮은 수들을 구하는 프로그램
# sco = []
# for i in range(5):
#     n = int(input("점수를 입력 : "))
#     sco.append(n)
#     avg = sum(sco) / 5    
# print(len(sco),"과목의 평균은", round(avg,2))
# for j in sco:
#     if j < avg:
#         print(j, "는 평균이하")

# 12
# 123456789101112

# j = []
# k = []
# a = []
# b = []
# c = []
# d = []

# N = int(input("수를 입력 : "))

# for i in range(1,N+1):
#     j.append(i)
# for k in j:
#     if k >= 10:
#         a.append(k)
#     if k >= 100:
#         b.append(k)
#     if k >= 1000:
#         c.append(k)
#     if k >= 10000:
#         d.append(k)
# m = len(a)
# q = len(b)
# l = len(c)
# z = len(d)
# print(len(j)+m+q+l+z)

# N = int(input("수를 입력 : "))
# st = ''
# for i in range(1, N + 1):
#     st += str(i) 
# print(st,len(st))

# N = int(input("수를 입력 : "))
# N2 = int(input("수를 입력 : "))
# if N > N2:
#     for i in range(1, N2+1):
#         if N % i == 0 and N2 % i ==0:
#             # print(N,N2,"공통약수: ",i)
#             x = i
            
# else:
#     for i in range(1, N+1):
#         if N % i ==0 and N2 % i ==0:
#             # print(N,N2,"공통약수: ",i)
#             x = i

# N = int(input("수를 입력 : "))
# su = 0

# for i in range(1, N+1):
#     if N % i == 0:
#         su +=1
# if su == 2:
#     print('소수')
# N = int(input("수를 입력 : "))

# li = []
# for i in range(1, N+1):
#     if N % i == 0:
#         li.append(i)
# if li == [1, N]:
#     print("소수")
# if sum(li) == N+1:
#     print("소수")
# if len(li) == 2:
#     print('소수')

# li2 = []
# N = int(input("수를 입력 : "))
# for i in range(2,N):
#     if N % i == 0:
#         li2.append(i)
# if li2 == []:
#     print("소수")

# li = []
# A = int(input("수를 입력 : "))
# for i in range(1, A):
#     if A % i == 0:
#         li.append(i)
#         if sum(li) == A:
#             print(li)
# print(A,'완전수입니다.')

# li = []
# A = int(input("수를 입력 : "))
# for i in range(1, A +1):
#     if A % i == 0:
#         li.append(i)
# if sum(li)-A == A:
#     print(A,'완전수입니다.')

# N = int(input("수를 입력 : "))
# 약수 = []
# for i in range(1,N):
#     if N % i == 0:
#         약수.append(i)
# if  약수 == N:
#     print(약수,"소수")

# for i in [1, 2, 3, 4, 5]: #외반복문
#     for j in [1, 2, 3, 4, 5]: #내반복문 

# N = int(input("수를 입력 : "))
# for i in range(1,10):
#     print(i,'x',N,'=',N * i)


# 적게반복 : 외반복문
# 많게반복 : 내반복문

# for i in range(0, 10):
#     for j in range(2,10):
#         if i == 0:
#             print(j,'단 출력', end='\t')
#         else:
#             print(j,'x',i,'=',j * i ,end='\t')
#     print()

# N = int(input("수를 입력 : "))
# for i in range(1, N+1):
#     su = 0
#     for j in range(1, i+1):
#         if j % 2 == 0:
#             su += 1
#     print(i,"이하의 짝수의 개수는",su)

# 확장
# a:범위 b : 점검
# a b
# 1 1
# 2 12
# 3 123


# N = int(input("수를 입력 : "))
# su = 0
# for i in range(1, N+1):
#     if i % 2 == 0:
#         su += 1
#     print(i,"이하의 짝수의 개수는",su)

# N = int(input("수를 입력 : "))
# for i in range(1, N+1):
#     su = 0
#     for j in range(1, i+1):
#         if j % 2 == 0:
#             su += 1
#     print(i,"이하의 짝수의 개수는",su)

# N = int(input("수를 입력 : "))
# N2 = int(input("수를 입력 : "))
# if N > N2:
#     for i in range(1,N2+1):
#         if N % i == 0 and N2 % i ==0:
#             print(i)
# else:
#     for i in range(1,N+1):
#         if N % i == 0 and N2 % i ==0:
#             print(i)

# A = int(input("수를 입력 : "))
# B = int(input("수를 입력 : "))

# li1 = []
# for i in range(1,A+1):
#     if A % i == 0:
#         li1.append(i)

# li2 = []
# for i in range(1, B+1):
#     if B % i == 0:
#         li2.append(i)
# print(set(li1)&set(li2))
# li = []
# N = int(input("수를 입력 : "))
# for i in range(1, N+1):
#     if N % i == 0:
#         li.append(i)
# if len(li) > 2:
#     print("소수아님")
# else:
#     print("소수")

# li = []
# N = int(input("수를 입력 : "))
# for i in range(1,N+1):
#     if N % i == 0:
#         li.append(i)
# if sum(li)-N == N:
#     print('완전수입니다.')
# a b
# 1 1
# 2 12 1개
# 3 123 1개
# 4 1234 2개
# 5 12345 2개 

# su = 0
# N = int(input("수를 입력 : "))
# for i in range(1,N+1):
#     for j in range(1, i+1):
#         if j % 2 ==0:
#             su += 1
# print(su)

# li = []
# N = int(input("수를 입력 : "))
# for i in range(1, N):
#     if N % i == 0:
#         li.append(i)
# if sum(li) == N:
#     print("완전수입니다.")
# else:
#     print("완전수가 아닙니다.")

# N을 입력받고 N이하의 짝수의 개수 구하기


# su = 0
# N = int(input("수를 입력 : "))
# for i in range(1, N+1):
#     if N % i ==0:
#         su +=1
# print('짝수는',su,'개 입니다.')

# i j
# 1 1
# 2 12 1개
# 3 123 1개
# 4 1234 2개
# A 대상  (덜바뀜)  외반복문  range(1, N+1)
# B 점검범위 (많이바뀜)  내반복문 range(1, 대상 +1)


# N = int(input('수를 입력 : '))

# for i in range(1,N+1):
#     su = 0
#     for j in range(1, i+1):
#         if j % 2 ==0: 
#             su += 1
#     print(i,'이하의 짝수는',su,'개 입니다.')

# 기획 
# 3 ~ N 까지 각각의 약수를 구하기 
# 3 ~ N 까지 for range(3,N+1)
# 각각의 약수 3~N값 을 1~N 숫자로 나눠서 나눠떨어지는 수

# N = int(input("수를 입력 : "))
# for i in range(3, N+1):
#     li = []
#     for j in range(1,i+1):
#         if i % j == 0:
#             li.append(j)
#     print(i,li)

# 확장
# N값을 입력 
# N값의 약수를 구하기 
# 입력 5 -> [1,5]

# 3~N값 출력 적용
# 입력 5 -> 3 13
#          4 124
#          5 125
# N = int(input("수를 입력 : "))

# for k in range(3,N+1):
#     li = []
#     for i in range(1,k+1):
#         if k % i == 0:
#             li.append(i)
#     print(k,li)

# 기획
# 1부터 N 입력
# 1부터 N값의 약수 구함 (1,N+1)
# a범위 b 점검 range(1,대상+1)
# 1    1
# 2    12
# 3    123 
# 약수를 더한 리스트
# 약수중 i값을 제외하고 더한값이 i값이면 완전수라고 출력

# N = int(input("수를 입력 : "))
# for i in range(1,N+1):
#     li = []
#     for j in range(1,i+1):
#         if i % j == 0:
#             li.append(j)
#     if sum(li)-i == i:
#         print(i,"완전수")



# 3~n 까지 입력  범위 range(3,N+1)
# 3 123
# 4 1234 
# 5 12345
# 점검  range(1,대상+1)
# 3~N 까지 소수 출력
#  10 입력시 
#  [3, 5, 7, 9]
# N = int(input("수 입력 : "))
# for i in range(3,N+1):
#     li = []
#     for j in range(1,i+1):
#         if i % j == 0:
#             li.append(j)
#     if len(li) ==2:
#         print(i,'소수입니다.')



# 1부터 N값  range(1,N+1)
# 1부터 N값에 점검 range(1,대상+1)
# 곱해져야하는 su변수 생성
# 범위가 바뀔때마다 su변수 초기화 (외반복문에추가)
# 5입력시 나와야하는 출력
# 범위(외) 점검 (내) 
# 1 =    1
# 2 =    1 x2
# 3 =    1x2x3
# 4 =    1x2x3x4
# 5 =    1x2x3x4x5
# N = int(input("수 입력 : "))

# for k in range(1,N+1):
#     su = 1
#     for i in range(1,k+1):
#         su *= i
#     print(k,su)

# 코드를 한국말로 표현하는연습
# for i in range(1,6):
#     for j in range(1,5):
#         print(i, j)
#         if j == 3:
#             break
#     print('A')

# break: 자신에게 제일 가까운 루프만 빠져나간다. 

# for i in ['a','b','c','d','e']:
#     if i == 'a':
#         continue
#     if i == 'd':
#         break
#     print(i)

# for i in range(1,6):
#     if i == 2:
#         pass
#     print(i)

# for i in range(1,11):
#     print(i)

# print('='* 20)

# i = 1
# while i < 11:
#     print(i)
#     i += 1
#  0입력시까지 숫자들의 평균이상인 수 출력
# 100 100 100 50 -> 100 100 100 출력
# li = []
# while True:
#     a = int(input("종료는 0 을 누르세요 : "))
#     li.append(a)
#     if a == 0:
#         print("Program EXIT!!")
#         del(li[-1])
#         break
# avg = (sum(li)/len(li))
# for i in li:
#     if i >= avg:
#         print(i)


# 자판기 코드 
# import os
# import time
# 남은금액 = 0
# 콜라 = 300
# 사이다 = 300
# 커피 = 200
# while True:
#     print("1.콜라 / 300")
#     print("2.사이다 / 300")
#     print("3.커피 / 200")
#     print("4.돈 넣기")
#     print("5.잔돈 반환")
#     print("6.종료")
#     print('='*20)
#     print("현재금액",남은금액)
#     user = int(input("메뉴 선택 : "))
#     if user == 1:
#         os.system("cls")
#         if 남은금액 < 콜라:
#             print("'금액이 부족합니다.'")
#             break
#         print("콜라 맛있게 드세요!")
#         남은금액 -= 콜라
#         time.sleep(1)
#         os.system("cls")
#     elif user == 2:
#         os.system("cls")
#         if 남은금액 < 사이다:
#             print("'금액이 부족합니다.'")
#             break
#         print("사이다 맛있게 드세요!")
#         남은금액 -= 사이다
#         time.sleep(1)
#         os.system("cls")
#     elif user == 3:
#         os.system("cls")
#         if 남은금액 < 커피:
#             print("'금액이 부족합니다.'")
#             break
#         print("커피 맛있게 드세요!")
#         남은금액 -= 커피
#         time.sleep(1)
#         os.system("cls")
#     elif user == 4:
#         os.system("cls")
#         돈 = int(input("돈을 넣어주세요 : "))
#         남은금액 += 돈
#         os.system("cls")
#     elif user == 5:
#         os.system("cls")
#         print("잔돈이 반환됩니다.")
#         time.sleep(1)
#         os.system("cls")
#         남은금액 = 0
#     elif user == 6:
#         os.system("cls")
#         print("종료됩니다.")
#         time.sleep(1)
#         os.system("cls")
#         break

# for i in range(10):
#     print(i)
#     if i == 2:
#         break

# for i in ['a','b','c','d','e','f']:
#     print(i)
#     if i == 'd':
#         break 

# for i in range(2,10):
#     for j in range(1, 10):
#         print(i,j,i*j)


# i = 1
# while i < 10:
#     print(f"{N} x {i} = {i * N}")
#     i += 1

# while True:
#     user = int(input("입력(종료0)"))
#     if user == 0:
#         print("Program EXIT!!")
#         break
# total = []
# while True:
#     N = int(input("수 입력 : "))
#     if N == 0:
#         print("종료됩니다.")
#         break
#     total.append(N)


# print(round(sum(total)/len(total),2))

# while True:
#     user = int(input("입력(종료는0):"))
#     if user == 0:
#         print("프로그램이 종료됩니다.")
#         break
# li = []
# while True:
#     N = int(input("입력 : "))
#     if N == 0:
#         avg =sum(li)/ len(li)
#         for i in li:
#             if i > avg:
#                 print(i,'는 평균이상입니다.')
#         print("프로그램 종료")
#         break
#     li.append(N)
# li = []
# while True:
#     N = int(input("수를 입력 : "))
#     if N == 0:
#         break

#     li.append(N)
# print("가장 큰 값 :",max(li),"가장 작은 값 :",min(li),"\n프로그램이 종료 됩니다.")
# import os
# import time
# 금액 = 0
# 콜라 = 300
# 사이다 = 300
# 커피 = 200
# while True:
#     print("1. 콜라 / 300")
#     print("2. 사이다 / 300")
#     print("3. 커피 / 200")
#     print("4. 돈 넣기")
#     print("5. 잔돈 반환")
#     print("6. 종료")
#     print("현재금액 : ", 금액)
#     메뉴 = int(input("메뉴 선택: "))
#     os.system("cls")
#     if 메뉴 == 1:
#         print("콜라 맛있게드세요!")
#         time.sleep(1)
#         금액 -= 콜라
#         os.system("cls")
#     if 메뉴 == 2:
#         print("사이다 맛있게드세요!")
#         time.sleep(1)
#         금액 -= 사이다
#         os.system("cls")
#     if 메뉴 == 3:
#         print("커피 맛있게드세요!")
#         time.sleep(1)
#         금액 -= 커피
#         os.system("cls")
#     if 메뉴 == 4:
#         돈 = int(input("돈을 넣어주세요: "))
#         금액 += 돈
#         os.system("cls")
#     if 메뉴 == 5:
#         print("잔돈이 반환됩니다.")
#         time.sleep(1)
#         금액 = 0
#         os.system("cls")
#     if 메뉴 == 6:
#         print("종료됩니다.")
#         time.sleep(1)
#         os.system("cls")
#         break
# while True:
#     try:
#         N1,N2 = input().split()
#         N1 = int(N1)
#         N2 = int(N2)
#     except:
#         break

# # 26 
# # 2 + 6 = 8 -> 68 
# # 6 + 8 = 14 -> 84
# # 8 + 4 = 12 -> 42
# # 4 + 2 = 6 -> 26
# 55
# 5 + 5 = 10






# while True:
#     try:
#         N = int(input()) # 26
#         li = []
#         li.append(N)
#         for i in li:
#             N1 = i // 10 # 2
#             N2 = i % 10  # 6
#             N3 = N1 + N2  # 8
#             if N3 >= 10:
#                 N3 %= 10
#             N4 = (N2*10) + N3 # 68
#             li.append(N4)
#             if li[-1] == N:
#                 break
#         print(len(li)-1)
#     except:
#         break



# import os
# import time

# money = 0

# while True:
    
#     # 메뉴출력
#     print("="*20)
#     print("1. 김치찌개 / 300")
#     print("2. 돈 입력")
#     print("3. 반환")
#     print("4. 종료")
#     print("="*20)
#     print(f"현재금액 {money}")

#     # 선택받고
#     user = int(input("메뉴 선택 : "))


#     # 처리
#     if user == 1:
#         if money < 300:
#             print("금액이 부족합니다.")
#         else:
#             print("김치찌개는 역시 돼지고기김치찌개지~~")
#             money -= 300
#     elif user == 2:
#         m = int(input("돈을 넣어주세요 : "))
#         money += m
#     elif user == 3:
#         print(f"{money} 원이 반환됩니다.")
#         money = 0   
#     elif user == 4:
#         print("Program EXIT!!!")
#         break
#     else:
#         print("입력이 바르지 않음 :(")
    
#     time.sleep(0.8)
#     os.system("cls")

# import os
# import time
# import random
# life = 5
# score = 0
# while True:
#     if life == 0:
#             print(f"GAME OVER\n점수는: {score}")
#             break
#     print('=' * 20)
#     print(f"점수 {score}")
#     print(f"남은 목숨 {life}")
#     print('=' * 20)
#     a= random.randint(1,100)
#     N = int(input("홀(1), 짝(0) 입력 : "))
    
#     if a % 2 == N :
#         score += 100
#         print("맞았습니다.",f"값은 {a}")
#     elif a % 2 == N :
#         score += 100
#         print("맞았습니다.",f"값은 {a}")
        
#     else:
#         life -= 1
#         print("틀렸습니다.",f"값은 {a} 였습니다.")
    
#     time.sleep(0.8)
#     os.system("cls")

# import random
# import os
# import time


# total = 0
# print('=' * 20)
# print("Up! Down!\nGAME!")
# print('=' * 20)
# time.sleep(0.8)
# os.system("cls")
# print('=' * 20)
# print("START!")
# print('=' * 20)
# time.sleep(0.8)
# os.system("cls")
# while True:
#     total = 0
#     while True:
#         print('=' * 20)
#         print("1. Easy (1,9)")
#         print("2. Easy (10,99)")
#         print("3. Easy (100,999)")
#         print('=' * 20)
#         level = int(input("난이도 설정 : "))

#         if level == 1:
#             N= random.randint(1,9)
#         elif level == 2:
#             N = random.randint(10,99)
#         elif level == 3:
#             N = random.randint(100,999)
#         else:
#             print("잘못 입력!")
#             continue
#         break
#     os.system("cls")
#     while True:
#         print(f"{total}번 시도!")
#         user = int(input("수를 입력 : "))
#         total += 1
#         if N > user:
#             print("Up!!!")
#             time.sleep(0.8)
#             os.system("cls")
            
#         elif N == user:
#             os.system("cls")
#             print("정답!")
#             print(f"{total}번 만에 맞췄습니다!")
#             break
#         else:
#             print("Down!!!")
#             time.sleep(0.8)
#             os.system("cls")
#     again = int(input("계속 하시겠습니까? yes(1) no(0) : "))
#     time.sleep(0.8)
#     os.system("cls")
#     if again == 0:
#         print("게임을 종료합니다.")
#         break




# import random
# import os
# import time

# print("1. easy 한자리수끼리")
# print("2. normal 두자리수끼리")
# print("3. hard 세자리수끼리")
# level = int(input("레벨을 정하세요 : "))
# os.system("cls")
# while True:   
#     if level == 1:
#         r1 = 1
#         r2 = 9
#     elif level == 2:
#         r1 = 10
#         r2 = 99
#     elif level == 3:
#         r1 = 100
#         r2 = 999
#     else: 
#         print("레벨 설정 오류!!")
#         continue
#     break

# life = 5
# score = 0

# while True:
#     if life == 0:
#         print(f"GAME OVER\n점수는 {score}")
#         break
#     A = random.randint(r1, r2)
#     B = random.randint(r1, r2)
#     op = random.randint(1, 2) 
#     s200 = random.randint(1, 5)
#     life2 = random.randint(1, 7) 
#     print('=' * 20)
#     print(f"점수 {score}\n남은 목숨 {'♥' * life+'♡'*(5-life)}")
#     print('=' * 20)
    
#     if s200 == 1:
#         print("이번문제 score + 200")
#         점수 = 200
#     else:
#         점수 = 100
#     if life2 == 1:
#         print("이번문제는 라이프 2개짜리입니다")
#         라이프 = 2
#     else: 
#         라이프 = 1
#         print("이번문제는 라이프 1개짜리 문제입니다")
    
    


#     if op == 1:
        
#         user = int(input(f"{A} + {B} = "))
#         정답 = A + B
#     elif op == 2:
#         if A > B:
#             user = int(input(f"{A} - {B} = "))

#             정답 = A - B
#         else:
#             user = int(input(f"{B} - {A} = "))

#             정답 = B - A

#     if user == 정답:

#         print("맞았습니다.")
#         score += 점수
#         time.sleep(0.5)
#         os.system("cls")
#     else:
#         print("틀렸습니다.")
#         life -= 라이프
#         time.sleep(0.5)
#         os.system("cls")


import random
import os 
import time

while True:
    print("="*30)
    print("1. EASY (1-9)")
    print("2. NORM (10-99)")
    print("3. HARD (100-999)")
    print("="*30)
    level = int(input("난이도 선택 : "))

    if level == 1:
        r1 = 1
        r2 = 9
    elif level == 2:
        r1 = 10
        r2 = 99
    elif level == 3:
        r1 = 100
        r2 = 999
    else:
        print("레벨 설정 오류!! :( ")
        continue
    break

life = 5
score = 0

while True:

    if life <= 0:
        print("GAME OVER!")
        print(f"Your score is {score} :)")
        break 

    A = random.randint(r1,r2)
    B = random.randint(r1,r2)
    op = random.randint(1,2) # 1 나왔을 때 더하기, 2 빼기
    s200 = random.randint(1,5) # 1 나왔을 때
    l2 = random.randint(1,7)

    print("="*20)
    print(f"Your Life {'♥ ' * life + '♡ '*(5-life)}")
    print(f"Your Score {score}")
    print("="*20)

    if s200 == 1:
        print("이번문제 score + 200")
        점수 = 200
    else:
        점수 = 100

    if l2 == 1:
        print("이번문제 life - 2")
        라이프 = 2
    else:
        라이프 = 1




    if op == 1:
        user = int(input(f"{A} + {B} = "))
        정답 = A + B
    elif op == 2:
        if A > B:
            user = int(input(f"{A} - {B} = "))
            정답 = A - B
        else:
            user = int(input(f"{B} - {A} = "))
            정답 = B - A
    

    if user == 정답:
        score += 점수
        print("맞았습니다 :) ")
    else:
        life -= 라이프
        print("틀렸습니다 :( ")
    
    time.sleep(0.6)
    os.system("cls")
