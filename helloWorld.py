import os
import sys
import pygame

def helpPrint():
    print("Hello World")

class Person:
    __age = 200
    __name = None

    def __init__(self, name):
        self.__name = name

    
    def hello(self):
        print(f"Hello! My name is {self.__name} and I am {self.__age}yo\n")


if __name__ == '__main__':
    print("Main function")
    helpPrint()

    person1 = Person("John")

    person1.hello()
