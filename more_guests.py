# 3-6. More Guests: You just found a bigger dinner table, so now more 
# space is available. Think of three more guests to invite to dinner.

# Start your program from Exercise 3-4 or 3-5. Add a print statement to 
# the end of your program informing people that you found a bigger 
# dinner table.

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

# Use insert() to add one new guest to the beginning of your list.
guests.insert(0, 'Harold Shipman')

# Use insert() to add one new guest to the middle of your list.
guests.insert(2, 'Jeffrey Dahmer')

# Use insert() to add one new guest to the end of your list.
guests.insert(-1, 'Jack the Ripper')

# Print a new set of invitation messages, one for each person in your list.
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
