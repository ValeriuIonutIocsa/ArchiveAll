import os
import subprocess
import sys
import time

start_time = time.time()
sys.stdout.write('\nstarting archive all script\n')

if sys.argv.__len__() < 2:
    sys.stderr.write('insufficient arguments\n\n')
    exit(-1)

i = 1
while i < sys.argv.__len__():

    arg = sys.argv[i]
    file_path = os.path.abspath(arg)
    sys.stderr.write('\narchiving ' + file_path + '\n')

    archive_path = file_path + '.7z'

    command = ['cmd', '/c', '7z9', file_path, archive_path]
    sys.stderr.write('running command: ' + command.__str__() + '\n')

    subprocess.run(command)
    i = i + 1

exec_time = str(round(time.time() - start_time, 2))
sys.stdout.write('\ndone; execution time: ' + exec_time + ' seconds\n')
