# Katrina Wilson
# kwils@uncc.edu
# ITSC3155: Bank Account Assigment

class BankAccount:
    title= "Wilson Bank";

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name;
        self.current_balance = current_balance;
        self.minimum_balance = minimum_balance;

    def deposit(self, amount):
        self.current_balance += amount;
        print("** Deposit successful.");

    def withdraw(self, amount):
        if (self.current_balance-amount <= self.minimum_balance):
            print("** Insufficient funds");
        else:
            self.current_balance -= amount;
            print("** Withdraw successful.");


    def print_customer_information(self):
        print("Bank Name: " + self.title);
        print(self.customer_name);
        print(self.current_balance);
        print();

p1 = BankAccount("Katrina", 400, 100);
p1.print_customer_information();
p1.deposit(50);
p1.withdraw(70);
p1.print_customer_information();

p2 = BankAccount("Sam", 100, 100);
p2.print_customer_information();
p2.withdraw(30);
p2.print_customer_information();


