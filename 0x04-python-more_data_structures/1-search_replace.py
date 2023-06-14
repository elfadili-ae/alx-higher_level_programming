#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = list(map(lambda x: x, my_list))
    for i in range(len(newList)):
        newList[i] = replace if newList[i] == search else newList[i]
    return newList
