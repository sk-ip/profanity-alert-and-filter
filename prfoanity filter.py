from profanity import profanity

def read_text():
    quotes = open("message.txt")
    contents_of_file = quotes.read()
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
        output = profanity.contains_profanity(text_to_check)
        if "True" in str(output):
            print("profanity alert!")
            print(profanity.censor(text_to_check))
        elif "False" in str(output):
            print("this document is good to go.")
        else:
            print("cannot scan the document properly.")


print("reading the text........")
read_text()

