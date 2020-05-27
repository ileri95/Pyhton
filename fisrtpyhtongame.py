import random

fistnumber=random.randrange(1,100)
print("welcome to new game ")
rightvalur=5
print("your first guess number")
print(fistnumber)

while rightvalur>0:

    number=int(input("guess : "))
    guess=fistnumber - number
    if(number==fistnumber):
        print("cong yon know the number")
        point=rightvalur*20
        print("point",point)
        break
    if (guess for a in range(1,100) ):
        print("up")
        rightvalur-=1
    else:
          print("down")
          rightvalur-=1
    if(rightvalur==0):
        print("you lost point zero")
