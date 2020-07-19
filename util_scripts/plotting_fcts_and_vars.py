# Standard imports
import sys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Global variables to be used in scripts and notebooks

years = [str(y) for y in range(2001,2018)]

columns = ["Area code", "Area name"] + years

growth_boroughs = ['Greenwich', 'Hackney', 'Newham', 'Tower Hamlets',
                   'Barking and Dagenham', 'Waltham Forest']

boroughs = ['City of London', 'Barking and Dagenham', 'Barnet', 'Bexley',
       'Brent', 'Bromley', 'Camden', 'Croydon', 'Ealing', 'Enfield',
       'Greenwich', 'Hackney', 'Hammersmith and Fulham', 'Haringey',
       'Harrow', 'Havering', 'Hillingdon', 'Hounslow', 'Islington',
       'Kensington and Chelsea', 'Kingston-upon-Thames', 'Lambeth',
       'Lewisham', 'Merton', 'Newham', 'Redbridge',
       'Richmond-upon-Thames', 'Southwark', 'Sutton', 'Tower Hamlets',
       'Waltham Forest', 'Wandsworth', 'Westminster']

west_boroughs = list(set(boroughs).difference(set(growth_boroughs)))

types = ["Bus", "Underground", "DLR", "Tram", "Overground", "Emirates Airline", "TfL Rail"]

# -----------------------------------------------------------------------------
# Global plotting options

FIGSIZE = (10, 6)
YEAR_XLABEL = 'Year'

PLOTS_DIR = '../plots'


# -----------------------------------------------------------------------------
# Plotting functions

def plot_boroughs(data):
    """
    Plots the growth (6 East London) boroughs

    data: pd.DataFrame with following columns (all names as strings):
            Area code, Area name, 2001, 2002, ..., 2016, 2017
    """
    plt.figure(figsize=FIGSIZE)
    plt.grid()

    plt.xlabel(YEAR_XLABEL)
    plt.xticks(np.arange(0,18),years, rotation=90)

    for borough in growth_boroughs:
        borough_by_year = data[data['Area name'] == borough]
        if borough_by_year.empty:
            continue
        borough_by_year = borough_by_year.drop(['Area code', 'Area name'], axis=1).values[0]
        # plot by year
        plt.plot(borough_by_year, label=borough)

    plt.legend()
    plt.show()


def plot_all_boroughs(data):
    """
    Plots the all boroughs:
        growth_boroughs (6 East London) in thick colourful lines
        west_boroughs (the rest) in thin dotted gray lines

    data: pd.DataFrame with following columns (all names as strings):
            Area code, Area name, 2001, 2002, ..., 2016, 2017
    """
    plt.figure(figsize=FIGSIZE)
    plt.grid()

    plt.xlabel(YEAR_XLABEL)
    plt.xticks(np.arange(0, 18), years, rotation=90)

    for borough in west_boroughs:
        borough_by_year = data[data['Area name'] == borough]
        if borough_by_year.empty:
            continue
        borough_by_year = borough_by_year.drop(['Area code','Area name'], axis=1).values[0]
        plt.plot(borough_by_year, color='gray', linewidth=1, linestyle=':')


    for borough in growth_boroughs:
        borough_by_year = data[data['Area name'] == borough]
        if borough_by_year.empty:
            continue
        borough_by_year = borough_by_year.drop(['Area code','Area name'], axis=1).values[0]
        plt.plot(borough_by_year, label=borough, linewidth=2)

    plt.legend()
    plt.show()


def plot_stations(data, col, highlight_stations, see_stations):
    """
    TODO: complete docstring
    """
    plt.figure(figsize=FIGSIZE)
    plt.grid()

    plt.xlabel(YEAR_XLABEL)
    plt.xticks(np.arange(0,18), years, rotation=90)


    for station in see_stations:
        station_by_year = data[data['station'] == station]
        if station_by_year.empty:
            continue
        station_by_year = station_by_year[col].values
        if station in highlight_stations:
            plt.plot(station_by_year, label=station, linewidth=2)
        else:
            plt.plot(station_by_year, color='gray', linewidth=1, linestyle=':')

    plt.legend()
    plt.show()


def plot_all_stations(data, col, see_stations):
    """
    TODO: complete docstring
    """
    plt.figure(figsize=FIGSIZE)
    plt.grid()

    plt.xlabel(YEAR_XLABEL)
    plt.xticks(np.arange(0,18), years, rotation=90)


    for station in see_stations:
        station_by_year = data[data['station'] == station]
        if station_by_year.empty:
            continue
        station_by_year = station_by_year[col].values
        if station in growth_stations:
            plt.plot(station_by_year, label=station, linewidth=2)
        else:
            plt.plot(station_by_year, color='gray', linewidth=1, linestyle=':')
    plt.legend()
    plt.show()


def plot_stations_percentage_changes(data, col, highlight_stations, see_stations):
    """
    TODO: complete docstring
    """
    plt.figure(figsize=FIGSIZE)
    plt.grid()

    plt.xlabel(YEAR_XLABEL)
    plt.xticks(np.arange(0,18),years, rotation=90)

    for station in see_stations:
        station_by_year = data[station]
        if station_by_year.empty:
            continue
        station_by_year = station_by_year[col].values
        if station in highlight_stations:
            plt.plot(station_by_year, label=station, linewidth=2)
        else:
            plt.plot(station_by_year, color='gray', linewidth=1, linestyle=':')

    plt.legend()
    plt.show()
