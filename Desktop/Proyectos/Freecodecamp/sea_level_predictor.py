import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
  data = pd.read_csv('epa-sea-level.csv')

  plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label='Data')

  # Calculate the best-fit line for all the data
  slope, intercept, r_value, p_value, std_err = linregress(
      data['Year'], data['CSIRO Adjusted Sea Level'])

  # Create the line of best fit through 2050
  years = range(1880, 2051)
  sea_level_fit = intercept + slope * years
  plt.plot(years, sea_level_fit, 'r', label='Best Fit Line (1880-2050)')

  # Calculate the best-fit line for data from year 2000
  datosrecientes = data[data['Year'] >= 2000]
  slope_recent, intercept_recent, _, _, _ = linregress(
      recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

  # Create the line of best fit from year 2000 through 2050
  years_recent = range(2000, 2051)
  sea_level_fit_recent = intercept_recent + slope_recent * years_recent
  plt.plot(years_recent,
           sea_level_fit_recent,
           'g',
           label='Best Fit Line (2000-2050)')

  # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')

  # Save plot and return data for testing
  plt.savefig('sea_level_plot.png')
  return plt.gca()


# Call the function to generate the plot
draw_plot()
