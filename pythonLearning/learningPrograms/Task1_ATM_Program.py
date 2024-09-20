
print ("Insert your card and")
print("choose the below options : \n 1.Deposit \n 2.Withdrawl \n 3.Current Balance \n 4.Exit ")
choice = int(input("enter your choice :"))
bal=1000.56
if(choice==1):
    dep = int(input("enter the amount to deposit : "))
    bal=bal+dep
    print("your current balance is : ",bal)
elif(choice==2):
    wdt = int(input("enter the amount to withdral : "))
    if(wdt>bal):
        print("insufficient balance")
    else:
        bal=bal-wdt
        print("your current balance is : ",bal)
elif(choice==3):
    print("your current balance is : ",bal)
elif(choice==4):

    print("Thanks for visiting the ATM")

else:
    print("invalid choice")