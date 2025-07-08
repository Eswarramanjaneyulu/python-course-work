name ={1:"eswar",2:"mani",3:"aditya",4:"sai"}
for i in name.keys():
    print(f"i-{name[i].title()}")
    print(f"i-{name[i].capitalize()}")

for i in range (1,21):
    print(f"7*[i]={7*i}")
    
for i in range(2,21,2):
    print(i)
    
for i in range(1,21,2):
    print(i)
    
for i in range(0,21,1):
    print(i)
    
email,pwd="eswar@gmail.com","Eswar@143"

max_attempt=5
cur_attempt=1

while cur_attempt <= max_attempt:
    e=input("enter the email:")
    p=input("enter the password:")
    
