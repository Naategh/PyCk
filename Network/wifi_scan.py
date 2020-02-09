#!/usr/bin/env python3.6
import subprocess
import argparse

def parseIwScan(iwres):
    #iwdev has a --somewhat-- parsable output
    #for example take this snippet iw dev <> scan output
    #BSS e0:1c:41:ca:90:2a(on wlp1s0)
    #	last seen: 283.395s [boottime]
    #	SSID: inhouse
    #		Channels [36 - 36] @ 17 dBm
    #iwdev uses tabs to create sub sections
    #This parser will be very limited because all
    #we want is bssid and ssid
    #Generator yields dict with info
    iwEnt = {"bssid": None, "ssid": None}
    depth = 0 
    for i in str(iwres).split("\n"):
        #Create a blank iw entry
        #Last element in the array is always a blank character
        if i == "":
            continue
        if i[0] != "\t":
            depth = 0

        if depth == 0:
            iwEnt["bssid"] = i.split("BSS ")[1]
            depth += 1

        elif depth == 1:
            try:
                par = i.split("SSID:")
                if len(par) == 2:
                    iwEnt["ssid"] = par[1]
                    yield iwEnt
                else:
                    continue
            except IndexError: 
                continue


def iw(iface):
    #Calls iw dev <iface> scan
    #returns output needs utf-8 encoding to recognize newlines
    out = subprocess.run(["iw", "dev", iface, "scan"], stdout=subprocess.PIPE, encoding="utf-8")
    return out.stdout 


def main():
    #Arg setup stuff
    parser = argparse.ArgumentParser(description="iw based wireless scanner")
    parser.add_argument("-i", "--iface", type=str, help="interface to scan with")
    args = parser.parse_args()
    if not args.iface:
        print("requires -i")
        exit()
    #Scanner code 
    output = iw(args.iface)
    for i in parseIwScan(output):
        print(i["bssid"])
        print(i["ssid"])

if __name__ == "__main__":
    main()
