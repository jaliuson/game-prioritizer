import psutil
import time

# list of processes that will be prioritized as foujnd by their name in
# Task Manager > right click > go to details
target_processes = {
    'VALORANT-Win64-Shipping.exe',
    'League of Legends.exe'
}
            
# find the target processes if they are running and return their pid
def find_process():
    output = []
    for process in psutil.process_iter(['pid', 'name']):
        #print('pid:' + str(process.info['pid']) + ' | name: ' + process.info['name']) //list out all the processes found
        if process.info['name'] in target_processes:
            output.append(process)
    print(f"Found \t\t {len(psutil.pids())} \tprocesses (total)")
    print(f'Optimizing \t {len(output)} \tprocesses (target)\n')
    return(output)

# increase the priority of the process running with pid parameter
def upgrade_priority(pid):
    target_process = psutil.Process(pid)
    target_process.nice(psutil.HIGH_PRIORITY_CLASS)
    print('>> Process ' + target_process.name() + ' switched to HIGH priority')
    
# reallocate the cores that handle the process such that they are not handled by cpu0
def reallocate_process(pid):
    print('started')
    core_count = psutil.cpu_count()
    target_process = psutil.Process(pid)
    target_process.cpu_affinity(range(1,core_count))
    print('>> Process ' + target_process.name() + ' affinity set to exclude CPU0')

def main():
    start = time.time()
    targets = find_process()
    # print('found' + str(targets))
    for process in targets:
        upgrade_priority(process.info['pid'])
        reallocate_process(process.info['pid'])
    end = time.time()
    print(f'Completed in: {round(end - start , 3)} seconds')

main()