def classify_age(age):
    if age < 0:
        print("Invalid age, it cannot be negative.")
    elif age <= 14:
        print("You are a child")
    elif age <= 18:
        print("You are a teen")
    elif age <= 50:
        print("You are an adult")
    else:
        print("You are a Senior")

while True:
    age = int(input("Enter your age: "))
    classify_age(age)