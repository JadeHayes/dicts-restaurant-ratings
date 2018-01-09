"""Restaurant rating lister."""

# put your code here
import sys

file_name = open(sys.argv[1])
ratings = {}

for line in file_name:
    line = line.rstrip().split(":")
    ratings[line[0]] = line[1]


def print_ratings(ratings):
    """turns dictionary into list of tuples and prints contents"""
    print "\n"
    ratings_lst = ratings.items()
    for name, rating in sorted(ratings_lst):
        print "{} is rated at {}".format(name, rating)

# call function to create dictionary with ratings
# ask user for new restaurant and ratings
# call function with users input
# print


def add_to_ratings():
    """gets restaurant and rating from user, adds to dictionary, calls print
    function"""

    user_restaurant = raw_input("What is the name of the restaurant? ").title()
    validate_rating = True

    while validate_rating:
        user_rating = int(raw_input("Rate {} between 1 and 5: ".format(user_restaurant)))
        if user_rating > 0 and user_rating <= 5:
            ratings[user_restaurant] = user_rating
            validate_rating = False
        else:
            print "Please try again with a rating between 1 and 5. "

    add_another = raw_input("Would you like to add another restaurant. 'Y' for "
                            "yes, 'N' for no. ")
    if add_another.upper() == "Y":
        add_to_ratings()

    return ratings


def prompt_user():
    print "\nWhat would you like to do?"
    user_selection = raw_input("A: view ratings \nB: add ratings \nQ: quit program\n").upper()

    if user_selection == 'Q':
        return
    elif user_selection == 'A':
        print_ratings(ratings)
    elif user_selection == 'B':
        add_to_ratings()
    prompt_user()

prompt_user()
