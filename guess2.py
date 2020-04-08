from open2 import *
import time

def guess2():
	print('''游戏规则：
系统会随机生成4位整数，由你猜
每次猜完都会给出相应提示
直至正确猜出，给出猜测所用的时间
提示解读：
A为正确的数字和正确位数
B为数字正确但是位置错误
没有提示则为全部都错误
（由于实现逻辑较为复杂，极大几率会存在BUG(\逻辑)，请谅解，我也会在后续进行完善）''')
	scores=[]
	cycle_count=0
	next_cyle=True
	while (next_cyle):
		begin_time=time.time()
		cycle_count +=1
		#玩一轮
		answer=generate_answer()
		win=False
		guess_count=0
		while(not win):
			try:	
				guess=make_guess() #交卷
				result=check_guess(answer,guess) #批改
				guess_count=guess_count+1
				win=process_result(guess_count,guess,result) #处理结果
				if(win):
					end_time=time.time()
					user_time=round(end_time-begin_time,2)
					scores.append((cycle_count,guess_count,user_time))
			except ValueError:
				print('输入错误，请输入四位整数')
			except IndexError:
				print('输入位数错误，请输入四位整数')
		show_scores(scores)

		#要不要继续
		next_cyle=should_continue()