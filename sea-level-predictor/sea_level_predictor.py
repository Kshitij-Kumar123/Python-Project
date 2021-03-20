import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data=df, x="Year", y="CSIRO Adjusted Sea Level")

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    year = np.arange(1880, 2050)

    plt.plot(year, intercept + slope*year, "r")
    # Create second line of best fit
    from_2000 = df.loc[df["Year"] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(from_2000["Year"], from_2000["CSIRO Adjusted Sea Level"])

    year = np.arange(2000, 2050)
    plt.plot(year, intercept + slope*year, "r")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level")
    plt.title("Rising Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()