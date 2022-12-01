print("Select operation")
print("1. Add") #+
print("2. Subtract") #-
print("3. Multiply") #*
print("4. Divide") #/
pil= int(input("Enter choice(1/2/3/4): "))
bil1= int(input("Enter first number: "))
bil2= int(input("Enter second number: "))
def add():
    if pil==1:
        tambah= bil1+bil2
        print(bil1 ,"+", bil2, "=",tambah);
def subtract():
    if pil==2:
        kurang= bil1-bil2
        print(bil1, "-", bil2, "=",kurang);
def multiply():
    if pil==3:
        kali= bil1*bil2
        print(bil1 ,"*" ,bil2 ,"=",kali);
def divide():
    if pil==4:
        bagi= bil1/bil2
        print(bil1 ,"/", bil2, "=",bagi);


