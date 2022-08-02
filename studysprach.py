#!/usr/bin/env python3
# Command-line based vocab practice tool
#
# Basic flash card deck for English/German practice.
import json
import random

from os.path import exists
from os import getcwd, stat, system
from pathlib import Path
from time import sleep


def main():
    selection = ""
    deck = Flash_Cards()

    while selection != "quit":
        selection = deck.menu()

        if selection == "practice":
            deck.practice()
        elif selection == "add":
            deck.add()
            deck.save_dictionary()
        elif selection == "remove":
            deck.remove()
            deck.save_dictionary()
        elif selection == "show":
            deck.show()
        else:
            deck.save_dictionary()
            print("Good studying!")
            return


class Flash_Cards:
    """
    Flash_Cards represents a deck of flash cards from English to German
    It saves the state to the disk as dictionary.json
    """

    def __init__(self):
        dictionary_directory = 'data'
        dictionary_file = 'dictionary.json'
        self.dictionary_path = Path(dictionary_directory, dictionary_file)

        self.dictionary = dict()
        self.load_dictionary()

    def add(self):
        """Add word pairs to deck"""
        another = 'y'
        while another == 'y':
            print("What word to add? ", end="")
            word = input()
            print("What is its pair? ", end="")
            pair = input()
            self.dictionary[word] = pair
            print("Another pair? ", end="")
            another = input().lower()[0]

    def remove(self):
        """Remove word pairs from deck"""
        another = 'y'
        print("Here are the words: ")
        self.show()

        while another == 'y':
            print("Which to remove? (use English) ", end="")
            key = input()
            if key in self.dictionary:
                self.dictionary.pop(key)
            print("Remove another? ", end="")
            another = input().lower()[0]

    def show(self):
        """Show a list of word pairs"""
        print()
        for key in self.dictionary:
            print(f"{key} - {self.dictionary[key]}")
        print()

    def practice(self):
        """Practice translating from English to German"""
        stop = ''
        while stop != 'q':
            system('clear')
            english, german = random.choice(list(self.dictionary.items()))
            print("Frage ('quit now' to quit): ")
            print(f"Übersetzung für \"{english}\"? ", end="")
            answer = input()
            if answer == german:
                print("Sehr gut!")
            elif answer.lower() == 'quit now':
                break
            else:
                print(f"Falsch! Das Richtige ist \"{german}\"")
            sleep(2)

    def save_dictionary(self):
        """Save a copy of the deck to disk"""

        with open(self.dictionary_path, 'w') as save_file:
            json.dump(self.dictionary, save_file)

    def load_dictionary(self):
        """Load a copy of the deck from disk"""
        if exists(self.dictionary_path) and stat(self.dictionary_path).st_size != 0:
            with open(self.dictionary_path, 'r') as load_file:
                self.dictionary = json.load(load_file)

    def menu(self):
        """Display menu of possible options"""
        print("1) Practice vocab")
        print("2) Add vocab")
        print("3) Remove vocab")
        print("4) Show vocab")
        print("5) Quit")
        print("Selection? ", end="")

        selection = input()

        if selection == "1":
            return "practice"
        elif selection == "2":
            return "add"
        elif selection == "3":
            return "remove"
        elif selection == "4":
            return "show"
        elif selection == "5":
            return "quit"
        else:
            print("Not a valid selection")


if __name__ == "__main__":
    main()
