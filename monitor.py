import os, sys

from logger import FILENAME

'''
Monitors the log file as a stream via the terminal
'''

if FILENAME not in os.listdir():
    with open(FILENAME, 'w') as f:
        f.write('')

if sys.platform == 'win32':
    os.system(
        f'powershell.exe -ExecutionPolicy RemoteSigned Get-Content '
        f' ./{FILENAME} -Tail 30 -Wait')
else:
    os.system(f'less +F {FILENAME}')
