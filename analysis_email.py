import re

f = open("output.csv", "r")

lines_to_write = []
unique_nodes = {}

# read lines from fetched emails
for line in f:
    parts = f.readline().split(';')

    if '<' in parts[1] and '>' in parts[1]:
        sender = re.search('<(.*)>', parts[1]).group(1).lower()
    else:
        sender = parts[1].lower()

    if '<' in parts[2] and '>' in parts[2]:
        recipient = re.search('<(.*)>', parts[2]).group(1).lower()
    else:
        recipient = parts[2].lower()

    if sender not in unique_nodes:
        unique_nodes[sender] = len(unique_nodes)
    if recipient not in unique_nodes:
        unique_nodes[recipient] = len(unique_nodes)

    lines_to_write.append(f"{unique_nodes[sender]};{unique_nodes[recipient]}")

f.close()

# save lines
f = open("email_edges.csv", "a")
f.write("Source;Target\n")
for line in lines_to_write:
    f.write(line + '\n')
f.close()
