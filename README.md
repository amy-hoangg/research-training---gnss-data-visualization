# research-training---gnss-data-visualization
# GNSS Data Visualization with React Native

## Overview

This repository contains a Dash app that visualizes GNSS (Global Navigation Satellite System) data from a CSV file. The app consists of three tabs: Measurement, Map, and Setting. Each tab displays different data visualizations.

## Dependencies

- datetime
- dash
- pandas
- plotly.express
- plotly.graph_objs

## Variables

- `df`: A pandas DataFrame that stores the data loaded from the CSV file.

## Functions

### 1. `app.layout`

Defines the layout of the Dash app, including a navbar with three buttons, a header with the app title, and a placeholder div for content.

### 2. `@app.callback`

A decorator that defines the callback function for all tab clicks. It takes three inputs, representing the number of times each tab has been clicked, and returns the content for the selected tab.

## Usage

1. Load the data into a CSV file with the filename 'navigation.csv' and the date_time column parsed as datetime.
2. Run the module to launch the Dash app.
3. Click on one of the three tabs to view the corresponding data visualization.

## Content Details

### Measurement Tab

This tab allows you to visualize GNSS measurement data. It includes:

- A date-time selector for the measurement start time.
- A date-time selector for the measurement stop time.
- A data selector for the measurement data to be plotted.
- A button to plot the selected data.
- A display area to show the resulting plot.

### Map Tab

This tab allows you to visualize GNSS data on a map. It includes the same date-time selectors and data selector as the Measurement tab. The plotted data is displayed on a map with longitude and latitude as coordinates.

### Setting Tab

This tab is for configuring app settings.

## Functions

### 1. `display_content`

This function takes in three parameters: `measurement_clicks`, `map_clicks`, and `setting_clicks`. It updates the content of the tabs in the Dash application based on the tab clicks.

### 2. `plot_measurement_data`

This function plots selected measurement data based on parameters like `start_time`, `stop_time`, `data_type`, `longitude`, and `latitude`. It creates a scatter plot of the selected measurement data against time, with longitude and latitude on the x and y axes.

### 3. `plot_map_data`

This function plots selected map data based on parameters like `start_time`, `stop_time`, `longitude`, and `latitude`. It creates a scatter plot of the longitude and latitude data, with color and size mapped to the time data.

### 4. `update_measurement_plot`

This callback function updates the measurement plot based on the selected data type and time range.

### 5. `update_map`

This callback function updates the map plot based on the selected data type and time range.

## Usage

Feel free to customize and enhance this app for your specific GNSS data visualization needs. If you have any questions or need assistance, please don't hesitate to reach out.

Happy data visualization! 📊🚀
