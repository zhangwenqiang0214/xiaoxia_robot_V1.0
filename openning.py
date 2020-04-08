from datetime import datetime
import requests
import json



def show_robot():
	print('''
      \_/
     (* *)
    __)#(__
   ( )...( )(_)
   || |_| ||//
>==() | | ()/
    _(___)_
   [-]   [-]''')
	print('------------------------')
	print('''欢迎使用小夏机器人V1.0版本''')
	print('------------------------')




def hello(name):
	print(f"你好{name}，我是'小夏'，很高兴认识你啊!")


def ask():
	name=input('我是小夏，我该怎么称呼你？\n')
	age=int(input('你多大了？\n'))

	if (age<=12):
		print('小孩子，要好好学习啊!')
	elif age<=18:
		print('这个年龄会遇到你一生中最难忘的人，要好好珍惜啊！')
	elif age<=30:
		print('买房了吗朋友？')
	elif age<=45:
		print('我喜欢成熟的人')
	else:
		print('你一定很幸福吧')
	return name


def show_time():
		dt=datetime.now()#调取一个现在是时间
		print(f'今天是{dt.year}年{dt.month}月{dt.day}日 现在是{dt.hour}：{dt.minute}：{dt.second}')

def ai_talk(question):
	return question.replace('你','我').replace('不','').replace('吗','').replace('？','！').replace('?','！')

def tianqi():	
	url = 'http://t.weather.sojson.com/api/weather/city/'
	city = input("请输入你要查询的城市：")
	f = open('city.json', 'rb')
	cities = json.load(f)

	city = cities.get(city)

	response = requests.get(url + city)
	d = response.json()

	if(d['status'] == 200):
	    print("城市：", d["cityInfo"]["parent"], d["cityInfo"]["city"])
	    print("时间：", d["time"], d["data"]["forecast"][0]["week"])
	    print("温度：", d["data"]["forecast"][0]["high"], d["data"]["forecast"][0]["low"])
	    print("天气：", d["data"]["forecast"][0]["type"])

def help():
	print('-------------------------')
	print('''您可以输入：
	几点了？------用来查询当前时间
	你好----------可以向你问好
	天气----------查询指定城市天气
	猜数字--------进入小游戏猜数字
	高级猜数字-----进入小游戏高级猜数字
	关于作者-------可了解Banxia
	88------------退出小夏
	帮助----------查看帮助''')
	print('-------------------------')