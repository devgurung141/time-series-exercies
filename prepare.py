# imports

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from acquire import acquire_energy_csv
from wrangle import acquire_store


def prep_store():
    
    '''acquires data, modifies a dataframe and returns a modified dataframe'''
    
    # acquire data
    df = acquire_store()
    
    # convert date column to datetime format
    df.sale_date = pd.to_datetime(df.sale_date, infer_datetime_format=True)
     
    # plot the distribution of sale_amount and item_price
    cols = ['sale_amount', 'item_price']
    for col in cols:
        sns.histplot(df[col])
        plt.show()
    

    # set the index to be the datetime variable
    df = df.set_index('sale_date').sort_index()
   
    # add columns
    df['month'] = df.index.month_name()
    df['day_of_week'] = df.index.day_name()
    df['sales_total'] = df['sale_amount']* df['item_price']
    
    # return a dataframe
    return df


def prep_energy():
    
    '''acquires data, modifies a dataframe and returns a modified dataframe'''

    
    # acquire data
    df = acquire_energy_csv()
    
    # convert date column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)
    
    # plot the distribution
    for col in df:
        sns.histplot(df[col])
        plt.show()
        
    # set the index to be the datetime variable    
    df = df.set_index('Date').sort_index()
    
    # add columns
    df['month'] = df.index.month_name()
    df['year']= df.index.year
    
    # fill missing values
    df= df.fillna(0)
    
    # return dataframe
    return df