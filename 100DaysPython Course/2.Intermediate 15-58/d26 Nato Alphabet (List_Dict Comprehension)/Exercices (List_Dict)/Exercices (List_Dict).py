import random


def ex1():
    names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
    names_upper_CAP = [var.upper() for var in names if len(var) > 5]
    print(names_upper_CAP)


# square
def ex2():
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    squared_numbers = [(var**2) for var in numbers]
    print(squared_numbers)


# even
def ex3():
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    result = [var for var in numbers if ((var % 2) == 0)]
    print(result)

# use Files in list


def ex4():
    file1 = open("file1.txt")
    file2 = open("file2.txt")
    list1 = file1.readlines()
    list2 = file2.readlines()
    list1_o = [var.strip("\n") for var in list1]  # retirar os \n
    list2_o = [var.strip("\n") for var in list2]
    final = [var for var in list1_o if (var in list2_o)]
    print(final)


# list to dict
def ex5():
    names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
    dict_names = {var: random.randint(1, 101) for var in names}
    dict_names_passed = {key: value for (
        key, value) in dict_names.items() if value >= 60}
    print(dict_names_passed)


# dict that key = word and value = len
def ex6():
    sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
    dict_string = {var: len(var) for var in sentence.split(" ")}
    print(dict_string)


# dict of temperatures
def ex7():
    weather_c = {
        "Monday": 12,
        "Tuesday": 14,
        "Wednesday": 15,
        "Thursday": 14,
        "Friday": 21,
        "Saturday": 22,
        "Sunday": 24,
    }

    def celsius_to_fahrenheit(temp_c):
        return ((temp_c * 9/5) + 32)

    dict_weater = {key: celsius_to_fahrenheit(
        value) for (key, value) in weather_c.items()}
    print(dict_weater)




ex7()
