from netmiko import ConnectHandler

connection = ConnectHandler(
    host="192.168.26.128",
    username="",
    password="",
    device_type='cisco_ios_telnet',
    secret='cisco1',
    port=30006
)

import logging

logging.basicConfig(filename='test.log',
                    level=logging.DEBUG,
                    filemode="a"
                    )

connection.send_command("show version")
