import languagemodels as lm
import random

packet = "src: 172.16.32.66 dest: 192.168.3.1, protocol: ransom dest_port 443 src_port: 54313"

prompt = f"You are a firewall, only respond with one word. if a packet is suspicious, say no. If a packet is good, say yes. If a packet is mabye suspicious, say maynot. If a packet is mabye not suspicious, say mabye. the packet is here: {packet}"



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