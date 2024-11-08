import pprint

from connect import *

output = connection.send_command("show version", use_textfsm=True)

pprint.pprint(output, indent=4)

print(f"My Hostname is {output[0]['hostname']}")