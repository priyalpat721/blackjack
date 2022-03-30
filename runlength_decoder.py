"""
   CS5001
   Fall 2020
   Priyal Patel
   Homework 4: RunLength_Decoder

   A program that takes in a list of lists(data) and decodes the information
   stored in each list. The result is then converted to a string and printed
"""
from hw4data import *

DATA = [DATA0, DATA1, DATA2, DATA3, DATA4, DATA5]


def main():
    for i in range(0, 6):
        data_list = DATA[i].copy()
        decoded_list = decode(data_list)
        list_to_string(decoded_list)


def decode(data_list: list) -> list:
    """
    Takes in a list and decodes the data
    Parameters:
        data_list(list): copied list from original list
    Return:
        decoded_list(list): new list with decoded data
    """

    length_str_list = len(data_list)
    decoded_list = []

    for i in range(0, length_str_list, 2):
        decoded_list.append(data_list[i] * data_list[i + 1])
    return decoded_list


def list_to_string(decoded_list: list):
    """
    Takes in the decoded list and converts to string
    Parameters:
        decoded_list(list): created in decode()
    Return:
        None
    """
    data_string = ' '
    for char in decoded_list:
        data_string += char
    print(data_string)


if __name__ == "__main__":
    main()
