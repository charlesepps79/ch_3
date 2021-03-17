# 3-4. Guest List: If you could invite anyone, living or deceased, to 
# dinner, who would you invite? Make a list that includes at least 
# three people you'd like to invite to dinner. Then use your list to 
# print a message to each person inviting them to dinner.

guests = ['Ted Bundy', 'Pedro Lopez', 'H.H. Holmes']

message = "To " + guests[0].title() + ". The honor of your presence is requested for dinner and cocktails"
print(message)

message = "To " + guests[1].title() + ". The honor of your presence is requested for dinner and cocktails"
print(message)

message = "To " + guests[-1].title() + ". The honor of your presence is requested for dinner and cocktails"
print(message)
