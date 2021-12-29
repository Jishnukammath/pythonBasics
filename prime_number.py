x=int(input("enter a number : "))



for i in range(2,x):
    if x%i==0:
        print("number is not  prime")
        print(i, "times", x // i, "is", x)
        break

else:
    print("its prime")

