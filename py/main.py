# Now I'm gonna improve performance
import multiprocessing as mp
import time
import math
import string
import Queue

N=1000000

def dump_queue(queue):
    result = []
    for i in iter(queue.get, 'STOP'):
        result.append(i)
    time.sleep(.1)
    return result

start = time.time()

myoutput = mp.Queue()

def checkPerfectNumber(num):
	a = 1
	for num2 in range(2,int(round(math.sqrt(num)))+1):
		if num % num2 == 0:
			a = a+num2+num//num2
	if(a==num):
		return(num)
	else:
		return

#processes = [mp.Process(target=checkPerfectNumber, args=(1000000,myoutput,)) for x in range(4)]

# Run processes
#for p in processes:
#	p.start()

# Exit the completed processes
#for p in processes:
#    p.join()

#myoutput.put('STOP')

# Get process results from the output queue

#results = dump_queue(myoutput)
#print(results)

#stop = time.time()

#print(results)

#print(stop-start)

pool = mp.Pool(processes=5)
results = [pool.apply_async(checkPerfectNumber, args=(x,)) for x in range(2,N)]
output = [p.get() for p in results]
print(output)