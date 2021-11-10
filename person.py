import random

class Person:
    def __init__(self, name, id):
        self.traits = {"Outgoing": random.randint(0, 10), "Friendly": random.randint(0, 10)}
        self.name = name
        self.friends = []
        self.id = id

    def add_friend(self, friend):
        self.friends.append(friend)