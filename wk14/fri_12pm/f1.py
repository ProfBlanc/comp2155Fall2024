"""
Connect to each router and create a back-up
of the config

1) import neccessary modules
    netmiko
    threading
"""
from netmiko import ConnectHandler
import threading

"""
define a function that
    accepts name, host, username, password, port, secret, device type

    connects to the device and back-ups the config
"""
def connect(name, port, host="192.168.159.128",
            username="", password="", secret="cisco1",
            device_type="cisco_ios_telnet"):
    connection = ConnectHandler(
        host=host,
        port=port,
        username=username,
        password=password,
        secret=secret,
        device_type=device_type
    )
    connection.disable_paging()
    connection.exit_enable_mode()
    connection.enable()
    open(f"{name}.txt", "w").write(connection.send_command("show run"))


devices = [
    {"name": "device1", "port": 30002},
    {"name": "device2", "port": 30003},
]

for device in devices:
    threading.Thread(target=connect, args=(device['name'], device['port'])).start()
