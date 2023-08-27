import subprocess

def kernel_func():
    uname = "uname"
    uname_arg = "-a"
    print("Collecting information about kernel with uname command : \n")
    subprocess.call([uname,uname_arg])

def diskspace_func():
    diskspace = "df"
    diskspace_arg = "-h"
    print("Gathering Hard Disk Space with df command : \n ")
    subprocess.call([diskspace, diskspace_arg])

def uptime():
    uptime = "uptime"
    print("Gathering uptime of the machine using uptime command: \n ")
    subprocess.call([uptime])

def tmp():
    disk_usage = "du"
    disk_args = "-sh"
    path = "/tmp"
    print("Disk usage of /tmp directory : \n ")
    subprocess.call([disk_usage,disk_args,path])


def main():
    kernel_func()
    diskspace_func()
    uptime()
    tmp()


main()