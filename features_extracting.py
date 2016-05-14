# -*- coding: utf8 -*-
from saText import parse_saText

conll_text = '2_astafiev_zhizn_prozhit.conll'
sent_arr = [['1\tХозяин\tхозяин\tN\tN\tNcmsny\t2\tпредик\t_\t_\n', '2\tсидит\tсидеть\tV\tV\tVmip3s-a-e\t0\tROOT\t_\t_\n', '3\tна\tна\tS\tS\tSp-l\t2\t1-компл\t_\t_\n', '4\tскамейке\tскамейка\tN\tN\tNcfsln\t3\tпредл\t_\t_\n', '5\tножка\tножка\tN\tN\tNcfsnn\t2\tсочин\t_\t_\n', '6\tна\tна\tS\tS\tSp-a\t5\tатриб\t_\t_\n', '7\tножку\tножка\tN\tN\tNcfsan\t6\tпредл\t_\t_\n', '8\t,\t,\t,\t,\t,\t7\tPUNC\t_\t_\n', '9\tсложив\tсложить\tV\tV\tVmgs---a-p\t2\tобст\t_\t_\n', '10\tих\tони\tP\tP\tP-3-pan\t9\t1-компл\t_\t_\n', '11\tвроде\tвроде\tS\tS\tSp-g\t9\tатриб\t_\t_\n', '12\tножниц\tножницы\tN\tN\tNcfpgn\t11\tпредл\t_\t_\n', '13\tи\tи\tC\tC\tC\t2\tсочин\t_\t_\n', '14\tвытянув\tвытянуть\tV\tV\tVmgs---a-p\t13\tсоч-союзн\t_\t_\n', '15\tнасколько\tнасколько\tR\tR\tR\t16\tобст\t_\t_\n', '16\tпозволяет\tпозволять\tV\tV\tVmip3s-a-e\t2\tизъясн\t_\t_\n', '17\tне\tне\tQ\tQ\tQ\t18\tогранич\t_\t_\n', '18\tтакая\tтакой\tP\tP\tP--fsna\t21\tопред\t_\t_\n', '19\tуж\tуж\tQ\tQ\tQ\t18\tогранич\t_\t_\n', '20\tвыразительная\tвыразительный\tA\tA\tAfpfsnf\t21\tопред\t_\t_\n', '21\tдлина\tдлина\tN\tN\tNcfsnn\t16\tпредик\t_\t_\n', '22\t.\t.\tS\tS\tSENT\t21\tPUNC\t_\t_\n'], ['1\tРуки\tрука\tN\tN\tNcfpnn\t4\tобст\t_\t_\n', '2\tон\tон\tP\tP\tP-3msnn\t4\tпредик\t_\t_\n', '3\tотчего-то\tотчего-то\tR\tR\tR\t4\tобст\t_\t_\n', '4\tдержал\tдержать\tV\tV\tVmis-sma-e\t0\tROOT\t_\t_\n', '5\tпереплетенными\tпереплетеннымь\tV\tV\tVmn----a-e\t4\t2-компл\t_\t_\n', '6\tна\tна\tS\tS\tSp-n\t5\t1-компл\t_\t_\n', '7\tгруди\tгрудь\tN\tN\tNcfsnnl\t6\tпредл\t_\t_\n', '8\t,\t,\t,\t,\t,\t7\tPUNC\t_\t_\n', '9\tвроде\tвроде\tQ\tQ\tQ\t13\tвводн\t_\t_\n', '10\tбы\tбы\tQ\tQ\tQ\t9\tвспом\t_\t_\n', '11\tкак\tкак\tC\tC\tC\t13\tсравнит\t_\t_\n', '12\tгрея\tгрея\tN\tN\tNcfsnn\t11\tсравн-союзн\t_\t_\n', '13\tпальцы\tпалец\tN\tN\tNcmpnn\t4\t1-компл\t_\t_\n', '14\tпод\tпод\tS\tS\tSp-i\t13\tатриб\t_\t_\n', '15\tмышками\tмышка\tN\tN\tNcfpin\t14\tпредл\t_\t_\n', '16\t,\t,\t,\t,\t,\t15\tPUNC\t_\t_\n', '17\t-\t-\t-\t-\t-\t15\tPUNC\t_\t_\n', '18\tпоза\tпоза\tN\tN\tNcfsnn\t4\tпредик\t_\t_\n', '19\tскорей\tскорей\tR\tR\tR\t20\tогранич\t_\t_\n', '20\tженская\tженский\tA\tA\tAfpfsnf\t4\tсуб-копр\t_\t_\n', '21\t,\t,\t,\t,\t,\t20\tPUNC\t_\t_\n', '22\tчем\tчем\tC\tC\tC\t19\tсравнит\t_\t_\n', '23\tмужская\tмужской\tA\tA\tAfpfsnf\t22\tсравн-союзн\t_\t_\n', '24\t.\t.\tS\tS\tSENT\t23\tPUNC\t_\t_\n'], ['1\tУ\tу\tS\tS\tSp-g\t4\tобст\t_\t_\n', '2\tТатьяны\tтатьяна\tN\tN\tNpfsgy\t1\tпредл\t_\t_\n', '3\tже\tже\tQ\tQ\tQ\t2\tогранич\t_\t_\n', '4\tФиногеновны\tфиногеновный\tA\tA\tAfpmpns\t0\tROOT\t_\t_\n', '5\tруки\tрука\tN\tN\tNcfpnn\t4\tпредик\t_\t_\n', '6\tобычно\tобычно\tR\tR\tR\t7\tогранич\t_\t_\n', '7\tв\tв\tS\tS\tSp-l\t4\tобст\t_\t_\n', '8\tколенях\tколено\tN\tN\tNcnpln\t7\tпредл\t_\t_\n', '9\t,\t,\t,\t,\t,\t8\tPUNC\t_\t_\n', '10\tладошка\tладошка\tN\tN\tNcfsnn\t4\tпредик\t_\t_\n', '11\tв\tв\tS\tS\tSp-l\t10\tатриб\t_\t_\n', '12\tладошке\tладошка\tN\tN\tNcfsln\t11\tпредл\t_\t_\n', '13\t,\t,\t,\t,\t,\t12\tPUNC\t_\t_\n', '14\tноги\tнога\tN\tN\tNcfpnn\t16\tпредик\t_\t_\n', '15\tшироко\tшироко\tR\tR\tR\t16\tобст\t_\t_\n', '16\tрасставлены\tрасставить\tV\tV\tVmps-p-psp\t4\tсент-соч\t_\t_\n', '17\t,\t,\t,\t,\t,\t16\tPUNC\t_\t_\n', '18\tупористо\tупористо\tR\tR\tR\t16\tсент-соч\t_\t_\n', '19\t,\t,\t,\t,\t,\t18\tPUNC\t_\t_\n', '20\tно\tно\tC\tC\tC\t18\tсочин\t_\t_\n', '21\tне\tне\tQ\tQ\tQ\t22\tогранич\t_\t_\n', '22\tчасто\tчасто\tR\tR\tR\t20\tсоч-союзн\t_\t_\n', '23\tдоводилось\tдоводиться\tV\tV\tVmis-snm-e\t4\tвводн\t_\t_\n', '24\tей\tона\tP\tP\tP-3fsdn\t23\tпредик\t_\t_\n', '25\tпосидеть\tпосидеть\tV\tV\tVmn----a-p\t4\tпредик\t_\t_\n', '26\tтак\tтак\tP\tP\tP-----r\t4\tобст\t_\t_\n', '27\tвот\tвот\tQ\tQ\tQ\t26\tогранич\t_\t_\n', '28\t,\t,\t,\t,\t,\t27\tPUNC\t_\t_\n', '29\tвольно\tвольно\tR\tR\tR\t0\tROOT\t_\t_\n', '30\t,\t,\t,\t,\t,\t29\tPUNC\t_\t_\n', '31\tв\tв\tS\tS\tSp-a\t0\tROOT\t_\t_\n', '32\tсвое\tсвой\tP\tP\tP--nsaa\t33\tопред\t_\t_\n', '33\tудовольствие\tудовольствие\tN\tN\tNcnsan\t31\tпредл\t_\t_\n', '34\t.\t.\tS\tS\tSENT\t33\tPUNC\t_\t_\n'], ['1\tКак\tкак\tC\tC\tC\t4\tобст\t_\t_\n', '2\tбы\tбы\tQ\tQ\tQ\t4\tаналит\t_\t_\n', '3\tнечаянно\tнечаянно\tR\tR\tR\t4\tобст\t_\t_\n', '4\tвцепившись\tвцепиться\tV\tV\tVmgs---m-p\t0\tROOT\t_\t_\n', '5\tв\tв\tS\tS\tSp-a\t4\t1-компл\t_\t_\n', '6\tскамейку\tскамейка\tN\tN\tNcfsan\t5\tпредл\t_\t_\n', '7\t,\t,\t,\t,\t,\t6\tPUNC\t_\t_\n', '8\tопершись\tопереться\tV\tV\tVmgs---m-p\t4\tобст\t_\t_\n', '9\tна\tна\tS\tS\tSp-a\t8\t1-компл\t_\t_\n', '10\tруки\tрука\tN\tN\tNcfpan\t9\tпредл\t_\t_\n', '11\t,\t,\t,\t,\t,\t10\tPUNC\t_\t_\n', '12\tспеленатая\tспеленатать\tV\tV\tVmgp---a-e\t8\tобст\t_\t_\n', '13\tболью\tболь\tN\tN\tNcfsin\t12\t2-компл\t_\t_\n', '14\tи\tи\tC\tC\tC\t13\tсочин\t_\t_\n', '15\tвнутренним\tвнутренний\tA\tA\tAfpnsif\t16\tопред\t_\t_\n', '16\tнапряжением\tнапряжение\tN\tN\tNcnsin\t14\tсоч-союзн\t_\t_\n', '17\t,\t,\t,\t,\t,\t16\tPUNC\t_\t_\n', '18\tбудто\tбудто\tC\tC\tC\t12\t1-компл\t_\t_\n', '19\tбеспомощный\tбеспомощный\tA\tA\tAfpmsnf\t20\tопред\t_\t_\n', '20\tмладенец\tмладенец\tN\tN\tNcmsny\t23\tпролепт\t_\t_\n', '21\tпеленальником\tпеленальник\tN\tN\tNcmsin\t20\tатриб\t_\t_\n', '22\t-\t-\t-\t-\t-\t21\tPUNC\t_\t_\n', '23\tвот\tвот\tQ\tQ\tQ\t24\tогранич\t_\t_\n', '24\tкак\tкак\tP\tP\tP-----r\t28\tобст\t_\t_\n', '25\tона\tона\tP\tP\tP-3fsnn\t28\tсуб-копр\t_\t_\n', '26\tпоследнее\tпоследний\tA\tA\tAfpnsaf\t27\tопред\t_\t_\n', '27\tвремя\tвремя\tN\tN\tNcnsan\t28\tпредик\t_\t_\n', '28\tсидела\tсидеть\tV\tV\tVmis-sfa-e\t18\tподч-союзн\t_\t_\n', '29\t:\t:\t-\t-\t-\t28\tPUNC\t_\t_\n', '30\tчаще\tчасто\tR\tR\tRc\t31\tобст\t_\t_\n', '31\tстало\tстать\tV\tV\tVmis-sna-p\t28\tизъясн\t_\t_\n', '32\tее\tона\tP\tP\tP-3fsan\t33\t1-компл\t_\t_\n', '33\tсхватывать\tсхватывать\tV\tV\tVmn----a-e\t31\t1-компл\t_\t_\n', '34\t,\t,\t,\t,\t,\t33\tPUNC\t_\t_\n', '35\tи\tи\tC\tC\tC\t31\tсент-соч\t_\t_\n', '36\tона\tона\tP\tP\tP-3fsnn\t37\tпредик\t_\t_\n', '37\tбоялась\tбояться\tV\tV\tVmis-sfm-e\t35\tсоч-союзн\t_\t_\n', '38\tупасть\tупасть\tV\tV\tVmn----a-p\t37\t1-компл\t_\t_\n', '39\tназемь\tназемь\tR\tR\tR\t38\tобст\t_\t_\n', '40\t.\t.\tS\tS\tSENT\t39\tPUNC\t_\t_\n'], '25']
sent_arr_np = [[['1', 'Хозяин'], ['4', 'скамейке', '3', 'на'], ['5', 'ножка', '6', 'на', '7', 'ножку'], ['7', 'ножку', '6', 'на', '5', 'ножка'], ['12', 'ножниц', '11', 'вроде'], ['21', 'длина', '18', 'такая', '17', 'не', '19', 'уж', '20', 'выразительная']], [['1', 'Руки'], ['7', 'груди', '6', 'на'], ['12', 'грея', '11', 'как', '13', 'пальцы'], ['13', 'пальцы', '9', 'вроде', '10', 'бы', '11', 'как', '12', 'грея', '14', 'под', '15', 'мышками'], ['15', 'мышками', '14', 'под', '13', 'пальцы'], ['18', 'поза']], [['2', 'Татьяны', '1', 'У', '4', 'Финогеновны', '3', 'же'], ['5', 'руки', '4', 'Финогеновны'], ['8', 'коленях', '7', 'в', '4', 'Финогеновны'], ['10', 'ладошка', '4', 'Финогеновны', '11', 'в', '12', 'ладошке'], ['12', 'ладошке', '11', 'в', '10', 'ладошка', '4', 'Финогеновны'], ['14', 'ноги'], ['33', 'удовольствие', '31', 'в', '32', 'свое']], [['6', 'скамейку', '5', 'в'], ['10', 'руки', '9', 'на'], ['13', 'болью', '14', 'и', '16', 'напряжением', '15', 'внутренним'], ['16', 'напряжением', '14', 'и', '13', 'болью', '15', 'внутренним'], ['20', 'младенец', '19', 'беспомощный', '21', 'пеленальником', '23', 'вот', '24', 'как'], ['21', 'пеленальником', '20', 'младенец', '23', 'вот', '24', 'как'], ['27', 'время', '26', 'последнее']]]

