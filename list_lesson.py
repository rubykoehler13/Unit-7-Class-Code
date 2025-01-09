"""
Name: Ruby Koehler
Date: 12-20-24
Description: List creation and manipulation and traversal
"""

# list creation - use [ ]

list_of_numbers = [1,2,3,4,5,6,8]
print(list_of_numbers)

# lists are mutable - can be changed
list_of_numbers[6] = 7
print(list_of_numbers)

# can be extended
list_of_numbers.append(8)
print(list_of_numbers)

list_of_numbers.remove(1) # value not index
print(list_of_numbers)

list_of_letters = ["a","b","c","d","e","f"]

# make elements of a list into a string
letter_string = "".join(list_of_letters)
print(letter_string)
letter_string = "*".join(list_of_letters)
print(letter_string)

# make a string into a list
vowels = "aeiou"
vowel_list = vowels.split() #doesn't work as intended
print(vowel_list)

# make each vowel an element
vowel_list.clear()
print(vowel_list)
for letter in vowels:
    vowel_list.append(letter)
print(vowel_list)

# iterating through a list
for vowel in vowel_list:
    print(vowel)

rand_nums = [7,1,12,-18,38,34,19,56]
even_count = 0
for num in rand_nums:
    if num%2 == 0:
        even_count = even_count + 1
        print("even")

print(even_count)