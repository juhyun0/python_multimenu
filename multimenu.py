import math

def mainMenu():
    print("1. 한식\n2. 중식\n3. 일식\n")
    num = int(input())

    return num

def food():
    while (True) :
        no=mainMenu()
        if(no == 3):
            return

        if(no<3):
            Bab()
        else:
            return

def Bab():
    while(True):
        n=mainMenu()
        if(n==3):
            return
        if(n==1):
            print("1. 식사류")
            print("1) 비빔밥\n2) 곰탕\n3) 이전으로")
        elif(n==2):
            print("2. 요리류")
            print("1) 불고기\n2) 갈치조림\n3) 이전으로")
        else:
            return
print(food())