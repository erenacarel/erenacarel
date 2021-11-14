my_name = "Eren Acarel"
my_id = "161024075"
my_email = "eren.acarel2016@gtu.edu.tr"

if __name__ == "__main__":
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")
    
# Fahreneit-Celcius dönüşümü
def problem1():
    x = float(input("Enter Fahrenheit degree: "))
    while True:
        if x>200.0 or x<-100.0:
            break   
        else:
            y = (x-32)*(5/9)
            return y
# print(problem1()) # 68 girin


# Celcius-Fahreneit dönüşümü    
def problem2():
    x1 = float(input("Enter Celsius degree: "))
    while True:
        if x1>100.0 or x1<-100.0:
            break         
        else:
            y1 = (x1*(9/5))+32
            return y1
# print(problem2()) # 20 girin


# Hekzagonal number -> h = 2n^2 -n
def problem3():
    x2 = int(input("Enter a number: "))
    while True:
        if x2<1 or x2>int(1E6):
            break
        else:         
            y2 = 2*(x2**2)-x2
            return y2
# print(problem3()) # 1 ve 6 deneyin


# Lucas number Örneği
def problem4():
    x3 = int(input("Enter a number: "))
    a=2
    b=1 
    c=0 
    i=0
    while True:
        if x3<0 or x3>1000000:
            break
        
        if x3==0:
            return a
        elif x3 == 1:
            return b
        else:
            for i in range(2,x3+1):
                c = a + b
                a = b
                b = c
            return b
# print(problem4()) # 0 ve 6 deneyin


# Reversing a string        
# Girilen stringi tersine çevirme
def problem5():
    x4 = input("Enter a string: ")
    while True:
        if len(x4)<0 or len(x4)>101:
            break
        else:
            return x4[::-1]
# print(problem5())


# Removing unwanted printable characters
# Verilen stringdeki istenmeyen karakterleri char içerisindeki..
#...değerlerle karşılaştırıyoruz ve onları atıyoruz.        
def problem6():
    x5 = input("Enter a string: ")
    chars ="""!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"""
    for i in chars:
        x5 = x5.replace(i, '')
    return x5


# Base 4 representation
# Verien sayıları 4 tabanında yazmaya çalışan program.
# Ancak negatif değeri de önüne - koyup döndürecek
# input: 14 -> 32
# input:-14 -> -32
# input: 27 -> 123
# input: -27 -> -123   
# aşağıdaki doğru  
def problem7():
    x6 = int(input("Enter input: "))
    s =""
    s2=""
    
    while True:
        if x6 == 0:
            break
        if x6<0:
            x6 = abs(x6)
        
        s += str(x6 % 4)
        s2 += str(abs(x6) % 4)
        x6 = x6 // 4
                        
    print(s[::-1])
    print("-"+s2[::-1])

    
# Valid brackets
# Köşeli parantezlerin birbirini kapatan değerini görürsek True döndür.  
# Aşağıdaki daha doğru  
def problem8():
    string = input("Enter input: ")

    open_list = ["[","{","("]
    close_list = ["]","}",")"]
    
    if len(string)%2 != 0:
        return False
    
    else:
        stack = []
        for i in string:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                pos = close_list.index(i)
                if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
                    stack.pop()
                    return True
                else:
                    return False
        if len(stack) == 0:
            return "Balanced"
        else:
            return "Unbalanced"


# Last word length
# Cümle biçimindeki Stringin sonundaki elemanın harf sayısını ölçecek. 
def problem9():
    lenght=0
    string = input("Enter a string: ")
    
    x = string.split() #Bütün stringi ayırıp liste haline aldı.
    y = x[-1]
    
    for i in range(len(y)):
        if y[i] == "":
            lenght = 0
        else:
            lenght +=1
    return lenght
 
        #### EKSTRA BİLGİLER ####
def problemm6():
    u = """!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"""
    
    s = str(input("Enter a string: "))
    ns = ""
    for i in s:
        negv=0
        for t in u:
            if t==i:
                negv=1
        if negv==1:
            continue
        ns+=i
    return ns
 
def problemm7():
    v = int(input("Enter input: "))
    s = ""
    
    if v>=0:
        while True:
            k = v%4
            v = v//4
            s += str(k)
            if v==0:
                break
        s =s[::-1]
    else:
        v*=-1 ## 0'dan küçükse sadece -1'le çarpıyoruz.
        while True:
            k = v%4
            v = v//4
            s += str(k)
            if v==0:
                break
        s = "-"+s[::-1]
    return s

def problemm8():
    s = str(input("Enter input: "))
    
    if len(s)%2 != 0:
        return False
    else:
        while len(s)>0:
            negv = 0
            for t in range(0, len(s)):
                if s[t:t+2]=="()" or s[t:t+2]=="[]" or s[t:t+2]=="{}":
                    s=s[0:t]+s[t+2::]
                    negv = 1
            if negv ==0:
                return False
    return len(s) == 0
# {}       -> True
# {}{}[]   -> True
# [{}]     -> True
# {([])}[] -> True
# {(})     -> False
# [)       -> False   
# [()      -> False

def problemm9():
    s = str(input("Enter a string: "))
    lw = ""
    for i in s[::-1]:
        if i == " ":
            break
        lw += i
    l = len(lw)
    return l

# Escape the maze
# e denirse doğuya, w denirse batıya...
#...n denirse kuzeye, s denirse güneye gidilsin
def problem10():
    r = str(input("Enter the exit route: "))
    x = 0
    y = 0
    eps = 1e-3
    for i in r:
        if i == "e":
            x=x+1
        elif i == "w":
            x=x-1
        elif i=="n":
            y=y+1
        else:
            y=y-1
            
    target = x**2+y**2
    guess = 1.0
    
    while True:
        if abs(guess**2 - target) < eps:
            break    
        guess = guess - (guess**2 - target)/(2*guess)   
    return guess
    
# print(problem10()) sewnsnwwwnsseeewnsswnwnwwnessnswwnewsn -> 6.00 çıkacak
#                    wwenn -> 2.23606797749979                     

