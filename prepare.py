import pandas as pd
import acquire as aq


def set_date_times(df1,df2,df3):

    # df1,df2,df3 = aq.acquire_fitbit()
    df1.index= pd.to_datetime(df1.index)
    df2.index= pd.to_datetime(df2.index)
    df3.index= pd.to_datetime(df3.index)

    return [df1,df2,df3]
