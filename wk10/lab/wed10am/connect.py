from netmiko import ConnectHandler

connection = ConnectHandler(
    host="192.168.26.128",
    password="",
    username="",
    device_type="cisco_ios_telnet",
    port=30004

)
