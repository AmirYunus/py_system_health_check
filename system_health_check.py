#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk, threshold=20):
    disk_usage = shutil.disk_usage(disk)
    free = disk_usage.free / disk_usage.total * 100
    return free > threshold

def check_cpu_usage(time=1, threshold=75):
    cpu_usage = psutil.cpu_percent(time)
    return cpu_usage < threshold

if not check_disk_usage("/"):
    print(f"Warning: High disk usage")

if not check_cpu_usage():
    print("ERROR! CPU is overloaded")

else:
    print("Everything is OK!")