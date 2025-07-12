
    
email = "eswar@gmail.com"
password = "Eswar@143"
max_attempt=5
cur_attempt=1

while cur_attempt <= max_attempt:
    email=input("enter the email: ")
    password=input("enter the password: ")
    
    if email == email and password == password:
        print("LOgin Successful!")
        break
    else:
        cur_attempt -= 1
        print(f"Incorrect creadentials.Attempts lesft:{cur_attempt}")
else:
    print("Too many failed attempts.Access blocked")
        