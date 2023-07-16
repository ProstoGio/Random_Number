import random

print("\nHello, My Name is HACHI <3. I am assistant, which can help you to choose random number from one number to second number")
fromnum=int(input("From which Number You want to choose random number?: "))
tonum=int(input(f"From '{fromnum}' to... : "))

random_number = random.randint(fromnum, tonum)

print(f"\nRandom number is: '{random_number}' <3")