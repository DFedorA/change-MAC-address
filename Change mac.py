import subprocess
import optparse
import re

def get_arg():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest = "interface", help="Interface to change its MAC addres")
    parser.add_option("-m","--mac",dest ="new_mac",help = "New MAC address")
    (options,arguments) = parser.parse_args()
    if options.interface == False:
        parser.error("Please specify an interface, --help")
    if options.new_mac == False:
        parser.error("Please specify an new mac, --help")
    return options

def change_mac(interface,new_mac):
    print("Changing MAC address for " + interface +" to " + new_mac)
    subprocess.call(["ifconfig",interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    capture = subprocess.check_output(["ifconfig", opthions.interface])
    capture_re = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", capture)
    if capture_re:
        return capture_re.group(0)
    else:
        print("Error MAC address")

opthions = get_arg()
curren_mac = get_current_mac(opthions.interface)
change_mac(opthions.interface,opthions.new_mac)
if curren_mac == opthions.new_mac:
    print("MAC address was successfully changed")
else:
    print("MAC address did not changed")

