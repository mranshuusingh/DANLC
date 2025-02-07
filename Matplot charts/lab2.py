import matplotlib.pyplot as plt

# Given data
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]


# Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', 
        colors=['red', 'blue', 'green', 'orange', 'magenta'], startangle=140)

# Add title
plt.title('Monthly Income Distribution by Source')

# Show the plot
plt.show()
