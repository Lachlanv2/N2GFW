import languagemodels as lm
import random

#### CONFIG

lm.set_max_ram(1.0)
lm.config['instruct_model']

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


    ephemeral_port = random.randint(1, 65535)
    inbound = inbound + ":" + str(ephemeral_port)
    common_ports = [22, 25, 53, 80, 115, 123, 118, 389, 443, 464, 500]
    outbound_port = random.choice(common_ports)
    outbound = outbound + ":" + str(outbound_port)
    if outbound_port == 443 or outbound_port == 53 or outbound_port == 22 or outbound_port == 25:
        good_packet = True
    break

prompt = f"You are firewall, here is source and dest IP and port: Src: {inbound} Dest: {outbound}"
answer = lm.do(prompt, choices=["yes", "no"])
if answer == "yes":
    print(f"{inbound}, {outbound} was Passed")




