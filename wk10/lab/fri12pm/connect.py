from netmiko import ConnectHandler
# router connection
connection = ConnectHandler(
    host='192.168.159.128',
    username='',
    password='',
    port=30001,
    secret='cisco1',
    device_type='cisco_ios_telnet'
)
