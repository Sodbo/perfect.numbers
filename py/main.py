import time
import math

N = 1000000
# Runtime 70.23607802391052
start = time.time()
for num in range(2,N+1):
	a = 1
	for num2 in range(2,round(math.sqrt(num))+1):
		if num % num2 == 0:
			a = a+num2+num//num2
	if(a==num):
		print('Perfect number ',num)

stop = time.time()

print(stop-start)