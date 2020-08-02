from random import randint

x = randint(0, 19)
y = int(input("input: "))
while  x != y:
	if y < x:
		print("go higher")
		y = int(input())
	if y > x:
		print("go lower")
		y = int(input())
	if y == x:
		print("ya got it")


