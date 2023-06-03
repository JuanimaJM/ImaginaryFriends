# Dictionary is a collection of key-value pairs, where each key must be unique.

# I will just use python for example
init python:
# Example 1
# The Key1...3 are the keys and can't be change. The Value1...3 are the values of keys and they can be change
# The values are follower by (:) after the keys and put a comma after the values if there is a next key-value pairs
# To access the value, you need a key correspons to the value that you want to get
# The keys can be any data types as except for list, and values can be all data types
    ex1 = {
        "Key1" : "Value1",
        "Key2" : "Value2",
        "Key3" : "Value3",
    }

# Example of accessing the value
    val1 = ex1["Key1"]

# Example of changing the value
    ex1["Key2"] = 123456789

# Example of iterating the items of dictionary
    for key, value in ex1.items():
        keys = key
        values = value


# Example 2
# This example shows a different data types as keys
    ex2 = {
        "string_key": "This is a string",
        42: "This is an integer key",
        (1, 2): "This is a tuple key",
        3.1415: "This is a float key",
        True: "This is a boolean key"
    }

# Example 3
# This example shows a different data types as values
# The "name" is a String, the "age" is an integer, the "is_student" is a boolean
# The "grades" is a list of integer, the "interest" is a tuple of Strings, and the "address" is a nested dictionary
    ex3 = {
        "name": "Lourence",
        "age": 30,
        "is_student": True,
        "grades": [80, 85, 90],
        "interests": ("music", "movies", "sports"),
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip": "12345"
        }
    }

# Note 1
# The arrays uses square brackets and all their items should be the same data types
    arr1 = [1, 2, 3]
    arr2 = ["red", "yellow", "blue"]

# Note 2
# The list uses square brackets and their items can be different data types
    list1 = [8, "blue", True]
    list2 = ["Kim", "Kheem", 358, 888, True, False]

# Note 3
# The tuples uses parenthesis and their items can be diffrent data types
# Tuples items can't be change unlike list and arrays
    tuple1 = ("Kheem", "Beller", 21, True)
    tuple2 = ("KL", 89, 88, 90, 95, True, True, False)

"""
In Python, you can use various methods to modify the contents of lists, tuples, arrays, and dictionaries without reassigning them. 
Here are some common methods and techniques:

Lists:
list.extend(iterable): Appends elements from an iterable to the end of the list.
list += iterable or list.extend(iterable): Concatenates another iterable to the end of the list.
list.append(item): Appends a single item to the end of the list.
List comprehension: Allows you to create a new list by applying an operation to each element of an existing list.

Tuples:
Tuples are immutable in Python, meaning their elements cannot be modified. 
To change the contents, you would need to create a new tuple.

Arrays:
array.extend(iterable): Extends the array by appending elements from an iterable.
array.fromlist(list): Appends items from a list to the array.
array.frombytes(bytes): Appends items from a bytes object to the array.


Dictionaries:
dict.update(other_dict): Merges the keys and values from another dictionary into the current dictionary.
Dictionary comprehension: Allows you to create a new dictionary by applying an operation to each key-value pair of an existing dictionary.
"""

# Uses of >>>random<<<
init python:
# Generate a random integer between 0 and 9
    random_int = random.randint(0, 9)

# Generate a random float between 0.0 and 1.0
    random_float = random.random()

# Generate a random float between 1.0 and 10.0
    random_float_range = random.uniform(1.0, 10.0)

    my_list = [1, 2, 3, 4, 5]
# Choose a random element from the list
    random_element = random.choice(my_list)

# Shuffle the list randomly
    random.shuffle(my_list)

# Choose 3 random elements from the list without replacement
    random_sample = random.sample(my_list, 3)

    my_list = ['A', 'B', 'C']
# Choose a random element based on the provided weights
    random_weighted = random.choices(my_list, weights=[0.2, 0.3, 0.5])
