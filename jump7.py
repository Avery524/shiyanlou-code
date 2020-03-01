for a in range (1,101):
	if a%7 ==0 or a//10==7 or a%10==7 :
		continue
	print(a)
        #a%7 ==0 7的倍数
        #a//10==7 十位数是7
        #a%10==7 个位数是7
