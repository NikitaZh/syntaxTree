# -*- coding: utf8 -*-
from saText import parse_saText

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
            dist_characters += len(word[1])
            dist_words += 1
    return dist_characters, dist_words

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
    #pronouns = ['он', 'она', 'оно', 'они', 'его', 'её', 'их', 'свой', 'мой', 'себя', 'который']
    perpronouns = ['он', 'она', 'оно', 'они', 'мой', 'их', 'его', 'её']
    refpronouns = ['свой', 'себя']
    relpronouns = ['который']
    pronoun_gram_info = s[-1][int(a_id)-1]
    pronoun_type = None
    if pronoun_gram_info[2] in perpronouns:
        #pronoun_type = 'per'
        pronoun_type = '1'
    elif pronoun_gram_info[2] in refpronouns:
        #pronoun_type = 'ref'
        pronoun_type = '2'
    elif pronoun_gram_info[2] in relpronouns:
        #pronoun_type = 'rel'
        pronoun_type = '3'
    if pronoun_type is None:
        print(pronoun_gram_info[2])
    return pronoun_type

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
                lemma_info = word[2]
                if lemma_info == lemma:
                    salience_value += 1
        else:
            break
    return salience_value

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

def syntax_depth(sent, ordinal_n, depth):
    """Возращает расстояние от узла до дерева"""
    d = depth
    #print(d)
    if sent[int(ordinal_n)-1][6] == '0':
        d += 1
        #print(d)
    else:
        d += 1
        d = syntax_depth(sent, sent[int(ordinal_n)-1][6], d)
    return d

def syntax_depth_root(sent, ordinal_n, d = []):
    """Возращает узлы на расстоянии от корня до исходного узла"""
    arr = d
    #print(d)
    if sent[int(ordinal_n)-1][6] == '0':
        arr.append(sent[int(ordinal_n)-1][0])
    else:
        arr.append(sent[int(ordinal_n)-1][0])
        syntax_depth_root(sent, sent[int(ordinal_n)-1][6], arr)
    return d

def syntax_root_connections(sent, ant_id, connections = []):
    con = connections
    if sent[int(ant_id)-1][6] != '0':
        con.append(sent[int(ant_id)-1][7])
        syntax_root_connections(sent, sent[int(ant_id)-1][6], con)
    return con

def syntax3(connections):
    pred = 'предик'
    compl1 = '1-компл'
    cluster_2 = ['подч-союзн', 'соч-союзн', 'квазиагент', 'обст', 'сент-соч', 'предл', 'сочин']
    cluster_3 = ['опред', 'аппоз', 'сравнит', 'агент', 'эксплет', 'аналит', '1-несобст-компл', 'разъяснит', 'вводн', 'об-аппоз', 'неакт-компл', 'ном-аппоз', 'пролепт', '4-компл', '3-компл', 'длительн', 'пасс-анал',  'изъясн', 'оп-опред', 'атриб',  'сравн-союзн', 'уточн', '2-компл', 'соотнос', 'инф-союзн', 'примыкат', 'релят', 'присвяз', 'эллипт', 'электив', 'дат-субъект', 'огранич']
    erste1 = 0
    erste2 = 0
    zweite = 0
    dritte = 0
    for q in connections:
        if q == pred:
            erste1 = 1
        elif q == compl1:
            erste2 = 1
        elif q in cluster_2:
            zweite = 1
        elif q in cluster_3:
            dritte = 1
    return erste1, erste2, zweite, dritte

def syntax_1_exp(sents, a_id):
    """Возращает глубину местоимения, тип связи местоимения, количество запятых, отношение глубины мест к глубине дерева и количество узлов с той же глубиной"""
    connections = {'вспом': 0, 'сравнит': 0, 'предик': 1, '1-компл': 4, 'атриб': 0, 'ROOT': 0, 'опред': 2, 'обст': 0, 'соч-союзн': 0, 'квазиагент': 5, 'дат-субъект': 0, 'сент-соч': 0, 'агент': 0, 'предл': 3, 'неакт-компл': 0, 'суб-копр': 0, '2-компл': 6}
    sent = sents[-1]
    connection = sent[int(a_id)-1][7]
    connection = connections[connection]
    con_to_root = sent[int(a_id)-1][6]
    dist_to_pron = syntax_depth(sent, con_to_root, depth=1)
    distances = []
    comma_count = 0
    for word in sent:
        root_distance = syntax_depth(sent, word[6], depth=1)
        if word[1] == ',' and int(word[0]) < int(a_id):
            comma_count += 1
        distances.append(root_distance)
    same_depth = 0
    for n in distances:
        #print(n)
        if n == dist_to_pron:
            same_depth += 1
    depth_ratio = round(int(dist_to_pron) / int(max(distances)), 2)
    return dist_to_pron, connection, comma_count, depth_ratio, same_depth

