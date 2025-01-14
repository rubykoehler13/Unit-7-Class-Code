"""
Name: Ruby Koehler
Date: 1/8/25
Topic: List methods
"""

my_list = [1,2,3,1,2]

num_of_twos = my_list.count(2)
print(num_of_twos) # prints '2' because there are TWO 2's
num_of_threes = my_list.count(3)
print(num_of_threes) # prints '1' because there is ONE 3

# add (append) item to list
my_list.append(4)
print(my_list) # prints my_list with a '4' at the end

my_list.append([5,6]) # 'my_list' is now [1,2,3,1,2,4], so adding [5,6]...
print(my_list) # will print [1,2,3,1,2,4,[5,6]] - not necessarily what we want

my_list.pop() # removes last item from list (undo)
# Without line 21, it would print '[1, 2, 3, 1, 2, 4, [5,6], 5, 6]'

# how to add both 5 and 6, not in a list?
my_list.extend([5,6]) # will now print 5 and 6 in the list, without brackets
print(my_list)

# sorting lists
my_list.sort() # modifies the list; goes smallest to largest numbers from left to right;
# returns None, not the list
print(my_list)

# can I store the sorted list in another variable?
new_list = [4,6,4,2,9,0,-5]
sorted_list = sorted(new_list)
print(sorted_list) # prints smallest to largest numbers from left to right
print(new_list) # prints original list, no modifications

random_words = ["galaxy", "apple", "forest", "dolphin", "breeze", "gallon", "canyon", "ember"]

print(sorted(random_words)) # prints the sorted list, but list unchanged
print(random_words.sort()) # COMMON MISTAKE - '.sort' returns None, not the list
print(random_words)

# remove first occurrence of an item
random_nums = [3,6,4,2,3,3,5,4]
random_nums.remove(4) # removes the FIRST occurrence of an item, not all of the occurrences
print(random_nums)

# remove item at specified index
random_nums.pop(4) # removes the 5th index because we previously (line 47) removed the 2nd index,
# meaning we skip that and now the 5th index, (3), is the 4th index
print(random_nums)

# pop without an argument removes the last item
random_nums.pop() # without previous modifications, this would just take off the last character,
# but since we have previous mods, it has taken off the 1st 4, 3rd 3, and now the last number, 4.
print(random_nums)

# insert item at specific location
random_nums.insert(1,4) # goes to the 1st index, shifts everything from the right of that,
# over to the right, then fills the space (1st index) with the new number, 4 in this case
print(random_nums)

# reverse
random_nums.reverse()
print(random_nums)