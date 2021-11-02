import subprocess
import os
from pyrnalist.pyrnalist import report

def ensure(command):
    try:
        report.verbose(f'Looking for program: {command}')
        subprocess.run(command, capture_output=True, text=True)
    except FileNotFoundError:
        report.error('Program not found.')
    except:
        report.error('Unknown error has occurred')

def exists(file_path):
    return os.path.exists(file_path)

def execute(command):
    report.command(' '.join(command))
    return subprocess.run(command, capture_output=True, text=True)
