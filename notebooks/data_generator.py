#  Request Deps ----->
import pandas as pd
import requests
import json
import csv
import time
import datetime as dt
import praw
from psaw import PushshiftAPI

#  Request Deps ----->
api = PushshiftAPI()
def grabdata(iterations,outputs):
    runge = range(1,iterations)
    for i in runge:
        start_epoch = int(dt.datetime(2017, 1, 1).timestamp())
        hello = list(api.search_submissions(after=start_epoch,
                                    # Dearest Eric: Uncomment this two to put in a "specific sub":
                           # subreddit='secret',
        filter=['url', 'title', 'subreddit','selftext','score'],
                            limit=outputs))
        df = pd.DataFrame(hello)
        out = "Data/final_data" + str(i)
        print("Data Completed:")
        print(out)
        df.to_csv(out)
        print("output at:",out)
grabdata(50,25000)