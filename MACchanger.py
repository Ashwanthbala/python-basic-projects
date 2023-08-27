import re
import subprocess
import optparse


def get_data(interface):
    ifconfig_capture = subprocess.check_output(["ifconfig", interface])
    print(ifconfig_capture)
    mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_capture))
    return mac_address.group(0)


def change_mac(interface,new_mac):
    subprocess.call(f"ifconfig {interface} down", shell=True)
    subprocess.call(f"ifconfig {interface} hw ether {new_mac}", shell=True)
    subprocess.call(f"ifconfig {interface} up",shell=True)

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Please enter the interface")
    parser.add_option("-m","--mac",dest="mac",help="Please enter the MAC address")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[+] Please enter the interface")
    if not options.mac:
        parser.error("[+] Please enter the MAC address")
    return options



options = get_arguments()
current_mac = get_data(options.interface)
print(f"[+] Current MAC Address: {str(current_mac)}")
change_mac(options.interface,options.mac)
current_mac = get_data(options.interface)
if options.mac == current_mac:
    print(f"[+] MAC address has been changed to {current_mac} ")
else:
    print("[-] MAC Address did not change")
