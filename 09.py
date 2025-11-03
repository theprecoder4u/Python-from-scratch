p1 = "make a lot"
p2 = "subscribe"

message = input("Enter the comment: ")

if(p1 in message or p2 in message):
    print("This is a spam comment")

else:
    print("This is not spam")