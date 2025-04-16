#SOURCE CODE FOR THE GRAPH: AIRMASS Vs. INSTRUMENTAL MAGNITUDE:
import numpy as np
import matplotlib.pyplot as plt
# Load the data from the first text file
data1 = np.loadtxt('C:\\Users\\27672\\Documents\\BLUE FILTER.csv', delimiter=',')
# Load the data from the second text file
data2 = np.loadtxt('C:\\Users\\27672\\Documents\\INDIGO FILTER1.csv', delimiter=',')
# Load the data from the third text file
data3 = np.loadtxt('C:\\Users\\27672\\Documents\\VIOLET FILTER1.csv', delimiter=',')
# Extract x and y columns for the first dataset (BLUE FILTER)
x1 = data1[:, 0]
y1 = data1[:, 5]
y1 = np.sort(y1)[::-1] # Sort and reverse the y values
x1 = np.linspace(min(x1), max(x1), len(y1)) # Adjust x accordingly
slope1, intercept1 = np.polyfit(x1, y1, 1) # Line of best fit
y_fit1 = slope1 * x1 + intercept1
# Extract x and y columns for the second dataset (INDIGO FILTER)
x2 = data2[:, 0]
y2 = data2[:, 5]
y2 = np.sort(y2)[::-1] # Sort and reverse the y values
x2 = np.linspace(min(x2), max(x2), len(y2)) # Adjust x accordingly
slope2, intercept2 = np.polyfit(x2, y2, 1) # Line of best fit
y_fit2 = slope2 * x2 + intercept2
# Extract x and y columns for the third dataset (VIOLET FILTER)
x3 = data3[:, 0]
y3 = data3[:, 5]y3 = np.sort(y3)[::-1] # Sort and reverse the y values
x3 = np.linspace(min(x3), max(x3), len(y3)) # Adjust x accordingly
slope3, intercept3 = np.polyfit(x3, y3, 1) # Line of best fit
y_fit3 = slope3 * x3 + intercept3
# Plot the data points and lines of best fit
plt.plot(x1, y1, marker='o', linestyle='-', color='b', label='BLUE FILTER Data Points')
plt.plot(x1, y_fit1, color='r', label='BLUE FILTER Line of Best Fit')
plt.plot(x2, y2, marker='s', linestyle='-', color='g', label='INDIGO FILTER Data Points')
plt.plot(x2, y_fit2, color='orange', label='INDIGO FILTER Line of Best Fit')
plt.plot(x3, y3, marker='d', linestyle='-', color='brown', label='VIOLET FILTER Data Points')
plt.plot(x3, y_fit3, color='purple', label='VIOLET FILTER Line of Best Fit')
# Add titles and labels
plt.title("Airmass Vs. Instrumental Magnitude")
plt.xlabel("Airmass")
plt.ylabel("Instrumental Magnitude")
plt.legend()
plt.grid(True)
# Display the slope and intercepts for all plots
plt.text(0.05, 0.95, f'BLUE FILTER:\nSlope: {slope1:.4f}\nIntercept: {intercept1:.4f}',
 transform=plt.gca().transAxes, fontsize=8, verticalalignment='top',
 bbox=dict(facecolor='white', alpha=0.5))
plt.text(0.05, 0.85, f'INDIGO FILTER:\nSlope: {slope2:.4f}\nIntercept: {intercept2:.4f}',
 transform=plt.gca().transAxes, fontsize=8, verticalalignment='top',
 bbox=dict(facecolor='white', alpha=0.5))
plt.text(0.05, 0.65, f'VIOLET FILTER:\nSlope: {slope3:.4f}\nIntercept: {intercept3:.4f}',
 transform=plt.gca().transAxes, fontsize=8, verticalalignment='top',
 bbox=dict(facecolor='white', alpha=0.5))
# Adjust layout to prevent overlap
plt.tight_layout()
# Display the plot
plt.show()