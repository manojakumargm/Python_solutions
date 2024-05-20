# condition is if person age >=18 are eligible for vote in india

age = int(input("Enter your age:"))
if age >= 0:
    if age >= 18:
        print("Hey! you are eligible for voting")
    else:
        print("sorry! you have to wait"+" "+str(18-age)+" "+ "years for voting")
else:
    print("incorrect input")

