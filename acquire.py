# imports

import requests
import pandas as pd

import os


#url = 'https://swapi.dev/api/'

def acquire_df_from_api(url, name):
    ''' 
    takes a url and string, gets api, writes data to csv file if a local does not exist and return df. 
    if a local file exists, return df.
    '''
    
    # check for csv file in local storage
    if os.path.isfile(f'{name}.csv'):
        # read a dataframe from csv file 
        df = pd.read_csv('people.csv')
    else: 
        # assign url
        url = f'{url}{name}/'
#         print(url)

        # call api
        response = requests.get(url)
#         print(response)

        # assign api data
        data = response.json()
#         print(data.keys())

        # create dataframe
        df = pd.DataFrame(data['results'])
        
        # loop through page to the last page
        while data['next'] != None:
            
            # get api of next page
            response = requests.get(data['next'])
            
            # assign api data
            data = response.json()
            
            # concat new dataframe created next page data to original
            df= pd.concat([df, pd.DataFrame(data['results'])], ignore_index=True)
            
        # write dataframe to csv file for local storage
        df.to_csv(f'{name}.csv', index=False)
  
    # return dataframe
    return df


def acquire_data():
    ''' 
    creates a dataframe from api data, write a csv file if one does not exist. if csv file exists, uses csv file 
    to create a dataframe. 
    combine dataframes and return a combined dataframe
    '''
    
    url = 'https://swapi.dev/api/'
    # get dataframe using a function
    df_1 = acquire_df_from_api(url,'people')
    df_2 = acquire_df_from_api(url,'planets')
    df_3 = acquire_df_from_api(url,'starships')
    
    # concat dataframes
    df= pd.concat([df_1,df_2,df_3],axis=1)
    
    # return a combined dataframe
    return df


def acquire_energy_csv():
    
    ''' 
    creates a dataframe from a csv file if one exist. if csv file does not exist, create a dataframe reading a csv file 
    from url.
    returns a dataframe
    '''
    
    url = 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'

    if os.path.isfile('opsd_germany_daily.csv'):
        
        # create a dataframe from csv file of local storage
        df = pd.read_csv('opsd_germany_daily.csv')
        
    else: 
        
        # create a dataframe from csv file of url
        df = pd.read_csv(url)
        
        # write csv file on local storage
        df.to_csv('opsd_germany_daily.csv', index=False)
    
    # return a dataframe
    return df
    