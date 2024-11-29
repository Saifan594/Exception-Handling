print("\033c")

def countAge(age):
    if age < 0:
        raise ValueError("only positive integers are allowed!")
    
    elif age % 2 == 0:
        print("The age is even")
    
    else:
        print("The age is odd")

try:
    integer = int(input("Enter age : "))
    countAge(integer)

except ValueError:
    print("only positive integers are allowed!")

except:
    print("something went wrong!")