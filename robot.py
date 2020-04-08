import openning as open
import guess
import guess2

import time

open.show_robot()#显示机器人
print('接下来我会对你稍微有个了解')
time.sleep(2)#程序暂停5秒

name=open.ask()#询问年龄
print('-------------------------')
print('''您可以输入：
几点了？------用来查询当前时间
你好----------可以向你问好
天气----------查询当前天气
猜数字--------进入小游戏猜数字
高级猜数字-----进入小游戏高级猜数字
关于作者-------可了解Banxia
88------------退出小夏
帮助----------查看帮助''')
while (True):

	print(f'你好{name}，请问有什么可以帮您？')
	order=input('')
	print('知道了')
	if order == "几点了？":
		open.show_time()
	elif order=='帮助':
		open.help()
	elif order == "你好":
		open.hello(name) #问好
	elif order=="88":
		print('好的再见')
		break#跳出循环
	elif order=='天气':
		open.tianqi()
	elif order=='彩蛋':
		print('其实我真的是一个价值百万的人工智能机器人')
		user_input=input()
		print(open.ai_talk(user_input))
	elif order=='猜数字':
		guess.guess1()
	elif order=='高级猜数字':
		guess2.guess2()
	elif order=='关于作者':
		print('''我是Banxia
这是我初上手Python的一个小程序
应该在大佬眼里很简陋了
您可以访问：https://banxia.ink了解我更多
期待和您成为朋友''')
	else:
		print('小夏会努力学习这些个问题，请再给我一点时间！')
		#print(open.ai_talk(order))
	print('-----------------------')


