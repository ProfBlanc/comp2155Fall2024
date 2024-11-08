from netmiko import ConnectHandler

connection = ConnectHandler(
    device_type="cisco_ios_telnet",
    host="192.168.159.128",
    password="",
    username="",
    port=30002
)
