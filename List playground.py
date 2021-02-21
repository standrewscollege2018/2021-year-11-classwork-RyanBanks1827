# For lists we use square brackets
# Items must be split by comma
Items = ["Item1", "Item2"]

print(Items[0])

# To add something to the end of a list, use append()
Items.append("Dr Evil")

# To add something directly into a list, use the Items.insert() or list.insert()

Items.insert(1, "Dr good")

# Lists are mutable, they can be written to and deleted from
# You can override a value of an item in the list, like this!
Items[1]= "Not any doctor here!"
print(Items)
