#Question 1: How many seconds are there in 42 minutes 42 seconds?


minutes = 42
seconds = 42

# print("The time duration is : ", minutes * 60 + seconds)

# Question 2 How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.

# 1 km = 1.61 miles
miles = 1.61

# print('There are ', miles * 10, ' miles in 10 kilometres ')

# Question 3: If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?

distance_km =  10
time_ran = minutes + (seconds/60)
pace = time_ran/distance_miles 

print('The average pace is: ', pace )
print('The average speed in miles per hour is: ', pace * 60)
