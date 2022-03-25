class Atm:
    def __init__(self,cardno,pin):
        self.cardno=cardno
        self.pin=pin
    def checkbalance(self):
        print("Your BALANCE IS=10000")   
    def withdrawal(self,amount):
        newamount=10000-amount
        print("YOUR BALANCE IS"+str(newamount))
def main():
    cardno=input("ENTER YOUR CARD NUMBER:")
    pinno=input("ENTER YOU PIN:")
    newuser=Atm(cardno,pinno)
    print("1.Balance Enquiry 2.Withdrawal")
    activity=int(input("Enter Your Activity:"))
    if(activity==1):
        newuser.checkbalance()
    elif(activity==2):
        amount=int(input("Enter Your Amount"))
        newuser.withdrawal(amount)
    else:
        print("Enter A Valid Number")
main ()                         