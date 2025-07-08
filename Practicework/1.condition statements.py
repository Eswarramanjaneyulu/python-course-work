#1.positive or negative
a=int(input("Enter a number : "))
if a>0:
    print("positive number")
else:
    print("negative number")
 
 #even or odd
a=int(input("Enter a number :  "))   
if a % 2 ==0:
     print("even")
else:
     print("odd")
     
#Divisible by 5
a=int(input("Enter a number : "))
if a%5==0:
     print("Divisible by 5")
else:
     print("not divisable by 5")
     
#divisable by 3and 7
a=int(input("Esnter a number : "))
if a%3==0 and a%7==0:
     print("Divisible by both 3 and 7")
elif a%3==0 :
     print("Divisible by  3 ")
elif a%7==0 :
     print("Divisible by 7")
else:
     print("none")
     
#check for leap year
a=int(input("Enter a year : "))
if a%4==0 and a%100!=0:
     print("it is a leap year")
else:
     print("its is a not leap year")
     
#Check Pass or Fail (Passing marks = 35)
a=int(input("Enter a marks:"))
if a>=35:
     print("pass")
else:
     print("fail")  
     
#check if number is 3-digit
digit=int(input("Enter a number:"))
if 100<= digit <=999:
     print("it's a 3-digit number")
else:
     print("it's not a 3-digit number")
     
digit = int(input("Enter a number"))
if digit>=100 and digit <=999:
     print("it's a 3-digit number")
else:
     print("it's not a 3-digit number")
     
#check if character is vowel
char=input("Enter a character:")
if len(char)==1 and char.lower() in "aeiou" :
     print(char,"vowel")
else:
     print(char,"not vowel")
#Check greatest of two numbers
     
    
a=int(input("Enter a num1:"))
b=int(input("Enter anum2:"))
if a<b:
     print(b,"is greater")
elif b<a:
     print(a,"is grater")
else:
     print("equal number")
     
#Check smallest of two numbers
     
a=int(input("Enter a num1:"))
b=int(input("Enter anum2:"))
if a>b:
     print(b,"is smaller")
elif b>a:
     print(a,"is smaller")
else:
     print("equal number") 