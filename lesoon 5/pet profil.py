# ==================================
# MY PET PROFILE
# ==================================

# Function to display pet information
def pet_profile(name, animal, age):
    print("\n--- My pet profile ---")
    print("pet Name:", name)
    print("animal:", animal)
    print("Age:", age, "years old")

    if age < 5:
        print("Your pet is stil young!")
    else:
        print("your pet is a groen-up!")


# Function to give a greeting
def pet_greeting(name):
    print("\nHello", name + "!")
    print("Welcome to your pet profile")

# Get information from the user
pet_name = input("Enter your pet's name: ")
pet_animal = input("Enter your animal type: ")
pet_age = int(input("Enter your pet's age: "))

# call the function
pet_greeting(pet_name)
pet_profile(pet_name, pet_animal, pet_age)