from netmiko import ConnectHandler, file_transfer

linux = ConnectHandler(
    host='192.168.26.128',
    username='root',
    password='pnet',
    port=22,
    device_type='linux'
)

# result = file_transfer(
#     ssh_conn=linux,
#     source_file="to_transfer_wed_10am.txt",
#     dest_file="right_here.txt",
#     direction="get",
#     file_system="/root",
#     overwrite_file=True
# )

result = file_transfer(
    ssh_conn=linux,
    source_file="getting_output_as_list_of_dictionary_objects.py",
    dest_file="f1.py",
    direction="put",
    file_system="/root",
    overwrite_file=True
)


print(result)