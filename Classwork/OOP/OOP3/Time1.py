class Time:
    """
    Represents the time of the day. 

    attributes: hour, minute, second

    """

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """
        return a time object in a human-readable format

        text representation of this object
        """
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def print_time(self):
        print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")

    def time_to_int(self):
        """Computes the number of seconds since midnight.
        time: Time object.
        """
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def increment(self, seconds):
        result = Time()
        result.hour, result.minute, result.second = self.hour, self.minute, self.second
        
        result.second += seconds
        
        if result.second >= 60:
            result.second -= 60
            result.minute += 1

        if result.minute >= 60:
            result.minute -= 60
            result.hour += 1

        return result

def int_to_time(seconds):
    """Makes a new Time object.
    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time



start = Time(3, 0, 0) #create and initialize the Time object 


# start.print_time()
print(start)

duration = Time(1, 35, 0)
end = start + duration
print(end)


# print(start.time_to_int())

# end = start.increment(100)
# end.print_time()
# print(end.is_after(start))

# now = Time(3, 36, 0) #creating a Time object with flexibility  
# now.print_time()

# time_2 = Time(minute = 30, second = 5)
# time_2.print_time()