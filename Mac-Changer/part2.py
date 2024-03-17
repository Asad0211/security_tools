#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its Mac address")
    parser.add_option("-m", "--new_mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a new Mac, use --help for more info")
    return options

def mac_changer(interface, mac_address):
    print("[+]Changing Mac address for " + interface + " to " + mac_address)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
mac_changer(options.interface, options.new_mac)

