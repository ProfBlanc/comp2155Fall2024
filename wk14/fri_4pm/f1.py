"""
Connect simultaneously to 3 devices
create a back-up of the config

1) import netmiko, threading
2) create a function
    named connect
        name    - not a netmiko param
        port
        host
        username
        password
        secret
        device_type
"""
from netmiko import ConnectHandler
import threading
def connect(name: str, port: int,
            host: str = "192.168.159.128",
            username: str = "", password: str = "",
            device_type: str = "cisco_ios_telnet",
            secret: str = "cisco1"):
    connection = ConnectHandler(
        host=host,
        username=username,
        password=password,
        device_type=device_type,
        secret=secret,
        port=port
    )
    connection.disable_paging()
    connection.exit_enable_mode()
    connection.enable()
    output = connection.send_command("show run")
    open(f"{name}.txt", "w").write(output)


devices = [
    {"port": 30002, "name": "device1"},
    {"port": 30003, "name": "device2"},
]

for device in devices:
    threading.Thread(target=connect,
                     args=(device["name"], device["port"])).start()
