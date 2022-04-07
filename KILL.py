import os
import psutil
for process in psutil.process_iter():
    if process.name() == "notepad.exe":
        os.system("taskkill /im " + str(process.pid))
