from pathlib import Path
from tqdm import tqdm

import numpy as np
import pandas as pd

import spacy


def main():
    data_dir = Path("reddit")
    text2vector = lambda x: nlp(x).vector
    nlp = spacy.load("en_core_web_lg")

    fps = tuple(data_dir.glob("*"))
    for fp in tqdm(fps):
        if "features" in fp.stem or "comments" in fp.stem or "meta_info" in fp.stem or "posts" in fp.stem or "README" in fp.stem:
            continue
        posts = pd.read_csv(fp, parse_dates=['date'])
        posts_stats = posts.groupby('date').agg('mean')

        posts_titles = posts.groupby('date').agg(titles=('title', lambda x: ' '.join(x)))
        titles_vectors = posts_titles.titles.map(text2vector)
        
        res = pd.DataFrame(np.column_stack((np.row_stack(titles_vectors.values), posts_stats)),
            columns=[f"titles_nlp_{i}" for i in range(300)] + list(posts_stats.columns),
            index=posts_stats.index)
        res.to_csv(fp.parent / f"{fp.stem}_features.csv")

if __name__ == "__main__":
    main()