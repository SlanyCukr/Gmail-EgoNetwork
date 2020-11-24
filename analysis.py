lines_to_write = []

f = open("output.csv", "r")


for line in f:
    parts = f.readline().split(';')

f.close()
