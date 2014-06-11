# Ex19.py: Functions and Variables

# define our function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses" % cheese_count
	print "You have %d boxes of crackers" % boxes_of_crackers
	print "Man, that's enough for a party!"
	print "Get a blanket.\n"


# call function and pass numbers as args
print "we can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# set variables, then call function and pass vars
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# call function and pass math as args
print "we can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# call function with math ans previously declared var
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)