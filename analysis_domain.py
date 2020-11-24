f = open("output.csv", "r")

lines_to_write = []
unique_nodes = {}

# read lines from fetched emails
for line in f:
    parts = f.readline().split(';')

    sender_domain = parts[1].split('@')[1]
    recipient_domain = parts[2].split('@')[1]

    if sender_domain not in unique_nodes:
        unique_nodes[sender_domain] = len(unique_nodes)
    if recipient_domain not in unique_nodes:
        unique_nodes[recipient_domain] = len(unique_nodes)

    # ignore same domain in recipient and sender
    if unique_nodes[sender_domain] != unique_nodes[recipient_domain]:
        lines_to_write.append(f"{unique_nodes[sender_domain]}:{unique_nodes[recipient_domain]}")

f.close()

# save lines
f = open("domain_edges.csv", "a")
for line in lines_to_write:
    f.write(line + '\n')
f.close()
