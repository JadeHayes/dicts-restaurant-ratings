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


def user_input():
    """gets restaurant and rating from user, adds to dictionary, calls print
    function"""

    user_restaurant = raw_input("What is the name of the restaurant? ").title()
    user_rating = raw_input("What is your rating for {}? ".format(user_restaurant))

    ratings[user_restaurant] = user_rating

    add_another = raw_input("Would you like to add another restaurant. 'Y' for "
                            "yes, 'N' for no. ")
    if add_another.upper() == "Y":
        user_input()

    return print_ratings(ratings)

user_input()
