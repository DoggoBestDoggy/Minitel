import psutil
# Iterate over all running process
for proc in psutil.process_iter():
    try:
        # Get process name & pid from process object.
        processName = proc.name()
        processID = proc.pid
        print("Name :", processName, "--", "PID :", processID)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
