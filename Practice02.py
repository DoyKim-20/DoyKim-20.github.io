print("2번 과제 시작!")
year = 19
pin = '990329-1083599'
if pin[7]==3 or pin[7]==4 :
    year = year + 1

print('김멋사군의 탄생일은 ' + str(year) + str(pin[0:2]) + '년 ' + str(pin[2:4]) + '월 ' + str(pin[4:6]) + '일 입니다')    
#60192164 김도영