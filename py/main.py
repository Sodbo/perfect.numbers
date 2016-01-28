# Now I'm gonna improve performance
import time
import math

N = 2000000
# Runtime 120 HZM ubuntu
# Run time 223.300662994 sec laptop

start = time.time()
for num in range(2,N+1):
	a = 1
	for num2 in range(2,int(round(math.sqrt(num))+1)):
		if num % num2 == 0:
			a = a+num2+num//num2
	if(a==num):
		print('Perfect number ',num)

stop = time.time()

print(stop-start)