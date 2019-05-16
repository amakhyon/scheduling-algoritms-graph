import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.style.use('seaborn-whitegrid')
tick_spacing = 1
fig, ax = plt.subplots(1,1)
txt ="A = Blue B=red C= green D = yellow E = black"
fig.text(.5, .05, txt, ha='center')

ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
plt.gca().invert_yaxis()

def draw(x,y,id):
	if id == 0:
		color = 'blue'
	if id == 1:
		color = 'red'
	if id == 2:
		color = 'green'
	if id == 3:
		color = 'yellow'
	if id ==4:
		color = 'black'
	ax.plot(x,y,color=color)


#global processes, arrival_time, service_time, finish_time, avg_time, turnaround_time, processes_number,turnaround_mean, avg_mean
# class Algorithm:
# 	def __init__(processes_number):

turnaround_mean =0
avg_mean = 0
processes = []
arrival_time = []
service_time = []
finish_time = []
avg_time = []
turnaround_time = []
processes_number = 0

class Process:
	def __init__(self,p_arrival_time, p_service_time):
		self.p_completion_time = 0
		self.p_waiting_time = 0
		self.p_arrival_time = p_arrival_time
		self.p_service_time = p_service_time
		self.p_service_time_temp = p_service_time
		self.p_inQue = False
		self.p_turnaround = 0
		self.p_avg = 0.0
		self.p_isComplete = False
		self.p_hasArrived = False


def use_default():
	global processes, arrival_time, service_time, finish_time, avg_time, turnaround_time, processes_number,turnaround_mean, avg_mean
	processes = ['P 0', 'P 1', 'P 2', 'P 3', 'P 4']
	arrival_time = [0, 2, 4, 6, 8]
	service_time = [3, 6, 4, 5, 2]
	processes_number = 5

def enter_processes():
	global processes_number, arrival_time, service_time
	processes_number = int(input('please enter number of processes: '))
	for process in range(processes_number):
		processes.append('P ' + str(process))
		arrival_time.append(int(input('please enter arrival time for P %d: '%process) ))
		service_time.append(int(input('please enter service time for P %d: '%process) ))

	for i in range(processes_number): #for sorting based on arrival time
		for j in range(i, processes_number):
			if(arrival_time[j] < arrival_time[i]):
				temp = arrival_time[j]
				arrival_time[j] = arrival_time[i]
				arrival_time[i] = temp
				temp = service_time[j]
				service_time[j] = service_time[i]
				service_time[i] = temp


def display(arrival_time, service_time, finish_time, turnaround_time, turnaround_mean, avg_time, avg_mean):
	print(arrival_time)
	print(service_time)
	print('\n\n')
	print(finish_time)
	print(turnaround_time,end='')
	print(" %.2f" %turnaround_mean)
	print(avg_time, end='')	
	print(" %.2f" %avg_mean)
	plt.show()


def FCFS():
	global processes, arrival_time, service_time, finish_time, avg_time, turnaround_time, processes_number, turnaround_mean, avg_mean
	finish_time = [0, 0, 0, 0, 0]
	turnaround_time = [0, 0, 0, 0, 0]
	avg_time = [0, 0, 0, 0, 0]
	process_list = list()
	que = list()
	for i in range(processes_number):
		arrival = arrival_time[i]
		service = service_time[i]
		process_list.append(Process(arrival, service))
		que.insert(i, process_list[i]) #insert all process in que in a FIFO manner

	timeline = 0
	completed_processes = 0

	for process in que:
		for i in range(process.p_service_time):
			x = [timeline, timeline+1]
			y = [process_list.index(process), process_list.index(process)]
			timeline += 1
			draw(x, y, process_list.index(process))
		process.p_completion_time = timeline


	i =0
	sum_turnaround = 0
	sum_avg = 0
	for process in process_list:
		process.p_turnaround = process.p_completion_time - process.p_arrival_time
		process.p_avg = round(float(process.p_completion_time / process.p_turnaround),2)
		finish_time[i] = process.p_completion_time
		turnaround_time[i] = process.p_turnaround
		avg_time[i] = round(float(turnaround_time[i] /service_time[i] ),2)
		sum_turnaround += turnaround_time[i]
		sum_avg += avg_time[i]
		i += 1
	print('\n FCFS \n')
	display(arrival_time, service_time, finish_time, turnaround_time, turnaround_mean, avg_time, avg_mean)

