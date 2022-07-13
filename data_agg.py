import pandas as pd
from disc_record import DiscRecord

DD_LF_URL = 'https://docs.google.com/spreadsheets/d/1s5YEXUNuzFypDPIDPF2AlTICnyQtEchbbf_aqBv83wg/gviz/tq?tqx=out:csv&sheet=Sheet1'

def get_records():
    df = pd.read_csv(DD_LF_URL, skipinitialspace=True)
    df.columns = df.columns.str.strip()
    records = []
    for name, color, disc, date in zip(df["Name"], df["Color"], df["Disc"], df["Date logged"]):
        addl_record = DiscRecord(name, color, disc, date)
        records.append(addl_record)
    return records



