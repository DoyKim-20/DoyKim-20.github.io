print('우리 4번째 과제를 시작해봐요!')

int1=int(input('첫 번째 수를 입력하세요: '))
int2=int(input('두 번째 수를 입력하세요: '))
int3=int(input('세 번째 수를 입력하세요: '))

if int1 < int2 :
	if int1 < int3:
		print('가장 작은 수는 ',int1,'입니다!')
elif int2 < int3:
    print('가장 작은 수는 ',int2,'입니다!')
else :
    print('가장 작은 수는 ',int3,'입니다!')
    
#60192164 김도영