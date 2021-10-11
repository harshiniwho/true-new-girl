import pandas as pd
import numpy as np
from numpy import genfromtxt
import json

def test_gen_data():
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    return a


def write_to_file(data):
    print(data)
    with open('test.csv', 'wb') as f:
        np.savetxt(f, data, delimiter=",")


def read_from_file():
    data = genfromtxt('test.csv', delimiter=',')
    print(data)


def test_gen_dict():
    a ={'a' : 1, 'b': 2, 'c': 3}
    b ={'a' : 2, 'b': 3, 'c': 4}
    c ={'a' : 3, 'b': 4, 'c': 5}
    d ={'a' : 4, 'b': 5, 'c': 6}
    l = [a, b, c, d]
    return l


def write_dict_jsons(data):
    with open('test.json', 'w') as f:
        json.dump(data, f)


def read_dict_jsons():
    with open('test.json', 'r') as f:
        data = json.load(f)
        print(len(data))
        print(type(data))
        print(data)
 

def main():
    # write_to_file(test_gen_data())
    # read_from_file()
    write_dict_jsons(test_gen_dict())
    read_dict_jsons()


if __name__ == "__main__":
    main()