#!/usr/bin/env python3.6
import scapy.all as scapy
import argparse


def main():
    # All code is in main function because no higher level wrapper functions are needed for scapy

    # Argparse setup
    parser = argparse.ArgumentParser(description="Packet sniffer")
    parser.add_argument("--iface", type=str, help="interface to sniff")
    parser.add_argument("--filter", type=str, help="bpf filter string")
    parser.add_argument("--outfile", type=str, help="Pcap file to output")
    args = parser.parse_args()

    if not args.iface:
        # Needs an interface
        print("--iface required")
        exit()

    # Default Values for opts
    outfile = "out.pcap"
    filt = None
    try:
        pkts = scapy.sniff(filter=filt, iface=args.iface)
        scapy.wrpcap(outfile, pkts)

    except PermissionError:
        # Raw sockets require root privs
        print("Must run as root")
        exit()


if __name__ == "__main__":
    main()
