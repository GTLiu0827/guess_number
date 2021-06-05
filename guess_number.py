#猜數字遊戲
#產生一個隨機整數
#使用者輸入數字去猜
#猜對 ==> 印出 "終於猜對了!"
#猜錯 ==> 顯示 比答案大或小

import random

max_num = input ('請輸入最大值:')
min_num = input ('請輸入最小值:')
print ('猜測範圍',min_num,'~',max_num,)

r = random.randint(int(min_num), int(max_num))

count = 0  

while True:
	count += 1 ## count ++
	n = input('請輸入猜測的數字')
	if int(n) == r:
		print ('終於猜對了!')
		print ('第',count,'次猜測')
		break
	elif int(n) > r:
		print (n,'比答案大')
	else :
		print (n,'比答案小')
	print ('第',count,'次猜測')