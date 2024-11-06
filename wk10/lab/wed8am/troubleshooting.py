from connection import *

import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko_logs")

output = connection.send_command("show version")
print(output)