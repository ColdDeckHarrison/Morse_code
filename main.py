# # convert all string into morse code.
# user input will be put into a split list.
# for loop to find each letter and compare it with a dictionary
#     key: value will be letter: morse symbol
# convert each letter into the corresponding morse code symbol while ignoring spaces, symbols and numbers.
# return the new string with the correct morse code.

morse_dict = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
    "i": "..", "j": ".---", "k": "-.-", "l": ".-..","m": "--", "n": "-.", "o": "---", "p": ".--.",
    "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.", "10": "-----", " ": "|",
}
keep_coding = True

while keep_coding:
    user_input = input("give me number, sentence or word. Will return in Morse Code. No Symbols. ").lower()
    morse_list = []
    split = [char for char in user_input]
    for chars in split:
        values = morse_dict.get(chars)
        morse_list.append(values)
    string = " ".join(str(char) for char in morse_list)
    print(string)
    again = input("\n Would you like to try again? Y or N? ").lower()
    if again == "n":
        keep_coding = False

