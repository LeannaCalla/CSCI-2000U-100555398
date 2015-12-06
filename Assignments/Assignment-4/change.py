f = open("Source_data_for_CFR_vaccine_map_abridged.csv")
f2 = open("Source_data_for_CFR_vaccine_map_abridged_2.csv", "w")

for line in f:
    for char in line:
        if char != '"':
            f2.write(char)

