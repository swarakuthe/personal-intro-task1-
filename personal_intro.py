Day 1: Setup & First Program - Install Python, create file, write Hello World
print("Hello, World!")

Day 2: 
name = input("What is your Name?")
age = input("What is your Age?")
address = input("Where do you live?")

print("Thanks for sharing your Details.")

Day 3:
name = input("What is your Name?")
age = input("What is your Age?")
address = input("Where do you live?")
hobby = input("What is your Hobby?")

print(f"\nWelcome {name}!")
print(f"You are {age} years old and You live in {address}.")
print(f"Your Favourite Hobby is {hobby}.")

Day 4: 
name = input("What is your Name?")
age = int(input("What is your Age?"))
address = input("Where do you live?")
hobby = input("What is your Favorite Hobby?")

#Basic Maths 
next_year_age = age+1

#Favourite Food List
foods = ["Pizza", "Burger", "Pasta", "Ice Cream", "Waffle", "Pancakes"]

print("\nPROFILE SUMMARY")
print(f"Name : {name}")
print(f"Age : {age}")
print(f"Next year your Age will be {next_year_age} years old")
print(f"Address : {address}")
print(f"Hobby : {hobby}")
print(f"Favourite Food : {foods[0]}")

Day 5: 
print("=" * 55)
print("             FINAL USER PROFILE PROGRAM")
print("=" * 55)

# --------- Personal Details ---------
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")

# --------- Academic Details ---------
course = input("Which course are you studying? ")
major = input("What is your major? ")

# --------- Personal Preferences ---------
hobby = input("Enter your favorite hobby: ")
favorite_color = input("Enter your favorite color: ")
dream_job = input("Enter your dream job: ")

# --------- Processing Section ---------
# Calculate age for the next year
next_year_age = age + 1

# Store favorite foods using a list
foods = ["Pizza", "Burger", "Pasta", "Ice Cream", "Waffle"]

# --------- Output Section ---------
print("\n" + "-" * 55)
print("                 PROFILE SUMMARY")
print("-" * 55)

print("PERSONAL INFORMATION")
print(f"Name            : {name}")
print(f"Current Age     : {age}")
print(f"Age Next Year   : {next_year_age}")
print(f"Address         : {address}")

print("\nACADEMIC INFORMATION")
print(f"Course          : {course}")
print(f"Major           : {major}")

print("\nPREFERENCES")
print(f"Hobby           : {hobby}")
print(f"Favorite Color  : {favorite_color}")
print(f"Dream Job       : {dream_job}")
print(f"Favorite Food  : {foods[0]}")

print("-" * 55)
print("Program executed and tested successfully ✅")
