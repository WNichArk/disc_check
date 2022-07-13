import pandas as pd

DD_LF_URL = 'https://docs.google.com/spreadsheets/d/1s5YEXUNuzFypDPIDPF2AlTICnyQtEchbbf_aqBv83wg/gviz/tq?tqx=out:csv&sheet=Sheet1'

def get_dataframe():
    df = pd.read_csv(DD_LF_URL, skipinitialspace=True)
