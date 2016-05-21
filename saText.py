# -*- coding: utf8 -*-
from path_to_texts import get_ids_text

def parse_saText(conll_text):
    """Parsing syntax-annotated text(.conll) for sentences"""
    sentences = [[]]
    saText = open(conll_text, 'r', encoding='utf-8')
    for line in saText:
        if line != '\n':
            line = line.strip('\n')
            line = line.split('\t')
            sentences[-1].append(line)
        else:
            sentences.append([])

    saText.close()
    return sentences

def get_shifts(text):
    #print(text)
    arr = []
    for line in text:
        l = []
        l.append(line[1])
        l.append(line[3])
        arr.append(l)
    return arr


def get_shift_info(sentences, shifts):
    sh = 0

    for sent in sentences:
        for word in sent:
            i = 0
            for q in range(len(shifts)):
                #print(shifts[q])
                if word[1] == shifts[q][1]:
                    word.append(shifts[q][0])
                    shifts = shifts[q:]
                    break
                else:
                    if i < 5:
                        i += 1
                    else:
                        word.append('000')
                        break
    return sentences







def pronoun_snips(parsed_text):
    """Finding pronoun and its context"""
    pronouns = ['он', 'она', 'оно', 'они', 'его', 'её', 'их', 'свой', 'мой', 'себя', 'который']
    snips = []
    #distance = 0
    for i in range(len(parsed_text)):
        for word in parsed_text[i]:
            #distance += 1
            syntax_info = word
            #print(syntax_info[1], distance)
            if syntax_info[2] in pronouns:
                #distance += 1
                if i-3 >= 0:
                    snips.append(parsed_text[i-3:i+1])
                else:
                    snips.append(parsed_text[:i+1])
                snips[-1].append(syntax_info[0])
    #print(distance)
    if len(snips) > 0:
        return snips
    """возвращает массив, в котором каждый элемент содержит контекст местоимений
     и номер(arr[i[-1]]), который показывает к какому местоимению найден контекст в последнем предложении"""






#t = parse_saText('2_astafiev_zhizn_prozhit.conll')
#q = get_shift_info(t, get_shifts(get_ids_text('Tokens.txt', 5)))

#p = pronoun_snips(t)
#print(p[30])

"""for word in t[0]:
    word = word.split('\t')
    print(word[0], '-', word[1])"""