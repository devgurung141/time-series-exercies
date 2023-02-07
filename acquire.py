# imports

import requests
import pandas as pd

import os


#url = 'https://swapi.dev/api/'

def acquire_df(url, name):
    ''' 
    takes a string, gets api, writes data to csv file if a local does not exist and return df 
    if a local file exists return df
    '''
    
    if os.path.isfile(f'{name}.csv'):
        # read a dataframe from csv file 
        df = pd.read_csv('people.csv')
    else: 
        url = f'{url}{name}/'
#         print(url)
        
        response = requests.get(url)
#         print(response)

        data = requests.get(url).json()
#         print(data.keys())

        # create a dataframe
        df= pd.DataFrame(requests.get(url).json()['results'])
        # write a dataframe to csv file 
        df.to_csv(f'{name}.csv', index=False)
        
    return df

def acquire_data():
    ''' 
    gets dataframes, concat dataframes and return a combined dataframe
    '''
    url = 'https://swapi.dev/api/'
    # get dataframe using api from a function
    df_1 = acquire_df(url,'people')
    df_2 = acquire_df(url,'planets')
    df_3 = acquire_df(url,'starships')
    
    # concat dataframes
    df= pd.concat([df_1,df_2,df_3],axis=1)
    
    return df


def acquire_csv(url):
    df = pd.read_csv(url)
    return df
    