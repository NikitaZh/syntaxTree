# -*- coding: utf8 -*-
from saText import parse_saText

#conll_text = 'OpenCorpora/682-done.conll'
#sent_arr = [[['1', 'И', 'и', 'C', 'C', 'C', '0', 'ROOT', '_', '_', '1410'], ['2', 'такая', 'такой', 'P', 'P', 'P--fsna', '3', 'опред', '_', '_', '1412'], ['3', 'оценка', 'оценка', 'N', 'N', 'Ncfsnn', '5', 'предик', '_', '_', '1418'], ['4', 'не', 'не', 'Q', 'Q', 'Q', '5', 'огранич', '_', '_', '1425'], ['5', 'подлежит', 'подлежать', 'V', 'V', 'Vmip3s-a-e', '1', 'соч-союзн', '_', '_', '1428'], ['6', 'никаким', 'никакой', 'P', 'P', 'P--msia', '7', 'опред', '_', '_', '1437'], ['7', 'ревизиям»', 'ревизиям»', 'N', 'N', 'Ncmsin', '5', '1-компл', '_', '_', '000'], ['8', ',', ',', ',', ',', ',', '7', 'PUNC', '_', '_', '1454'], ['9', '—', '—', '-', '-', '-', '10', 'предик', '_', '_', '1456'], ['10', 'отметил', 'отметить', 'V', 'V', 'Vmis-sma-p', '1', 'вводн', '_', '_', '1458'], ['11', 'премьер', 'премьер', 'N', 'N', 'Ncmsny', '10', '1-компл', '_', '_', '1466'], ['12', '.', '.', 'S', 'S', 'SENT', '11', 'PUNC', '_', '_', '1473']], [['1', 'Между', 'между', 'S', 'S', 'Sp-i', '6', 'обст', '_', '_', '1475'], ['2', 'тем', 'то', 'P', 'P', 'P--nsin', '1', 'предл', '_', '_', '1481'], ['3', 'настойчивость', 'настойчивость', 'N', 'N', 'Ncfsnn', '6', 'предик', '_', '_', '1485'], ['4', 'Лужкова', 'лужков', 'N', 'N', 'Npmsgy', '3', 'квазиагент', '_', '_', '1499'], ['5', 'ещё', 'ещё', 'N', 'N', 'Ncmsnn', '6', 'огранич', '_', '_', '1507'], ['6', 'сильнее', 'сильный', 'A', 'A', 'Afcmsnf', '0', 'ROOT', '_', '_', '1511'], ['7', 'распалила', 'распалить', 'V', 'V', 'Vmis-sfa-p', '0', 'ROOT', '_', '_', '1519'], ['8', 'противников', 'противник', 'N', 'N', 'Ncmpay', '7', '1-компл', '_', '_', '1529'], ['9', 'размещения', 'размещение', 'N', 'N', 'Ncnsgn', '8', '1-компл', '_', '_', '1541'], ['10', 'упомянутых', 'упомянуть', 'V', 'V', 'Vmps-p-pfpg', '11', 'опред', '_', '_', '1552'], ['11', 'стендов', 'стенд', 'N', 'N', 'Ncmpgn', '9', '1-компл', '_', '_', '1563'], ['12', '.', '.', 'S', 'S', 'SENT', '11', 'PUNC', '_', '_', '1570']], [['1', 'Столичным', 'столичный', 'A', 'A', 'Afpmpdf', '2', 'опред', '_', '_', '1572'], ['2', 'властям', 'власть', 'N', 'N', 'Ncfpdn', '3', '2-компл', '_', '_', '1582'], ['3', 'обещают', 'обещать', 'V', 'V', 'Vmip3p-a-e', '0', 'ROOT', '_', '_', '1590'], ['4', 'массовые', 'массовый', 'A', 'A', 'Afpmpnf', '5', 'опред', '_', '_', '1598'], ['5', 'митинги', 'митинг', 'N', 'N', 'Ncmpnn', '3', '1-компл', '_', '_', '1607'], ['6', 'протеста', 'протест', 'N', 'N', 'Ncmsgn', '5', '1-компл', '_', '_', '1615'], ['7', 'и', 'и', 'C', 'C', 'C', '5', 'сочин', '_', '_', '1624'], ['8', 'украшение', 'украшение', 'N', 'N', 'Ncnsnn', '7', 'соч-союзн', '_', '_', '1626'], ['9', 'Москвы', 'москва', 'N', 'N', 'Ncfsgn', '8', 'квазиагент', '_', '_', '1636'], ['10', 'баннерами', 'баннер', 'N', 'N', 'Ncmpin', '3', 'обст', '_', '_', '1643'], ['11', 'с', 'с', 'S', 'S', 'Sp-i', '10', 'атриб', '_', '_', '1653'], ['12', 'информацией', 'информация', 'N', 'N', 'Ncfsin', '11', 'предл', '_', '_', '1655'], ['13', 'о', 'о', 'S', 'S', 'Sp-l', '12', '1-компл', '_', '_', '1667'], ['14', 'преступлениях', 'преступление', 'N', 'N', 'Ncnpln', '13', 'предл', '_', '_', '1669'], ['15', 'Сталина', 'сталин', 'N', 'N', 'Npmsgy', '14', 'квазиагент', '_', '_', '1683'], ['16', '.', '.', 'S', 'S', 'SENT', '15', 'PUNC', '_', '_', '1690']], [['1', '«Если', '«если', '-', '-', '-', '12', 'обст', '_', '_', '000'], ['2', 'мэрия', 'мэрия', 'N', 'N', 'Ncfsnn', '3', 'предик', '_', '_', '1698'], ['3', 'хочет', 'хотеть', 'V', 'V', 'Vmip3s-a-e', '1', 'предл', '_', '_', '1704'], ['4', 'развернуть', 'развернуть', 'V', 'V', 'Vmn----a-p', '3', '1-компл', '_', '_', '1710'], ['5', 'на', 'на', 'S', 'S', 'Sp-l', '4', 'обст', '_', '_', '1721'], ['6', 'улицах', 'улица', 'N', 'N', 'Ncfpln', '5', 'предл', '_', '_', '1724'], ['7', 'борьбу', 'борьба', 'N', 'N', 'Ncfsan', '4', '1-компл', '_', '_', '1731'], ['8', 'плакатов', 'плакат', 'N', 'N', 'Ncmpgn', '7', 'квазиагент', '_', '_', '1738'], ['9', ',', ',', ',', ',', ',', '8', 'PUNC', '_', '_', '1746'], ['10', 'она', 'она', 'P', 'P', 'P-3fsnn', '12', 'предик', '_', '_', '1748'], ['11', 'её', 'её', '-', '-', '-', '12', 'вспом', '_', '_', '1752'], ['12', 'получит»', 'получит»', 'N', 'N', 'Ncfsnn', '0', 'ROOT', '_', '_', '000'], ['13', ',', ',', ',', ',', ',', '12', 'PUNC', '_', '_', '1763'], ['14', '—', '—', '-', '-', '-', '0', 'ROOT', '_', '_', '1765'], ['15', 'заявил', 'заявить', 'V', 'V', 'Vmis-sma-p', '0', 'ROOT', '_', '_', '1767'], ['16', 'руководитель', 'руководитель', 'N', 'N', 'Ncmsny', '15', 'предик', '_', '_', '1774'], ['17', 'правозащитного', 'правозащитный', 'A', 'A', 'Afpnsgf', '18', 'опред', '_', '_', '1787'], ['18', 'объединения', 'объединение', 'N', 'N', 'Ncnsgn', '16', '1-компл', '_', '_', '1802'], ['19', '«Мемориал»', '«мемориал»', '-', '-', '-', '18', 'атриб', '_', '_', '000'], ['20', 'Олег', 'олег', 'N', 'N', 'Npmsny', '16', 'аппоз', '_', '_', '1825'], ['21', 'Орлов', 'орлов', 'N', 'N', 'Npmsny', '20', 'аппоз', '_', '_', '1830'], ['22', '.', '.', 'S', 'S', 'SENT', '21', 'PUNC', '_', '_', '1835']], ['10', '1748']]
#sent_arr_np = [[['3', 'оценка', '1418', '2', 'такая', '1412'], ['7', 'ревизиям»', '000', '6', 'никаким', '1437'], ['11', 'премьер', '1466']], [['3', 'настойчивость', '1485', '4', 'Лужкова', '1499'], ['4', 'Лужкова', '1499'], ['5', 'ещё', '1507'], ['8', 'противников', '1529', '9', 'размещения', '1541', '11', 'стендов', '1563'], ['9', 'размещения', '1541', '11', 'стендов', '1563'], ['11', 'стендов', '1563']], [['2', 'властям', '1582', '1', 'Столичным', '1572'], ['5', 'митинги', '1607', '4', 'массовые', '1598', '6', 'протеста', '1615', '7', 'и', '1624', '8', 'украшение', '1626', '9', 'Москвы', '1636'], ['6', 'протеста', '1615'], ['8', 'украшение', '1626', '9', 'Москвы', '1636'], ['9', 'Москвы', '1636'], ['10', 'баннерами', '1643', '11', 'с', '1653', '12', 'информацией', '1655', '13', 'о', '1667', '14', 'преступлениях', '1669', '15', 'Сталина', '1683'], ['12', 'информацией', '1655', '13', 'о', '1667', '14', 'преступлениях', '1669', '15', 'Сталина', '1683'], ['14', 'преступлениях', '1669', '15', 'Сталина', '1683'], ['15', 'Сталина', '1683']], [['2', 'мэрия', '1698'], ['6', 'улицах', '1724'], ['7', 'борьбу', '1731', '8', 'плакатов', '1738'], ['8', 'плакатов', '1738'], ['12', 'получит»', '000', '1', '«Если', '000', '10', 'она', '1748', '11', 'её', '1752'], ['16', 'руководитель', '1774', '18', 'объединения', '1802', '17', 'правозащитного', '1787', '19', '«Мемориал»', '000', '20', 'Олег', '1825', '21', 'Орлов', '1830'], ['18', 'объединения', '1802', '17', 'правозащитного', '1787', '19', '«Мемориал»', '000'], ['20', 'Олег', '1825', '21', 'Орлов', '1830'], ['21', 'Орлов', '1830']]]
#chains_arr = [['сами', '800'], [['местных властей', '783'], ['которые', '792'], ['сами', '800']]]

