# lab5.py
# By: Vanessa Arreola
# November 20, 2021
# SDEV 300
"""This program allows a user to select one of two csv files and perform
various histogram analysis for the datasets"""
import csv
import matplotlib.pyplot as plt
import re
import pandas as pd
import numpy as np


def show_menu():
    """Shows user the menu and allows them to pick a csv file"""
    # runs until user enters a valid entry
    print('Select the file you want to analyze')
    flag = False
    while not flag:
        print('a - Population Data\nb - Housing Data\nc - Exit the Program')
        user_choice = input(': ')
        if re.findall(r'[a-c]', user_choice):
            flag = True
        else:
            print('Please enter a valid choice')
    return user_choice


def get_choice_pop():
    """Gets and verifies the users choice for data analysis"""
    flag = False
    while not flag:
        user_choice = input(': ').lower()
        if re.findall(r'[a-d]', user_choice):
            flag = True
        else:
            print('Please enter a valid letter')
    return user_choice


def get_choice_housing():
    """Gets and verifies the users choice for data analysis"""
    flag = False
    while not flag:
        user_choice = input(': ').lower()
        if re.findall(r'[a-f]', user_choice):
            flag = True
        else:
            print('Please enter a valid letter')
    return user_choice


def find_quartiles(df):
    """Finds the statistical dispersion"""
    q1 = df.quantile(0.25)
    q3 = df.quantile(0.75)
    iqr = q3 - q1
    return iqr


def trim_data_pop(df, col):
    """Trims outliers from the dataframe"""
    ind = df[df[col] >= 150_000]
    print(ind)
    return ind


def trim_data_housing(df, col):
    """Trims outliers from the dataframe"""
    ind = df[df[col] <= 0]
    print(ind)
    return ind


def plot_histogram(data_frame, column):
    """Plots a histogram from the given data frame and column"""
    data_frame.hist(column=column, grid=True)
    plt.show()
    plt.close()


print('*************Welcome to the Python Data Analysis App*************')

while True:  # runs as long as user would like to use program
    # Calls show_menu and opens the correct csv file
    which_file = show_menu()

    if which_file == 'a':  # population data choice
        print('You have chosen Population Data')
        # opens the csv and loads data into a data frame from analyzing
        pop_frame = pd.read_csv('PopChange.csv')

        # allows user to choose a column to analyze
        while True:
            print('Select the column you want to analyze: ')
            print('a Pop Apr 1\nb Pop Jul 1\nc Change Pop\nd Exit Column')
            pop_op = get_choice_pop()

            # Find the indices of outliers in the data frame
            print('Outliers: ')
            trim_data_pop(pop_frame, 'Pop Apr 1')

            # executes the correct analysis based on user choice
            if pop_op == 'a':
                print('You selected Pop April 1')
                print('The statistics for this column are:')
                print(pop_frame['Pop Apr 1'].describe())
                pop_frame.drop(labels=[97, 223, 377, 501, 550], axis=0,
                               inplace=True)  # drops the outliers
                plot_histogram(pop_frame, 'Pop Apr 1')
            if pop_op == 'b':
                print('You selected Pop Jul 1')
                print('the statistics for this column are:')
                print(pop_frame['Pop Jul 1'].describe())
                pop_frame.drop(labels=[97, 223, 377, 501, 550], axis=0,
                               inplace=True)  # drops the outliers
                plot_histogram(pop_frame, 'Pop Jul 1')
            if pop_op == 'c':
                print('You selected Change in Pop')
                print('The statistics for this column are:')
                print(pop_frame['Change Pop'].describe())
                pop_frame.drop(labels=[97, 223, 377, 501, 550], axis=0,
                               inplace=True)  # drops the outliers
                plot_histogram(pop_frame, 'Change Pop')
            if pop_op == 'd':
                print('Thank you for choosing Population Data')
                break

    if which_file == 'b':  # Housing data choice
        print('You have chose Housing Data')
        # opens the csv and loads data into a data frame for analyzing
        housing_frame = pd.read_csv('Housing.csv')

        # allows a user to choose a column to analyze
        while True:
            print('Select the column you want to analyze: ')
            print('a Age\nb Bedrooms\nc Year Built\nd Rooms\ne Utility\n'
                  'f Exit Column')
            housing_op = get_choice_housing()

            # Find the indices of outliers in the data frame
            print('Outliers: ')
            trim_data_housing(housing_frame, 'AGE')

            q1 = housing_frame.quantile(0.25)
            q3 = housing_frame.quantile(0.75)
            iqr = q3 - q1

            if housing_op == 'a':
                print('You selected Age')
                print('the statistics for this column are:')
                print(housing_frame['AGE'].describe())
                plot_histogram(housing_frame, 'AGE')

            if housing_op == 'b':
                print('You selected Bedrooms')
                print('the statistics for this column are:')
                print(housing_frame['BEDRMS'].describe())
                plot_histogram(housing_frame, 'BEDRMS')
            if housing_op == 'c':
                print('You selected Year Built')
                print('the statistics for this column are:')
                print(housing_frame['BUILT'].describe())
                plot_histogram(housing_frame, 'BUILT')
            if housing_op == 'd':
                print('You selected Rooms')
                print('the statistics for this column are:')
                print(housing_frame['ROOMS'].describe())
                plot_histogram(housing_frame, 'ROOMS')
            if housing_op == 'e':
                print('Utility')
                print('the statistics for this column are:')
                print(housing_frame['UTILITY'].describe())
                plot_histogram(housing_frame, 'UTILITY')
            if housing_op == 'f':
                print('Thank you for choosing Housing Data')
                break
    if which_file == 'c':  # exits program
        print('Thank you for using the Python Data Analysis App')
        break
