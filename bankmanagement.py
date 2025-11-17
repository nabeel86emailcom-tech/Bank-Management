account = {
    "balance" : 1000 ,
    "name" : "nabeel ul rehman"
}

def balanceamount():
    print(account["balance"])

def deposite(amount):
    account["balance"] += amount
    

def witdraw(amount):
    if amount <= account["balance"]:
        account["balance"] -= amount
    else:
        print("Insuficient Amount")

def main():

    while True:
        print("Enter 1 to CheckBalance: \nEnter 2 to Deposite: \nEnter 3 to Withdraw: \nEnter q to Quit:")
        choice = input("Enter your Choice: ")
        if choice == "q":
            print("Thank you for using ABC Bank.")
            break
        elif choice == "1":
            balanceamount()
        elif choice == "2":
            deposite(float(input("Enter Aount to Deposite: ")))
        elif choice == "3" :
            witdraw(float(input("Enter amount to withdraw:")))
        else :
            print("Invalid choice!")


main()