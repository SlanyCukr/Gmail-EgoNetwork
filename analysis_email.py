f = open("output.csv", "r")

lines_to_write = []
unique_nodes = {}

# read lines from fetched emails
for line in f:
    parts = f.readline().split(';')

    sender = parts[1]
    recipient = parts[2]

    if sender not in unique_nodes:
        unique_nodes[sender] = len(unique_nodes)
    if recipient not in unique_nodes:
        unique_nodes[recipient] = len(unique_nodes)

    lines_to_write.append(f"{unique_nodes[sender]}:{unique_nodes[recipient]}")

f.close()

# save lines
f = open("email_edges.csv", "a")
for line in lines_to_write:
    f.write(line + '\n')
f.close()
