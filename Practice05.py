print('5번째 과제를 시작해볼까용?')
r=int(input('반지름을 입력하세요: '))

if r <= 0 :
    print('잘못된 입력값입니다.')
else :
    area = 3.141592 * r*r
    if area > 200 :
        print('너무 큰 원의 넓이는 구하기가 힘들어요ㅠㅠ')
    else :
        print('원의 넓이는 ', area,'입니다.') 

        #60192164 김도영