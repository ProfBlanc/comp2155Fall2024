from netmiko import ConnectHandler, file_transfer

connection = ConnectHandler(
    device_type="linux",
    host="192.168.159.128",
    username="root",
    password="pnet",
    port=22
)
src_file = "to_transfer_fri_4pm.txt"
dst_file = "right_here.txt"
direction = "get"   # put
file_system_root = "/root"  # of host B


result = file_transfer(
    ssh_conn=connection,
    source_file=src_file,
    direction=direction,
    dest_file=dst_file,
    file_system=file_system_root,
    overwrite_file=True
)
print(result)
