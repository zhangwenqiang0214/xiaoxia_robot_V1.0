
import random

def generate_answer():
	return random.randint(1000,9999)
	#return 9527
def make_guess():
	return input('请输入你猜测的4位整数：')

def check_guess(answer,guess):
	guess= int(guess)
	a_num= check_guess_A(answer,guess)
	b_num= check_guess_B(answer,guess)
	result=f'{a_num}A{b_num}B'
	return result



def check_guess_A(answer,guess):
	count=0
	answer_str=str(answer)
	guess_str=str(guess)
	for index,chre in enumerate(answer_str):
		if (guess_str[index]==chre):
			count=count+1
	return count

def check_guess_B(answer,guess):
	count=0
	answer_str=str(answer)
	guess_str=str(guess)

	a_indexex=[]
	for index,chre in enumerate(answer_str):
		if guess_str[index]==chre:
			a_indexex.append(index)

	for chre in guess_str:
		if chre in guess_str:
			index2=answer_str.index(chre)
			if index2 not in a_indexex:
				count +=1
	return count


def process_result(guess_count,guess,result):#如果赢了返回True，否则返回False
	print(guess_count,guess,result)
	if result =='4A0B':
		print('你猜对了')
		return True
	return False

def show_scores(scores):
	print('=============================')
	print('轮次/轮'.ljust(5),'猜测次数/次'.ljust(8),'用时/秒'.ljust(5))
	for sc in scores:
		cycle=str(sc[0]).ljust(7)
		guess=str(sc[1]).ljust(12)
		user_time=str(sc[2]).ljust(5)
		print(cycle,guess,user_time,)
	print('=============================')


def should_continue():
	com=input('继续输入y，任意字符退出')
	if(com=='y' or com=='Y'):
		return True
	else:
		print('再见')
		return False


if __name__ == '__main__':
	print('testing')
	assert(check_guess_A(9527, 9522)==3)  #断言
	assert(check_guess_A(9527, 9572)==2)  #断言
	assert(check_guess_A(9527, 9527)==4)  #断言
	assert(check_guess_A(9527, 9342)==1)  #断言
	assert(check_guess_A(9527, 7342)==0)  #断言
	assert(check_guess_B(9527, 5923)==2)  #断言
	assert(check_guess_B(9527, 5972)==4)  #断言









