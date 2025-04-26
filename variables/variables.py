# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains


# Strings
first_name = "Tiago"
food = "Pizza"
email = "tiago123@fake.com"

# Fstrings
print(f"Hello {first_name}")
print(f"You like {food}" )
print(f"Your email is: {email}")

#Integers
age = 19
quantity = 3
num_of_students = 30

# Fstrings
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# Float
price = 10.99
gpa = 3.2
distance = 5.5

# Fstrings
print(f"The price is {price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance}km")

# Boolean (True or False)
#is_student = True
#for_sale = True
is_online = True

if is_online:
    print("You are online")
else:
    print("You are offline")

#print(f"Are you a student?: {is_student}")