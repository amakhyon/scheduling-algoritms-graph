
This is a simple tool to plot scheduling algorithms and calculate : finish time, turnaround time and some averages and means 

python version 3.7, it will be buggy on older versions
this project uses matplotlib, to install if you have pip: pip install matplotlib
to install pip: download this script https://bootstrap.pypa.io/get-pip.py then cd into directory and use $python get-pip.py (works on windows, linux, mac)


contains:
1- FCFS (first come first solved)
2-SRT (shortest remaining time)
3- SPN (shortest process next)
4- RR (round robin)


Assem Makhyon

this script calculates only 5 processes, if you want it to calculate more then follow these instructions:

in the "use_default()" method add the arrival and service time and modify process number(count) , also add a label for each process
in the "draw()"  method increment an id and add a color following the same pattern it was written with
