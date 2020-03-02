import random

target_number = random.randrange(0, 10)
print(target_number)
while True:
    try:
     user_number = int(input("Enter the number: "))
    except:
        print("Incorrect input")
    if target_number == user_number:
        print("You win!")
        break
    elif target_number > user_number:
        print("take a bit higher")
    elif target_number < user_number:
        print("take a bit lower")
