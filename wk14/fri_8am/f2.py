from netmiko import ConnectHandler
import threading
import time


def connect(name, port, hostname="192.168.26.128", username="", password="",
            device_type="cisco_ios_telnet", secret="cisco1", command=""):
    connection = ConnectHandler(
        host=hostname,
        port=port,
        username=username,
        password=password,
        device_type=device_type,
        secret=secret
    )

    connection.disable_paging()
    connection.enable()
    output = connection.send_command(command if len(command) > 0 else "show run")
    open(f"{name.lower()}.txt", "w").write(output)



devices = [
    {"name": "device1", "port": 30008},
    {"name": "device2", "port": 30009}
]

for device in devices:
    threading.Thread(target=connect, args=(device["name"], device["port"])).start()
