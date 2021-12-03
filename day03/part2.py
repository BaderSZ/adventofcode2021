inp = []
o2_generator = co2_scrubber = 0
o2_generator_bin = co2_scrubber_bin = ""

# seperate lines, don't want memory copy
clean_list_ones = []
clean_list_zeros = []

with open("input","r") as f:
    for i in f.readlines():
        inp.append(i.rstrip("\n"))

working_list = inp.copy()

# most common
for i in range(len(working_list[0])):
    one_count = zero_count = 0
    max_len = len(working_list)
    if max_len == 1:
        break
    for j in range(max_len):
        if working_list[j][i] == "1":
            one_count+=1
        elif working_list[j][i] == "0":
            zero_count+=1

    if one_count >= zero_count:
        for j in range(max_len):
            if working_list[j][i] == "1":
                clean_list_ones.append(working_list[j])
    else:
        for j in range(max_len):
            if working_list[j][i] == "0":
                clean_list_ones.append(working_list[j])
    working_list = clean_list_ones.copy()
    clean_list_ones = []

o2_generator_bin = working_list[0]


#####
# Start again
#####

working_list = inp.copy()

# least common
for i in range(len(working_list[0])):
    one_count = zero_count = 0
    max_len = len(working_list)
    if max_len == 1:
        break
    for j in range(max_len):
        if working_list[j][i] == "0":
            zero_count+=1
        elif working_list[j][i] == "1":
            one_count+=1

    if zero_count <= one_count:
        for j in range(max_len):
            if working_list[j][i] == "0":
                clean_list_zeros.append(working_list[j])
    else:
        for j in range(max_len):
            if working_list[j][i] == "1":
                clean_list_zeros.append(working_list[j])
    working_list = clean_list_zeros.copy()
    clean_list_zeros = []

co2_scrubber_bin = working_list[0]

## Done!

print("co2_scrubber_bin = {}, o2_generator_bin = {}".format(co2_scrubber_bin, o2_generator_bin))

o2_generator = int(o2_generator_bin, 2)
co2_scrubber = int(co2_scrubber_bin, 2)

print("co2_scrubber = {}, o2_generator = {}".format(co2_scrubber, o2_generator))
print("co2_scrubber * o2_generator = {}".format(co2_scrubber * o2_generator))
