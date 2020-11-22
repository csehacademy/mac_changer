import subprocess
import optparse
import re

def get_user_input():

    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change")
    parse_object.add_option("-m","--mac",dest="mac_adress",help="this is new mac adress")

    return parse_object.parse_args()

#example;
#interface = "eth0"
#mac_adress = "00:22:33:23:43:54"

def change_mac_adress(user_interface,user_mac_adress):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_adress])
    subprocess.call(["ifconfig",user_interface,"up"])

def control_new_mac(interface):

    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("Mac Changer Started!")
(user_input,arguments) = get_user_input()
change_mac_adress(user_input.interface,user_input.mac_adress)
finalized_mac = control_new_mac(str(user_input.interface))

if finalized_mac == user_input.mac_adress:
    print("Mac Changer Success!")
else:
    print("Attempt Failed, Try Again!")