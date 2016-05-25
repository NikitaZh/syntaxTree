# -*- coding: utf8 -*-
from saText import *
from NPinSnips import *
from features_extracting import *


#chains = [[['которые', '412'], [['рядовыми солдатами , колхозниками и тружениками тыла', '368'], ['которые', '412']]], [['Мы', '603'], [['Мы', '603'], ['нашу', '619']]], [['которые', '792'], [['местных властей', '783'], ['которые', '792'], ['сами', '800']]], [['сами', '800'], [['местных властей', '783'], ['которые', '792'], ['сами', '800']]], [['свою', '1033'], [['столичных властей', '978'], ['столичные власти', '1016'], ['свою', '1033'], ['Столичным властям', '1582'], ['мэрия', '1698'], ['она', '1748']]], [['она', '1748'], [['столичных властей', '978'], ['столичные власти', '1016'], ['свою', '1033'], ['Столичным властям', '1582'], ['мэрия', '1698'], ['она', '1748']]], [['её', '1752'], [['борьбу плакатов', '1731'], ['её', '1752']]], [['их', '1957'], [['стендами с изображением Иосифа Сталина', '307'], ['такие плакаты', '491'], ['портреты Сталина', '682'], ['упомянутых стендов', '1563'], ['стенды', '1923'], ['их', '1957'], ['стендов', '2054']]], [['нас', '1985'], [['Столичные анархисты', '1847'], ['нас', '1985'], ['анархистской группировки « Автономное действие »', '2261']]], [['она', '2010'], [['хорошая краска', '2002'], ['она', '2010']]], [['его', '2217'], [['Иосифа Сталина', '331'], ['Сталина', '691'], ['генсека', '1068'], ['Сталина', '1683'], ['« отцу народов »', '2180'], ['его', '2217'], ['генсека', '2333'], ['его', '2366'], ['Сталин', '2456']]]]

#id = '66'
#text = 'OpenCorpora/682-done.conll'
#text2write = 'vectors.txt'
#tokens = 'Tokens.txt'

def doc_features(conll_text, chains, id, txt2wr8, tokens_txt):
    raw_sentences = parse_saText(conll_text)
    txt2write = open(txt2wr8, 'a', encoding='utf-8')
    shifts = get_shift_info(raw_sentences, get_shifts(get_ids_text(tokens_txt, id)))
    snips = pronoun_snips(raw_sentences)
    #if len(snips) != len(chains):
        #print('ERROR')
    for s in range(len(snips)):
        #pron = snips[s][-2][int(snips[s][-1])-1]
        pron_shift = snips[s][-1][1]
        nps = get_noun_phrases(snips[s])
        for pron in range(len(chains)):
            if chains[pron][0][1] == pron_shift:
                vectors = get_features(snips[s], nps, conll_text, chains[pron][1])
                for q in vectors:
                    #print(q)
                    for item in q:
                        txt2write.write(str(item)+';')
                    txt2write.write('\r\n')
                break
        #print(s)
    txt2write.close()

#doc_features(text, chains, id, text2write, tokens)
