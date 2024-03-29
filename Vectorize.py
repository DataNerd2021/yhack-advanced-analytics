from tqdm import tqdm
import json
import numpy as np
import string

def create_vector_dict(comments: list[str], stopwords: set[str]) -> dict[str, int]:
    '''Creates a dictionary of words and their corresponding index in the vectorized representation of the comments'''
    word_set = set()
    for comment in comments:
        comment = comment.translate(str.maketrans('', '', string.punctuation))
        words = comment.split()
        for word in words:
            word_set.add(word)
    word_set = word_set - stopwords
    return {word: i for i, word in enumerate(word_set)}

def vectorize_comment(comment: str, word_dict: dict[str, int]) -> list[int]:
    '''Vectorizes a comment using the word dictionary'''
    comment = comment.translate(str.maketrans('', '', string.punctuation))
    words = comment.split()
    vectorized_comment = [0] * len(word_dict)
    for word in words:
        if word in word_dict:
            vectorized_comment[word_dict[word]] += 1
    return vectorized_comment

def vectorize_comments(comments: list[str], word_dict: dict[str, int]) -> list[int]:
    '''Vectorizes a list of comments using the word dictionary and returns a sum of the vectors'''
    sum_vec = np.zeros(len(word_dict), dtype=np.int16)
    for comment in tqdm(comments):
        sum_vec += vectorize_comment(comment, word_dict)
    return sum_vec.tolist()

def read_file_to_list(fpath: str) -> set[str]:
    return set(open(fpath, 'r').read().split('\n'))

if __name__ == '__main__':
    import pandas as pd
    ds = pd.read_csv('comments.csv')
    ds.dropna(inplace=True)
    pos_comments: list[str] = ds[ds['Sentiment'].isin([1.0, 2.0])]['Comment'].to_list()
    neg_comments: list[str] = ds[ds['Sentiment']==0.0]['Comment'].to_list()
    comments: list[str] = ds['Comment'].to_list()
    fpath = 'stopwords.txt'
    STOPWORDS = read_file_to_list(fpath)
    word_dict = create_vector_dict(comments, STOPWORDS)

    # print(word_dict)
    comments_vec = vectorize_comments(pos_comments, word_dict)
    with open('pos_comments_vec.json', 'w') as f:
        json.dump(comments_vec, f)
    
    comments_vec = vectorize_comments(neg_comments, word_dict)
    with open('neg_comments_vec.json', 'w') as f:
        json.dump(comments_vec, f)
    
    with open('word_dict.json', 'w') as f:
        json.dump(word_dict, f)
