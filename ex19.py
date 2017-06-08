def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "you have %d cheese!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man thats enough for a party!"
    print "Get a blanket.\n"
# defining a function

print "We can just give the functions numbers directly:"
cheese_and_crackers(20, 30)
# call/run function with arguments 20, 30


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# variables to use in function

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# call function
# using variabless in function

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
# doing math with function


print "And we can combime the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# call function, using variables and math
