print("-----HARSHITS DIGIT COUNTER-----")
original_number= int(input("Enter any number:"))
number=abs(original_number)
if number==0:
    count=1
else:
    count=0
    while number > 0:
        number= number//10
        count+=1
print(f"The number of digits in {original_number}is: {count}")
    
