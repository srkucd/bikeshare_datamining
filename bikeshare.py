import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

month_dict = {1: 'january',
              2: 'february',
              3: 'march',
              4: 'april',
              5: 'may',
              6: 'june'}

weekday_dict = {1: 'monday',
                2: 'tuesday',
                3: 'wednesday',
                4: 'thursday',
                5: 'friday',
                6: 'saturday',
                7: 'sunday'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("Insert the name of city you are interested in(Chicago, New York City, Washington)")
        if city.lower() in CITY_DATA.keys():
            print('Okay, got it. you choose ' + city.title() + '.')
            break
        else:
            print("Invalid data, please confirm your input city is Chicago, New York City or Washington.")
            continue

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month_input = input("Insert the number of the month you are interested.[Jan(1)-Jun(6)], for unfiltered data, please input 'all'.")
        if month_input in str(list(month_dict.keys())):
            month = month_dict.get(int(month_input))
            print('Okay, got it. you choose ' + month.title() + '.')
            break
        elif month_input == 'all':
            month = 'all'
            print("Okay, got it, no month filter selected.")
            break
        else:
            print("Invalid data, please confirm your input between 1-6")
            continue
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day_input = input("Insert the weekday number you are interested.[Mon-Sun:1-7],for unfiltered data, please input 'all'.")
        if day_input in str(list(weekday_dict.keys())):
            day = weekday_dict.get(int(day_input))
            print('Okay, got it. you choose ' + day.title() + '.')
            break
        elif day_input == 'all':
            day = 'all'
            print('Okay, got it, no weekday filter selected.')
            break
        else:
            print("Invalid data, please confirm your input between 1-7")
            continue

    print('City: '+city.title())
    print('Month: '+month.title())
    print('Weekday: '+day.title())



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA.get(get_filters()[0]))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = month_dict.values()
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month


    # TO DO: display the most common day of week


    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
