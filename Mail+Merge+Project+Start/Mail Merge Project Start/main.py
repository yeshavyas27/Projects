with open("./Input/Letters/starting_letter.txt") as start_letter:
    data = start_letter.readlines()

with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()
first_line = data[0]

i = 0
for name in name_list:
    with open(f"./Output/ReadyToSend/letter{i}.txt", mode="w") as final_letter:
        final_name = name.strip('\n')
        final_line = first_line.replace("[Name]", f"{final_name}")
        data[0] = final_line
        final = ''.join(data)
        final_letter.write(final)

    i += 1






























