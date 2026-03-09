#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open ("Input/Letters/starting_letter.txt") as opening_letter_file:
    opening_letter_txt = opening_letter_file.read()

with open ("Input/Names/invited_names.txt", "r") as invited_names_file:
    invited_names_txt = invited_names_file.readlines()

for name in invited_names_txt:
    invited_attende_name = name.strip('\n')
    letter_to_send = opening_letter_txt.replace("[name]", invited_attende_name)
    with open (f"Output/ReadyToSend/{invited_attende_name}.txt", "w") as output_letter_name_file:
        output_letter_name_file.write(letter_to_send)