#!/usr/bin/env python
import subprocess
import optparse
import re


def change_mac(interface, new_mac):

    print("[+] Changing mac address for " + interface + " to " + new_mac)
    # si spegne l'interfaccia
    subprocess.call(["ifconfig", interface, "down"])
    # si cambia il MAC address per l'interfaccia di interesse
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    # si riaccende l'interfaccia
    subprocess.call(["ifconfig", interface, "up"])


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface and not options.new_mac:
        parser.error("[-] Please enter a valid MAC address and a valid interface, use --help for more info")
    elif not options.interface:
        parser.error("[-] Please enter a valid interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please enter a valid MAC address, use --help for more info")
    return options


def find_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    match = re.search(r'ether ([0-9a-fA-F:]+)', str(ifconfig_result))
    if match:
        return match.group(1)
    print("[-] Couldn't read mac address")
    exit()
