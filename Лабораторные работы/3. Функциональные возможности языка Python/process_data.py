import json
import os
from operator import concat
from unique import Unique
from field import field
from gen_random import gen_random
from cm_timer import cm_timer_1

path = os.path.dirname(__file__) + "\\data_light.json"

def f1(arg):
	return Unique([i['job-name'] for i in field(arg, 'job-name')], ignore_case=True)

def f2(arg):
	return filter(lambda a: a.startswith('программист'), arg)

def f3(arg):
	return list(map(lambda x: concat(x, ' c опытом Python'), arg))

def f4(arg):
	return zip(arg, gen_random(len(arg), 137287, 200000))

def main():
	with open(path, encoding='utf-8') as f:
		data = json.loads(f.read())
		for i in f4(f3(f2(f1(data)))):
			print(i)    

if __name__ == '__main__':
	with cm_timer_1():
		main()