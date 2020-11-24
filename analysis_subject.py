f = open("output.csv", "r")

lines_to_write = []
unique_nodes = {}

# read lines from fetched emails
for line in f:
    parts = f.readline().split(';')

    words = parts[4].split(' ')

    for word in words:
        if word not in unique_nodes:
            unique_nodes[word] = len(unique_nodes)

    # inspired by GetCombination method in Jakub Plesnik's C# hint of solution
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            lines_to_write.append(f"{unique_nodes[words[i]]}:{unique_nodes[words[j]]}")

f.close()

# save lines
f = open("words_edges.csv", "a")
for line in lines_to_write:
    f.write(line + '\n')
f.close()
