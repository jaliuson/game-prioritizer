import psutil
import time;

target_processes = {
    'valorant'
}

def main():
    # for process in psutil.process_iter(attrs=['pid', 'name']):
    for process in psutil.process_iter(['pid', 'name']):
        print('pid:' + str(process.info['pid']) + ' | name: ' + process.info['name'])
        if process.info['name'] in target_processes
            
        

main()
