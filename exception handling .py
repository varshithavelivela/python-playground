a = input("Enter your number: ")
print(f"Multiplication table of {a} is :")
try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except:
    print("Sorry invalid input!!")

print("Try again")
print("The End")
    
