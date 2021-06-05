#猜數字遊戲
#產生一個隨機整數
#使用者輸入數字去猜
#猜對 ==> 印出 "終於猜對了!"
#猜錯 ==> 顯示 比答案大或小

import random

r = random.randint(1, 100)

while True:
	n = input('請輸入1~100中的數字')
	if int(n) == r:
		print ('終於猜對了!')
		break
	elif int(n) > r:
		print (n,'比答案大')
	else :
		print (n,'比答案小')
