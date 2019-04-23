import pandas as pd
import acquire as aq


def set_date_times(foods,activ,log):

    # df1,df2,df3 = aq.acquire_fitbit()
    foods.index= pd.to_datetime(foods.index)
    activ.index= pd.to_datetime(activ.index)
    log.index= pd.to_datetime(log.index)

    return [foods,activ,log]

def merge_dfs(foods,activ,log):
    merged = pd.merge(activ.reset_index(),log.reset_index(),how='right')
    merged = pd.merge(merged,foods.reset_index(),how='left')
    return merged

def prepare_fitbit():

    return merge_dfs(*set_date_times(*aq.acquire_fitbit())).set_index('index').convert_objects(convert_numeric=True, convert_dates=True)
