#!/usr/bin/env python
# al terminale esegui un comando simile al seguente:
# python3 main.py --interface eth0 --mac 00:11:22:33:44:55
# or
# python3 main.py -i eth0 -m 00:11:22:33:44:55
# il mac address dell'interfaccia cambierà
import mac_changer
# implementazione effettuata nel file py mac_changer

try:
    options = mac_changer.get_arguments()
    current_mac = mac_changer.find_mac(options.interface)
    print("Current Mac = ", str(current_mac))
    mac_changer.change_mac(options.interface, options.new_mac)
    current_mac = mac_changer.find_mac(options.interface)
    if current_mac == options.new_mac:
        print("[+] The MAC address has been successfully changed to " + current_mac)
    else:
        print("[-] The MAC address is not changed.")
except Exception as e:
    print(f"\n[-] Something went wrong: {e}\n"
          "[-] You can run the 'python3 main.py --help' command for more information.\n"
          "[-] You can use the following example command as a reference:\n"
          "\t'python3 main.py --interface eth0 --mac 00:11:22:33:44:55'.")
