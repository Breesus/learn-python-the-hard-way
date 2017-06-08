cars = 100
# How many cars
space_in_a_car = 4.0
# how many seats available
drivers = 30
# drivers available
passengers = 90
# how many passengers there are today
cars_not_driven = cars - drivers
# how mnay empty cars
cars_driven = drivers
# how many cars available
carpool_capacity = cars_driven * space_in_a_car
# how many people can travel
average_passengers_per_car = passengers / cars_driven
# how many people for each car

print
print "There are", cars, "cars available"
print "There only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "we can transsport", carpool_capacity, "people today"
print "we have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car"
