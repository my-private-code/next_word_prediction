# %%
import torch
import string

from transformers import BertTokenizer, BertForMaskedLM
bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased') # 500M, seems best model in my tests
bert_model = BertForMaskedLM.from_pretrained('bert-base-uncased').eval()

# from transformers import BartTokenizer, BartForConditionalGeneration
# bart_tokenizer = BartTokenizer.from_pretrained('facebook/bart-large') # 1.2G
# bart_model = BartForConditionalGeneration.from_pretrained('facebook/bart-large').eval()

# from transformers import ElectraTokenizer, ElectraForMaskedLM
# electra_tokenizer = ElectraTokenizer.from_pretrained('google/electra-small-generator')
# electra_model = ElectraForMaskedLM.from_pretrained('google/electra-small-generator').eval()

from transformers import AutoTokenizer, AutoModelForMaskedLM
bert_tokenizer_cn = AutoTokenizer.from_pretrained("bert-base-chinese")
bert_model_cn = AutoModelForMaskedLM.from_pretrained("bert-base-chinese").eval()

top_k = 10


def decode(tokenizer, pred_idx, top_clean):
    ignore_tokens = string.punctuation + '[PAD]'
    tokens = []
    for w in pred_idx:
        token = ''.join(tokenizer.decode(w).split())
        if token not in ignore_tokens:
            tokens.append(token.replace('##', ''))
    return '\n'.join(tokens[:top_clean])


def encode(tokenizer, text_sentence, add_special_tokens=True):
    text_sentence = text_sentence.replace('<mask>', tokenizer.mask_token)
    # if <mask> is the last token, append a "." so that models dont predict punctuation.
    if tokenizer.mask_token == text_sentence.split()[-1]:
        text_sentence += ' .'

    input_ids = torch.tensor([tokenizer.encode(text_sentence, add_special_tokens=add_special_tokens)])
    mask_idx = torch.where(input_ids == tokenizer.mask_token_id)[1].tolist()[0]
    return input_ids, mask_idx


def get_all_predictions(text_sentence, top_clean=5):
    # ========================= BERT =================================
    print(text_sentence)
    input_ids, mask_idx = encode(bert_tokenizer, text_sentence)
    with torch.no_grad():
        predict = bert_model(input_ids)[0]
    bert = decode(bert_tokenizer, predict[0, mask_idx, :].topk(top_k).indices.tolist(), top_clean)

    # ========================= BERT =================================
    print(text_sentence)
    input_ids, mask_idx = encode(bert_tokenizer_cn, text_sentence)
    with torch.no_grad():
        predict = bert_model_cn(input_ids)[0]
    bert_cn = decode(bert_tokenizer_cn, predict[0, mask_idx, :].topk(top_k).indices.tolist(), top_clean)

    # # ========================= BART =================================
    # input_ids, mask_idx = encode(bart_tokenizer, text_sentence, add_special_tokens=True)
    # with torch.no_grad():
    #     predict = bart_model(input_ids)[0]
    # bart = decode(bart_tokenizer, predict[0, mask_idx, :].topk(top_k).indices.tolist(), top_clean)

    # # ========================= ELECTRA =================================
    # input_ids, mask_idx = encode(electra_tokenizer, text_sentence, add_special_tokens=True)
    # with torch.no_grad():
    #     predict = electra_model(input_ids)[0]
    # electra = decode(electra_tokenizer, predict[0, mask_idx, :].topk(top_k).indices.tolist(), top_clean)

    return {'bert': bert,
            'bert_cn': bert_cn,
            # 'bart': bart,
            # 'electra': electra
            }
