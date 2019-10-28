#!/usr/bin/env python3
# coding: utf-8

' OOP sample '

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def print(self):
        print('%s: %s' % (self.name, self.score))

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

if __name__ == '__main__':
    bart = Student('Bart', 59)
    lisa = Student('Lisa', 87)
    bart.print()
    lisa.print()

    dog = Dog()
    dog.run()

    cat = Cat()
    cat.run()