import time

def input_limit():
	try:
		limit=int(input('请输入要猜的次数：\n'))#最大猜测次数
	except:
		limit=int(input('请重新输入:\n'))
	return limit

def calc_time(begin_time):
	eng_time=time.time()
	user_time=round((eng_time-begin_time),2)#每轮所用的时间
	print(f'你一共用时{user_time}秒')
	return user_time
	
def print_score(scores):
	best_score=min(scores,key=lambda X:X[2] if X[1] else 9999)
	print('==========战绩============')
	for _cycle,_is_right,_user_time in scores:
		label='胜利' if(_is_right) else '失败'
		best_label='最棒的' if(_cycle == best_score[0] and best_score[1]) else ''
		print(f'第{_cycle}轮，用时{_user_time}秒，{label},{best_label}')
	print('==========结尾============')