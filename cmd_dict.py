"""
author: Jason Cheung
description: A command-line dictionary with word-suggestions from difflib 
             and json data handling from json library
"""

import json
from difflib import get_close_matches
 
"""
Loads json data file of words and their definitions
"""
def load_json():
    data = json.load(open("data.json"))
    return data

"""
Checks if there is a similar word in the dataset 
for an incorrect input and offers it if available
"""
def check_sim(data, search):
    suggestion = get_close_matches(search, data.keys())
    if len(suggestion) > 0:
        print(f"Did you mean '{suggestion[0]}'?")
        response = input("y/n: ").lower()
        if response == "y":
            return data[suggestion[0]]
        else:
            return "bad"


"""
Asks user to search a word and displays 
appropriate response
"""
def prompt(data):
    search = input("Enter a word (/quit to exit): ").lower()
    if search in data.keys():
        return data[search]
    elif search == "/quit":
        return "/quit"
    else:
        print("Word not found.")
        return check_sim(data, search)

"""
Runs all functions when program is executed
"""
def main():
    data = load_json()
    while True:
        query = prompt(data)
        if query == "/quit":
            break
        elif query == None or query == "bad":
            continue
        else:
            print()
            for definition in query:
                print(f"- {definition}")
            print()


main()