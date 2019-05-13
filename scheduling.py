


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
		self.p_inQue = False
		self.p_turnaround = 0
		self.p_avg = 0.0


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



def FCFS():
	global processes, arrival_time, service_time, finish_time, avg_time, turnaround_time, processes_number, turnaround_mean, avg_mean
	sum = 0
	finish_time.append(service_time[0])
	for i in range(1, processes_number): # get fininsh time
		finish_time.append(finish_time[i-1] + service_time[i])
	for i in range(processes_number): # get turn around time 
		t = finish_time[i] - arrival_time[i]
		sum += t 
		turnaround_time.append(t)
	turnaround_mean = float(sum/processes_number)
	sum = 0
	for i in range(processes_number): # get average time
		t = round(float(turnaround_time[i] / service_time[i]),2)
		sum+= t
		avg_time.append(t)
	avg_mean = float(sum / processes_number)
	display(arrival_time, service_time, finish_time, turnaround_time, turnaround_mean, avg_time, avg_mean)

def SPN():
	global processes, arrival_time, service_time, finish_time, avg_time, turnaround_time, processes_number, turnaround_mean, avg_mean
	finish_time = []
	avg_time = []
	turnaround_time = []
	for i in range(processes_number):
		finish_time.append(0)
	timeline = 0
	temp_arrival = arrival_time[:]
	for i in range(processes_number): #get finish time
		min_arrival = []
		for j in range(len(temp_arrival)):
			if temp_arrival[j] <= timeline: # get all arrived processes
				min_arrival.append(service_time[arrival_time.index(temp_arrival[j])])
		chosen_process = min(min_arrival)
		timeline+= chosen_process	 #get the min of all arived processes and add to timeline
		temp_arrival.remove(arrival_time[service_time.index(chosen_process)])
		finish_time[service_time.index(chosen_process)] = timeline
	sum = 0
	for i in range(processes_number): # get turn around time 
		t = finish_time[i] - arrival_time[i]
		sum += t 
		turnaround_time.append(t)
	turnaround_mean = float(sum/processes_number)
	sum = 0
	for i in range(processes_number): # get average time
		t = round(float(turnaround_time[i] / service_time[i]),2)
		sum+= t
		avg_time.append(t)
	avg_mean = float(sum / processes_number)
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
	quantum = 4
	quantum_counter =0
	global processes, arrival_time, service_time, finish_time, avg_time, turnaround_time, processes_number, turnaround_mean, avg_mean
	finish_time = [0, 0, 0, 0, 0]
	turnaround_time = [0, 0, 0, 0, 0]
	avg_time = [0, 0, 0, 0, 0]
	process_list = list()
	for i in range(processes_number):
		arrival = arrival_time[i]
		service = service_time[i]
		process_list.append(Process(arrival, service))
	timeline = 0
	que = list()
	p_index = 0
	completed_processes = 0
	current_process = process_list[0]
	cursor = 0
	while(completed_processes < processes_number):
		for process in process_list: #check for arrived processes
			if process.p_arrival_time <= timeline and process.p_inQue == False:
				que.append(process)
				print("added %d to que" %process.p_arrival_time)
				process.p_inQue = True
		print('current process is %d ' %current_process.p_arrival_time)
		timeline += 1
		print('time is %d' %timeline)
		quantum_counter += 1
		current_process.p_service_time -= 1

		if current_process.p_service_time == 0: #completed
			completed_processes += 1
			que.remove(current_process)
			print('removed %d from que ' %current_process.p_arrival_time)
			current_process.p_completion_time = timeline
			p_index += 1
			if p_index >= len(que):
				p_index = 0

			if que:
				current_process = que[p_index]
				print('current process is %d ' %current_process.p_arrival_time)
				quantum_counter = 0


		if quantum_counter >= quantum: #quantum expired
			quantum_counter = 0
			p_index += 1
			if p_index >= len(que) :
				p_index = 0
			if que:
				current_process = que[p_index]
				print('current process is %d ' %current_process.p_arrival_time)

			#switch


	i = 0
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
	print('\n RR \n')
	display(arrival_time, service_time, finish_time, turnaround_time, turnaround_mean, avg_time, avg_mean)


def calculate():
	# FCFS()
	# print('-----\n\n')
	# SPN()
	# SRT()
	RR()

			

while True:
	print('--------------------------------------')
	print('1) use default data')
	print('2) enter processes')
	print('3) calculate')
	print('--------------------------------------')
	choice = int(input('select: '))
	if choice == 1:
		use_default()
	if choice == 2:
		enter_processes()
	if choice == 3:
		calculate()