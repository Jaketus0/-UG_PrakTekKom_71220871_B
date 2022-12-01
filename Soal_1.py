print("Select operation")
print("1. Add") #+
print("2. Subtract") #-
print("3. Multiply") #*
print("4. Divide") #/
pil= int(input("Enter choice(1/2/3/4): "))
bil1= int(input("Enter first number: "))
bil2= int(input("Enter second number: "))
if pil==1:
    def add():
    tambah= bil1+bil2
    print(bil1 ,"+", bil2, "=",tambah);
    bil1= int(input("Enter first number: "))
    bil2= int(input("Enter second number: "))
    add()
elif pil==2:
    def subtract():
    kurang= bil1-bil2
    print(bil1, "-", bil2, "=",kurang);
    bil1= int(input("Enter first number: "))
    bil2= int(input("Enter second number: "))
    subtract()
elif pil==3:
    kali= bil1*bil2
    def multiply():
        print(bil1 ,"*" ,bil2 ,"=",kali);
        bil1= int(input("Enter first number: "))
        bil2= int(input("Enter second number: "))
    multiply()
elif pil==4:
    bagi= bil1/bil2
    def divide():
        print(bil1 ,"/", bil2, "=",bagi);
        bil1= int(input("Enter first number: "))
        bil2= int(input("Enter second number: "))
    divide()

