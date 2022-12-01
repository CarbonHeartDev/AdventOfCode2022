"""Calorie calculator"""

import functools

def top(input_filename):
    """Find the elf with more calories and how much calories he carries"""
    top_elf = functools.reduce(
        lambda a,b : a if a[1] > b[1] else b,
        ElfIterator(input_filename),
        (0,0))

    return top_elf if top_elf != (0,0) else None

def top3(input_filename):
    """Find the three elves with more calories and how much calories are carried by each"""

    top3_carriers = []

    for elf in ElfIterator(input_filename):
        top3_carriers.append(elf)
        top3_carriers.sort(key= lambda a : a[1], reverse=True)
        top3_carriers = top3_carriers[0:3]

    return top3_carriers

class ElfIterator:
    """Reads line by line a file with the calories of the food items carried by each elf
    and iterates the totals"""

    def __init__(self, file_name):
        self.file_name = file_name

        self.elf_number = None
        self.file_object = None

    def __iter__(self):
        self.elf_number = 0
        self.file_object = open(self.file_name, "r", encoding="utf8")
        return self

    def __next__(self):

        self.elf_number += 1
        current_calories = 0

        while True:
            current_line = self.file_object.readline()

            if current_line == "" and current_calories == 0:
                self.file_object.close()
                raise StopIteration()
            elif current_line == "\n" or current_line == "":
                return (self.elf_number, current_calories)
            else:
                current_calories += int(current_line)

