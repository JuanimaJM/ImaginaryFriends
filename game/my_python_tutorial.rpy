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


# Scripts Tutorial
define Anna = Character("Anna Lisa", color="#00ffff")
define Alex = Character("Alex Gonzafa", color="#00ff00")

label script_tutorial:
    Anna "Hello, nice to meet you [Alex.name]" #outputs: Hello, nice to meet you Alex Gonzaga
    Alex "Nice to meet you too, Anna"

    "Once upon a time."
    "There was a boy who loves to eat apples."

    Anna "Uwu, ILY, LOLOLOL."
    Alex "R u ok?"

    scene name_of_scene their_attribute

    scene backyard
    pause #---> this will let the player to view the scene without the dialogue and wait for them to click the screen
    
    scene bedroom day
    scene bedroom night

    hide bedroom #---> this will hide the bedroom scene, don't need to add their attribute. however hiding a scene will show a transparent background(checkered)
    # you need to show a new scene when a hiding the previous scene

    # define the video first
    image my_bg = Movie(play="filename.mp4")

    # displaying the video as background/scene
    show my_bg
    hide my_bg #---> hides the scene


    play music music_filename
    play sound sound_filename


    play music let_it_go
    play music let_it_go loop # make the music loops unless new music is played or it stopped
    play music let_it_go fadein 0.5 # sets fadein for .5seconds
    play music let_it_go volume 5.0 # sets volume for times 5
    play music let_it_go loop fadein 2.0 volume 3.0
    stop music #---> stops all music
    stop mudic fadeout 3.0

    play sound doorbell
    play sound doorbell loop
    play sound doorbell fadein 1.0
    play sound doorbell volume 10.0
    play sound doorbell loop fadein 0.5 volume 0.5
    stop sound
    stop sound fadeout 0.5

    "I will choose something"
    menu:
        "Option1":
            "Script of option 1 goes here"
        "Option2":
            "Script of option 2 goes here"
    "I already choose something"

label main_route:
    "1"
    call my_choice # proceed to my_choice 
    "..." # proceed here if the return is called in my_choice
    "Oh Im here again"

label my_choice:
    "I choose something"
    menu:
        "Yes":
            "Ok"
            jump second_route # proceed to second route
        "No":
            "Grrrr"
            return # go back to main route
    "....." # can't be shown

label second_route:
    "2"
    "3"
    jump end_route # proceed to end route

label end_route:
    "ending"
    return # ends the game

label third_route:
    "999"
    "9999"
    "99999"

label start_of_loop:
    "Starting the Loop"
    call the_loop
    "Ending the loop"
    return # end the game

label the_loop:
    menu:
        "Loop Again":
            "Again.."
            call the_loop
        "End the loop":
            return # return to start_of_loop
        