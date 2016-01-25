# Now I'm gonna improve performance
import time
import math

N = 200000

start = time.time()
for num in range(1,N+1):
	a = 1
	for num2 in range(2,round(math.sqrt(num))+1):
		if num % num2 == 0:
			a = a+num2+num//num2
	if(a==num):
		print('Perfect number ',num)

stop = time.time()

print(stop-start)