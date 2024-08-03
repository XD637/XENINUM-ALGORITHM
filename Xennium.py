""" let's assume you have initially 10 xennium coins, call it iv (initial value). 
for each xennium coin you spend (sv - spend value), the true value of the one last xennium coin depreciates in a way, 
when the total xennium coin spent becomes 9 (in this case), 
the true value (tv) of the xennium coin becomes 0% (initially it was 100%), 
which means you can not spend the last xennium coin since it lost it's true value for you.
Means 1 became 0 """

#Xennium Algorithm

import matplotlib.pyplot as plt

class xennium:
    def __init__(self, iv):
        self.iv = iv  # initial value
        self.tv = 100  # initial true value
        self.depreciation_history = []  # list to store depreciation over time

    def x_algorithm(self):
        while self.iv > 1:  # Continue until only one coin is left
            sv = int(input("Enter the xennium to be spent: "))
            
            # Validate the input
            if sv > self.iv:
                print("Not enough xennium coins to spend.")
                break
            
            # Calculate remaining xennium coins and spent percentage
            self.iv -= sv  # subtract the spent amount
            spent_percentage = (sv / self.iv) * 100 if self.iv != 0 else 100 #spent percentage
            
            # Calculate depreciation and adjust true value
            depreciation = min(spent_percentage, self.tv) #check for bounds
            self.tv -= depreciation
            
            # Append true value to the history for plotting
            self.depreciation_history.append(self.tv)
        
        print("End of simulation. Remaining xennium coins:", self.iv)
        self.plot_depreciation()
    
    def plot_depreciation(self):
        # Plotting the depreciation history
        plt.plot(range(len(self.depreciation_history)), self.depreciation_history, marker='o')
        plt.xlabel('Time')
        plt.ylabel('True Value (%)')
        plt.title('Depreciation of xennium Coins Over Time')
        plt.grid(True)
        plt.show()

# funtion calling
if __name__ == "__main__":
    initial_xennium = 10
    xennium_simulator = xennium(initial_xennium)
    xennium_simulator.x_algorithm()

"""this algorithm shows the peculiar way of depreciation based on the how much you spend,
you may not realise but even if you spend the smallest amount , it changes the true value and depreciates it's value for you.
"""
