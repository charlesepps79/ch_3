# 3-7. Shrinking Guest List: You just found out that your new dinner 
# table won't arrive in time for the dinner, and you have space for 
# only two guests.

# Start with your program from Exercise 3-6. Add a new line that prints 
# a message saying that you can invite only two people for dinner.
guests = ['Ted Bundy', 'Pedro Lopez', 'H.H. Holmes']

message = "To " + guests[0].title() + ". The honor of your presence is requested for dinner and cocktails"
print(message)
message = "To " + guests[1].title() + ". The honor of your presence is requested for dinner and cocktails"
print(message)
message = "To " + guests[-1].title() + ". The honor of your presence is requested for dinner and cocktails"
print(message)

message = "I regret to inform you that " + guests[0].title() + " will not be able to attend as he is having a friend for dinner."
print(message)
popped_guest = guests.pop(0)
guests.insert(0, 'John Wayne Gacy')

message = "To " + guests[0].title() + ". The honor of your presence is requested for dinner and cocktails"
print(message)
message = "To " + guests[1].title() + ". The honor of your presence is requested for dinner and cocktails"
print(message)
message = "To " + guests[-1].title() + ". The honor of your presence is requested for dinner and cocktails"
print(message)

message = "Honored guests, I am pleased to announce that I have found a bigger table!"
print(message)

guests.insert(0, 'Harold Shipman')
guests.insert(2, 'Jeffrey Dahmer')
guests.insert(-1, 'Jack the Ripper')

message = "To " + guests[0].title() + ". The honor of your presence is requested for dinner and cocktails"
print(message)
message = "To " + guests[1].title() + ". The honor of your presence is requested for dinner and cocktails"
print(message)
message = "To " + guests[2].title() + ". The honor of your presence is requested for dinner and cocktails"
print(message)
message = "To " + guests[3].title() + ". The honor of your presence is requested for dinner and cocktails"
print(message)
message = "To " + guests[4].title() + ". The honor of your presence is requested for dinner and cocktails"
print(message)
message = "To " + guests[-1].title() + ". The honor of your presence is requested for dinner and cocktails"
print(message)

message = "I regret to inform you that I can only invite two guests"
print(message)

# Use pop() to remove guests from your list one at a time until only 
# two names remain in your list. Each time you pop a name from your 
# list, print a message to that person letting them know you're sorry 
# you can't invite them to dinner.
popped_guest = guests.pop(0)
message = "To " + popped_guest.title() + ". I regret to inform you that your presence will no longer be needed"
print(message)

popped_guest = guests.pop(0)
message = "To " + popped_guest.title() + ". I regret to inform you that your presence will no longer be needed"
print(message)

popped_guest = guests.pop(1)
message = "To " + popped_guest.title() + ". I regret to inform you that your presence will no longer be needed"
print(message)

popped_guest = guests.pop(1)
message = "To " + popped_guest.title() + ". I regret to inform you that your presence will no longer be needed"
print(message)

# Print a message to each of the two people still on your list, letting 
# them know they're still invited.
message = "To " + guests[0].title() + ". The honor of your presence is requested for dinner and cocktails"
print(message)
message = "To " + guests[1].title() + ". The honor of your presence is requested for dinner and cocktails"
print(message)

# Use del to remove the last two names from your list, so you have an 
# empty list. Print your list to make sure you actually have an empty 
# list at the end of your program.
del guests[0:2]
print(guests)
