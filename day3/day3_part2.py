#!/bin/env python3

f = open("input","r")
items = f.read().split('\n')
items.pop(-1)

chunked_items = [items[i:i+3] for i in range(0, len(items), 3)]

item_priority = {}
for x in range(26):
    item_priority[chr(x+97)] = x+1
    item_priority[chr(x+65)] = x+27

# break needs to be there because there's an unenumerated rule that you have to use the first dupe and not all dupes
dupe_items = []
for x in range(len(chunked_items)):
    for item in chunked_items[x][0]:
        if item in chunked_items[x][1]:
            if item in chunked_items[x][2]:
                dupe_items.append(item)
                break

priority_sum = 0
for x in dupe_items:
    priority_sum += item_priority[x]

print(priority_sum)