def SPN():
	global processes, arrival_time, service_time, finish_time, avg_time, turnaround_time, processes_number, turnaround_mean, avg_mean
	finish_time = [0, 0, 0, 0, 0]
	turnaround_time = [0, 0, 0, 0, 0]
	avg_time = [0, 0, 0, 0, 0]
	process_list = list()
	que = list()
	for i in range(processes_number):
		arrival = arrival_time[i]
		service = service_time[i]
		process_list.append(Process(arrival, service))
	timeline = 0
	completed_processes = 0
	que.append(process_list[0])
	process_list[0].p_inQue = True
	while(completed_processes < processes_number):

		minimum_process = que[0]
		for process in que: #get minimum prcoss
			if process.p_service_time < minimum_process.p_service_time and process.p_hasArrived == True:
				minimum_process = process
				min = process.p_service_time
		for t in range(minimum_process.p_service_time):
			x = [timeline,timeline+1]
			y = [process_list.index(minimum_process)+1,process_list.index(minimum_process)+1]
			draw(x,y,process_list.index(minimum_process))
			for process in process_list: #check for arrived processes
				if process.p_arrival_time <= timeline and process.p_inQue == False:
					que.append(process)
					process.p_hasArrived = True
					process.p_inQue = True
			timeline += 1

		que.remove(minimum_process)
		minimum_process.p_completion_time = timeline
		completed_processes += 1





	i =0
	sum_turnaround = 0
	sum_avg = 0
	for process in process_list:
		process.p_turnaround = process.p_completion_time - process.p_arrival_time
		process.p_avg = round(float(process.p_completion_time / process.p_turnaround),2)
		finish_time[i] = process.p_completion_time
		turnaround_time[i] = process.p_turnaround
		avg_time[i] = round(float(turnaround_time[i] /service_time[i] ),2)
		sum_turnaround += turnaround_time[i]
		sum_avg += avg_time[i]
		i += 1
	print('\n SPN \n')
	display(arrival_time, service_time, finish_time, turnaround_time, turnaround_mean, avg_time, avg_mean)

def SRT():
	global processes, arrival_time, service_time, finish_time, avg_time, turnaround_time, processes_number, turnaround_mean, avg_mean
	finish_time = [0, 0, 0, 0, 0]
	turnaround_time = [0, 0, 0, 0, 0]
	avg_time = [0, 0, 0, 0, 0]
	waiting_time=[]
	process_list = list()
	for i in range(processes_number):
		arrival = arrival_time[i]
		service = service_time[i]
		process_list.append(Process(arrival, service))
	timeline = 0
	completed_processes = 0
	que = list()
	#que.append(process_list[0])
	while(completed_processes < processes_number):
		for process in process_list: #check for arrived processes
			if process.p_arrival_time <= timeline and process.p_inQue == False:
				que.append(process)
				process.p_inQue = True

		mini = 999
		for process in que: #get process with minimum remaining time
			if process.p_service_time < mini:
				mini = process.p_service_time
				minimum_process = process
		timeline += 1
		x = [timeline-1,timeline]
		y = [process_list.index(minimum_process)+1,process_list.index(minimum_process)+1]
		draw(x,y,process_list.index(minimum_process))
		minimum_process.p_service_time -= 1
		if minimum_process.p_service_time == 0: #a completed process
			minimum_process.p_completion_time = timeline
			completed_processes += 1		
			que.remove(minimum_process)

	i =0
	sum_turnaround = 0
	sum_avg = 0
	for process in process_list:
		process.p_waiting_time = process.p_completion_time - process.p_arrival_time - process.p_service_time
		process.p_turnaround = process.p_waiting_time + process.p_service_time
		process.p_avg = round(float(process.p_completion_time / process.p_turnaround),2)
		finish_time[i] = process.p_completion_time
		turnaround_time[i] = process.p_turnaround
		avg_time[i] = round(float(turnaround_time[i] /service_time[i] ),2)
		sum_turnaround += turnaround_time[i]
		sum_avg += avg_time[i]
		i += 1
	print('\n SRT \n')
	display(arrival_time, service_time, finish_time, turnaround_time, turnaround_mean, avg_time, avg_mean)

