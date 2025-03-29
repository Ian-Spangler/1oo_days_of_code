#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

cleaned_list = [name.strip() for name in name_list]

with open("./Input/Letters/starting_letter.txt", "r") as file:
    letter_format = file.read()
    for name in cleaned_list:
        letter = letter_format.replace("[name]",name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as file_2:
            file_2.write(letter)
