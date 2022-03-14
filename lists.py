

friends = ["ayush", "nishant", "sagar", "adi", "pratik", "shardul", "ritesh"]
num = [4, 12, 78, 32 ,23, 13]
friends.extend(num)
# mergers two lists
friends.append("om")
# adds item at the end of list
friends.insert(3, "om")
# adds item at the specfic index
friends.remove("om")
# removes the item
friends.clear()
# clear the whole list
friends.pop()
# removes the last itam from the list

print(friends.index("adi"))
print(friends.count("adi"))
# counts the items with same value

num.sort()
print(num) [4, 12, 13, 23, 32, 78]
num.reverse()
print(num) [13, 23, 32, 78, 12, 4]

friends_two = friends.copy()
print(friends_two)
# copy the exatly the same list
