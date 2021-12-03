inp = []
gamma = epsilon = 0
gamma_bin = epsilon_bin = ""


with open("input","r") as f:
    for i in f.readlines():
        inp.append(i.rstrip("\n"))

for i in range(len(inp[0])):
    one_count  = zero_count = 0
    for j in range(len(inp)):
        if inp[j][i] == "1":
            one_count += 1
        elif inp[j][i] == "0":
            zero_count += 1

    if one_count > zero_count:
        gamma_bin   += "1"
        epsilon_bin += "0"
    elif zero_count > one_count:
        gamma_bin   += "0"
        epsilon_bin += "1"

gamma = int(gamma_bin, 2)
epsilon = int(epsilon_bin, 2)

print("epsilon_bin = {}, gamma_bin = {}".format(epsilon_bin, gamma_bin))
print("epsilon = {}, gamma = {}".format(epsilon, gamma_bin))
print("epsilon * gamma = {}".format(epsilon * gamma))
