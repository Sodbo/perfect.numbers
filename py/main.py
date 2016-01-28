# Now I'm gonna improve performance
import multiprocessing as mp
import time
import math
import string
import Queue

N=2000000
# Runtime 8 seconds

start = time.time()

def checkPerfectNumber(numlow,numup):
	result = []
	for num in range(numlow,numup+1):
		a = 1
		for num2 in range(2,int(round(math.sqrt(num)))+1):
			if num % num2 == 0:
				a = a+num2+num//num2
		if(a==num):
			result = result + [num]
	return result

pool = mp.Pool(processes=4)
results = [pool.apply_async(checkPerfectNumber, args=(x*1000+1,x*1000+1000)) for x in range(0,int(N/1000))]
output = [p.get() for p in results]
print(output)

stop = time.time()
print(stop-start)
