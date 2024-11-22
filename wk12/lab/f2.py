import telnetlib

tn = telnetlib.Telnet(
    host="192.168.159.128",
    port=30003
)

print(tn)
print(tn.host)
tn.read_until(b"down", timeout=5)
tn.write('\n\n\n\n\n'.encode())
print(tn.read_all())
tn.close()
