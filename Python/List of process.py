'''list running processes'''
import psutil

for proc in psutil.process_iter():
    print(proc.name())
