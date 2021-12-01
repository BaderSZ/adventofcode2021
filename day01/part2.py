arr = []
increases = 0

with open("input","r") as f:
    for i in f.readlines():
            arr.append(int(i.rstrip("\n")))


for i in range(len(arr)):
    if sum(arr[i:i+3]) < sum(arr[i+1:i+4]):
        increases+=1

print("Number of Increases: ", increases)
