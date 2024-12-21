#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
from zmq.backend import first

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

all_names = []
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    for name in names:
        all_names.append(name.strip())

print(names)

for name in all_names:
    with open("./Input/Letters/starting_letter.txt", "r") as letter:
        content = letter.readlines()

        first_line = content[0]
        changed_first_line = first_line.replace("[name]", name)

        content[0] = changed_first_line
    with open(f"./Output/ReadyToSend/{name}.txt","w") as nameLetter:
        nameLetter.writelines(content)
