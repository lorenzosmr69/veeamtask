from dirsync import sync  # importing dirsync for synchronization
import schedule  # importing schedule for task automation
import time
import logging  # importing logging for log creation
import os.path

# defining inputs for source & replica folder
# defining input for log.txt creation path
source_folder = input('Enter source folder path: ')
replica_folder = input('Enter replica folder path: ')
log_path = input('Enter path for log.txt creation: ')

paths = [source_folder, replica_folder, log_path]

for x in paths:
    if os.path.exists(x):
        print(f'{x} Path Recognized Successfully')

    else:
        raise FileNotFoundError(f'No such file or directory found at {x}')

print("Starting Folder Synchronization...")


# defining function for synchronization, logging & stdout)
def synchronize():

    # using sync to synchronize source folder & replica in way that replica is matching the source folder
    sync(source_folder, replica_folder, 'sync', twoway=True, purge=True)

    # creating log file on custom folder
    logging.basicConfig(filename=log_path+"/logs.log",
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=logging.DEBUG,
                        )


# setting timer of 5 seconds
schedule.every(5).seconds.do(synchronize)

# setting periodical run of the function
while 1:
    schedule.run_pending()
    time.sleep(1)
