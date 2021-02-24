#This HW4PS2
#Marco Chavez
#StudentID 913519
#CS 10

def main():
    abbrv_dict = file_to_dict("textabbv.txt")
    print("Enter a message to be translated: ")
    translated = str(input())
    print("The Translated text is: ")
    print(trans_text(abbr_dict, translated)

def file_to_dict(filename):
    dictionary = {}
    open_file = open(filename, "r")
    for line in open file:
        pair = line.split(":")
        dictionary[pair[0]] = pair[1].rstrip()
    open_file.close()
    return dictonary

def trans_abbrv(dictionary, abbrev)
    last_character = abbrev[-1]
    if last_character in "?.!,:":
        abbrev = abbrev.rstrip(last_character)
    else:
          last_character = ""
    if abbrev in dictionary:
        word = dictionary[abbrev]
    else:
          word = abbrev
    return word + last_character

def trans_text(dictionary, text):
    output_trans = ""
    for line in text.split():
        output_trans += trans_abbrv(dictionary, line) + " "
    return output_trans


main()
    
        
