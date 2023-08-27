class BankAccount:
    # class object attribute
    no_of_cust = 0
    acc_num = 42376
    def __init__(self, name, mobile_no, initial_depo, pin):
        self.name = name
        self.cust_acc_num = BankAccount.acc_num
        self.mobile_no = mobile_no
        self.acc_balance = initial_depo
        self.pin = pin
        BankAccount.acc_num = BankAccount.acc_num + 1
        BankAccount.no_of_cust = BankAccount.no_of_cust + 1

    def basic_details(self):
        print(f"User: {self.name}\t Account No: {self.cust_acc_num}\t Balance: Rs.{self.acc_balance}")

    def deposit(self):
        amount = int(input("Enter the deposit amount: "))
        if amount > 0:
            self.acc_balance = self.acc_balance + amount
            print(f"Transanction completed. Current Balance: Rs.{self.acc_balance}")
        else:
            print("Invalid amount")
    def withdrawl(self):
        amount = int(input("Enter the withdrawl amount: "))
        if amount > 0 and amount <= self.acc_balance:
            self.acc_balance = self.acc_balance - amount
            print(f"Transanction completed. Current Balance: Rs.{self.acc_balance}")
        else:
            print("Invalid amount")
    def payment(self, other):
        amount = int(input("Enter the amount to be transferred amount: "))
        if amount > 0 and amount <= self.acc_balance:
            self.acc_balance = self.acc_balance - amount
            other.acc_balance = other.acc_balance + amount
            print(f"Transanction completed. Current Balance: Rs.{self.acc_balance}")
        else:
            print("Invalid amount")
if __name__ == "__main__":
    cust1 = BankAccount(name="Ashwanth", mobile_no=7558168777, initial_depo=1000, pin=123)
    cust2 = BankAccount(name="Arthi", mobile_no=75589754440, initial_depo=1200, pin=456)
    print("No of cutomers: ", BankAccount.no_of_cust)
    cust1.basic_details()
    cust2.basic_details()
    cust1.deposit()
    cust1.basic_details()
    cust2.withdrawl()
    cust2.basic_details()
    cust1.payment(cust2)
    cust2.basic_details()