def np_length(np):
    length_characters = 0
    length_words = 0
    for q in np[1::2]:
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
            word = word.split('\t')
            dist_characters += len(word[1])
            dist_words += 1
    return dist_characters, dist_words


#print(distance_np2pronoun(sent_arr[:-1], ['5', 'руки', '4', 'Финогеновны'], 2, 25))

def gram_agreement(s, np, s_number, a_id):
    gender = 0 #doesnt match
    number = 0
    ordinal_id = int(np[0])
    candidate_gram_info = s[s_number][ordinal_id-1]
    candidate_gram_info = candidate_gram_info.split('\t')
    candidate_gram_info = candidate_gram_info[5]
    cand_gender = candidate_gram_info[2]
    cand_number = candidate_gram_info[3]
    pronoun_gram_info = s[-1][int(a_id)-1]
    pronoun_gram_info = pronoun_gram_info.split('\t')
    pronoun_gram_info = pronoun_gram_info[5]
    pron_gender = pronoun_gram_info[3]
    pron_number = pronoun_gram_info[4]
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
    pronoun_gram_info = pronoun_gram_info.split('\t')
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
    lemma = lemma.split('\t')
    lemma = lemma[2]
    main_sent = s[s_number]
    for q in sentences:
        if q != main_sent:
            for word in q:
                word = word.split('\t')
                lemma_info = word[2]
                if lemma_info == lemma:
                    salience_value += 1
        else:
            break
    return salience_value

#noun_salience('2_astafiev_zhizn_prozhit.conll', sent_arr[:-1], ['27', 'время', '26', 'последнее'], 3)

def get_features(sents, nps):
    snips, anaph_id = sents[:-1], sents[-1]
    for s in range(len(nps)):
        #print(s)
        for np in nps[s]:
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
            print(vect)


get_features(sent_arr, sent_arr_np)