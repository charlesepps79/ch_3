# 3-9. Dinner Guests: Working with one of the programs from Exercises 
# 3-4 through 3-7 (page 46), use len() to print a message indicating 
# the number of people you are inviting to dinner.
guests = ['Ted Bundy', 'Pedro Lopez', 'H.H. Holmes']

message = "To " + guests[0].title() + ". The honor of your presence is requested for dinner and cocktails"
print(message)

message = "To " + guests[1].title() + ". The honor of your presence is requested for dinner and cocktails"
print(message)

message = "To " + guests[-1].title() + ". The honor of your presence is requested for dinner and cocktails"
print(message)

print(len(guests))
