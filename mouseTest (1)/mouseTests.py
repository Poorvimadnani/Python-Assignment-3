import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
# COMP-2120/DIGIHUM-2220/COMP-9642 Assignment 3 Fall 2023
# Your Name: Poorvi Madnani
# Your Student Number: 251178757
# Date: 2023-11-15
# Course Name: Compsci 2120
# Instructor Name: Caro Strickland
# Description: This program reads in a text file containing data 
# about mice and their fight results. It then calculates the average win ratio
# for each dosage and plots the results. As well as also checks if the mouse_id is already in the result_dict
# and if not then it adds it to the dictionary and updates the win and total fight counts based on dosage and win or loss
# and then calculates and stores the average win ratio for the dosage and plots the values and adds a line of best fit
# and displays the plot
#Start with importing the libraries
import matplotlib.pyplot as plt
import numpy as np
def generateDictionary(textfile):
# Create an empty dictionary to store the results
    result_dict = {}
    
 # Open the text file and read the data line by line
    with open(textfile, 'r') as file:
        for line in file:
            line = line.strip().split(', ')
            mouse_id, dosage, win_or_loss = line
            
            # Check if the mouse_id is already in the result_dict
            if mouse_id not in result_dict:
                result_dict[mouse_id] = {'5mg/kg': [0, 0], '10mg/kg': [0, 0], '15mg/kg': [0, 0]}
            
    # Update the win and total fight counts based on dosage and win or loss
            if win_or_loss == 'W':
                result_dict[mouse_id][dosage][0] += 1
            result_dict[mouse_id][dosage][1] += 1
   # Calculate and store the average win ratio for the dosage 
    return result_dict
# Creating a function to calculate the average win ratios for each dosage
def calculateAverageWinRatios(data):
    # Create a dictionary to store average win ratios for each dosage
    average_ratios = {}
    
    # Iterate through the dosages
    dosages = ['5mg/kg', '10mg/kg', '15mg/kg']
    for dosage in dosages:
        total_wins = 0
        total_fights = 0
        
        # Iterate through mice and accumulate wins and fights for the current dosage
        for mouse_data in data.values():
            total_wins += mouse_data[dosage][0]
            total_fights += mouse_data[dosage][1]
        
        # Calculate and store the average win ratio for the dosage
        average_ratios[dosage] = total_wins / total_fights if total_fights > 0 else 0.0
  # Return the dictionary of average win ratios  
    return average_ratios
# Creating a function to plot the dosages and their corresponding values
def plotDosageInformation(dosage_info):
    
    # Extract the dosages and their corresponding values
    dosages = list(dosage_info.keys())
    values = [dosage_info[dosage] for dosage in dosages]
    
    # Sort dosages and its values in ascending order
    dosages, values = zip(*sorted(zip(dosages, values), key=lambda x: float(x[0].split('mg/kg')[0])))

    
    # Create an array of x-values for the dosages
    x = np.arange(len(dosages))
    
    # Create a figure and axis for the plot
    fig, ax = plt.subplots()
    
    # Plot the values
    plt.plot(x, values, marker='o', linestyle='-', label='Data')
    
    # Add labels to the x-axis
    ax.set_xticks(x)
    ax.set_xticklabels(dosages)
    
    # Add a line of best fit
    z = np.polyfit(x, values, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), linestyle='--', label='Line of Best Fit')
    
    # Add labels and a legend
    plt.xlabel('Dosage')
    plt.ylabel('Value')
    plt.title('Dosage Information')
    plt.legend()
    
    # Display the plot
    plt.grid(True)
    plt.show()

# Main program
data = generateDictionary('mouse_data.txt')
plotDosageInformation(calculateAverageWinRatios(data))
