from netmiko import ConnectHandler, file_transfer


connection = ConnectHandler(
    device_type='linux',
    username='root',
    password='pnet',
    host='192.168.159.128',
    port=22
)
src_file = "to_transfer_fri_12pm.txt"
dst_file = "saved.txt"
direction = "get"  # put
file_system_root = "/root"

result = file_transfer(
    ssh_conn=connection,
    source_file=src_file,
    dest_file=dst_file,
    direction=direction,
    file_system=file_system_root,
    overwrite_file=False
)
print(result)