from connect import *

import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="test.log", filemode="a")
logger = logging.getLogger("netmiko")

output = connection.send_command("show version")
print(type(output))
print(output)
