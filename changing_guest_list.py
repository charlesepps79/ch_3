# 3-5. Changing Guest List: You just heard that one of your guests 
# can't make the dinner, so you need to send out a new set of 
# invitations. You'll have to think of someone else to invite.

# Start with your program from excercise 3-4. Add a print statement at 
# the end of your program stating the name of the guest who can't make it.

# Modify your list, replacing the name of the guest who can't make it 
# with the name of the new person you are inviting.

# Print a second set of invitation messages, one for each person who is 
# stil in your list.

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