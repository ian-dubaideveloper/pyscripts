upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
operation = input()
num = int(input())
rotors = []
for i in range(3):
    rotors += (input(),)
message = input()

encoded_message = "".join(
    upp[(upp.find(f) + num + ind) % 26] for ind, f in enumerate(message)
)
for rotor in rotors:
    encoded_message = "".join(rotor[upp.find(f)] for f in encoded_message)
for rotor in rotors[::-1]:
    message = "".join(upp[rotor.find(f)] for f in message)

message = "".join(upp[(upp.find(f) - num - ind) % 26] for ind, f in enumerate(message))
print(encoded_message if operation == "ENCODE" else message)
