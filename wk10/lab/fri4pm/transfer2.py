from netmiko import ConnectHandler, file_transfer

connection = ConnectHandler(
    device_type="linux",
    host="192.168.159.128",
    username="root",
    password="pnet",
    port=22
)

# copy the file troubleshooting.py to remote host with new name of 'source_code_fri_4pm.py'
src_file = "troubleshooting.py"
dst_file = "source_code_fri_4pm.py"
direction = "put"
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
