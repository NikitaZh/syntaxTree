# -*- coding: utf8 -*-


def parse_saText(conll_text):
    """Parsing syntax-annotated text(.conll) for sentences"""
    sentences = [[]]
    saText = open(conll_text, 'r', encoding='utf-8')
    for line in saText:
        if line != '\n':
            sentences[-1].append(line)
        else:
            sentences.append([])

    saText.close()
    return sentences

def pronoun_snips(parsed_text):
    """Finding pronoun and its context"""
    pronouns = ['он', 'она', 'оно', 'они', 'я', 'свой', 'мой', 'себе', 'который']
    snips = []
    count = 0
    for i in range(len(parsed_text)):
        for word in parsed_text[i]:
            syntax_info = word.split('\t')
            if syntax_info[2] in pronouns:
                #print(syntax_info[0],syntax_info[2])
                count += 1
                if i-3 >= 0:
                    snips.append(parsed_text[i-3:i+1])
                else:
                    snips.append(parsed_text[:i+1])
                snips[-1].append(syntax_info[0])
    print(count)
    if len(snips) > 0:
        return snips
    """возвращает массив, в котором каждый элемент содержит контекст местоимений
     и номер(arr[i[-1]]), который показывает к какому местоимению найден контекст в последнем предложении"""






#t = parse_saText('2_astafiev_zhizn_prozhit.conll')
#p = pronoun_snips(t)

#for q in p:
    #print(q)

#print(p[0], p[1])

"""for word in t[0]:
    word = word.split('\t')
    print(word[0], '-', word[1])"""