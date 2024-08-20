x = int(input("Enter your age: "))

if x <= 18:
    print(f"your are  not eligible to vote {x}")
elif x >= 18:
    print(f"your are eligible to vote {x}")
else:
    print("Both conditions are false")
