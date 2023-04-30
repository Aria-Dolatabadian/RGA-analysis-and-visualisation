import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('RGA.csv')

# Initialize dictionaries to store the counts
total_counts = {}
type_counts = {}

# Iterate over the columns representing chromosomes
for chromosome_column in df.columns[1:]:
    # Count the total number of RGAs in the current chromosome
    total_rga_count = df[chromosome_column].count()
    total_counts[chromosome_column] = total_rga_count

    # Count the number of each type of RGA on the current chromosome
    type_rga_counts = df[chromosome_column].value_counts().to_dict()
    type_counts[chromosome_column] = type_rga_counts

# Create a DataFrame to store the results
results = pd.DataFrame({'Chromosome': df.columns,
                        'Total RGA Count': df.apply(lambda x: x.count(), axis=0),
                        'Type Counts': df.apply(lambda x: x.value_counts().to_dict(), axis=0)})

# Split the Type Counts column into separate columns
results = pd.concat([results.drop('Type Counts', axis=1),
                     results['Type Counts'].apply(pd.Series)], axis=1)

# Export the results as a new CSV file
results.to_csv('results.csv', index=False)




import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('results.csv')

# Get the column names for the RGA types
rga_types = df.columns[2:]

# Set the chromosome column as the index
df.set_index('Chromosome', inplace=True)

# Calculate the percentage of each RGA type on each chromosome
df_percentage = df[rga_types].div(df[rga_types].sum(axis=1), axis=0) * 100

# Plot the stacked bar chart with percentages
df_percentage.plot(kind='bar', stacked=True)
plt.xlabel('Chromosome')
plt.ylabel('Percentage')
plt.title('Percentage of RGA Types on Each Chromosome')
plt.xticks(rotation='vertical')

# Move the legend outside of the plot
plt.legend(bbox_to_anchor=(1, 1), loc='upper left')

plt.tight_layout()  # Ensures the legend is not cut off
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('results.csv')

# Get the column names for the RGA types
rga_types = df.columns[2:]

# Set the chromosome column as the index
df.set_index('Chromosome', inplace=True)

# Plot the stacked bar chart
df[rga_types].plot(kind='bar', stacked=True)
plt.xlabel('Chromosome')
plt.ylabel('RGA Count')
plt.title('RGA Counts on Each Chromosome')
plt.xticks(rotation='vertical')

# Move the legend outside of the plot
plt.legend(bbox_to_anchor=(1, 1), loc='upper left')

plt.tight_layout()  # Ensures the legend is not cut off
plt.show()
