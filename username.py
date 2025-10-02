username = input("Enter a username: ")

if len(username) > 12 :
     print("Your username con not contain more than 12 characters.")
elif not username.find(" ") == -1 :
     print("Your username can not contain any space.")
elif not username.isalpha() :
     print("Your user name can not contain any digits.")
else:
     print(f"Welcome {username}")
