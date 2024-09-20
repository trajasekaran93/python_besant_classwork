


stock={"banana":10,"apple":15,"orange":20}
price={"banana":5,"apple":60,"orange":40}

stocklist=stock.copy()
# print(stocklist)
while(True):
        for i in stocklist:
            print("fruit name is", i, "available quantity is : ", stocklist[i])

        fruitselect = input("choose your fruit name :").lower()
        if (fruitselect == "banana"):
            quan = int(input("enter the no of quantity : "))
            if (quan <= stocklist["banana"]):
                totalamount = quan * price["banana"]
                print("total amount to pay : ", totalamount)
                print("Thanks for purchasing...Visit Again")
                print("************************************")
            else:
                print("stock is not available")
        elif (fruitselect == "apple"):
            quan = int(input("enter the no of quantity : "))
            if (quan <= stocklist["apple"]):
                totalamount = quan * price["apple"]
                print("total amount to pay : ", totalamount)
                print("Thanks for purchasing...Visit Again")
                print("************************************")
            else:
                print("stock is not available")
        elif (fruitselect == "orange"):
            quan = int(input("enter the no of quantity : "))
            if (quan <= stocklist["orange"]):
                totalamount = quan * price["orange"]
                print("total amount to pay : ", totalamount)
                print("Thanks for purchasing...Visit Again")
                print("************************************")
            else:
                print("stock is not available")
        else:
            print("invalid entry pls enter valid fruit name")
            break