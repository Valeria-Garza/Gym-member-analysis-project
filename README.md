# Gym Member Exercise Tracking Analysis

This project performs analysis on a gym member exercise tracking dataset. The primary goal is to compute descriptive statistics, correlations, and build a regression model to understand relationships between various exercise-related factors like weight and calories burned.


## Project Overview

This Python script loads a CSV file containing gym member exercise tracking data and performs the following tasks:
1. Computes descriptive statistics of the dataset.
2. Analyzes correlations between numerical variables.
3. Builds a regression model to analyze relationships between weight and calories burned.

## Data Description

The dataset, `gym_members_exercise_tracking.csv`, contains information about gym members' exercise activities, including:
- `Weight_kg`: Weight of the gym member (independent variable in the regression model).
- `Calories_Burned`: Number of calories burned during a workout (dependent variable in the regression model).
- Other columns may contain additional details such as workout types, duration, etc.

## Steps and Analysis

1. **Descriptive Statistics**: Summarize the dataset and display basic statistics for each column.
2. **Correlation Matrix**: Compute and display correlations between numerical features.
3. **Regression Model**: Create a regression model to predict `Calories_Burned` based on `Weight_kg`.

## Technologies Used

- **Python**: The main programming language.
- **Libraries**:
  - `pandas` for data manipulation.
  - `statsmodels` for building the regression model.
