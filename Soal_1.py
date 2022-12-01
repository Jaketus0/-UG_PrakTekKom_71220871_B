print("Select operation")
print("1. Add") #+
print("2. Subtract") #-
print("3. Multiply") #*
print("4. Divide") #/
pil= int(input("Enter choice(1/2/3/4): "))
def add():
    tambah= bil1+bil2
    print(bil1 ,"+", bil2, "=",tambah)
def subtract():
    kurang= bil1-bil2
    print(bil1, "-", bil2, "=",kurang)
def multiply():
    kali= bil1*bil2
    print(bil1 ,"*" ,bil2 ,"=",kali)
def divide():
    bagi= bil1/bil2
    print(bil1 ,"/", bil2, "=",bagi)
if pil==1:
    bil1=float(input("Enter first number: "))
    bil2=float(input("Enter second number: "))
    add()
elif pil==2:
    bil1=float(input("Enter first number: "))
    bil2=float(input("Enter second number: "))
    subtract()
elif pil==3:
    bil1=float(input("Enter first number: "))
    bil2=float(input("Enter second number: "))
    multiply()
elif pil==4:
    bil1=float(input("Enter first number: "))
    bil2=float(input("Enter second number: "))
    divide()


