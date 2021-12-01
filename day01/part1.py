arr = []
increases = 0

with open("input","r") as f:
    for i in f.readlines():
            arr.append(int(i.rstrip("\n")))


for i in range(len(arr)):
    if i == 0:
        continue
    if arr[i-1] < arr[i]:
        increases=increases+1

print("Number of Increases: ", increases)
