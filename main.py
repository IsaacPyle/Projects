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

# Add friendships depending on the population size
allUsers.cycle(population_size)

print("Initial Population:\n"
      "Users: {}\n"
      "Average number of Friends: {}\n"
      "Type '?' or 'help' for a list of commands.\n".format(len(allUsers.users), sum(len(x) for x in allUsers.users.friends)))

# Print all persons initially in the Network (COMMENTED DUE TO LARGE SIZES PRINTING TOO MUCH)
# print("Initial Population:")
# allUsers.print_users()

# Initialize with empty command
command = ""

cmd_list = ["q", "quit","?", "help", "users", "add users", "friends", "cycle", "traits"]

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
                "'friends' -> List the friends of a particular user.\n"
                "'traits' -> List the traits of a particular user")
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

    elif command == "traits":
        allUsers.traits()
        continue