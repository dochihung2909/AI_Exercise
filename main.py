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
    for key in mydict.keys():
        print(key)


def print_dict_value(mydict):
    for value in mydict.values():
        print(value)


def print_dict_key_value(mydict):
    for key, value in mydict.items():
        print(key, value)


# cau 5
def print_sequence(a,b):
    for i,x in enumerate(a):
        print(x, b[i])

# cau 6a
def count_consonants_2(word):
    vowels = "AEIOUaeiou"
    sum = 0
    for w in word:
        if w in vowels:
            continue
        else:
            sum += 1
    print(sum)

# cau 6b
def count_consonants(word):
    vowels = "AEIOUaeiou"
    print(sum(1 for char in word if char.isalpha() and char not in vowels))

# cau 7
def print_a():
    for a in range(-2, 3):
        try:
            print(10/a)
        except ZeroDivisionError:
            print("can't divide by zero")


# cau 8
def print_tuples():
    names = ['Hoa', 'Lam', 'Nam']
    ages = [23,10,80]
    age_name_tuples = list(zip(ages, names))

    # Sort the list of tuples by age
    sorted_age_name = sorted(age_name_tuples, key=lambda x: x[0])
    print(sorted_age_name)


# cau 9
def read_file(filename):
    f = open(filename, 'r', encoding="utf8")
    print(f.read())
    f.close()


# Define a function
# Cau 1
def sum_number(a,b):
    return a + b


# Cau 2
def print_matrix():

    # Creating a NumPy array 'x' using arange() from 2 to 11 and reshaping it into a 3x3 matrix
    M = np.arange(1, 10).reshape(3, 3)
    list_v = [1,2,3]
    v = np.array(list_v)
    # Printing the resulting 3x3 matrix 'x'
    print(f'Matrix {M}')
    print(f'Vector {v}')

    # cau 3
    new_matrix = [[element + 3 for element in row] for row in M]
    new_matrix = np.array(new_matrix).reshape(3,3)
    print(new_matrix)


# cau 6
def plus_matrix():
    a = [10,15]
    b = [8,2]
    c = [1,2,3] # a-c will lead an error because it out of range
    a_matrix = np.array(a)
    b_matrix = np.array(b)
    result_add_np = a_matrix + b_matrix
    result_minus_np = a_matrix - b_matrix
    print(f'{a_matrix} + {b_matrix} = {result_add_np}')
    print(f'{a_matrix} - {b_matrix} = {result_minus_np}')

    # compute dot product of a and b
    dot_product_a_b = np.dot(a_matrix, b_matrix)
    print(f'Dot product of a, b = {dot_product_a_b}')


# cau 8
def check_matrix():
    A = [[2, 4, 9], [3, 6, 7]]
    matrix_A = np.array(A).reshape(2,3)
    rank_A = np.linalg.matrix_rank(matrix_A)
    value_7 = matrix_A[1][2] # this way can get the value 7 in A
    second_column_A = [row[1] for row in matrix_A]
    print(f'Matrix A = {matrix_A}')
    print(f'Rank A = {rank_A}')
    print(f'Second column A = {second_column_A}')


# Cau 9
def create_matrix():
    matrix = np.random.randint(-10, 11, size=(3,3))
    print(f'Random Matrix = \n{matrix}')

#     Cau 10 identify matrix
    identify_matrix = np.eye(3)
    print(f'Identify Matrix = \n{identify_matrix}')
# cau 11 a
    matrix_range = np.arange(1,10).reshape(3,3)
    print(f'Matrix in range(1,10) = \n{matrix_range}')
#     b
    matrix_range_forLoop = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(j + i*3 + 1)
        matrix_range_forLoop.append(row)
    print(f'Matrix in range(1,10) use for = \n{matrix_range_forLoop}')
# cau 12
    matrix_main_diagonal = np.diag([1,2,3])
    print(f'Matrix with main diagonal 1 2 3 = \n{matrix_main_diagonal}')


# cau 13
def calc_determinant():
    A = [[1, 1, 2], [2, 4, -3], [3, 6, -5]]
    matrix_A = np.array(A).reshape(3,3)
    determinant_A = np.linalg.det(matrix_A)
    print(f'Determinant of A = {determinant_A}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_name("Đỗ Chí Hưng")
    # print_odd()

    mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    # print_dict_key(mydict)

    courses = [131, 141, 142, 212]
    names = ['Maths', 'Physics', 'Chem', 'Bio']

    # print_sequence(names, courses)
    # count_consonants_2('jabbawocky')
    # print_tuples()
    # read_file(r'D:\2151053026_DoChiHung\firstname.txt')
    calc_determinant()