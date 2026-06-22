alphabet=(input("Enter any character: "))
#isalpha()checks if the string contains only alphabetic characters
if len(alphabet)==1 and alphabet.isalpha():
    print(f"'{alphabet}'is an alphabet letter")
else:
    print(f"'{alphabet}'is not an alphabet letter")
          
