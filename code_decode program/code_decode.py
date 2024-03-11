
from flask import Flask, render_template, request


code_decode = app = Flask(__name__, static_url_path='/static')


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


@code_decode.route("/")
def index():
    current_page = request.path
    return render_template("program.html", current_page=current_page)


@code_decode.route("/", methods=["POST", "GET"])
def get_info():
    
    choice = request.form.get("choice")
    if choice == "encode":
        return encode()
    if choice == "decode":
        return decode()
    if not choice:
        return decode()
              



@code_decode.route("/", methods=["POST", "GET"])
def encode():
    try:
        shift_number = int(request.form["shift_number"])
        message = request.form.get("message_in").lower()
        #if not message:
            #message = "123" 
        code_message = []

        for letter in message:
            if letter == " ":
                code_message.append(" ")
            elif letter.isalnum() == False or letter.isnumeric() == True:
                code_message.append(letter)
            elif letter:
                max_index = len(alphabet) - 1
                index_new_letter = (alphabet.index(letter)+shift_number)
                if index_new_letter <= max_index:
                    new_letter = alphabet[index_new_letter]
                    code_message.append(new_letter)
                elif index_new_letter > max_index:
                    index_new_letter -= len(alphabet) 
                    new_letter1 = alphabet[index_new_letter]
                    code_message.append(new_letter1)  

        message_out = "".join(code_message)  

        return render_template("program.html", message_out=message_out, message=message)
    except (ValueError, TypeError):
        return "Invalid input"


@code_decode.route("/", methods=["POST", "GET"])
def decode():
    try:
        shift_number = int(request.form["shift_number"])
        message = request.form.get("message_in").lower() 
        decode_message = []

        for letter in message:
            if letter == " ":
                decode_message.append(" ")
            elif letter.isnumeric() == True or letter.isalnum() == False:
                decode_message.append(letter)
            else:
                original_letter = alphabet[alphabet.index(letter)-shift_number]
                decode_message.append(original_letter)

        message_original = "".join(decode_message)

        return render_template("program.html", message_original=message_original, message=message)
    except (ValueError, TypeError):
        return "Invalid input"


if __name__ == "__main__":
    code_decode.run(host="127.0.0.1", port=5000, debug=True)

