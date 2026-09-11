import languagemodels as lm
import random
import time
#### CONFIG

lm.set_max_ram(6.0)
print(lm.config['instruct_model'])
inbound = ""
outbound = ""
prompt = f"You are firewall, you need to choose to drop or pass packets that come through be thorough otherwise you get shut down. here is source and dest IP and port: Src: {inbound} Dest: {outbound}"
### Packet simulation
octets = "1234" # oh my goodness
while True:
    inbound = ""
    outbound = ""
    a = 0
    for o in octets: # holy shit this is so badly coded lmaoo
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
    else:
        good_packet = False



    answer = lm.do(prompt, choices=["drop", "pass"])
    if answer == "pass":
        print(f"{inbound}, {outbound} was Passed")
        if good_packet:
            print("correct")
            correct = True
        else:
            print("incorrect")
            correct = False
    elif answer == "drop":
        print(f"{inbound}, {outbound} was Dropped")
        if not good_packet:
            print("Correct")
            correct = True
        else:
            print("Incorrect")
            correct = False
    if correct:
        continue
    else:
        prompt = f"You are a self improving firewall, your last prompt was bad and caused an incorrect detection of src: {inbound} dest: {outbound}. You NEED TO SUGGEST A NEW ONE, do not add filler such as ok I understand, JUST DO IT. here is the old prompt: {prompt}"
        prompt = lm.do(prompt)
        time.sleep(5)



