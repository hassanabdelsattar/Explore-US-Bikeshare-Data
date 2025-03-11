import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def load_data(city, month, day):
    
    df = pd.read_csv(CITY_DATA[city])
    
    df_columns = df.columns 
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    
    df['day'] = df['Start Time'].dt.weekday_name
    
    if month != 'all' :
        months = ('january', 'february', 'march', 'april', 'may', 'june')
        month = monnths.index(month) + 1
        df = df[df['month'] == month]
            
    if day != 'all' :
        df = df[df['day'] == day.title()]
        
    
    

    return df


def main():
    while True:
#         city,month,day = get_filters()
        df = load_data(city, month, day)

#         time_stats(df)
#         station_stats(df)
#         trip_duration_stats(df)
#         user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()