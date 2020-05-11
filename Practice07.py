i = 0

while True:
    num=int(input('숫자를 입력해주세요:'))
    if num == 0:
        break
    if num%2==0:
        i+=1
print('짝수의 개수는: ',i,'개')

#0에서 멈추라고 break쓰고 밑에서 카운트하기
#60192164 김도영