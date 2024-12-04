import threading
from netmiko import ConnectHandler


def connect(
            name: str,
            port: int, secret: str,
            host: str = "192.168.26.128",
            username: str = "", password: str = ""):
    connection = ConnectHandler(
        device_type="cisco_ios_telnet",
        host=host,
        port=port,
        username=username,
        password=password,
        secret=secret
    )
    connection.enable()
    connection.disable_paging()
    output = connection.send_command("show run")
    open(name.lower() + ".txt", "w").write(output)

devices = [
    {"port": 30009, "name": "Device1", "secret": "cisco1"},
    {"port": 30008, "name": "Device2", "secret": "cisco1"},
]

for device in devices:
    thread = threading.Thread(target=connect, args=(device['name'],
                                                    device['port'],
                                                    device['secret']))
    thread.start()

print("Done")