import math
from datetime import timedelta

##  Question 1 : # What is the volume of a sphere with radius 5?
pi = math.pi
radius = 5

Volume = (4/3)*pi*(radius**3)
print('The Volume of the sphere is {:.2f}'.format(Volume))

# Question 2 : Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

cover_price = 24.95
discount_cost = cover_price * 0.6
copies = 60
book_costs = discount_cost * copies
shipping_costs = 3 + (copies-1)*0.75
total_costs = book_costs + shipping_costs

print('The total cost of the books is ${:.2f}'.format(total_costs))

# Question 3: If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

a = timedelta(0,0,0,0,52,6,0)
easy_pace = timedelta(minutes=8, seconds=15)
fast_pace = timedelta(minutes=7, seconds=12)
combined_run_time = (easy_pace * 2) + (fast_pace * 3)
# print(combined_run_time)

b = a + combined_run_time
print('The time you arrive back home is', b)



# If my average grade rises from 82 to 89. What is the percentage of the increase? Format the result as 'xx.x%'. Keep one figure after decimal point.

beg_grade = 82
end_grade = 89

increase = (end_grade-beg_grade)/beg_grade * 100

print('The grade rose by {:04.1f}%.'.format(increase))

print('hello')