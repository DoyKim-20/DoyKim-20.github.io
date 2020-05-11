num=int(input('자릿수를 알고싶은 숫자를 입력해주세요!'))
print(type(num))
a = 0
while num > 1:
    num = num / 10
    a = a + 1
print('num은', a, '자리 수 입니다.')
#60192164 김도영