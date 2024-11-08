from netmiko import ConnectHandler, file_transfer

connection = ConnectHandler(
    host='192.168.26.128',
    device_type='linux',
    username='root',
    password='pnet',
    port=22
)
direction = "get"  # put local => remote; get remote=>local
src_file = "to_transfer_fri_8am.txt"
dst_file = "./data/test.txt"
file_system_root = "/root"

result = file_transfer(
    ssh_conn=connection,
    source_file=src_file,
    dest_file=dst_file,
    direction=direction,
    file_system=file_system_root
)

print(result)
