print("--------POWER CALCULATOR------")
base= float(input("Enter any base number :"))
exponent=int(input("Enter the power/exponention (integer):"))
result=1.0
for _ in range(abs(exponent)):
    result*=base
if exponent < 0 :
    result= 1.0 / result
print(f"{base}raised to the power of {exponent} is:{result}")