def np_length(np):
    length_characters = 0
    length_words = 0
    for q in np[1::3]:
        length_characters += len(q)
        length_words += 1
    return length_characters, length_words

def np_distance(nps, np, s_number, a_id):
    dist_np = 0
    cut_nps = nps[s_number:]
    for q in range(len(cut_nps[-1])):
        word = cut_nps[-1][q]
        if int(word[0]) > int(a_id):
            cut_nps[-1] = cut_nps[-1][:q-1]
            break
    for q1 in range(len(cut_nps[0])):
        #print(len(cut_nps))
        word1 = cut_nps[0][q1]
        if word1[0] == np[0]:
            cut_nps[0] = cut_nps[0][q1:]
            break
    for s in cut_nps:
        dist_np += len(s)
    return dist_np
    #print(cut_nps)


#print(np_distance(sent_arr_np, ['12', 'грея', '11', 'как', '13', 'пальцы'], 1, 25))

def distance_np2pronoun(s, n, s_number, a_id): #snips, noun_phrase, number of sentence with np(-1), anaphora id
    dist_characters = 0
    dist_words = 0
    sents = s[s_number:]
    start = int(n[0])-1
    first_sent = sents[0]
    first_sent = first_sent[start:]
    sents[0] = first_sent
    last_sent = sents[-1]
    last_sent = last_sent[:int(a_id)-1]
    sents[-1] = last_sent
    for sent in sents:
        for word in sent:
            #word = word.split('\t')
            dist_characters += len(word[1])
            dist_words += 1
    return dist_characters, dist_words

