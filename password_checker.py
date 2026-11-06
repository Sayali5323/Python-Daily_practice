
def check_password(password):
    has_upper=False
    has_digit=False

    for char in password:
        if char.isupper():
            has_upper=True

        if char.isdigit():
                    has_digit=True
    if len(password)>=8 and has_upper and has_digit:
          print("Password is Strong")
    else:
          print("password is weak")

password=input("Enter password")
check_password(password)
