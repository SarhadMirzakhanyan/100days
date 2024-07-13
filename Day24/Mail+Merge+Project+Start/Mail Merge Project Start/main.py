# TODO: Create a letter using starting_letter.txt 
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as start_letter:
    with open("./Input/Names/invited_names.txt") as names_file:
        names = names_file.readlines()
        starting_letter = start_letter.read()
        for name in names:
            with open(f"./Output/ReadyToSend/{name}-letter.txt", "w") as out_letter:
                text_to_write = starting_letter.replace("[name]", name.strip()  )
                # print(f"Writing to the letter file:\n {text_to_write}")
                out_letter.write(text_to_write)

