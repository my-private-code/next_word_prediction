
# venv/bin/pip3 install happytransformer

from happytransformer import HappyWordPrediction
#--------------------------------------#
# https://github.com/EricFillion/happy-transformer/blob/master/examples/word_prediction/readme_examples.py

happy_wp = HappyWordPrediction()  # default uses distilbert-base-uncased
result = happy_wp.predict_mask("I think therefore I [MASK]", top_k=3)
print(result)  # [WordPredictionResult(token='am', score=0.10172799974679947)]
print(result[0].token)  # am

print(happy_wp.predict_mask("The goal of [MASK].", top_k=10))