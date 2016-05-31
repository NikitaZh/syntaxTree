# -*- coding: utf8 -*-
from path_to_texts import *
from all_features import *

text_to_write = 'vectors.txt'
documents = 'docs.txt'
txt_tokens = 'Tokens.txt'
txt_chains = 'Groups.txt'

def inception(txt_all_docs, txt_tokens, txt_chains, text2write):
    #all_connections = []
    ids_texts = get_doc_ids(txt_all_docs)
    for file in ids_texts:
        id, text = file[0], file[1]
        text = text[:-3]+'conll'
        print(text)
        groups = get_ids_text(txt_chains, id)
        chains = get_coref_chains(groups)
        doc_features(text, chains, id, text2write, txt_tokens)
        #all_connections += p
    #return all_connections


inception(documents, txt_tokens, txt_chains, text_to_write)









