from netmiko import ConnectHandler

connection = ConnectHandler(
    host='192.168.26.128',
    username='',
    password='',
    secret="cisco1",
    device_type='cisco_ios_telnet',
    port=30008
)
connection.enable()
connection.disable_paging()
output = connection.send_command("show run")
open("backup.txt", "w").write(output)

"""
Connect to all three devices simultaneously
using threading module
Step 1) import threading module
Step 2) Create a method/function that connects to a router
        inside of method, connect, and create back-up
Step 3) Create a thread using Thread class & target, and args params
Step 4) START the threads

"""
