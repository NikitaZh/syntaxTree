# -*- coding: utf8 -*-

def NP_connections(s, order=None, reference = None):
    arr = []
    for word in s:
        #word = word.split('\t')
        if order and word[6] == order and word[7] != 'PUNC' and word[7] != 'огранич' and word[3] != 'V':
            if word[5][0] == 'A' and word[5][2] == 'c':
                break
            else:
                arr += word[:2]
                arr.append(word[-1])
                #print(word[-1])
                if word[3] == 'S':
                    arr += NP_connections(s, order=word[0])
                if word[7] == 'сочин':
                    arr += NP_connections(s, order=word[0])
                if word[3] == 'N':
                    arr += NP_connections(s, order=word[0])

        #if reference and word[0] == reference and word[3] != 'V' and word[3] != 'C':
            #arr += word[:2]
            #print(word[:2])
            #arr += NP_connections(s, reference=word[6])

    return arr

def get_noun_phrases(snip):
    '''Возвращает именные группы по заданному снипу(предложения расположены соответствующим образом)'''
    '''Каждый элемент массива начинается с головы ИГ'''
    sent_nps = []
    sentences, deadline = snip[:-1], snip[-1]
    for q in range(len(sentences)):
        noun_count = False
        np = []
        if q != len(sentences):
            for word in sentences[q]:
                #word = word.split('\t')
                orderN, gram, refer2 = word[0], word[3], word[6]
                if gram == 'N':
                    noun_count = True
                    np.append(word[:2])
                    np[-1].append(word[-1])
                    #np[-1].append(word[5]) #добавить грам инфу для головы ИГ
                    np[-1] += NP_connections(sentences[q], orderN, refer2)
        if noun_count is False:
            np.append(['0', 'None', '000'])
        if len(np) > 0:
            sent_nps.append(np)
    return sent_nps




