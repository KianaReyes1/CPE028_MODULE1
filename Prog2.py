fullname="Kiana Mikaella V. Reyes"
num_x = 5.0
num_y = 10.25
routers = ["R1", "R2", "R3"]
print("My Name is ", fullname)
print("The sum of ",num_x," and ",num_y," is ", num_x+num_y)
print(routers)
ipaddress = {"Manila": "10.0.0.1",
             "QC": "10.0.0.5",
             "Marikina": "10.0.0.10"}
print(ipaddress)
print("The ipaddress of Manila is ",ipaddress["Manila"])
for item in routers:
    print(item)

ip_address = {
    "Manila": "10.0.0.1",
    "QC": "10.0.0.5",
    "Marikina": "10.0.0.10"
}

for x, y in ip_address.items():
    print(x, y)