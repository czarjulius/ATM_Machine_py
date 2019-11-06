# User account balance
balance = 10000.00

# User 4 digit pin
pin = 1234

# The application status
status = True

print("Welcome to GTBank")
while status:
    user_pin = int(input("Please Enter Your 4 Digit Pin "))

    if user_pin == pin:
        print(" What would you like to do ")
        print("""
        1)        Balance
        2)        Withdraw
        3)        Deposit
        4)        Quit


        """)
        Option=int(input("Enter Option: "))

# User needs wants to check account balance
        if Option==1:
            print("Balance  ₦",balance)
            follow_up = print("Do You want to perform another transaction Yes(y)/ No(n)")
            trigger_status = input("Enter response ")
            trigger_status = trigger_status.upper()

            if trigger_status == 'N':
                status = False

# User wants to withdraw cash
        if Option==2:
            print("Balance  ₦",balance)
            Withdraw=float(input("Enter Withdraw amount ₦ "))
            if (Withdraw < balance):
                if Withdraw>0:
                    forewardbalance=(balance-Withdraw)
                    print("Foreward Balance  ₦",forewardbalance)
                    follow_up = print("Do You want to perform another transaction Yes(y)/ No(n)")
                    trigger_status = input("Enter response ")
                    trigger_status = trigger_status.upper()

                    if trigger_status == 'N':
                        status = False
                    
                elif Withdraw>balance:
                    print("No funs in account")
                else:
                    print("None withdraw made")
            else:
                print("Insufficient balance")
                follow_up = print("Do You want to perform another transaction Yes(y)/ No(n)")
                trigger_status = input("Enter response ")
                trigger_status = trigger_status.upper()

                if trigger_status == 'N':
                    status = False
                
# User wants to deposit cash
        if Option==3:
            print("Balance  ₦",balance)
            Deposit=float(input("Enter deposit amount ₦ "))
            if Deposit>0:
                forewardbalance=(balance+Deposit)
                print("Forewardbalance  ₦ ",forewardbalance)
                follow_up = print("Do You want to perform another transaction Yes(y)/ No(n)")
                trigger_status = input("Enter response ")
                trigger_status = trigger_status.upper()

                if trigger_status == 'N':
                    status = False
            else:
                print("None deposit made")

# User wants to exit 
        if Option==4:
            exit()
    else:
        print("The Pin Is Incorrect")
        follow_up = print("Do You want to perform another transaction Yes(y)/ No(n)")
        trigger_status = input("Enter response ")
        trigger_status = trigger_status.upper()

        if trigger_status == 'N':
            status = False