#this is HW4PS2
#Marco Chavez
#Student ID 913519
#CS 10
import string

def main():
    text = create_textLang()
    translate = input("Enter a message to be translated: ")
    #print("The translated text is: ", text[translate])
    toEnglish(text, translate)

def create_textLang():
    text = {"r":"are","y":"why", "u":"you", "ttyl":"talk to you later",
                    "l8":"late", "brb":"be right back", "lol":"laughing out loud",
                    "bbl":"be back later", "tldr":"too long didn't read",
                    "rofl":"rolling on floor laughing", "gtg":"got to go",
                    "cya":"see you", "cuzz":"because", "bff":"best friend forever",
                    "idk":"I don't know", "sup":"what's up?", "omg":"oh my gosh",
                    "nbd":"no big deal","tisnf":"this is not fair","nw":"no way!",
                    "rus":"are you serious?", "myob":"mind your own business","njoy":"enjoy",
                    "nter":"enter", "1ce":"once", "aka":"also known as", "afk":"away from keyboard",
                    "jk":"just kidding", "asap":"as soon as possible", "app":"application",
                    "atm":"at the moment", "b4":"before", "fyi":"for your information",
                    "bday":"birthday","k":"okay", "msg":"message", "np":"no problem",
                    "pic":"picture", "plz":"please", "sry":"sorry", "dunno":"don't know",
                    "wut":"what", "wuts":"what's"}
    return text

def toEnglish(text, translate):
    textTrans = translate.split()
    newSent = "The translated text is: "

    for translate in textTrans:
        if translate in text:
            newSent += text[translate] + " "
        else:
            newSent += translate + " "

    print(newSent)
    
        
main()
'''Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Enter a message to be translated: r u lol
The translated text is: are you laughing out loud 
>>> '''
