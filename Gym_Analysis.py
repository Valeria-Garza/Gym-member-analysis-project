# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:48:21 2024

@author: vgarz
"""
import pandas as pd
import statsmodels.formula.api as smf

# Block Comment (Overview)
'''
Purpose:
This program analyzes a dataset containing gym member exercise tracking data. 
It provides functions to compute descriptive statistics, correlations, and a regression model.

Inputs:
The input dataset is a CSV file, read into a Pandas DataFrame.

Processing:
1. Descriptive statistics function to summarize the dataset.
2. Correlation function to analyze relationships between numerical columns.
3. Regression model function to analyze relationships between independent and dependent variables, in this case weight and calories.

Outputs:
The program prints descriptive statistics, correlation matrices, and regression model summaries.
'''

# Read the dataset

gym_DF = pd.read_csv('gym_members_exercise_tracking.csv')

# Set pandas display options for better readability
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.width', 1000)

print(gym_DF)
print("Dataset loaded successfully.")

# Function to compute descriptive statistics
def descriptive_stats(df):
    print("Function descriptive_stats has started.")
    
    def format_descriptive_stats(stats):
        # Nested function to format stats for display
        print("Nested function format_descriptive_stats has started.")
        return stats.to_string()
    
    stats = df.describe()  # Compute descriptive statistics
    formatted_stats = format_descriptive_stats(stats)  # Format the stats
    print("Descriptive Statistics:\n" + formatted_stats)  # Print formatted stats

# Function to compute correlations
def compute_correlations(df):
    print("Function compute_correlations has started.")
    
    # Select only numerical columns. Excludes Gender and Workout_Type.
    numeric_df = df.select_dtypes(include='number')
    correlations = numeric_df.corr()  # Compute correlation matrix
    print("Correlation Matrix:")
    print(correlations)  # Print the correlation matrix
    return correlations

# Function to build a regression model
def regression_model(df, independent_var, dependent_var):
    print("Function regression_model has started.")
    
    # Construct the string for the regression formula
    formula = dependent_var + " ~ " + independent_var
    print("Building regression model for " + dependent_var + " based on " + independent_var + "...\n")
    
    # Create and fit the regression model
    model = smf.ols(formula, data=df).fit()
    
    # Print and return the regression model summary
    print("Regression Model Summary:\n")
    print(model.summary())
    return model.summary()

# Main function to control the program execution
def main():
    print("Main function has started.")
      
    # Call the descriptive stats function
    print("Call function descriptive_stats to create summary statistics for the dataset.")
    descriptive_stats(gym_DF)
    
    # Call the correlation function
    print("Call function compute_correlations to analyze correlations in the dataset.")
    compute_correlations(gym_DF)
    
    # Call the regression model function
    print("Call function regression_model to create a regression model.")
    regression_model(gym_DF, "Weight_kg", "Calories_Burned")  #Weight_kg as independent var and Calories_Burned as dependent var

# Run the main function
if __name__ == "__main__":
    main()
