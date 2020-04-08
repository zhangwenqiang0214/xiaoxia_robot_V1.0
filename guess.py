import random
import sys
import time
import open

		
	
def guess1():
	print('''游戏规则：
小夏会在1~10的整数中随机选一个数字给你猜
在你每次猜完以后会提示你猜大了或者小了
直到你猜出正确结果
每轮游戏都会记录时间，并且找出最棒的那一轮
注意：游戏开始之前会让你先输入一个猜测的次数
比如你输入3，如果你在3次之内猜不中的话，游戏失败''')
	guess_limit=open.input_limit()
	scores=[]

	cycle=0#第几轮
	while (True):
		cycle=cycle+1
		answer=random.randint(1,10)#调用一个1~10之间的整数	
		
		guess_count=0#已经猜测的次数
		is_right=False

		begin_time=time.time()
		for i in range(guess_limit):
			guess=int(input('请猜一个1~10之间的数字，你猜是那个？\n'))
			if guess==answer:
				is_right=True
				break;
			elif guess>answer:
				print('太大了',end=',')
			else:
				print('太小了',end=',')
			if i<guess_limit-1:
				print('继续猜')
		if (is_right):
			print('猜对了，恭喜你')
		else:
			print('猜错了，你没有机会了')
		user_time=open.calc_time(begin_time)

		scores.append((cycle,is_right,user_time))
		open.print_score(scores)

		exit=input('输入q退出，任意字符继续游戏')
		if exit=="q":
			print('再见')
			break






	 