data = {}

class BudgetApp:

    def __init__(self):
        
        self.category = 'food'
        self.amount = 1500
        self.menu()

    # METHODS
    def menu(self):
        
        print('**** Welcome to Knight BudgetApp ****')
        
        user = int(input('\n *** What would you like to do? *** \n press (1) to create a new budget \n press (2) to deposit into a budget \n press (3) to make a withdrawal from chosen budget \n press (4) to check your budget balance \n press (5) to transfer between budget categories \n press (6) to quit. \n'))

        if user == 1:

            self.newBudget()
        
        elif user == 2:

            self.deposit()

        elif user == 3:

            self.withdrawal()

        elif user == 4:

            self.balance()

        elif user == 5:

            self.transfer()
            
        elif user == 6:

            self.quit()

        else:

            print('Invalid input \n')
            
            self.menu()

    
    def newBudget(self):

        print('\n**** Creating a new budget **** \n')
        
        categoryName = input('Enter category name \n')
        amount = int(input('Enter budget amount \n $'))

        data[categoryName] = amount

        print(f'New budget has been created: Budget {categoryName} was setup with ${amount} \n')

        try:
            selected = int(input('\n Do you want to perfom another transaction? \n Press (1) To create a new budget. \n Press (2) To continue to main menu. \n Press (3) To quit. \n'))

        except:

            print('Invalid input \n')
            self.menu()

        if(selected == 1):
            
            self.newBudget()

        elif(selected == 2):

            self.menu()
        
        elif(selected == 3):

            self.quit()

        else:

            print('Invalid input \n')
            self.quit()



    def deposit(self):

        print('**** Depositing into your budget **** \n')

        for key, value in data.items():
            print(f'- {key}')
        
        try:
            selected = int(input('\n Thank you for depositing into your budget. \n Do you want to perfom another transaction? \n Press (1) To continue to the main menu. \n Press (2) To quit the app. \n'))

        except:

            print('Invalid input \n')
            self.menu()

        if(selected == 1):
            
            self.menu()

        elif(selected == 2):

            self.quit()

        else:

            print('Invalid input \n')
            self.quit()

    def balance(self):

        print('**** Your available balance is been fetched **** \n')
        
        try:
            selected = int(input('Do you want to perfom another transaction? \n Press (1) To continue to the main menu. \n Press (2) To quit the app. \n'))

        except:

            print('Invalid input \n')
            self.menu()

        if(selected == 1):
            
            self.menu()

        elif(selected == 2):

            self.quit()

        else:

            print('Invalid input \n')
            self.quit()


    def withdrawal(self): 

        print('**** Withdrawal process is ongoing.... **** \n')
        
        try:
            selected = int(input('Do you want to perfom another transaction? \n Press (1) To continue to the main menu. \n Press (2) To quit the app. \n'))

        except:

            print('Invalid input \n')
            self.menu()

        if(selected == 1):
            
            self.menu()

        elif(selected == 2):

            self.quit()

        else:

            print('Invalid input \n')
            self.quit()


    def transfer(self):

        print('**** Your transfer is ongoing.... **** \n')
        
        try:
            selected = int(input('Do you want to perfom another transaction? \n Press (1) To continue to the main menu. \n Press (2) To quit the app. \n'))

        except:

            print('Invalid input \n')
            self.menu()

        if(selected == 1):
            
            self.menu()

        elif(selected == 2):

            self.quit()

        else:

            print('Invalid input \n')
            self.quit()
    
    
    def quit(self):

        try:
            selected = int(input('Are you sure, you want to quit? \n Press (1) To quit \n Press (2) To continue \n'))

        except:

            print('Invalid input \n')
            self.quit()

        if(selected == 1):
            
            print('\n We hope you had a good budgeting experience, sayanora.')

        elif(selected == 2):

            self.menu()

        else:

            print('Invalid input \n')
            self.quit()



BudgetApp()






