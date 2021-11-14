my_name = "Eren Acarel"
my_id = "161024075"
my_email = "eren.acarel2016@gtu.edu.tr"

if __name__ == "__main__":
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")

# Find the King
# İçinde K harfi varsa True döndür.    
def problem1(x):
    if len(x) == 1 or len(x) == 0:
        return False
    y = list(x)
    liste = ["K"]
    count = 0
    for s in y:
        for l in liste:
            if s==l:
                count += 1
    return True
# print("problem1 için 12313 denendi: ",problem1('12313'))
# print("problem1 için K713 denendi: ",problem1('K713'))
# print("problem1 için Q denendi: ",problem1('Q'))
# print("problem1 için 631J43K146 denendi: ",problem1('631J43K146'))

# Minimum of the four
# 4 tamsayı arasından min olanı döndür.          
def problem2(a,b,c,d):
    #return min(a,b,c,d)
    return float(min(a,b,c,d))
#print("problem2 için 2.3, -2.4, -1, 4.3 değerleri denendi: ",problem2(2.3, -2.4, -1, 4.3))

# Volume of a cylinder    
def problem4(radius=None, height=None, pi=3.1415):
    volume = pi*(radius**2)*height
    return volume

# Volume of a cylinder with error check    
def problem5(radius, height, pi=3.1415):
    
    if type(radius) != int:
        return -1
    elif type(height) != int:
        return -1
    elif pi == True:
        return -1
    else:
        volume = pi*(radius**2)*height
        return volume
# print(problem5(2, 3))
# print(problem5(2, 3, pi=3))
# print(problem5(2, 3, 3))
# print(problem5(radius=2, height=3))
# print(problem5(radius='test', height=3))
# print(problem5(2, 'test', 3))
# print(problem5(2, 2, True))
# print(problem5(2, None, 3))


# Ascending ordered string
# harfleri sıralı bir şekilde görürse True döndür.
def problem7(x):
    y = list(x)
    if y == sorted(x):
        return True
    else:
        return False


#Unique characters
def problem8(str):
    for i in range(len(str)):
        for j in range(i+1, len(str)):
            if (str[i] == str[j]):
                return False
    return True
 
# Similarity
# aynı indexteki arka arkaya gelen harflerin sayını gösterir.
# Aşağıdaki daha doğru
def problem10(strA, strB):
    answer = ""
    len1 = len(strA)
    len2 = len(strB)
    if len1==1 or len2==1:
        return 0
    for i in range(len1):
        for j in range(len2): 
            match = ""
            negv = 0
            while((i+negv < len1) and (j+negv<len2) and strA[i+negv] == strB[j+negv]):
                match += strB[j+negv]
                negv += 1
            
            if(len(match)>len(answer)):
                answer = match
    return len(answer)    
    
##########   EKSTRA BİLGİLER #######

def problemm1(a):
    flag = False
    for i in a:
        if i=="K":
            flag=True
    return flag

# Round to the nearest
# Bu problemde a ve b sayılarını karşılaştıracak. a veya b'den...
#...herhangi birinin en yakın olduğu tamsayıyı ekrana...
#...yazdırmayı isteyecek.
# import yasak olmasına rağmen import ile çözüm yapılmış amk !!!
def problemm3(a,b):
    from math import floor,ceil
    sign2=ceil(b) # ceil ile yuvarlama yapıyor...
                  # a=3.1 ceil(a)=4 iken a=-3.1 ceil(a)=-3
    sign3=floor(b) # floor ile yuvarlama yapıyor...
                   # a=2.6 floor(a)=2 iken a=-2.6 floor(a)=-3 olur.
    
    if b>0:
        if type(b)==int:
            if a>b:
                return floor(a) 
            else:
                return ceil(a)
        else:
            if abs(sign2-b)<abs(b-sign3):
                return ceil(a)
            elif abs(sign2-b)>abs(b-sign3):
                return floor(a)
            elif abs(sign2-b)==abs(b-sign3):
                return ceil(a)
    else:
        if type(b)==int:
            if a>b:
                return floor(a)
            else:
                return ceil(a)
        else:
            if abs(sign2-b)>abs(b-sign3):
                return floor(a)
            elif abs(sign2-b)<abs(b-sign3):
                return ceil(a)
            elif abs(sign2-b)==abs(b-sign3):
                return floor(a)            
