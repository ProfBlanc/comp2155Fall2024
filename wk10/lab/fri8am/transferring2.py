from netmiko import ConnectHandler, file_transfer

connection = ConnectHandler(
    host='192.168.26.128',
    device_type='linux',
    username='root',
    password='pnet',
    port=22
)
direction = "put"  # put local => remote; get remote=>local
src_file = "troubleshooting.py"
dst_file = "uploaded_via_local_host.py"
file_system_root = "/root"

result = file_transfer(
    ssh_conn=connection,
    source_file=src_file,
    dest_file=dst_file,
    direction=direction,
    file_system=file_system_root
)

print(result)