#print(distance_np2pronoun(sent_arr[:-1], ['5', 'руки', '4', 'Финогеновны'], 2, 25))

def gram_agreement(s, np, s_number, a_id):
    gender = 0 #doesnt match
    number = 0
    ordinal_id = int(np[0])
    candidate_gram_info = s[s_number][ordinal_id-1]
    #candidate_gram_info = candidate_gram_info.split('\t')
    candidate_gram_info = candidate_gram_info[5]
    cand_gender = candidate_gram_info[2]
    cand_number = candidate_gram_info[3]
    pronoun_gram_info = s[-1][int(a_id)-1]
    #pronoun_gram_info = pronoun_gram_info.split('\t')
    #print(pronoun_gram_info)
    pronoun_gram_info = pronoun_gram_info[5]
    if len(pronoun_gram_info) > 1:
        pron_gender = pronoun_gram_info[3]
    else:
        pron_gender = pronoun_gram_info
    if len(pronoun_gram_info) > 1:
        pron_number = pronoun_gram_info[4]
    else:
        pron_number = pronoun_gram_info
    if cand_number == pron_number:
        number = 1
    if cand_gender == pron_gender:
        gender = 1
    return gender, number

def pronoun_info(s, a_id):
    perpronouns = ['он', 'она', 'оно', 'они', 'я', 'мой']
    refpronouns = ['свой', 'себе']
    relpronouns = ['который']
    pronoun_gram_info = s[-1][int(a_id)-1]
    #pronoun_gram_info = pronoun_gram_info.split('\t')
    pronoun_type = None
    if pronoun_gram_info[2] in perpronouns:
        pronoun_type = 'per'
    elif pronoun_gram_info[2] in refpronouns:
        pronoun_type = 'ref'
    elif pronoun_gram_info[2] in relpronouns:
        pronoun_type = 'rel'
    return pronoun_type

