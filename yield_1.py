def gen_nums():
	n = 0
	while n < 20:
		yield n
		n += 1

for num in gen_nums():
	print(num)
