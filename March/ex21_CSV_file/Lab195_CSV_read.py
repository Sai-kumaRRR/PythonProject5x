import pandas as pd
import csv


class Test_READ():

    def test_read_csv(self):
        with open("UserData.CSV") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row[0],row[1])




    def test_read_pandas(self):
        df = pd.read_csv("UserData.CSV")
        print(df)