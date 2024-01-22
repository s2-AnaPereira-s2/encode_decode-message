#encode a message by shifting the letter by a given number

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def encode(shift_number):
    message = input("what is the message?\n").lower()
    code_message = []
    """this is to add the spaces containing in the message and then add the shifting number to the letter index to get the new letter"""
    for letter in message:
        if letter == " ":
            code_message.append(" ")
        elif letter.isalnum() == False or letter.isnumeric() == True:
            code_message.append(letter)
        elif letter:
            """I had to specify the max index to prevent the index out of range error and start the list again"""
            max_index = len(alphabet) - 1
            index_new_letter = (alphabet.index(letter)+shift_number)
            if index_new_letter <= max_index:
                new_letter = alphabet[index_new_letter]
                code_message.append(new_letter)
            elif index_new_letter > max_index:
                index_new_letter -= len(alphabet) 
                new_letter1 = alphabet[index_new_letter]
                code_message.append(new_letter1)    
     
    print(f'Your encode message is: {"".join(code_message)}')
    
def decode(shift_number):
    message = input("what is the message?\n").lower()
    decode_message = []
    for letter in message:
        if letter == " ":
            decode_message.append(" ")
        elif letter.isnumeric() == True or letter.isalnum() == False:
            decode_message.append(letter)
        else:
            original_letter = alphabet[alphabet.index(letter)-shift_number]
            decode_message.append(original_letter)
        
    print(f'The message is: {"".join(decode_message)}')


while True:
    try:
        print("Hello\n")
        choice = int(input("choose an option:\n1: encode\n2: decode\n"))

        match choice:

            case 1:
                shift_number = int(input("Please provide the shifting number:\n"))
                encode(shift_number)
                break
            
            case 2:
                shift_number = int(input("Please provide the shifting number:\n"))
                decode(shift_number)
                break
    except ValueError:
        print("Invalid input")






