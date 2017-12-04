rows = []
with open("data.txt", "r") as file:
    for line in file:
        rows.append(line.split())

checksum = 0

for row in rows:
    small = float('inf')
    big = -1
    for item in row:
        item = int(item)
        if item > big:
            big = item
        if item < small:
            small = item
    checksum += big - small

print(checksum)