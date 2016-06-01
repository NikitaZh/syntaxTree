# -*- coding: utf8 -*-
from saText import *
from NPinSnips import *
from features_extracting import *

def doc_features(conll_text, chains, id, txt2wr8, tokens_txt):
    raw_sentences = parse_saText(conll_text)
    #connections = []
    txt2write = open(txt2wr8, 'a', encoding='utf-8')
    shifts = get_shift_info(raw_sentences, get_shifts(get_ids_text(tokens_txt, id)))
    snips = pronoun_snips(raw_sentences)
    for s in range(len(snips)):
        #pron = snips[s][-2][int(snips[s][-1])-1]
        pron_shift = snips[s][-1][1]
        nps = get_noun_phrases(snips[s])
        for pron in range(len(chains)):
            if chains[pron][0][1] == pron_shift:
                vectors = get_features(snips[s], nps, conll_text, chains[pron][1])
                #connections += syntax_cons
                for q in vectors:
                    #print(q)
                    for item in q:
                        txt2write.write(str(item)+';')
                    txt2write.write('\r\n')
                break
        #print(s)
    txt2write.close()
    #return connections

