#  assign var x with formatter
x = "There are %d types of people." % 10
# set var binary
binary = "binary"
# set var do_not
do_not = "don't"
# set var y
y = "Those who know %s and those who %s." % (binary, do_not)

# print both vars
print x
print y

# print out statements incorporating other vars 
print "I said: %r." % x
print "I also said: '%s'." % y

# set 2 new vars
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# print vars
print joke_evaluation % hilarious

# set vars
w = "This is the left side of..."
e = "a string with a right side"

#print concatenated strings
print w + e