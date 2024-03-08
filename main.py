# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np


def print_name(name):
    # Use a breakpoint in the code line below to debug your script.
    for a in name:
        print(a)


def print_odd():
    for i in range(1, 10):
        if i & 1 > 0:
            print(i)


def sum_from_range(a, b):
    total = 0
    for i in range(a, b):
        total += i
    print(total)


def print_dict_key(mydict):
    for key, value in mydict.items():
        print(key)


def print_dict_value(mydict):
    for key, value in mydict.items():
        print(value)


def print_dict_key_value(mydict):
    for key, value in mydict.items():
        print(key, value)


def print_sequence(a,b):
    for i,x in enumerate(a):
        print(x, b[i])


def count_consonants(word):
    vowels = "AEIOUaeiou"
    print(sum(1 for char in word if char.isalpha() and char not in vowels))


def print_a():
    for a in range(-2, 3):
        try:
            print(10/a)
        except ZeroDivisionError:
            print("can't divide by zero")


def print_tuples():
    names = ['Hoa', 'Lam', 'Nam']
    ages = [23,10,80]


def read_file(filename):
    f = open(filename, 'r', encoding="utf8")
    print(f.read())
    f.close()


def sum_number(a,b):
    return a + b


def print_matrix():

    # Creating a NumPy array 'x' using arange() from 2 to 11 and reshaping it into a 3x3 matrix
    x = np.arange(2, 11).reshape(3, 3)

    # Printing the resulting 3x3 matrix 'x'
    print(x)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_name("Đỗ Chí Hưng")
    # print_odd()

    mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    # print_dict_key(mydict)

    courses = [131, 141, 142, 212]
    names = ['Maths', 'Physics', 'Chem', 'Bio']

    # print_sequence(names, courses)
    # count_consonants('jabbawocky')

    # read_file(r'D:\2151053026_DoChiHung\firstname.txt')
    print_matrix()