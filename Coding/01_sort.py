# take in the number
n = str(input())

# calculate answer
n = n.split()
maximum = n[0]
minimum = maximum
for i  in n:
    if float(i) > float(maximum):
        maximum = i
    elif float(i) < float(minimum):
        minimum = i
# print answer
print(minimum+"\n"+maximum)