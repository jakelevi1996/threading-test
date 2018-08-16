import threading
import numpy as np
from time import sleep
import numpy as np

# Number of threads to keep active and experiments for them to run
NUM_THREADS = 5
NUM_EXPERIMENTS = 13

# List to store each of the threads
thread_list = []
for _ in range(NUM_THREADS):
    thread_list.append(threading.Thread())

# List of experiments
experiment_list = [i for i in range(13)]

# Toy function to be run by each thread
def experiment_func(arg, thread_num):
    print("Thread {} is waiting for {} seconds".format(
        thread_num, arg))
    sleep(arg)
    print("Thread {} has finished waiting for {} seconds".format(
        thread_num, arg))

# Keep looping until no more experiments left
while len(experiment_list) > 0:
    # Check each of the threads
    for thread_num, thread in enumerate(thread_list):
        # If a thread is not alive and there are still experiments left,
        # pop an experiment from the list and assign to a new thread,
        # replacing the old thread in thread_list
        if (not thread.is_alive()) and (len(experiment_list) > 0):
            print("Thread {} is not alive".format(thread_num))
            arg = experiment_list.pop()
            thread_list[thread_num] = threading.Thread(
                target=experiment_func, args=[arg, thread_num])
            thread_list[thread_num].start()

print("No more experiments are left in the list")