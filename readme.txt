Function add_time that takes 3 parameters:

a) Starting time (e.g. 11:30 AM)
b) Time to add to the first clock (e.g. 2:32)
c) (Optional) day of the week (e.g. Monday)


Returns a valid time and number of days passed (e.g. if putting 200:00 would add 200 hours) if any.


Assumptions:

a) The start time (first parameter) is a valid time
b) Minutes of second parameter wont exceed 60 (e.g. 2:70). Hours can be any number
c) Valid day of the week inserted. It will handle casing on valid days