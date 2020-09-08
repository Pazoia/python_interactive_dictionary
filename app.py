import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]

    if w.title() in data:
        return data[w.title()]

    if w.upper() in data:
        return data[w.upper()]

    if len(get_close_matches(w, data.keys())) > 0:
        closest_match = get_close_matches(w, data.keys(), cutoff=0.8)[0]
        user_choice = input("Word not recognised, did you mean %s? Enter Y if yes, or N if no: " % closest_match).upper()
        if user_choice == "Y":
            print(f"Word: {closest_match}")
            return data[closest_match]
        elif user_choice == "N":
            return "This word does not exist!!! Please restart and try again."
        else:
            return "We didn't understand your entry!"
    else:
        return "This word does not exist!!!"

word = input("Enter a word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
