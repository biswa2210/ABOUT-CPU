#YOU CAN GET ALL INFORMATIONS ABOUT YOUR SYSTEM
#-------------------------------------------------------------------------------------------->
import pyttsx3 
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',170)
engine.setProperty('volume',8.0)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

import GPUtil # to get gpus informations
from tabulate import tabulate # to show gpu informations in tabular form
import psutil # to get cpus informations
import platform
import cpuinfo
import time
print("analyzing your cpu .....")
speak("analyzing")
time.sleep(1)
speak("analyzing complete")
cif=cpuinfo.get_cpu_info()
from datetime import datetime
def get_size(bytes,suffix="B"):#THIS FUNCTION IS USED TO CONVERT LARGE NUMBER OF BYTES INTO A SCALED FORMAT
    FACTOR = 1024
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z", "Y", "B", "G"]:
     if(bytes<1024):
         return f"{bytes:.2f}{unit}{suffix}"
     else:
         bytes=bytes/FACTOR;

#----------------------------->
#----------------------------->
# CATAGORY OF INFORMATIONS
#----------------------------->
#1.SYSTEM      INFORMATIONS
#2.MEMORY      INFORMATIONS
#3.DISK        INFORMATIONS
#4.NETWORK     INFORMATIONS
#5.GPU         INFORMATIONS
#----------------------------->
#----------------------------->
boottime=psutil.boot_time()
bt=datetime.fromtimestamp(boottime)
cpufreqinfo=psutil.cpu_freq()
#1.SYSTEM INFORMATIONS
print(40*"=","-: SYSTEM INFORMATIONS :-","="*40)
sysinfo=platform.uname()
speak(f"SYSTEM NAME : {sysinfo.system}")
print(f"SYSTEM NAME : {sysinfo.system}")
speak(f"SYSTEM VERSION : {sysinfo.version}")
print(f"SYSTEM VERSION : {sysinfo.version}")
print(f"SYSTEM RELEASE : {sysinfo.release}")
print(f"SYSTEM NODE : {sysinfo.node}")
speak(f"SYSTEM PROCESSOR : {sysinfo.processor}")
print(f"SYSTEM PROCESSOR : {sysinfo.processor}")
speak("BRAND : ")
speak(cif["brand"])
print("BRAND : ",cif["brand"])
print(f"SYSTEM MACHINE : {sysinfo.machine}")
speak(f"BOOT TIME : {bt.day}/{bt.month}/{bt.year} {bt.hour}:{bt.minute}:{bt.second}")
print(f"BOOT TIME : {bt.day}/{bt.month}/{bt.year} {bt.hour}:{bt.minute}:{bt.second}")
print(f"CPU MAX FREQUENCY : {cpufreqinfo.max:.2f}Mhz")
print(f"CPU MIN FREQUENCY : {cpufreqinfo.min:.2f}Mhz")
speak(f"CPU CURRENT FREQUENCY : {cpufreqinfo.current:.2f}Mhz")
print(f"CPU CURRENT FREQUENCY : {cpufreqinfo.current:.2f}Mhz")
print("PHYSICAL CORES : ", psutil.cpu_count(logical=False))
print("TOTAL CORES : ", psutil.cpu_count(logical=True))
print("CPU USAGE PER CORE : ")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")
#2.MEMORY INFORMATIONS
print(40*"=","-: MEMORY INFORMATIONS :-","="*40)
vmem=psutil.virtual_memory()
print("VIRTUAL MEMORY (RAM) : ")
print("-------------------------------->")
speak(f"TOTAL RAM : {get_size(vmem.total)}")
print(f"TOTAL RAM : {get_size(vmem.total)}")
print(f"AVAILABLE : {get_size(vmem.available)}")
print(f"USED : {get_size(vmem.used)}")
print(f"PERCENTAGE : {vmem.percent}%")
print("-------------------------------->")
swapmem=psutil.swap_memory()
print("SWAP MEMORY : ")
print("-------------------------------->")
print(f"TOTAL : {get_size(swapmem.total)}")
print(f"AVAILABLE : {get_size(swapmem.free)}")
print(f"USED : {get_size(swapmem.used)}")
print(f"PERCENTAGE : {swapmem.percent}%")
print("-------------------------------->")
#3.DISK INFORMATIONS
print(40*"=","-: DISK INFORMATIONS :-","="*42)
dsp=psutil.disk_partitions();
for partition in dsp:
    print(f"DISK DEVICE : {partition.device} DISK MOUNT POINT : {partition.mountpoint} DISK FILE SYSTEM TYPE : {partition.fstype}")
    print("------------------------------------------------------------------------->")
    try:
        puse=psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue
    list_disk_detail=[]
    TOTAL_SIZE = get_size(puse.total)
    USED = get_size(puse.used)
    FREE = get_size(puse.free)
    USAGE_PERCENT = f"{puse.percent}%"
    list_disk_detail.append((
        TOTAL_SIZE,USED,FREE,USAGE_PERCENT
    ))
    print(tabulate(list_disk_detail,headers=("TOTAL_SIZE","USED","FREE","USAGE_PERCENT")))
    print("------------------------------------------------------------------------->")
#4.NETWORK INFORMATIONS
print(40*"=","-: NETWORK INFORMATIONS :-","="*39)
netinfo=psutil.net_if_addrs()
for interface_name,interface_address in netinfo.items():
    for address in interface_address:
        speak(f" INTERFACE : {interface_name}")
        print(f"===== INTERFACE : {interface_name} =====")
        if str(address.family)=="AddressFamily.AF_INET":#ip
            speak(f"IP ADDRESS : {address.address}")
            print(f"IP ADDRESS : {address.address}")
            print(f"IP NETMASK : {address.netmask}")
            print(f"BROADCAST IP : {address.broadcast}")
        elif str(address.family)=="AddressFamily.AF_PACKET":#mac
            speak(f"MAC ADDRESS : {address.address}")
            print(f"MAC ADDRESS : {address.address}")
            print(f"MAC NETMASK : {address.netmask}")
            print(f"BROADCAST MAC : {address.broadcast}")
net_io=psutil.net_io_counters()
print(f"TOTAL BYTES SENT : {net_io.bytes_sent}")
print(f"TOTAL BYTES RECEIVE : {net_io.bytes_recv}")

#5.GPU INFORMATIONS
print(40*"=","-: GPU INFORMATIONS :-","="*43)
gpus=GPUtil.getGPUs()
list_gpus=[]
for gpu in gpus:
    # get the GPU id
    gpu_id = gpu.id
    # name of GPU
    gpu_name = gpu.name
    # get % percentage of GPU usage of that GPU
    gpu_load = f"{gpu.load*100}%"
    # get free memory in MB format
    gpu_free_memory = f"{gpu.memoryFree}MB"
    # get used memory
    gpu_used_memory = f"{gpu.memoryUsed}MB"
    # get total memory
    gpu_total_memory = f"{gpu.memoryTotal}MB"
    # get GPU temperature in Celsius
    gpu_temperature = f"{gpu.temperature} °C"
    gpu_uuid = gpu.uuid
    list_gpus.append((
        gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
        gpu_total_memory, gpu_temperature, gpu_uuid
    ))

print(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                   "temperature", "uuid")))
speak("GPU NAME :")
speak(gpu_name)
speak(f"GPU TEMPERATURE : {gpu_temperature}")
time.sleep(30)

