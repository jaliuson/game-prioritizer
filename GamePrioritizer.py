import psutil
import time

from data.GamesList import GAME_OPTIONS

# list of processes that will be prioritized as foujnd by their name in
# Task Manager > right click > go to details
            
# find the target processes if they are running and return their pid
def findProcess(targetProcessName):
    output = []
    for process in psutil.process_iter(['pid', 'name']):
        #print('pid:' + str(process.info['pid']) + ' | name: ' + process.info['name']) //list out all the processes found
        if process.info['name'] == GAME_OPTIONS[targetProcessName]:
            output.append(process)
    print(f"Found \t\t {len(psutil.pids())} \tprocesses (total)")
    print(f'Optimizing \t {len(output)} \tprocesses (target)\n')
    return(output)

# increase the priority of the process running with pid parameter
def UpgradePriority(pid):
    target_process = psutil.Process(pid)
    target_process.nice(psutil.HIGH_PRIORITY_CLASS)
    print('>> Process ' + target_process.name() + ' switched to HIGH priority')
    
# reallocate the cores that handle the process such that they are not handled by cpu0
def ReallocateProcess(pid):
    print('started')
    core_count = psutil.cpu_count()
    target_process = psutil.Process(pid)
    target_process.cpu_affinity(range(1,core_count))
    print('>> Process ' + target_process.name() + ' affinity set to exclude CPU0')

def run(targetProcessName):
    start = time.time()
    targets = findProcess(targetProcessName)
    # print('found' + str(targets))
    for process in targets:
        UpgradePriority(process.info['pid'])
        ReallocateProcess(process.info['pid'])
    end = time.time()
    print(f'Completed in: {round(end - start , 3)} seconds')