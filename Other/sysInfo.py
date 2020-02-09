#!/usr/bin/env python
import os
import time
import platform
import cpuinfo


def main():
    os.system("clear")
    print("\t" + "#" * 80 + "#")
    print("\t" + "#\033[91m\t[*] This is a simple script to show your system information\033[0m\t\t" + "#")
    print("\t" + "#" * 80 + "#")
    print("")

    print("\033[91m\tTime: \033[0m" + time.ctime())
    print("\033[91m\tCurrent directory: \033[0m" + os.getcwd())
    print("\033[91m\tPython Version: \033[0m" + cpuinfo.get_cpu_info()["python_version"])
    print("\033[91m\tOperation System: \033[0m" + platform.system())
    print("\033[91m\tNode: \033[0m" + platform.node())
    print("\033[91m\tOS Version: \033[0m" + platform.uname()[3])
    print("\033[91m\tSystem Type: \033[0m" + platform.architecture()[0])
    print("\033[91m\tCores: \033[0m" + str(cpuinfo.get_cpu_info()["count"]))
    print("\033[91m\tCPU: \033[0m" + cpuinfo.get_cpu_info()["brand"])


if __name__ == "__main__":
    main()
