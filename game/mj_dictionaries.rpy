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
        "name": "John",
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
    tuple1 = ("MJ", "Escalona", 21, True)
    tuple2 = ("JM", 89, 88, 90, 95, True, True, False)