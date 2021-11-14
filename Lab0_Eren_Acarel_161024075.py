my_name = "Eren Acarel"
my_id = "161024075"
my_email = "eren.acarel2016@gtu.edu.tr"

if __name__ == "__main__":
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")

def problem1():
    name1 = "Hi all, This is Eren Acarel!!!"
    return name1

def problem2():
    name2 = input("Enter some input name: ")
    sonuc = "Input was " + name2
    return sonuc

def problem3():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    sonuc2 = a + b
    return sonuc2

def problem4():
    c = float(input("Enter first number: "))
    d = float(input("Enter second number: "))
    sonuc3 = c - d
    return sonuc3
    
def problem5():
    e = int(input("Enter first number: "))
    f = int(input("Enter first number: "))
    sonuc4 = e % f
    return sonuc4

def problem6():
    pi_approx = 22/7
    r = float(input("Enter radius: "))
    h = float(input("Enter high: "))
    sonuc5 = pi_approx*h*(r**2)
    return sonuc5

def problem7():
    edge = float(input("Enter edge: "))
    alan = str(edge**2)
    sonuc6 = "The perimeter of the square is value: " + alan
    return sonuc6


    
    
    