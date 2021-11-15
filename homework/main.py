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


def show_menu():
    """Shows user the menu and allows them to pick a csv file"""
    # runs until user enters a valid entry
    print('Select the file you want to analyze')
    flag = False
    while not flag:
        print('a - Population Data\nb - Housing Data\nc - Exit the Program')
        user_choice = input(': ')
        # if choice == 'a':
        #     return 'a'
        # if choice == 'b':
        #     return 'b'
        # if choice == 'c':

        #     return 'c'
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


print('*************Welcome to the Python Data Analysis App*************')

while True:
    # Calls show_menu and opens the correct csv file
    which_file = show_menu()
    if which_file == 'c':  # exits program
        print('Thank you for using the Python Data Analysis App')
        break
    if which_file == 'a':  # population data choice
        print('You have chosen Population Data')

        # allows user to choose a column to analyze
        while True:
            print('Select the column you want to analyze: ')
            print('a Pop Apr 1\nb Pop Jul 1\nc Change Pop\nd Exit Column')
            pop_op = get_choice_pop()

            # opens the csv and loads data into a data frame from analyzing
            pop_frame = pd.read_csv('PopChange.csv')
            pd.set_option('display.max_columns', None)
            # print(pop_frame)

            # execute the correct analysis based on user choice
            if pop_op == 'a':
                print('You selected Pop April 1')
                print('The statistics for this column are:')
                print(pop_frame['Pop Apr 1'].describe())
                # hist = pop_frame['Pop Apr 1'].hist()
                hist = pop_frame.hist(column='Pop Apr 1', grid=True)
                plt.show()
                plt.close()
            if pop_op == 'd':
                print('Thank you for choosing Population Data')
                break

