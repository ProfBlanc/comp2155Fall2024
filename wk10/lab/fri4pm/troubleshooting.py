from connect import *

import logging

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    filemode='a'
)

connection.send_command("show version")
