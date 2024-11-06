from connection import connection
from netmiko import file_transfer, ConnectHandler

outcome = file_transfer(

    source_file="to_transfer_wed_8am.txt",
    dest_file="./from_remote_wed_8am.txt",
    ssh_conn=ConnectHandler(host="192.168.26.128", username="root",
                            password="pnet", port=22, device_type="linux"),

    file_system="/root",
    direction="get", # put = local=>remote, get=remote=>local
)

print(outcome)
