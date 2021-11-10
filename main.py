import random

from person import Person
from users import Users

# Initial number of people in the network
initial_count = input("How many starting users?\n")
while not initial_count.isnumeric():
    initial_count = input("'{}' not recognized. Must input a number of users (1, 2, 3, etc.)\n".format(initial_count))
initial_count = int(initial_count)

# Initialize users
allUsers = Users(initial_count)

# Initialize a size of population, to be updated later
population_size = initial_count

# Set a random number of friends for each user
for user in range(population_size):
    numFriends = random.randint(0, population_size-1 // 3)
    for friend in range(numFriends):
        if len(allUsers.get_users()[user].friends) == population_size - 1:
            continue
        friend_id = random.randint(0, population_size-1)
        while allUsers.get_users()[friend_id] == allUsers.get_users()[user] or allUsers.get_users()[friend_id] in allUsers.get_users()[user].friends:
            friend_id = random.randint(0, population_size-1)

        if friend_id not in allUsers.get_users()[user].friends and user not in allUsers.get_users()[friend_id].friends:
            allUsers.get_users()[user].add_friend(allUsers.get_users()[friend_id])
            allUsers.get_users()[friend_id].add_friend(allUsers.get_users()[user])

# Print all persons initially in the Network
print("Initial Population:")
allUsers.print_users()

# Initialize with empty command
command = ""

cmd_list = ["q", "quit","?", "help", "users", "add users", "friends", "cycle"]

# Main loop, which runs while the user continues entering commands other than 'q' and 'quit'.
while command != "q" and command != "quit":
    command = input("\n>>>")

    while command not in cmd_list:
        command = input("Unknown command. Enter '?' or 'help' for a list of commands.\n>>>")
    
    # Main Command Options
    if command == "?" or command == "help":
        print("Available commands:\n"
                "'q', 'quit' -> Exit the simulation.\n"
                "'?', 'help' -> List available commands.\n"
                "'users' -> List users in the Social Network.\n"
                "'add users' -> Add user(s) to the Social Network.\n"
                "'cycle' -> Run one iteration of adding new users and friends.\n"
                "'friends' -> List the friends of a particular user.\n")
        continue

    elif command == "users":
        allUsers.print_users()
        continue

    elif command == "add users":
        allUsers.create_additional_users()
        population_size = len(allUsers.get_users())
        continue

    elif command == "friends":
        allUsers.print_friends()
        continue

    elif command == "cycle":
        allUsers.cycle()
        population_size = len(allUsers.get_users())
        continue