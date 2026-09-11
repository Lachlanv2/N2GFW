import languagemodels as lm
import random

packet = "src: 172.16.32.66 dest: 192.168.3.1, protocol: ransom dest_port 443 src_port: 54313"

prompt = f"You are a firewall, only respond with one word. if a packet is suspicious, say no. If a packet is good, say yes. If a packet is mabye suspicious, say maynot. If a packet is mabye not suspicious, say mabye. the packet is here: {packet}"


'''
answer = lm.do(prompt)

if answer == "yes":

    print(f"{packet} was Passed")

elif answer == "no":
    print(f"{packet} was Blocked")

elif answer == "maybe":
    print("mabye not suspicious")
    chance = random.randint(0, 100)
    if chance < 75:
        print("Packet is safe")
    else:
        pass

elif answer == "maynot":
    print("mabye not suspicious")
    chance = random.randint(0, 100)
    if chance < 75:
        print("Packet is unsafe, dropped")
    else:
        print("Packet is safe")

else:
    pass
'''


### Packet simulation
octets = "abcd"
while True:
    inbound = ""
    outbound = ""
    a = 0
    for o in octets:
        a += 1
        octet = random.randint(1, 255)
        inbound = inbound + str(octet)

        if a == 4:
            pass
        else:
            inbound = inbound + "."

    a = 0
    for o in octets:
        a += 1
        octet = random.randint(1, 255)
        outbound = outbound + str(octet)
        if a == 4:
            pass
        else:
            outbound = outbound + "."

    inbound_direction = random.randint(0, 1)
    if inbound_direction == 0: # going out
        ephemeral_port = random.randint(1, 65535)
        inbound = inbound + ":" + str(ephemeral_port)
        common_ports = [22, 25, 53, 80, 115, 123, 118, 389, 443, 464, 500]
        outbound_port = random.choice(common_ports)
        outbound = outbound + ":" + str(outbound_port)
    else: # going in
        ephemeral_port = random.randint(1, 65535)
        outbound = outbound + ":" + str(ephemeral_port)
        common_ports = [22, 25, 53, 80, 115, 123, 118, 389, 443, 464, 500]
        inbound_port = random.choice(common_ports)
        inbound = inbound + ":" + str(inbound_port)

    if inbound_direction == 1:
        print("Inbound direction")
    else:
        print("outbound direction")
    print("Source =", inbound)
    print("Destination =", outbound)
    exit()