def syntax_interval_same_sentence(sent, ant_id, anaph_id):
    d1 = syntax_depth_root(sent, ant_id, d = [])
    d2 = syntax_depth_root(sent, anaph_id, d = [])
    #print(d1)
    #print(d2)
    t = 0
    k = None
    if len(d1) < len(d2):
        for q1 in range(len(d1)+1):
            if q1 != 0:
                if d2[-q1] == d1[-q1]:
                    t += 1
                else:
                    k = len(d1) + len(d2) + 2
                    break
    else:
        for q1 in range(len(d2)+1):
            if q1 != 0:
                if d1[-q1] == d2[-q1]:
                    t += 1
                else:
                    k = len(d1) + len(d2) + 2
                    break
    root = (len(d1) - t + 1) + (len(d2) - t + 1) + 1
    if k:
        root = k
    return root

def syntax_2_exp(sents, np, s_number, a_id):
    """Возращает синт. расстояние от антцедента до анафоры, разницу в их глубине, глубину антецедента"""
    connections = {'предл': 1, 'аппоз': 2, '1-компл': 3, 'соч-союзн': 4, 'квазиагент': 5, 'предик': 6}
    sent_with_anaphora = sents[-1]
    sent_with_antecedent = sents[s_number]
    anaphora_link = sent_with_anaphora[int(a_id)-1][6]
    antecedent_link = sent_with_antecedent[int(np[0])-1][6]
    antecedent_connection = sent_with_antecedent[int(np[0])-1][7]
    dist_2_anaphora = syntax_depth(sent_with_anaphora, anaphora_link, depth=1)
    dist_2_antecedent = syntax_depth(sent_with_antecedent, antecedent_link, depth=1)
    #print(dist_2_anaphora, dist_2_antecedent)
    depth_difference = dist_2_antecedent-dist_2_anaphora
    corefer_interval = 0
    if antecedent_connection in connections:
        antecedent_connection = connections[antecedent_connection]
    else:
        antecedent_connection = 0
    if s_number != len(sents) - 1:
        if s_number == 0:
            corefer_interval = ((len(sents) - 1) * 100) + dist_2_anaphora + dist_2_antecedent
        elif s_number == 1:
            corefer_interval = ((len(sents) - 2) * 100) + dist_2_anaphora + dist_2_antecedent
        elif s_number == 2:
            corefer_interval = ((len(sents) - 3) * 100) + dist_2_anaphora + dist_2_antecedent
    else:
        corefer_interval = syntax_interval_same_sentence(sent_with_anaphora, antecedent_link, anaphora_link)
    return corefer_interval, depth_difference, dist_2_antecedent, antecedent_connection

def get_features(sents, nps, conll_text, chains):
    vectors = []
    #syntax_connections = []
    snips, anaph_id = sents[:-1], sents[-1][0]
    for s in range(len(nps)):
        for np in nps[s]:
            #dbl = False
            if np[1] != "None":
                #print('1')
                vect = []
                len_ch, len_w = np_length(np)
                dist_ch, dist_w = distance_np2pronoun(snips, np, s, anaph_id)
                #baseline
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
                #syntax1
                distance_to_pronoun, con_type, commas, depth_ratio, same_depth_ration = syntax_1_exp(snips, anaph_id)
                vect.append(distance_to_pronoun)
                vect.append(con_type)
                vect.append(commas)
                vect.append(depth_ratio)
                vect.append(same_depth_ration)
                #syntax2
                coref_interval, depth_dif, dist_2_ant, ant_con = syntax_2_exp(snips, np, s, anaph_id)
                vect.append(coref_interval)
                vect.append(depth_dif)
                vect.append(dist_2_ant)
                vect.append(ant_con)
                #syntax3
                feature1, feature2, feature3, feature4 = syntax3(syntax_root_connections(snips[s], np[0], connections=[]))
                vect.append(feature1)
                vect.append(feature2)
                vect.append(feature3)
                vect.append(feature4)
                #target
                target, db = target_value(np, chains)
                #if db is True:
                    #dbl = True
                #if target == 1:
                    #syntax_connections += syntax_root_connections(snips[s], np[0], connections=[])
                vect.append(target)                                    #UNCOMMEND
                vectors.append(vect)
            #if dbl is True:
                #print('GOT IT')
    #print('NEXT')
    return vectors
