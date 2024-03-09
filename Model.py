import pandas as pd
from Vectorize import read_file_to_list, create_vector_dict, vectorize_comment, vectorize_comments
import numpy as np

class Model:
    def __init__(self):
        comments = pd.read_csv('comments.csv').dropna()
        neg_comments = comments[comments['Sentiment'] == 0.0]['Comment'].to_list()
        pos_comments = comments[comments['Sentiment'] == 2.0]['Comment'].to_list()[:len(neg_comments)]

        fpath = 'stopwords.txt'
        STOPWORDS = read_file_to_list(fpath)
        self.word_dict = create_vector_dict(pos_comments + neg_comments, STOPWORDS)
        self.pos_vec = vectorize_comments(pos_comments, self.word_dict)
        self.neg_vec = vectorize_comments(neg_comments, self.word_dict)
        
        self.comments_sum = np.array(self.pos_vec) + self.neg_vec
        self.pos_prob_vec = self.pos_vec / self.comments_sum
        self.neg_prob_vec = 1 - self.pos_prob_vec
    
    def run(self, text: str) -> float:
        test_vec = vectorize_comment(text, self.word_dict)
        test_pos = np.dot(test_vec, self.pos_prob_vec)
        test_neg = np.dot(test_vec, self.neg_prob_vec)
        return test_pos/(test_pos + test_neg)