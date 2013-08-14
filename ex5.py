name = "Zed A. Shaw"
age = 35
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Lets's talk about %s." % name
print "He's %d inches tall." % height
print "That's %d cm in metric." % (height * 2.54)
print "He's %d pounds heavy" % weight
print "That's %d kg in metric." % (weight / 2.2)
print "Actually that's not too heavy."
print "He's got %s eyes and %r hair" % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)