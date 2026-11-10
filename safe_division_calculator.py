try:
    #try contains the code that might cause an error.
    no1=float(input("Enter the first no:"))
    no2=float(input("Enter the second no:"))
    result=no1/no2
    print("Result:",result)
except ValueError:
    #valueError handles invalid numeric input.
    print("Please enter valid numbers:")
except ZeroDivisionError:
    #handles division by zero
    print("Cannot divide by zero.")
