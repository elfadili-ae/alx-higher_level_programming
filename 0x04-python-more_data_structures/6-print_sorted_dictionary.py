#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedDict = sorted(a_dictionary.keys())
    for key in sortedDict:
        print("{}: {}".format(key, a_dictionary[key]))
