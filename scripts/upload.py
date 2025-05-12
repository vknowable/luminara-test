import datadotworld as dw
import pandas as pd

df = pd.read_csv('data/hourly_agg.csv')
dw.append_rows(
    dataset_key='youruser/poc-endpoint-history',
    table_name='hourly_status',
    data=df,
    format='pandas'
)