#gram_agreement(sent_arr[:-1],['33', 'удовольствие', '31', 'в', '32', 'свое'], 2, 25)

def noun_salience(conll_text, s, np, s_number):
    sentences = parse_saText(conll_text)
    salience_value = 0
    ordinal_id = int(np[0])
    lemma = s[s_number][ordinal_id-1]
    #lemma = lemma.split('\t')
    lemma = lemma[2]
    main_sent = s[s_number]
    for q in sentences:
        if q != main_sent:
            for word in q:
                #word = word.split('\t')
                lemma_info = word[2]
                if lemma_info == lemma:
                    salience_value += 1
        else:
            break
    return salience_value

#noun_salience('2_astafiev_zhizn_prozhit.conll', sent_arr[:-1], ['27', 'время', '26', 'последнее'], 3)

def target_value(np, chains):
    new_chains = []
    p = False
    target = 0
    for q in chains:

        #q = sorted(q)
        new_chains.append(q[1])
    new_np = np[2]
    #print(np[2])
    if new_np in new_chains:
        target = 1
        p = True
    return target, p

def get_features(sents, nps, conll_text, chains):
    vectors = []
    snips, anaph_id = sents[:-1], sents[-1][0]
    for s in range(len(nps)):
        for np in nps[s]:
            dbl = False
            if np[1] != "None":
                #print('1')
                vect = []
                len_ch, len_w = np_length(np)
                dist_ch, dist_w = distance_np2pronoun(snips, np, s, anaph_id)
                vect.append(len_ch)
                vect.append(len_w)
                vect.append(dist_ch)
                vect.append(dist_w)
                vect.append(np_distance(nps, np, s, anaph_id))
                gend, numb = gram_agreement(snips, np, s, anaph_id)
                vect.append(gend)
                vect.append(numb)
                vect.append(pronoun_info(snips, anaph_id))
                vect.append(noun_salience(conll_text, snips, np, s))
                target, db = target_value(np, chains)
                if db is True:
                    dbl = True
                vect.append(target)                                    #UNCOMMEND
                vectors.append(vect)
            if dbl is True:
                print('GOT IT')
    print('NEXT')
    return vectors

#p = get_features(sent_arr, sent_arr_np, conll_text, chains_arr)
#for q in p:
    #print(q)