my_name = "Eren"
my_id = "161024075"
my_email = "eren.acarel2016@gtu.edu.tr"

if __name__ == "__main__":
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")

# Bu soruda ismimizin ilk harfini string olarak döndürmeyi istemektedir. 
def problem1():    
    return my_name[0]

# Bu soruda ismimizin harflerini döndüren bir uygulama istiyoruz...
#...len(my_name) kullansak daha iyi olacaktı.    
def problem2():
    parameter1 = int(input("Enter a number: "))
    y = int(parameter1 % 4)         
    return my_name[y]    

# Bu soruda slicing yapmamız isteniyor. Girilen birinici ve ikinci...
#...numaradan max ve min olanı belirlenir, ardından ikisi arasındaki...
#...değerleri yazdırmamız istenecek. Aşağıdaki doğru. 
def problem3():
    parameter2 = int(input("Enter first number: "))
    parameter3 = int(input("Enter second number: "))
    z = int(parameter2 % 4)
    x = int(parameter3 % 4)
    return my_name[z:x]

# Bu soruda iki tane stringde ortak karakterleri buluruz. Ardından...
#...ortak olanları sayıp sayılan değeri döndürüyoruz.     
def problem4():
    string = str(input("Enter input: "))
    wovels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    count = 0
    for s in string:
        for l in wovels:
            if s==l:
                count += 1
    return count

# Okul numaramızdaki rakamları topluyoruz.
# Aşağıda kısa hali de mevcut    
def problem5():
    toplam1 = 0
    for digit in str(my_id): #int
        toplam1 += int(digit)
    return toplam1

# Faktöriyel hesabı yapıyoruz.
def problem6():
    toplam2 = 1
    x = int(input("Enter input: "))
    for i in range(1,x+1):
        toplam2 *= i    
        if x>30:
            break
    return toplam2    

# 3'e ve 7'ye bölünenleri True diye döndürüyoruz.    
def problem7():
    a = int(input("Enter a number: "))     
    if a%3 == 0 and a%7 == 0:
        return True
    else:
        return False

# 3'e ve 7'ye bölünenleri alıyoruz.
# Sadece 3'e ve 7'ye bölünenleri ayrı alıyoruz.    
def problem8():
    b = int(input("Enter a number: "))    
    if b%7 == 0 and b%3 == 0:
        return 3
    elif b%3 == 0:
        return 1
    elif b%7 == 0:
        return 2
    # else:
    #     return False
# print(problem8()) ## None döndürülsün istenmiş

# Prime number arıyoruz ancak 9'a False demesi lazım.
# Aşağıdaki doğru.
def problem9():
    c = int(input("Enter a number: "))
    if c > 1:
        for i in range(2,c):
            if c%i ==0:
                return False
            else:
                return True
# print(problem9())

# Heron's method ile karekök bulma yöntemi            
def problem10():
    error_value = 0.0000000001
    starting_guess = 1
    N = float(input("Enter a number: "))
    x = 1e9
    
    while True:
        if N<0 and N>x:
           break
       
        old_guess = N
        while abs(starting_guess - old_guess) > error_value:
            old_guess = starting_guess
            starting_guess = (old_guess + N/old_guess)/2
        return old_guess
########################################
       # Ekstra Anlatımlar #
########################################

def problemm2():
    parameter1 = int(input("Enter a number: "))
    uzunluk = len(my_name)
    y = int(parameter1 % uzunluk)         
    return my_name[y] 

def problemm3():
    uzunluk = len(my_name)
    parameter2 = int(input("Enter first number: "))
    parameter3 = int(input("Enter second number: "))
    
    z = int(parameter2 % uzunluk)
    x = int(parameter3 % uzunluk)
    
    m1 = min(z,x) # hangisinin min 
    m2 = max(z,x) # hangisinin max olduğuna karar veriliyor. 
    
    return my_name[m1:m2+1] # m2 +1 denmesinin sebebi m2 deki değeri de almaktır
                            # orası da dahil olsun. 

def problemm5():
    return sum(int(digit) for digit in my_id)


def problemm9(): # 9 sayısı sağlanmıyordu burada sağlanıyor
    flag = True
    c = int(input("Enter a number: "))
    if c > 1:
        for i in range(2,c):
            if c%i ==0:
                flag=False
    return flag    
                
#print(problemm9())

def problemm10():
    sayi = int(input("Enter a number: "))
    guess = 0.0
    step = 0.0001 # decreasing increment size -> slower program
    eps = 0.001   # increasing epsilon -> less accurate answer
     
    counter = 0
    while True:
        counter += 1
        if abs(guess * guess - sayi) < eps:
            print("Bulduk")
            break
        elif guess * guess > sayi:
            print("Bulamadik")
            break
        guess += step        
    print(counter,guess)
    
def problem11(): ### BISECTION SEARCH
    sayi = int(input("Enter a number: "))
    
    low = 1
    high = sayi
    eps = 1E-4 # 1E-9 yazarsak adımlar artar, yavaşlar
    
    counter = 0
    while True:
        counter += 1
        guess = (high + low) / 2
        if abs(guess*guess - sayi) < eps:
            print("bulduk")
            break
        if guess*guess > sayi:
            high = guess
        else:
            low = guess
    print(counter,guess)
    
def problem12(): ## dec to binary
    target = 42
    s =" "
    
    while True:
        if target == 0:
            break
        s += str(target%2)
        target = target // 2 ## 6//4 = 1
        
    # print(s)
    # print(s[::-1])
      
def problem13():
    target = 0.625
    
    t = int(target)
    f = target - t
    
    s = ''
    while True:
        if abs(f - 0) < 1e-9:
            break
        f *= 2
        
        s += str(int(f))
        f = f - int(f)
    print("0."+s)
    
        






