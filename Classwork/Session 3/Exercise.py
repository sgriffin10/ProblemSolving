#Exercises 

import datetime as dt

# 1.1
a = 3
a + 2
print(a)
# answer: a = 5

# 1.2
a = a + 1.0
a
#answer: a = 4

# 1.3
a = 3
b
# answer: b not defined

# 1.4
a = 3
a == 5.0
a 
# answer: False & a = 3

# 1.5
b = 10
c = b > 9
c 
# answer: c = True (c variable is a boolean)

# 1.6
5/2 == 5/2.0
# answer: True


#2. 

3.0 - 1.0 != 5.0 - 3.0 #false

3 > 4 or (2 < 3 and 9 > 10) #false

4 > 5 or 3 < 4 and 9 > 8 #true

not(4 > 3 and 100 > 6) #false

#3. 

print(dt.datetime.now()) #current time
 
epoch_date = dt.datetime(1970,1,1)
today_date = dt.datetime(2019,9,14)

today_date - epoch_date

#answer: days since epoch equals 18,153

