# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 11:34:12 2022

@author: ERENACAREL
"""

## LAB 5'i yeniden doğru cevaplarıyla çözdüm.
## Burada bir listedeki elemanların tekrar edenlerinin sayısı kadar olan değerleri return etmesini isteyeceğiz ve sonucu görüyoruz
## 0 girersek hiç tekrar eden eleman yok iken geçersiz sayı girersek boş liste dönecek

def problem1(liste,n):
    boslist = []
    for i in liste:
        if liste.count(i) == n: ## i sayısından listede kaç tane var
            boslist.append(i)   ## en sona eleman ekler
    boslist = set(boslist) ## her eleman bir tane olacak şekilde yazdırıyor
    boslist = list(boslist)
    return boslist
 
print(problem1([1, 2, 1, 1, 1, 2, 3, 4], 1))
print(problem1([1, 2, 1, 1, 1, 2, 3, 4], 0))
print(problem1([1, 2, 1, 1, 1, 2, 3, 4], -2))
print(problem1([1, 2, 1, 1, 1, 2, 3, 4], 2))
print(problem1([1, 2, 1, 1, 1, 2, 3, 4], 3))
print(problem1([], 0))
print(problem1([], 1))


## Buradaki problemimizde bize bir dict verilecek, eleman sayısı tekse ortadaki
## değeri döndürecek. Eleman sayısı çiftese ortadaki iki elemanın ortalamasını 
## alıp döndürecek.

def problem2(dic):
    uzunluk = len(dic)
    liste1 = list(dic.values()) ## values demek dict'in ikinci elemanlarını alır. keys ise birinci elemanlarını alır.
    average = 0
    # if uzunluk==2:            
    #     average = (liste1[0] + liste1[1])/2
    if uzunluk%2==0:
        bas = int(uzunluk/2)-1
        son = int(uzunluk/2)
        average = (liste1[bas] + liste1[son]) / 2
    else:
        average = liste1[int(uzunluk/2)]
    return average

#print(problem2({'ahmet': 30, 'ali': 20, 'mehmet':10}))
#print(problem2({'ahmet': 10, 'ali': 20}))      
#print(problem2({'ahmet': 30, 'ali': 20, 'deneme': 99, 'mehmet':10}))


## Verilen transkript dosyasının önüne name, credit, term, grade... 
##...isimlerini koyup liste şekliyle döndürüyoruz.

def problem3(fname):
    try:
        file1 = open(fname,"r")
    except FileNotFoundError:
        return []
       
    file2 = file1.read().splitlines() ## Satırları ayırıp her satır bitiminde virgül koyuyor ve listeye atıyor
    
    liste2 = ["name", "credit", "term", "grade"] ## ilk elemanlar bunlar
    dic_list = []
    lup = len(file2)
    liste3 = file2[0].split(",") ## 0. indisimiz bir cümle olduğundan bunu da her kelimesini arasına... 
                                 ##...virgül gelecek şekilde ayırıyoruz.
    
    ## strip boslukları kaldırır en bastan ve en sondan veya istenmeyen her şeyi kaldırır
    ## split listeyi parçalara ayırır.
    
    for i in range(lup):
        liste3 = file2[i].strip().split(",") # strip boşlukları almak için kullanılır
        liste3[1] = int(liste3[1]) # 1. ve 2. indisleri int atadık
        liste3[2] = int(liste3[2])
        liste3[3] = liste3[3].strip() ## 3. indisteki boşluk değerlerinden de kurtuluyorum.
        if liste3[-1] == "":
            liste3[-1] = "NA"
            
        d1 = zip(liste2,liste3) ## key ve value kısımlarını birleştiriyoruz
        dic_list.append(dict(d1)) ## d1 dictionary'e atıyorum
                                 ## list'in içinde dictionary'ler var
    file1.close()
    return dic_list


a = problem3('transcript1.txt')
#print(a)


## transkripte girilen harf notlarına göre ortalama hesaplaması yapacağız. 

def problem4(d,t):
    grades = {"AA": 4.0, "BA": 3.5, "BB": 3.0, "CB":2.5, "CC": 2.0, "DC": 1.5, "DD": 1.0, "FF": 0.0, "NA":"NA"}
    uz = len(d)
    weight = []
    ortalama = []
    alt = 0
    üst = 0
    for i in range(uz): ## dictionary uzunluğu kadar döngü döndürelim
        dic_no = d[i] ## dictionary'nin ilk elemanını aldım.
        if int(dic_no["term"] == t): ## dönemin t'si, dic_no["term"] == 1 , 1. döneme dikkat edilecek 
            if grades[dic_no["grade"].lstrip()] != "NA":  ## dic_no'nun önündeki boşlukları alıyorum.
                                                          ## NA'ya eşit olmadığı sürece notları dikkate alıyorum.
                ortalama.append(grades[dic_no["grade"].lstrip()])
                weight.append(int(dic_no["credit"])) ## hem krediye hem de harf notlarına ihtiyacımız var.
                ## gerek olmasa bile integer dönüşümü yaptık.
                
        alt = sum(weight)                    ## creditleri topluyorum.
        üst = sum(i*j for i,j in zip(ortalama, weight)) ## iki listeyi birleştiriyorum.
        try:
            return üst/alt ## ortalamayı bulmak için kredilerin toplamına bölmek gerekiyor. son iki digit aldık.
            #return round(int(üst/alt),2)
        except ZeroDivisionError: ## 0/0 hatasıyla karşılaşmamak için
            return 0
        
b = problem4( [{'name' : 'inf211', 'credit' : 6, 'term' : 1, 'grade' : 'DC'},  {'name' : 'elm101', 'credit' : 2, 'term' : 1, 'grade' : 'BA'}, {'name' : 'mat101', 'credit' : 7, 'term' : 1, 'grade' : 'NA'}], 2)
print(b)


def right_ffunc(n):
    liste4 = list(range(0, n+1))
    liste4 = str(liste4)
    return liste4.count("1")

def problem5(f,n2):
    pass














## Burada harf kombinasyonlarını test ediyoruz.
## Sıralama yapmamız isteniyor ve tekrarlayan kombinasyonlar istenmiyor
## mesela ABC kombinasyonunu düşünelim.
## Yaptığımız ilk yöntem iki aynı listeyi toplamak oldu.
## ABC + ABC = ABCABC
## Bunları yan yana koyup kombinasyon yaptığımızda A AB ABC B BC BCA C CA CAB ... A AB ABC B BC BCA C CA CAB diye gidiyor.
## Tekrarları yok edip alfabetik sıraya göre sıralarız.

## O KADAR SAÇMA Kİ :/

def problem6(s):
    boy = len(s)
    new = s + s
    liste5 = []
    
    for i in range(boy):
        for j in range(i, i + boy):
            liste5.append(new[i:j+1])
    liste5 = set(liste5) ## tekrarlayan eleman istemiyoruz.
    liste5 = sorted(list(liste5))
    return liste5

print(problem6("aba"))




def problem7(string, dosya):
    filee1 = open(dosya, "r")
    filee2 = filee1.read().splitlines()
    
    boyy = len(string)
    neww = string + string     
    
    ret_list = []
    for i in range(boyy):
        for j in range(i, i + boyy):
            #ret_list = filee2[i].strip()
            ret_list.append(neww[i: j+1])
    ret_list = set(ret_list) ## tekrarlayan eleman istemiyoruz.
    ret_list = sorted(list(ret_list))
    return ret_list 
                 
print(problem7("abaa", "words.txt"))         


def problem8():
    pass



def problem9(ss):
    sstring = ""
    adet = []
    for i in ss:
        if i not in adet: # i, adet'in içinde değilse
            adet.append(i)
            
    #count = 0
    for i in adet:
        if ss.count(i) != 1:
            sstring = sstring + i + str(ss.count(i))

        else:
            sstring = sstring + i

    azalma = len(ss) - len(sstring)
    percentage = int((azalma/len(ss))*100)
    return sstring, percentage, adet ## tuple döndürme şartı virgül koymaktır.

## Sıkıştırma oranı: kaydedilen alanın tekrarlayan alana yüzdesi
print(problem9('goooooollllll'))



## Missing number
# def problem10(listem):
#     a = min(listem)
#     b = max(listem)
#     for i in range(a, b+1):
#         if i not in listem:
#             return i      
#     return b+1
    

# print(problem10([1, 3, 2, 5]))
# print(problem10([4, 1, 2]))
# print(problem10([0, -1, -2, 2, 3]))
# print(problem10([0]))
# print(problem10([5, 3, 4]))

def problem10(p10):
    sıralı = sorted(p10)
    start = sıralı[0]
    end = sıralı[-1]
    new_list = list(range(start,end+1))
    for i in new_list:
        if i not in sıralı:
            return i
        
        elif sıralı == new_list:
            return int(new_list[-1]+1)
        
print(problem10([1, 3, 2, 5]))
print(problem10([4, 1, 2]))
print(problem10([0, -1, -2, 2, 3]))
print(problem10([0]))
print(problem10([5, 3, 4]))   
    