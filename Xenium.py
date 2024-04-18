""" let's assume you have initially 10 xenium coins, call it iv (initial value). 
for each xenium coin you spend (sv), the value of the one last xenium coin depreciates in a way, 
when the total xenium coin spent becomes 9 (in this case), 
the true value (tv) of the xenium coin becomes 0% (initially it is 100%), 
which means you can not spend the last xenium coin since it lost it's true value.
Means 1 became 0 """
#Xenium Algorithm

import matplotlib.pyplot as plt

class Xenium:
    def __init__(self, iv):
        self.iv = iv  # initial value
        self.tv = 100  # initial true value
        self.depreciation_history = []  # list to store depreciation over time

    def x_algorithm(self):
        while self.iv > 1:  # Continue until only one coin is left
            sv = int(input("Enter the xenium to be spent: "))
            
            # Validate the input
            if sv > self.iv:
                print("Not enough xenium coins to spend.")
                break
            
            # Calculate remaining xenium coins and spent percentage
            self.iv -= sv  # subtract the spent amount
            spent_percentage = (sv / self.iv) * 100 if self.iv != 0 else 100 #spent percentage
            
            # Calculate depreciation and adjust true value
            depreciation = min(spent_percentage, self.tv) #check for bounds
            self.tv -= depreciation
            
            # Append true value to the history for plotting
            self.depreciation_history.append(self.tv)
        
        print("End of simulation. Remaining xenium coins:", self.iv)
        self.plot_depreciation()
    
    def plot_depreciation(self):
        # Plotting the depreciation history
        plt.plot(range(len(self.depreciation_history)), self.depreciation_history, marker='o')
        plt.xlabel('Time')
        plt.ylabel('True Value (%)')
        plt.title('Depreciation of Xenium Coins Over Time')
        plt.grid(True)
        plt.show()

# funtion calling
if __name__ == "__main__":
    initial_xenium = 10
    xenium_simulator = Xenium(initial_xenium)
    xenium_simulator.x_algorithm()

"""this algorithm shows the peculiar way of depreciation based on the how much you spend,
you may not realise but even if you spend the smallest amount , it changes the true value and depreciates it.
what happens when the depriciation is recurive? means it itself changes the Xenium value, find out!!!"""
