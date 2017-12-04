rows = []
sum = 0

with open("data.txt", "r") as file:
    for line in file:
        rows.append(line.split())

def findDivisible(num, curr, row):
    global sum
    num = int(num)
    for (i, item) in enumerate(row):
        if i == curr:
            continue
        item = int(item)
        if num >= item and (num / item) == int(num / item):
            sum += num / item
            return True
        elif item > num and (item / num) == int(item/num):
            sum += item / num
            return True
    return False

for row in rows:
    found = False
    for (i, item) in enumerate(row):
        if not found:
            found = findDivisible(item, i, row)

print(sum)