def create_vector_dict(comments: list[str]) -> dict[str, int]:
    '''Creates a dictionary of words and their corresponding index in the vectorized representation of the comments'''
    word_set = set()
    for comment in comments:
        words = comment.split()
        for word in words:
            word_set.add(word)
    return {word: i for i, word in enumerate(word_set)}

def vectorize_comment(comment: str, word_dict: dict[str, int]) -> list[int]:
    '''Vectorizes a comment using the word dictionary'''
    words = comment.split()
    vectorized_comment = [0] * len(word_dict)
    for word in words:
        if word in word_dict:
            vectorized_comment[word_dict[word]] = 1
    return vectorized_comment

if __name__ == '__main__':
    import pandas as pd
    ds = pd.read_csv('comments.csv')
    ds.dropna(inplace=True)
    X: list[str] = ds['Comment'].to_list()
    comments = ['I love this movie', 'I hate this movie', 'This movie is great']
    word_dict = create_vector_dict(X)
    print(word_dict)
    # print(vectorize_comment('I love this movie', word_dict))
    # print(vectorize_comment('I hate this movie', word_dict))
    # print(vectorize_comment('This movie is great', word_dict))