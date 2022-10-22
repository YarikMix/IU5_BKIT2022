import json
import os
from operator import concat
from unique import Unique
from field import field
from gen_random import gen_random
from cm_timer import cm_timer_1

path = os.path.dirname(__file__) + "\\data_light.json"

with open(path, encoding="utf-8") as f:
	data = json.loads(f.read())

def f1(arg):
	return Unique([i["job-name"] for i in field(arg, "job-name")], ignore_case=True)

def f2(arg):
	return filter(lambda a: a.startswith("программист"), arg)

def f3(arg):
	return list(map(lambda x: concat(x, " c опытом Python"), arg))

def f4(arg):
	_zip = zip(arg, gen_random(len(arg), 100000, 200000))
	_str = [f"{a}, зарплата {b} руб." for a,b in _zip]
	return _str

if __name__ == '__main__':
	with cm_timer_1():
		for i in f4(f3(f2(f1(data)))):
			print("'" + i + "'")