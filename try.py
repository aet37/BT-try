from time import sleep
for i in range(10):
	sleep(0.5)
	if i == 0:
		print("i = 0", end="")
	else:
		print("\r", end="")
		print("i = " + str(i), end="")