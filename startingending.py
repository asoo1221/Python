starting = int(input("please input the starting number"))
ending = int(input("please input the ending number"))
count = int(input("please input the count"))


counter = 0
counter = counter + starting
total = 0

for counter in range (starting,ending + 1, count):
    print(counter)
    total += counter
    counter += count

print("total is ", total)