import psutil
import time;

target_processes = {
    'VALORANT-Win64-Shipping.exe'
}
            
# find the target processes if they are running and return their pid
def find_process():
    output = []
    for process in psutil.process_iter(['pid', 'name']):
        print('pid:' + str(process.info['pid']) + ' | name: ' + process.info['name'])
        if process.info['name'] in target_processes:
            output.append(process)
    return(output)

# increase the priority of the process running with pid parameter
def upgrade_priority(pid):
    target_process = psutil.Process(pid)
    target_process.nice(psutil.HIGH_PRIORITY_CLASS)
    
# reallocate the cores that handle the process such that they are not handled by cpu0
#def reallocate_process(pid):

def main():
    targets = find_process()
    print('found' + str(targets))
    for process in targets:
        upgrade_priority(process.info['pid'])

main()
