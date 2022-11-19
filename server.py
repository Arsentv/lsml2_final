#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
from transformers import BertTokenizer, BertForSequenceClassification
import os
import requests
from flask import Flask

app = Flask(__name__)

tokenizer = BertTokenizer.from_pretrained(
    'bert-base-uncased',
    do_lower_case = True
    )

def preprocessing(input_text, tokenizer):

    return tokenizer.encode_plus(
                        input_text,
                        add_special_tokens = True,
                        max_length = 32,
                        pad_to_max_length = True,
                        return_attention_mask = True,
                        return_tensors = 'pt'
                   )

model = BertForSequenceClassification.from_pretrained(
    'bert-base-uncased',
    num_labels = 2,
    output_attentions = False,
    output_hidden_states = False,
)
model.load_state_dict(torch.load('spamham.bin', map_location="cpu"))
model.eval()

@app.route('/')
def output(new_sentence): 
    test_ids = []
    test_attention_mask = []

    encoding = preprocessing(new_sentence, tokenizer)

    test_ids.append(encoding['input_ids'])
    test_attention_mask.append(encoding['attention_mask'])
    test_ids = torch.cat(test_ids, dim = 0)
    test_attention_mask = torch.cat(test_attention_mask, dim = 0)

    with torch.no_grad():
        #output = model(test_ids.to(device), token_type_ids = None, attention_mask = test_attention_mask.to(device))
        output = model(test_ids, token_type_ids = None, attention_mask = test_attention_mask)

    prediction = 'Spam' if np.argmax(output.logits.cpu().numpy()).flatten().item() == 1 else 'Ham'

    return prediction

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

