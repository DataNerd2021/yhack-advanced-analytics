from tqdm import tqdm
import json
<<<<<<< HEAD
from numba import njit
=======
>>>>>>> 35623d5ccc52dd16378318105139d5da9003c6fb

def create_vector_dict(comments: list[str], stopwords: set[str]) -> dict[str, int]:
    '''Creates a dictionary of words and their corresponding index in the vectorized representation of the comments'''
    word_set = set()
    for comment in comments:
        words = comment.split()
        for word in words:
            word_set.add(word)
    word_set = word_set - stopwords
    return {word: i for i, word in enumerate(word_set)}

def vectorize_comment(comment: str, word_dict: dict[str, int]) -> list[int]:
    '''Vectorizes a comment using the word dictionary'''
    words = comment.split()
    vectorized_comment = [0] * len(word_dict)
    for word in words:
        if word in word_dict:
            vectorized_comment[word_dict[word]] += 1
    return vectorized_comment

def vectorize_comments(comments: list[str], word_dict: dict[str, int]) -> list[int]:
    '''Vectorizes a list of comments using the word dictionary and returns a sum of the vectors'''
    vectors = [vectorize_comment(comment, word_dict) for comment in tqdm(comments)]
<<<<<<< HEAD
    return [sum(x) for x in tqdm(zip(*vectors))]
=======
    return [sum(x) for x in tqdm(zip(*vectors), total=len(word_dict))]
>>>>>>> 35623d5ccc52dd16378318105139d5da9003c6fb

def read_file_to_list(fpath: str) -> set[str]:
    return set(open(fpath, 'r').read().split('\n'))

if __name__ == '__main__':
    import pandas as pd
    ds = pd.read_csv('comments.csv')
    ds.dropna(inplace=True)
    X: list[str] = ds['Comment'].to_list()
    fpath = 'stopwords.txt'
    STOPWORDS = read_file_to_list(fpath)
    comments = ['I love this movie', 'I hate this movie', 'This movie is great']
    word_dict = create_vector_dict(X, STOPWORDS)

    # print(word_dict)
    comments_vec = vectorize_comments(X, word_dict)
    print(comments_vec)
<<<<<<< HEAD
    with open('vectors.json') as file:
        json.dump(comments_vec, file)
    # print(vectorize_comment('I love this movie', word_dict))
    # print(vectorize_comment('I hate this movie', word_dict))
    # print(vectorize_comment('This movie is great', word_dict))
=======
    with open('comments_vec.json', 'w') as f:
        json.dump(comments_vec, f)
>>>>>>> 35623d5ccc52dd16378318105139d5da9003c6fb
