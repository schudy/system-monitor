import platform
import psutil
import time

def get_system_info():
    system_name = platform.system()
    system_version = platform.release()
    machine = platform.machine()
    
    print("System:", system_name)
    print("Version:", system_version)
    print("Machine:", machine)

def get_resource_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    
    print("CPU Usage:", cpu_usage, "%")
    print("Memory Usage:", memory.percent, "%")
    print("Disk Usage:", disk.percent, "%")

    if cpu_usage > 80:
        print("WARNING: High CPU usage")

    if memory.percent > 80:
        print("WARNING: High memory usage")

    if disk.percent > 85:
        print("WARNING: High disk usage")

def show_top_processes():
    processes = []

    for process in psutil.process_iter():
        try:
            process.cpu_percent()
            processes.append(process)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    time.sleep(1)
    process_data = []

    for process in processes:
        try:
            info = {
                "pid": process.pid,
                "name": process.name(),
                "cpu": process.cpu_percent()
            }

            process_data.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    process_data.sort(key=lambda process: process["cpu"], reverse=True)

    print("\nTop Processes by CPU Usage:")

    for process in process_data[:5]:
        print(
            "PID:", process["pid"],
            "| CPU:", process["cpu"], "%",
            "| Name:", process["name"]
            )
        
 

get_system_info()
get_resource_usage()
show_top_processes()
