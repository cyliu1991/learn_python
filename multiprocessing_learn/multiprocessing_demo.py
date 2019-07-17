import multiprocessing
import os
import time


def run_proc(name):
    print('Child process {0} {1} Running'.format(name, os.getpid()))


def run_task(name):
    print('Task {0} pid {1} is running, parent id is {2}'.format(name, os.getpid(), os.getpgid()))
    time.sleep(1)
    print('Task {0} end.'.format(name))


if __name__ == '__main__':
    print('Current process {0}'.format(os.getpid()))
    # print('Parent process {0} is Running'.format(os.getpid()))
    p = multiprocessing.Pool(processes=3)
    for i in range(6):
        p.apply_async(run_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All Processes done!')
