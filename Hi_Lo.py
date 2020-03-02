import random

target_number = random.randrange(0, 10)
print(target_number)
user_number = int(input("Enter the number: "))
if target_number == user_number:
    print("You win!")
else:
    print("You lose!")