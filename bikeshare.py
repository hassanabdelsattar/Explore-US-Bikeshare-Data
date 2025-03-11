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
   
    # Getting user input for city (chicago, new york city, washington):
    city = input("which city do you want to explore ?, choose one:\nChicago\nNew York City\nWashington\n  ").lower()
    while city not in CITY_DATA.keys():
        print("That\'s invalid input!..\nPlease ensure that you type your choice from the provided cities ") 
        city = input("which city do you want to explore ?\ntype:\n     Chicago\n Or   New York City\n Or   Washington\n  ").lower()
    
    # Getting user input for month (all, january, february, ... , june):
    months = ( 'january', 'february', 'march', 'april', 'may', 'june', 'all')
    month = input("\n\nDo you want to filter {}\'s data by a particular month ? \nChoose from the list: \nJanuary \nFebruary \nMarch \nApril \nMay \nJune \nor type \"all\" to provide with no month filter: ".format(city)).lower()  
    while month not in months:
        print("That\'s invalid input!..\nPlease ensure that you type your choice from the provided list of month, or you can type \"all\" in case you want no day filter \n")
        month = input("Try again.. \nDo you want to filter {}\'s data by a particular month ? \nChoose from the list: \nJanuary \nFebruary \nMarch \nApril \nMay \nJune \nor type \"all\" to provide with no month filter: ".format(city)).lower()
              
    # Getting user input for day of week (all, monday, tuesday, ... sunday):
    days = ( 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all')
    day = input("\n\nDo you want to filter {}\'s data by a particular day ? \nName of the day \nor type \"all\" to provide with no day filter: ".format(city)).lower()
    while day not in days:
        print("That\'s invalid input!..\nPlease ensure that you type your choice from the provided list of month, or you can type \"all\" in case you want no day filter")
        day = input("Try again.. \nDo you want to filter {}\'s data by a particular day ? \nName of the day \nor type \"all\" to provide with no day filter: ".format(city)).lower()
 
    print('-'*40)
    return city,month,day

#########################################################################################
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
    # Loading data for the specified city :   
    df = pd.read_csv(CITY_DATA[city])
    
    # splitting start time data by (month, day, hour) :
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    
    # Evaluating & loading data for the specified city:
    if month != 'all' :
        months = ('january', 'february', 'march', 'april', 'may', 'june')
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all' :
        df = df[df['day'] == day.title()]
        
    
    return df

#########################################################################################
def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""
    
    months = ('january', 'february', 'march', 'april', 'may', 'june')
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Calculating the most common month:
    if month == 'all' :
        most_common_month = df['month'].mode()[0]
        print("The most common month: {}".format(months[most_common_month - 1]))
        
    # Calculating the most common day of week:
    if day == 'all' :
        most_common_day = df['day'].mode()[0]
        print("The most common day: ",most_common_day)
        
    # Calculating the most common start hour:
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print("The most common hour: ",most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#########################################################################################
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Calculating the most commonly used start station:
    most_commonly_used_start_station = df["Start Station"].mode()[0]
    print("The most commonly used start station: ",most_commonly_used_start_station)
    
    # Calculating the most commonly used end station:
    most_commonly_used_end_station = df["End Station"].mode()[0]
    print("The most commonly used end station: ",most_commonly_used_end_station)
    
    # Calculating the most frequent combination of start station and end station trip:
    df["Most Frequent Trip"] =  df["Start Station"] + "   >>   " + df["End Station"]
    most_frequent_trip = df["Most Frequent Trip"].mode()[0]
    print("The most frequent trip is: ",most_frequent_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#########################################################################################
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Calculating the total travel time:
    total_travel_time = df["Trip Duration"].sum()
    print("The total travel time is: ",total_travel_time)

    # Calculating the average travel time:
    mean_travel_time =  df["Trip Duration"].mean()  
    print("The average travel time is: ",mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#########################################################################################
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Extracting the unique columns :
    df_columns = df.columns
    
    # Calculating counts of user types:
    counts_of_user_types = df["User Type"].value_counts()
    print("The counts of user types: ",counts_of_user_types)
    
    # Evaluating & Calculating counts of gender:
    if 'Gender' in df_columns :
        counts_of_gender = df['Gender'].value_counts() 
        print("counts of gender: ", counts_of_gender)
    else :
        print("No availab data for gender in Washington! ")
              
    
    # Evaluating & Calculating earliest, most recent, and most common year of birth:
    if 'Birth Year' in df_columns :
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year =  df['Birth Year'].max()
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        
        print("The earliest birth year: ",int(earliest_birth_year))
        print("The recent birth year: ",int(most_recent_birth_year))
        print("The most common year of birth: ",int(most_common_year_of_birth))
    else :
        print("No availab data for birth year in Washington! ")
              
       
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#########################################################################################
def display_raw_data(city):
    """importing city from get_filters function as input and returns the raw data of that city as chunks of 5 rows based upon user input.
    """
    # Loading data for the specified city:
    df = pd.read_csv(CITY_DATA[city])
    print('\nRaw data is available to check... \n')
    
    # Getting user input:
    response = input("Would you like to see some ?\nType \'Yes\' or \'No\': ").lower()
      
    # Looping & Loading 5 rows at a time according to user input:    
    while response == 'yes' :
        for chunk in pd.read_csv(CITY_DATA[city], chunksize = 5) :
            print("Here is a five rows from the raw data:\n\n", chunk)
            response = input("Would you like to see another 5 rows ?\nType \'Yes\' or \'No\': ").lower()
            # Evaluating user input:
            if response not in ['yes' , 'no'] :
                print('\nInvalid input...')
                response = input( 'make assure that you\'re typing ( yes or no ): ')
            elif response == 'yes' :
                continue
            elif response == 'no' :
                print('\n        Thank You \n\nExisting... ')
                break
                
#########################################################################################
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('   THANK YOU   ')
            break


if __name__ == "__main__":
	main()
