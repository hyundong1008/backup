#int str float list dict tuple 


#a = [1,2,3,4,5]
#b = len(a)
#print (b)

#a = 17 
#if a<10: 
 #    print("a는 10보다 작습니다")
#elif a<20:
#    print("a는 20보다 작습니다")
#if not a == 10:



#b = [1,2,3,4,5]    
#a = 3 
#if a in b:        # 만약 a가 b에 포함되어있으면
#    print("a가 b에 포함되어있습니다")    
    
#for 임시변수 in 리스트:
 #   code     
#wallet = 0
#for hand in b:      # b라는 변수에서 hand라는 변수로 하나씩 빼옴   
#    wallet = hand+wallet            # 기존에있던 wallet 이라는 변수에 hand변수가 더해짐 
#print(wallet)  # b라는 리스트 안에 있는 데이터들을 wallet에 모두 합한 결과를 출력함 

# a = 0 
# while a>3:
    # a = 1+a
    # print("a1")

# a = [1,2,3,4]
# a.index(1)
# print(a.index(1))

# a = [1,2,3,4,5]
# a.insert(0,3)
# print(a.insert(0,3))

# dic = {'name':'hyundong' , 'phone':'010101010'}
# di

# x or y x와 y 중둘에 하나만 참이면 참이다
# x and y x와 y 모두 참이어야 참이다
# not x x가 거짓이면 참이다

# money = 3000
# if money >= 3000:
#     print("타고가라")
# else:
#     print("걸어가라")


# money = 2000 
# watch = 0
# if money >= 3000 or watch:
#     print("택시를 타고 가라 ")
# else:
#     print("걸어가라")

# treehit = 0 
# while treehit < 10 :
#     treehit = treehit+1
#     print("나무를한번 찍었습니다") 

# a = [4,1,3,2]       
# minimum = a[0] # 4 
# for c in a:           # a에서 c로 4,1,3,2 순으로 빼옴
#     if c < minimum:    # 만약 c가 minimum(4) 보다 작을때 
#         minimum = c   # c가 minimum이 됨 
# print(minimum)         # 
# a.remove(minimum)
# print(a)     

# a = [1,2,3,4,5,6,7,8,9,10]    
# wallet = 0                   # 지갑을 0으로 
# for b in a:                  # a라는 리스트에서 값을 하나씩 빼오는데 그값이 b에 담김
#     if b % 2 == 0:           # b에 2를 나눠서 나머지가 0이 되는 값들(짝수)만 걸러냄
#         wallet = b + wallet  # 지갑(0)에 걸러낸 b값들을 하나씩 더함
# print(wallet)         
        
# a = input("숫자를 입력하세요 : ") # 사용자가 입력한 값 (문자열)
# c = 0
# for b in a:
#     c = int(b) + c 
# if int(a) % c == 0:
#     print("하샤드수입니다")    

# print(c)

# a = input("숫자를 입력하세요 :")
# b = input("숫자를 입력하세요 :")
# for


# print(a)
# print(b)
  


# a = input('숫자를 입력하세요 : ')  
# b = input('숫자를 입력하세요 : ')
# wallet = 0  
# for i in a:     input에 입력된 값을 담아둠  
#    for e in b:          
#       print(str(i) + "x" + str(e) +  "=  " + str(int(i) * int(e)))   a input에 입력된 값을 각 자리수로 빼와서 b input에서 빼온 값들을 순서대로 곱하고 곱한 값들을 출력
#       wallet = int(i) * int(e) + wallet                              순차적으로 wallet에 값을 더함  
      
# print(wallet)      

# def 함수명(인풋):
#    코드
#    return 아웃풋

# def plus(a, b):
#    c = a+b
#    return c

# c = plus(4,5)
# print(c) 


# def minus(a,b):  함수 = 기능 예를들어 이 minus라는 함수를 쓰면 빼기를 하는 코드를 사용하지않아도 숫자랑 minus함수만 쓰면 알아서 빼줌
#    c = a-b
#    return c      c 에다가 a-b의 값을 넣어줌 

# c = minus(10,5)  
# print(c)

# requests  / 웹사이트에 정보를 가져오는 역할
# bs4       / 가져온 정보에서 원하는것만 가져옴 
# lxml      / 파싱도구 
