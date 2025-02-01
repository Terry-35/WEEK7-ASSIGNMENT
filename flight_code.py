#!/usr/bin/env python3

"""
Script to load and analyze the flights dataset using pandas and matplotlib.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Load dataset
    try:
        df = pd.read_csv('flights.csv')
        print("Dataset loaded from 'flights.csv'.")
    except FileNotFoundError:
        print("Error: 'flights.csv' not found.")
        return

    # Display the first 5 rows
    print("First 5 rows:")
    print(df.head())

    # Check for missing values
    print("\nMissing values:")
    print(df.isnull().sum())

    # Create a date column from 'year' and 'month'
    try:
        df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'] + '-01')
        df.sort_values('date', inplace=True)
    except Exception as e:
        print("Error creating date column:", e)

    # Display statistical summary
    print("\nStatistical summary:")
    print(df.describe())

    # Group by month and calculate average passengers
    grouped = df.groupby("month")["passengers"].mean().reset_index()
    print("\nAverage passengers per month:")
    print(grouped)

    # Set a seaborn style
    sns.set(style="whitegrid")

    # Line Plot: Airline passengers over time
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['passengers'], marker='o', label='Passengers')
    plt.title('Monthly Airline Passengers Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Passengers')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
