from netmiko import ConnectHandler

connection = ConnectHandler(
    device_type='cisco_ios_telnet',
    host='192.168.26.128',
    username="",
    password="",
    secret="cisco1",
    port=30006
)
connection.enable()
output = connection.send_command("show ip int brief",

                                 use_textfsm=True)

if type(output) == list:
    for result in output:
        print(result)
else:
    print(output)

# for result in output:
#     print(result['interface'])
#     print(result['ip_address'])
#     print(result['status'])
