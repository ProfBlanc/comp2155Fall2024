from netmiko import ConnectHandler

connection = ConnectHandler(
    host="192.168.159.128",
    username="root",
    password="pnet",
    port=22,
    device_type="linux"
)

#################################

from connection_linux import *

# commands = ["touch f1_fri_4pm.txt", "mkdir dir1Fri4pm"]
# connection.send_config_set(commands)

connection.send_config_from_file("./commands_to_run.txt")
output = connection.send_command("ls")
print(output)


#################################


from netmiko import ConnectHandler

connection = ConnectHandler(
    host="192.168.159.128",
    username="",
    password="",
    device_type="cisco_ios_telnet",
    port=30002,
    secret="cisco1"
)


#################################

from connection_router import *

print( connection.find_prompt() )

print( connection.send_command("show ip int brief") )

connection.enable()
print( connection.find_prompt() )

connection.disable_paging()  # terminal length 0

output = connection.send_command("show run")
# print(output)
# open("config_back.txt", "w").write(output)

from datetime import datetime

today = datetime.now()

year = today.year
month = today.month
day = today.day
hour = today.hour
minute = today.minute
second = today.second


open(f"config_backup_{year}-{month}-{day}_{hour}-{minute}-{second}.txt", "w").write(output)

connection.exit_enable_mode()
