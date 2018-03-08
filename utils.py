import numpy as np
import pandas as pd
import datetime
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

#constants
date2016 = datetime.date(2016,7,3)
date2017 = datetime.date(2017,4,19)
date2012 = datetime.date(2012,9,24)
date2014 = datetime.date(2014,11,16)
thirty = (29,31)
fifteen = (14,16)
forty = (39,42)
fifty = (49,54)
sixty = (59,62)

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

def get_sorted_dataset(df):
	return df.sort_values(by=['user_id','order_date'])

def make_data_string(st,user_id,interval,fdate = date2017):
    datapoints = diff_month(datetime.date.today(),fdate)
    for i in range(datapoints):
        rnd = np.random.randint(*interval)
        odate = date2017 + datetime.timedelta(i*rnd)
        st += f'{user_id},{odate}|'
    return st

def get_delta_array(sorted_df,user_id):
    a = sorted_df[sorted_df['user_id'] == user_id]['order_date'][:-1]
    b = sorted_df[sorted_df['user_id'] == user_id]['order_date'][1:]
    target = (b.values - a.values).astype('timedelta64[D]')
    return target

def create_learn_df(sorted_df):
    ss = []
    for user in sorted_df.user_id.unique():
        delta_array = get_delta_array(sorted_df,user).astype('int')
        s = pd.DataFrame({'user_id':[user]*len(delta_array),'delta':delta_array})
        ss += [s[['user_id','delta']]]
    return pd.concat(ss)

def create_dataframe(datastring):
    with open('data.csv','w') as f:
	    for i in datastring.split('|'):
	        f.write(i+'\n')
    df = pd.read_csv('data.csv',header=None,columns=['user_id','user_email','product','order_date'])
    return df

def train_model(df,model='linear'):
	if model == 'linear':
		pdtr = LinearRegression(normalize=True)
	if model == 'ensemble':
		pdtr = RandomForestRegressor(n_estimators=100)
	pdtr.fit(main_df[['user_id','product']],main_df['delta'])



