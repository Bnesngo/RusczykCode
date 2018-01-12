import random

def getRandomInt(a, b):
    return random.randint(a, b)

def getRandomDecimal(a, b):
	if(a < b):
		return random.random() * (b - a) + a;
	else:
		return random.random() * (a - b) + b;