def RR():
	quantum = 1
	quantum_counter = 0
	global processes, arrival_time, service_time, finish_time, avg_time, turnaround_time, processes_number, turnaround_mean, avg_mean
	finish_time = [0, 0, 0, 0, 0]
	turnaround_time = [0, 0, 0, 0, 0]
	avg_time = [0, 0, 0, 0, 0]
	process_list = list()
	for i in range(processes_number):
		arrival = arrival_time[i]
		service = service_time[i]
		process_list.append(Process(arrival, service))
	timeline =  0
	que = list()
	completed_processes = 0
	que.append(process_list[0])
	process_list[0].p_inQue = True
	current_process = que[0]
	def switch(index):
		
		if len(que) <= index +1:
			index = 0
			return que[index]
		else:
			index += 1
			return que[index]

	while(completed_processes < processes_number):

		if current_process.p_service_time_temp == 0: #process completed
			current_process.p_isComplete = True
			for process in process_list: #check for arrived processes
				if process.p_arrival_time <= timeline and process.p_inQue == False:
					print('added %d' %process.p_arrival_time)
					que.append(process)
					process.p_hasArrived = True
					process.p_inQue = True
			print('%d is complete, removing from que' %current_process.p_arrival_time)
			index = que.index(current_process)
			que.remove(current_process)
			quantum_counter = 0
			completed_processes += 1
			current_process.p_completion_time = timeline
			if que:
			# 	index = timeline % len(que)
			# 	current_process = que[index]
				current_time = current_process.p_arrival_time
				for process in que: # if there is a greater element
					if process.p_arrival_time > current_time:
						current_process = que[que.index(process)]
						break
					current_process = que[0] #we are already at the bigger element
				print('que is ')
				for p in que:
					print(p.p_arrival_time)
				print('currnt process is  %d because last job completed index = %d' %(current_process.p_arrival_time, index))


		if quantum_counter == quantum: #quantum expired
			for process in process_list: #check for arrived processes
				if process.p_arrival_time <= timeline and process.p_inQue == False:
					que.append(process)
					process.p_inQue = True
					print('added %d because quantum expired ' %process.p_arrival_time)
			print('quantum expired')
			if len(que) == 1 :
				quantum_counter = 0
				print('cant switch')

			else:
				index = que.index(current_process)	
				if que:
					current_process = switch(index)
				print('quantum expired, current process is %d index is %d' %(current_process.p_arrival_time, index))
				quantum_counter = 0
		if completed_processes == len(process_list):
			break
		# if current_process.p_service_time_temp == 0: #process completed
		# 	current_process.p_isComplete = True
		# 	for process in process_list: #check for arrived processes
		# 		if process.p_arrival_time <= timeline and process.p_inQue == False:
		# 			print('added %d' %process.p_arrival_time)
		# 			que.append(process)
		# 			process.p_hasArrived = True
		# 			process.p_inQue = True
		# 	print('%d is complete, removing from que' %current_process.p_arrival_time)
		# 	index = que.index(current_process)
		# 	que.remove(current_process)
		# 	quantum_counter = 0
		# 	completed_processes += 1
		# 	current_process.p_completion_time = timeline
		# 	if que:
		# 		current_process = switch(index)
		# 		print('que is ')
		# 		for p in que:
		# 			print(p.p_arrival_time)
		# 		print('added %d because last job completed index = %d' %(current_process.p_arrival_time, index))

		timeline += 1
		x = [timeline-1 ,timeline]
		y = [process_list.index(current_process)+1,process_list.index(current_process)+1]
		draw(x,y,process_list.index(current_process))
		print('time is %d' %timeline)
		

		quantum_counter += 1
		current_process.p_service_time_temp -= 1
		for process in process_list: #check for arrived processes
			if process.p_arrival_time <= timeline and process.p_inQue == False:
				que.append(process)
				process.p_inQue = True
				print('added %d to que because it arrived ' %process.p_arrival_time)
				print('que is ')
				for p in que: 
					print(p.p_arrival_time)
		print('remaining time is %d' %current_process.p_service_time_temp)





	i = 0
	sum_turnaround = 0
	sum_avg = 0
	for process in process_list:
		process.p_turnaround = process.p_completion_time - process.p_arrival_time
		process.p_avg = round(float(process.p_completion_time / process.p_turnaround),2)
		finish_time[i] = process.p_completion_time
		turnaround_time[i] = process.p_turnaround
		avg_time[i] = round(float(turnaround_time[i] /service_time[i] ),2)
		sum_turnaround += turnaround_time[i]
		sum_avg += avg_time[i]
		i += 1
	print('\n RR \n')
	display(arrival_time, service_time, finish_time, turnaround_time, turnaround_mean, avg_time, avg_mean)



			

while True:
	print('--------------------------------------')
	print('1) use default data')
	print('2) enter processes')
	print('3) FCFS')
	print('4) SPN ')
	print('5) SRT ')
	print('6) RR ')
	print('--------------------------------------')
	choice = int(input('select: '))
	if choice == 1:
		use_default()
	if choice == 2:
		enter_processes()
	if choice == 3:
		FCFS()
	if choice == 4:
		SPN()
	if choice == 5:
		SRT()
	if choice == 6:
		RR()
