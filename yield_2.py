import random

z = 0

def limit_count():

	limit_x = random.randint(0,50)

	while limit_x > 0:
		
		yield limit_x
		limit_x -= 1

limit_count()

for x in limit_count():
	z += x

print(z)
