import matplotlib.pyplot as plt

# Given data
segments = ['Product A', 'Product B', 'Services', 'Licensing']
revenue_percentages = [45, 25, 15, 15]

# Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(revenue_percentages, labels=segments, autopct='%1.1f%%', 
        colors=['red', 'blue', 'green', 'orange'], startangle=140)

# Add title
plt.title("Distribution of Company Revenue by Business Segment")

# Show the plot
plt.show()
