import pprint

from connect import *

output = connection.send_command("show ip int brief", use_textfsm=True)

pprint.pprint(output)
for item in output:
    print(item['interface'])
    print(item['ip_address'])
    print(item['status'])
    print(item['proto'])