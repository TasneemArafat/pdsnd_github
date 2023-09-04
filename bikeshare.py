import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

Months = ['january', 'february', 'march', 'april', 'may', 'june']

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
    city = input("For which city Would you like to get the data for chicago, new york city or Washington?\n")
    while(city.lower() not in CITY_DATA):
        city = input("Please input one of the three cities chicago, new york city or washington\n")
    # TO DO: get user input for month (all, january, february, ... , june)
    month_day_filter = input("Would you like to specify a month and day filter? Y or N\n")
    while(month_day_filter.lower() != 'n' and month_day_filter.lower() != "y"):
        month_day_filter = input("Please add a valid value Y or N\n")
    if month_day_filter.lower() == "n":
        day = "all"
        month = "all"
    else:
        month = input("For which month you want the data for january, february, march, april, may, june or all?\n")
        while(month.lower() not in Months and month.lower() != 'all'):
            month = input("Please type a valid month january, february, march, april, may, june or all\n")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = input("For Which day of the week would you like the data for monday, tuesday, wednesday, thursday, friday,    saturday, sunday or all?\n")
        while(day.lower() not in days and day.lower() != "all"):
            day = input("Please add a valid day or all\n")
    
        print('-'*40)
    return city.lower() , month.lower() , day.lower()


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
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = Months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("Most Common Month:{}".format(Months[most_common_month-1]))
    
    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print("Most Common Day Of Week:{}".format(most_common_day_of_week))

    # TO DO: display the most common start hour
    most_common_start_hour = df['Start Time'].dt.hour.mode()[0]
    print("Most Common Start hour:{}".format(most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station: {}".format(most_common_start_station))
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("Most commonly used end station: {}".format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = 'Starts at: ' + df['Start Station'] + ' and Ends at: '+ df['End Station']
    print("Most frequent combination of start and end stations: {}".format(df['combination'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time: {}".format(total_travel_time))
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time: {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Count of User Types:")
    for idx, user_type in enumerate(df['User Type'].value_counts().index.tolist()):
        print("Type: {} Count: {}".format(user_type, df['User Type'].value_counts()[idx]))
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print("\nCount of Gender:")
        for idx, user_type in enumerate(df['Gender'].value_counts(dropna = True).index.tolist()):
            print("Gender: {} Count: {}".format(user_type, df['Gender'].value_counts()[idx]))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("\nEarliest, Most Recent and Most Common Year of Birth")
        print("Earliest Birth Year: {}".format(int(df['Birth Year'].min())))
        print("Most Recent Birth Year: {}".format(int(df['Birth Year'].max())))
        print("Most Common Birth Year: {}".format(int(df['Birth Year'].mode())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def raw_data(df, index = 1):
    raw_data_value = input("Would you like to see some raw data? Enter Y or N\n")
    while(raw_data_value.lower() != 'n' and raw_data_value.lower() != "y"):
        raw_data_value = input("Please add a valid value Y or N\n")
    if raw_data_value.lower() == 'n':
        return
    else:
        index = index + 1
        if(index > df.shape[0]):
            return
        print(df.head(index + 1))
        raw_data(df, index)
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
