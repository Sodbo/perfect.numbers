# Now I'm gonna improve performance
import multiprocessing as mp
import time
import math

start = time.time()

output = mp.Queue()

def checkPerfectNumber(num, output):
	a = 1
	for num2 in range(2,round(math.sqrt(num))+1):
		if num % num2 == 0:
			a = a+num2+num//num2
	if(a==num):
		output.put(num)

#for i in range(1,N):
#	checkPerfectNumber(i)
	
processes = [mp.Process(target=checkPerfectNumber, args=(10, output)) for x in range(2)]

# Run processes
for p in processes:
	p.start()

# Exit the completed processes
for p in processes:
    p.join()

# Get process results from the output queue
results = [output.get() for p in processes]

stop = time.time()

print(results)

print(stop-start)