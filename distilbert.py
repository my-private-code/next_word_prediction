from transformers import pipeline
unmasker = pipeline('fill-mask', model='distilbert-base-uncased')

print(unmasker("The goal of life is [MASK]."))
print(unmasker("Thanks [MASK]."))


# from transformers import DistilBertTokenizer, DistilBertModel
# tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
# model = DistilBertModel.from_pretrained("distilbert-base-uncased")
# text = "Thank you [MASK]."
# encoded_input = tokenizer(text, return_tensors='pt')
# output = model(**encoded_input)
# print(output)
