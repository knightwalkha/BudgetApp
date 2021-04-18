import os

database = {}

class BudgetApp:

    def __init__(self):
        
        os.system('cls')
        self.category = 'food'
        self.amount = 1500
        self.menu()

    # METHODS
    def menu(self):
        
        os.system('cls')
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
        n = int(input('Number of elements: '))

        for i in range(n):
            category = input('Enter your budget category: \n')
            amount = int(input('Enter your budget amount: \n $'))
            database.update({category:amount})
            print(database)
            
        self.menu()


    def deposit(self):

        print('**** Depositing into your budget **** \n')
        
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




# database = {}

# categoryOpen = True

# while categoryOpen:

#     categoryName = input('What new budget category are you creating \n')
#     amount = int(input('What is the amount you want to budget for this category \n $'))

#     # Stores the response in the dictionary
#     database[categoryName] = amount

#     repeat = input('Do you want to create another budget category? \n')
#     if repeat == 'no':
#         categoryOpen = False


# # To get the data in database
# print('\n ***** category line *****')
# for categoryName, amount in database.items():
#     print(categoryName + 'has' + amount + 'rent')






