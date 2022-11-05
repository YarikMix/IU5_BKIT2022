import random

from config import ADMIN_ID
from .db import write_data, load_data


def generateBalance():
	balance = random.randint(0, 10000)
	data = {
		"user_id": ADMIN_ID,
		"balance": balance
	}

	write_data(data)


def getBalance():
	data = load_data()
	return data["balance"]


def changeBalance(newBalance):
	data = load_data()
	data["balance"] = newBalance
	write_data(data)