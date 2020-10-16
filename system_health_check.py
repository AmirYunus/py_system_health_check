#!/usr/bin/env python3
import shutil
import psutil
import sys

def check_disk_usage(disk, threshold=20, minimum_absolute = 2, minimum_percentage = 10):
    """
    Returns True if there is enough disk space. Otherwise, returns False.
    """
    disk_usage = shutil.disk_usage(disk)

    # Calculate the percentage of free space
    free_percentage = disk_usage.free / disk_usage.total * 100
    
    # Calculate how many free gigabytes
    free_gigabytes = disk_usage.free / 2**30

    if free_percentage < minimum_percentage or free_gigabytes < minimum_absolute:
        return False

    return True

def check_cpu_usage(time=1, threshold=75):
    """
    Returns True if CPU is not overloaded. Otherwise, returns False.
    """
    cpu_usage = psutil.cpu_percent(time)
    return cpu_usage < threshold

if not check_disk_usage("/"):
    print(f"Warning: High disk usage")
    sys.exit(1)

if not check_cpu_usage():
    print("ERROR! CPU is overloaded")
    sys.exit(1)

print("Everything is OK!")
sys.exit(0)