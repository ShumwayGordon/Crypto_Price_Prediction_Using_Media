import yaml
import datetime as dt
from pathlib import Path
from tqdm import tqdm

from utils.parser import RedditParser

import numpy as np
import pandas as pd

import yfinance as yf


def main():
    # parameters
    subreddits = []
    tickers = []
    posts_per_day = 10
    output_folder = Path("reddit")
    if not output_folder.exists(): output_folder.mkdir()

    # with open('reddit_api.yaml') as f:
    #     api_creds = yaml.safe_load(f)
    # parser = RedditParser(*api_creds.values())
    # for post parsing using psaw api, which don't need api credentials
    parser = RedditParser()
    
    for subreddit, ticker in zip(subreddits, tickers):
        print(f"Parsing {ticker=} {subreddit=}")
        history = yf.Ticker(ticker).history(start="2010-01-01",  end=dt.datetime.now())
        one_day = dt.timedelta(1)
        posts = []
        psaw_filter = ['full_link', 'url','author', 'title', 'num_comments', 'score', 'selftext', 'id']

        for date in tqdm(history.index):
            new_posts = parser.get_posts(subreddit=subreddit, start_date=date, end_date=date + one_day,
                                        filter=psaw_filter, limit=posts_per_day)
            for post in new_posts:
                post.append(date)
            posts.extend(new_posts)
        
        posts_df = pd.DataFrame(posts, columns=psaw_filter + ['date'])
        print(f"Got {len(posts_df)} posts")
        posts_df.to_csv(output_folder / f"{subreddit}.csv", index=False)

if __name__ == "__main__":
    main()