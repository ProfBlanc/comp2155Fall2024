from connection import *

output = connection.send_command("show ip int brief",
                                 use_textfsm=True)
# print(repr(output))
print(output)
print(output[0]['ip_address'])
for item in output:
    print(item['interface'])
    print(item['ip_address'])
    print(item['status'])
    print(item['proto'])
