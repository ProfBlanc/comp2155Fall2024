from netmiko import ConnectHandler

connection = ConnectHandler(
    device_type='cisco_ios_telnet',
    host='192.168.26.128',
    username='',
    password="",
    secret="cisco1",
    port=30008
)

connection.enable()
connection.disable_paging()
output = connection.send_command("show run")
open("bu-1.txt", "w").write(output)


"""
Step 1)
            threading

Step 2)
        Create a function to connect to a device and run the commands found on lines 12-15

Step 3)
        Create the threads using the threading.Thread()
        RUN the thread\
        
"""