# print(problemm3(2.6, 1))
# print(problemm3(2.6, 2))
# print(problemm3(2.6, 3))
# print(problemm3(3, 10))
# print(problemm3(3, -10))
# print(problemm3(2.6, 5))
# print(problemm3(-0.7, 10))
# print(problemm3(-0.7, -10))
# print(problemm3(0.7, 0.6))
# print(problemm3(0.7, 0.9))
# print(problemm3(0.7, 0.3))
# print(problemm3(0.7, 0.5))

# Volume of a cylinder with error check
# isinstance ile kontrol edilebiliyor.    
def problemm5(radius=None, height=None, pi=3.1415):
    if (isinstance(radius, (int, float))==True) and (isinstance(height, (int, float)==True)) and (isinstance(pi, (int, float))==True and type(pi) != bool):
        return (radius**2)*height*pi
    else:
        return -1
# print(problemm5(2, 3))
# print(problemm5(2, 3, pi=3))
# print(problemm5(2, 3, 3))
# print(problemm5(radius=2, height=3))
# print(problemm5(radius='test', height=3))
# print(problemm5(2, 'test', 3))
# print(problemm5(2, 2, True))
# print(problemm5(2, None, 3))

# Mr. Lonely
# tekrarlamayan elemanı yazmasını istiyoruz.
def problem6(a):
    s = ""
    for i in a:
        if a.count(i)<2:
            s=s+i
    return s
    
### alfabetik sıraya göre dizme    
def problemm7(a):
    a=a.lower()
    sırala=sorted(a)
    s=""
    for i in sırala:
        s=s+i
    if s==a:
        return True
    else:
        return False
   
### uniqe karakter bulma
def problemm8(a):
    s=""
    for i in a:
        if a.count(i)>1:
            s=s+i
    if len(s)>1:
        return False ##aynı karak. tekrarlıyorsa
    else:
        return True
    
# Recursive with me
# f(i,j) = f(i-1, j-1) + f(i-1, j)
# f(i=1, j=1)=1
# f(i, j=1)=3 i>1
# f(i, j=i)=2 i>1
# j<=i
def problem9(row, column):
    if row==1 and column==1:
        return 1
    elif column==1:
        return 3
    elif column==row:
        return 2
    return problem9(row-1, column-1)+problem9(row-1,column)
    ### şartlar sağlanmazsa bu fonksiyonu döndür.
# print(problem9(1,1))   
# print(problem9(4,1))
# print(problem9(9,1))
# print(problem9(row=5,column=5))
# print(problem9(8,8))
# print(problem9(8,3))     
# print(problem9(12,7))  

# Similarity
# aynı indexteki arka arkaya gelen harflerin sayını gösterir.
def problemm10(s1="", s2=""):
    len1 = len(s1)
    len2 = len(s2)
    iter = min(len1, len2) # len1 6 karakterde len2 8 karakterde..
    #... diyelim. for döngüsünde aynı indislerin eşit olup olmadığına...
    #... bakmak için en kısaya göre iterasyon yapmalıyım. Minimum...
    #... stringin uzunluğuna göre.
    count = 0    
    for i in range(iter):
        if s1[i] == s2[i]:
            count += 1
    return count
    
# print(problemm10('tarkan', 'gurkan'))
# print(problemm10('kesit', 'telas'))
# print(problemm10('ke@', 'telas'))
# print(problemm10('k', 'tekkk'))
# print(problemm10('telas', 'ke'))
# print(problemm10('!telas', 'k'))

  
    