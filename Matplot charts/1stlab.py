import numpy as np
import matplotlib.pyplot as plt

# Given data
square_footage = np.array([1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000])
selling_prices = np.array([250, 290, 315, 380, 410, 450, 500, 525, 570, 610])

# Create scatter plot with specified marker and color
plt.figure(figsize=(8,6))
plt.scatter(square_footage, selling_prices, color='green', edgecolors='black', marker='o', label='House Data')

# Add labels and title
plt.xlabel('Square Footage(sq. ft.)')
plt.ylabel('Selling Price (in $1000s)')
plt.title('Relationship between House Size and Selling Price')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()