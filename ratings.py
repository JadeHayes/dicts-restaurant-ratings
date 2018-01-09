"""Restaurant rating lister."""

# put your code here
import sys

file_name = open(sys.argv[1])
ratings = {}

for line in file_name:
    line = line.rstrip().split(":")
    ratings[line[0]] = line[1]

ratings_lst = ratings.items()

for name, rating in sorted(ratings_lst):
    print "{} is rated at {}".format(name, rating)
