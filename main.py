import random
import names

users = []

class Person:
    def __init__(self, name):
        self.traits = {"Outgoing": random.randint(0, 10), "Friendly": random.randint(0, 10)}
        self.name = name
        self.friends = []
        self.id = len(users)

    def add_friend(self, friend):
        self.friends.append(friend)

    def remove_friend(self, friend):
        if friend in users:
            self.friends.remove(friend)
            friend.friends.remove(self)

    def get_name(self):
        return self.name

class AddUser:
    def __init__(self, num_people=2):
        for _ in range(num_people):
            name = names.get_full_name()
            users.append(Person(name))

    def add_user(self, name):
        p = Person(name)
        users.append(p)


class Cmds():
    def help(self):
        print("Available commands:\n"
                "'q', 'quit' -> Exit the simulation.\n"
                "'?', 'help' -> List available commands.\n"
                "'users' -> List users in the Social Network.\n"
                "'add users' -> Add user(s) to the Social Network.\n"
                "'cycle' -> Run one iteration of adding new users and friends.\n"
                "'friends' -> List the friends of a particular user.\n")

    def users(self):
        for i in users:
            print("ID: {}, {}: Friends: {}".format(i.id, i.name, len(i.friends)))

    def add(self):
        newUsers = input("How many new users?\n")
        while not newUsers.isnumeric():
            newUsers = input("'{}' not recognized. Must input a number of users (1, 2, 3, etc.)\n".format(newUsers))
        newUsers = int(newUsers)

        for _ in range(newUsers):
            name = names.get_full_name()
            initUsers.add_user(name)
            print("Added user {}".format(name))

    def print_friends(self):
        user_id = input("Enter ID of the user to view their friend list:\n")


        while not user_id.isnumeric() or int(user_id) not in [x.id for x in users]:
            user_id = input("'{}' not recognized or ID not found. Must input a number of users (1, 2, 3, etc.)\n".format(user_id))

        user = users[int(user_id)]
        for friend in user.friends:
            print(friend.name)

    def cycle(self):
        def check_friend(user, friend):
            if friend not in users or friend == user or friend in user.friends:
                return False
            return True

        for user in users:
            if user.traits["Outgoing"] > random.randint(0,9) and user.traits["Friendly"] > random.randint(2, 8):
                for _ in range(0, random.randint(0, len(user.friends) // 2)):
                    friend = users[random.randint(0, len(users)-1)]
                    if check_friend(user, friend) and friend.traits["Friendly"] > random.randint(0, 5):
                        user.friends.append(friend)
                        friend.friends.append(user)
            
            # IF NOT OUTGOING AND NOT FRIENDLY, OR EXTREMES OF EITHER, CHANCE TO REMOVE FRIENDS.
            # else:

            #     for i in range(0, random.randint(1, len(user.friends) // 2)):
            #         if check_friend(user, users[i]) and users[i].traits["Friendly"] > random.randint(0, 5):
            #             user.friends.append(users[i])
            #             users[i].friends.append(user)


# Initial number of people in the network

initial_count = input("How many starting users?\n")
while not initial_count.isnumeric():
    initial_count = input("'{}' not recognized. Must input a number of users (1, 2, 3, etc.)\n".format(initial_count))
initial_count = int(initial_count)

initUsers = AddUser(initial_count)
cmd = Cmds()

# Initialize a size of population, to be updated later
population_size = initial_count

# Set a random number of friends for each user
for user in range(population_size):
    numFriends = random.randint(0, population_size-1 // 3)
    for friend in range(numFriends):
        if len(users[user].friends) == population_size - 1:
            continue
        friend_id = random.randint(0, population_size-1)
        while users[friend_id] == users[user] or users[friend_id] in users[user].friends:
            friend_id = random.randint(0, population_size-1)

        if friend_id not in users[user].friends and user not in users[friend_id].friends:
            users[user].add_friend(users[friend_id])
            users[friend_id].add_friend(users[user])

# Print all persons, and their friends

print("Initial Population:")
cmd.users()

# Initialize with empty command
command = ""

cmd_list = ["q", "quit","?", "help", "users", "add users", "friends", "cycle"]

while command != "q" and command != "quit":
    command = input("\n>>>")

    while command not in cmd_list:
        command = input("Unknown command. Enter '?' or 'help' for a list of commands.\n>>>")
    
    # Main Command Options
    if command == "?" or command == "help":
        cmd.help()
        continue

    elif command == "users":
        cmd.users()
        continue

    elif command == "add users":
        cmd.add()
        population_size = len(users)
        continue

    elif command == "friends":
        cmd.print_friends()
        continue

    elif command == "cycle":
        cmd.cycle()
        population_size = len(users)
        continue