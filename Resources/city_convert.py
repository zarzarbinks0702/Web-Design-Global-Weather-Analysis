#importing dependencies
import pandas as pd
import csv
from datetime import datetime as dt

#read the csv file
cities_csv_path = ('cities.csv')
with open(cities_csv_path, encoding="utf8") as cities_csv:
    cities_csvreader = csv.reader(cities_csv, delimiter=',')
    cities_csv_header = next(cities_csvreader)

    #create a dataframe from the csvfile
    cities_df = pd.DataFrame(cities_csvreader, columns=cities_csv_header)

    #convert date to datetime
    for index, row in cities_df.iterrows():
        date = int(row["Date"])
        format_date = dt.fromtimestamp(date)
        row["Date"] = format_date
        
#convert dataframe to html code
cities_df.to_html(r'cities_table_html.html', index=False)
