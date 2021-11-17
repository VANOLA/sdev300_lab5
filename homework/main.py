# lab5.py
# By: Vanessa Arreola
# November 20, 2021
# SDEV 300
"""This program allows a user to select one of two csv files and perform
various histogram analysis for the datasets"""
import re
import matplotlib.pyplot as plt
import pandas as pd


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


def trim_data_housing(data_frame, col):
    """Trims outliers from the dataframe"""
    index = data_frame.index
    if col == 'Pop Apr 1':
        condition = data_frame[col] >= 150_000
    if col == 'AGE':
        condition = data_frame[col] <= 0
    if col == 'UTILITY':
        condition = data_frame[col] >= 600
    age_indices = index[condition]
    age_indices_list = age_indices.tolist()
    return age_indices_list


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
        pop_frame.drop(labels=trim_data_housing(pop_frame, 'Pop Apr 1'),
                       axis=0, inplace=True)

        # allows user to choose a column to analyze
        while True:
            print('Select the column you want to analyze: ')
            print('a Pop Apr 1\nb Pop Jul 1\nc Change Pop\nd Exit Column')
            pop_op = get_choice_pop()

            # Find the indices of outliers in the data frame
            print('Outliers: ')

            # executes the correct analysis based on user choice
            if pop_op == 'a':
                print('You selected Pop April 1')
                print('The statistics for this column are:')
                print(pop_frame['Pop Apr 1'].describe())
                plot_histogram(pop_frame, 'Pop Apr 1')
            if pop_op == 'b':
                print('You selected Pop Jul 1')
                print('the statistics for this column are:')
                print(pop_frame['Pop Jul 1'].describe())
                plot_histogram(pop_frame, 'Pop Jul 1')
            if pop_op == 'c':
                print('You selected Change in Pop')
                print('The statistics for this column are:')
                print(pop_frame['Change Pop'].describe())
                plot_histogram(pop_frame, 'Change Pop')
            if pop_op == 'd':
                print('Thank you for choosing Population Data')
                break

    if which_file == 'b':  # Housing data choice
        print('You have chose Housing Data')
        # opens the csv and loads data into a data frame for analyzing
        housing_frame = pd.read_csv('Housing.csv')
        housing_frame.drop(labels=trim_data_housing(housing_frame, 'AGE'),
                           axis=0, inplace=True)
        # pylint: disable=E1101
        housing_frame.drop(labels=trim_data_housing(housing_frame, 'UTILITY'),
                           axis=0, inplace=True)

        # allows a user to choose a column to analyze
        while True:
            print('Select the column you want to analyze: ')
            print('a Age\nb Bedrooms\nc Year Built\nd Rooms\ne Utility\n'
                  'f Exit Column')
            housing_op = get_choice_housing()

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
