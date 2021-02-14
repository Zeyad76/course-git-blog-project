import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input("\nPlease enter the name of city from chicago, new york city, washington to explore bike share data: ").lower()

    while city.lower() not in ['chicago', 'new york city', 'washington']:
        city = input( "invalid city!, please enter a valid city name: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("\nPlease enter the name of month from the next January, February, March, April, May, June :").lower()
    
    while month.lower() not in ['january','february','march','april','may','june']:
        month = input( "invlid month!, please enter a valid month: ").lower()     

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please enter the day from Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday :").lower()

    while day.lower() not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
        day = input('invalid day!, please enter a valid day: ').lower()

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
    #TO DO: Load the data to df:
    df = pd.read_csv(CITY_DATA[city])
    
    #TO DO: convert the Start Time to datetime:
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #TO DO: create new two colums Month and Day:
    df['Month'] = df['Start Time'].dt.month
    df['Day_of_week'] = df['Start Time'].dt.day_name() ## dt.weekday_name can be use also

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('The most popular month: ', popular_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday
    popular_day = df['day_of_week'].mode()[0]
    print('The most popular day of week: ', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular start hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('This is the most commonly used start station:\n',common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('This is the most commonly used end station:\n',common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    df['frequent_combination'] = df['Start Station'] + ' to ' + df['End Station']
    frequent_combination = df['frequent_combination'].mode()[0]
    print('This is the most frequent combination of start station and end station trip:\n', frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('\nThe total travel time: {}'.format(total_travel))

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('\nThe mean travel time: {}'.format(mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users_types = df['User Type'].value_counts()
    print('counts of users types:\n', users_types)
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\ncount of gender: \n', gender_counts)
    else:
        print('\nOh!There is no available data for Gender')

    # TO DO: Display earliest, most recent, and most common year of birth
    #earliest year of birth
    if 'Brith Year' in df.columns:
        
        earliest_year = df['Birth Year'].min()
        print('\nEarliest year of birth:\n', earliest_year)
        #most recent year of birth
        recent_year = df['Birth Year'].max()
        print('\nMost recent year of birth:\n', recent_year)
        #most common year of birth
        common_year = df['Birth Year'].mode()[0]
        print('\nMost common year of birth:\n', common_year)
        
    else:
        print('\nOh!There is no available data for Brith Year')
        
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
def display_raw_data(df):
    """ Disply 5 rows of the data at a time """
    i = 0
    raw = input('\nWould you like to see the row data? Enter yes or no.').lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.head) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input('\nWould you like to see more? Enter yes or no.').lower() # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
