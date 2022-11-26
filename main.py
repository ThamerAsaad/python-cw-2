# write your code here
my_name = input("who are you ?")
my_age = input("Nice to mate you , how older you? ")
print(f"My name is {my_name} , I am {my_age} years old")

first_number, second_number , operation = eval(input("Enter a first number and a second number , The operation "))


if operation == "*": 
    equal = first_number * second_number 
    print(equal)
elif operation ==  "+":
    equal = first_number + second_number
elif operation == "-":
    equal = first_number - second_number
    print(equal)
elif operation == "/":
    equal = first_number + second_number
    print(equal)
else:
    print("the operation is not valid")



number = input("Enter a number from 1 to 12:")
noun = input("Enter a noun (plural): ")
name = input("Enter a name")
sentence = input("Enter any sentence: ")
verb = input("Enter a verb ")

print(f"It was {number} o'clock when I heard a knock at the door.")
print(f"I opened the door and there was a box full of {noun} with a note saying From Mr. Stephen Sedoll. ")
print(f"Just as I closed the door I heard a scream {sentence}")
print(f"I froze in place and all I could do was {verb} ")





