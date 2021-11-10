import names
import random
from person import Person

class Users:
    def __init__(self, num_people=2):
        self.users = []
        for _ in range(num_people):
            name = names.get_full_name()
            self.users.append(Person(name, len(self.users)))

    def create_initial_users(self, name):
        p = Person(name, len(self.users))
        self.users.append(p)

    def get_users(self):
        return self.users
    
    def print_users(self):
        for i in self.users:
            print("ID: {}, {}: Friends: {}".format(i.id, i.name, len(i.friends)))

    def print_friends(self):
        user_id = input("Enter ID of the user to view their friend list:\n")
        while not user_id.isnumeric() or int(user_id) not in [x.id for x in self.users]:
            user_id = input("'{}' not recognized or ID not found. Must input a number of users (1, 2, 3, etc.)\n".format(user_id))

        user = self.users[int(user_id)]
        for friend in user.friends:
            print(friend.name)

    def remove_friend(self, user, friend):
        if friend in self.users:
            self.users.remove(friend)
            friend.friends.remove(user)

    def create_additional_users(self):
        newUsers = input("How many new users?\n")
        while not newUsers.isnumeric():
            newUsers = input("'{}' not recognized. Must input a number of users (1, 2, 3, etc.)\n".format(newUsers))
        newUsers = int(newUsers)

        for _ in range(newUsers):
            name = names.get_full_name()
            self.create_initial_users(name)
            print("Added user {}".format(name))

    def cycle(self):
        cycle_count = input("How many cycles?\n")
        while not cycle_count.isnumeric():
            cycle_count = input("'{}' not recognized. Must input a number of users (1, 2, 3, etc.)\n".format(cycle_count))
        cycle_count = int(cycle_count)

        def check_friend(user, friend):
            if friend not in self.users or friend == user or friend in user.friends:
                return False
            return True
        for _ in range(cycle_count):
            for user in self.users:
                if user.traits["Outgoing"] > random.randint(0,9) and user.traits["Friendly"] > random.randint(2, 8):
                    for _ in range(0, random.randint(0, len(user.friends) // 2)):
                        friend = self.users[random.randint(0, len(self.users)-1)]
                        if check_friend(user, friend) and friend.traits["Friendly"] > random.randint(0, 5):
                            user.friends.append(friend)
                            friend.friends.append(user)
            
            # IF NOT OUTGOING AND NOT FRIENDLY, OR EXTREMES OF EITHER, CHANCE TO REMOVE FRIENDS.
            # else:

            #     for i in range(0, random.randint(1, len(user.friends) // 2)):
            #         if check_friend(user, users[i]) and users[i].traits["Friendly"] > random.randint(0, 5):
            #             user.friends.append(users[i])
            #             users[i].friends.append(user)

    def traits(self):
        user_id = input("Enter ID of the user to view their traits:\n")
        while not user_id.isnumeric() or int(user_id) not in [x.id for x in self.users]:
            user_id = input("'{}' not recognized or ID not found. Must input a number of users (1, 2, 3, etc.)\n".format(user_id))

        user = self.users[int(user_id)]
        
        for trait in user.traits:
            print("{}: {}".format(trait, user.traits[trait]))