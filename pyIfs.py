userAge = int(input("What's your age again?"))

if userAge < 18:
    print("Minor!")
elif userAge >= 65:
    print("Holy shit you're old.")
elif userAge >= 18:
    print("Adult!")


#Challenge 6
#Write a program that asks the user to enter their age and prints a message indicating whether they are a minor (under 18),
# an adult (18 or over), or a senior (65 or over).