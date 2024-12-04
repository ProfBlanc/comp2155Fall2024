import threading
from netmiko import ConnectHandler

def connect(
        name: str,
        port: int,
        host: str,
        secret: str,
        username: str = "",
       password: str = ""
):
    connection = ConnectHandler(
        host=host,
        port=port,
        username=username,
        password=password,
        secret=secret,
        device_type="cisco_ios_telnet"
    )

    connection.enable()
    connection.disable_paging()
    open(name.lower() + '.txt', 'w').write(connection.send_command("show run"))


devices = [
    {"name": "device1", "port": 30008, "host": "192.168.26.128", "secret": "cisco1"},
    {"name": "device2", "port": 30009, "host": "192.168.26.128", "secret": "cisco1"},
]

for device in devices:
    threading.Thread(target=connect, args=(device["name"],
                                           device["port"],
                                           device["host"],
                                           device["secret"])).start()

print("finished script!")

