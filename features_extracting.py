# -*- coding: utf8 -*-
from saText import parse_saText

#conll_text = 'OpenCorpora/682-done.conll'
#sent_arr = [[['1', 'Ивану', 'иван', 'N', 'N', 'Npmsdy', '0', 'ROOT', '_', '_', '2256'], ['2', 'Тихоновичу', 'тихонович', 'N', 'N', 'Npmsdy', '1', 'аппоз', '_', '_', '2263'], ['3', 'ближе', 'близкий', 'A', 'A', 'Afcmsnf', '1', 'опред', '_', '_', '2275'], ['4', 'к', 'к', 'S', 'S', 'Sp-d', '3', '1-компл', '_', '_', '2281'], ['5', 'сердцу', 'сердце', 'N', 'N', 'Ncnsdn', '4', 'предл', '_', '_', '2283'], ['6', ',', ',', ',', ',', ',', '5', 'PUNC', '_', '_', '2289'], ['7', 'конечно', 'конечно', 'R', 'R', 'R', '12', 'вводн', '_', '_', '2291'], ['8', ',', ',', ',', ',', ',', '7', 'PUNC', '_', '_', '2298'], ['9', 'синий', 'синий', 'A', 'A', 'Afpmsnf', '10', 'опред', '_', '_', '2301'], ['10', 'платочек', 'платочек', 'N', 'N', 'Ncmsnn', '12', 'предик', '_', '_', '2308'], ['11', '-', '-', '-', '-', '-', '10', 'PUNC', '_', '_', '2317'], ['12', 'краса', 'краса', 'N', 'N', 'Ncfsnn', '1', 'сочин', '_', '_', '2319'], ['13', 'и', 'и', 'C', 'C', 'C', '12', 'сочин', '_', '_', '2326'], ['14', 'память', 'память', 'N', 'N', 'Ncfsnn', '13', 'соч-союзн', '_', '_', '2328'], ['15', 'незабвенных', 'незабвенный', 'A', 'A', 'Afpmpaf', '16', 'опред', '_', '_', '2335'], ['16', 'лет', 'год', 'N', 'N', 'Ncmpgn', '14', 'атриб', '_', '_', '2348'], ['17', 'войны', 'война', 'N', 'N', 'Ncfsgn', '16', 'квазиагент', '_', '_', '2352'], ['18', ',', ',', ',', ',', ',', '17', 'PUNC', '_', '_', '2357'], ['19', 'совсем', 'совсем', 'R', 'R', 'R', '20', 'огранич', '_', '_', '2359'], ['20', 'почти', 'почти', 'R', 'R', 'R', '21', 'огранич', '_', '_', '2366'], ['21', 'отцветший', 'отцветший', 'A', 'A', 'Afpmsnf', '22', 'опред', '_', '_', '2372'], ['22', 'платочек', 'платочек', 'N', 'N', 'Ncmsnn', '12', 'сочин', '_', '_', '2383'], ['23', ',', ',', ',', ',', ',', '22', 'PUNC', '_', '_', '2391'], ['24', 'с', 'с', 'S', 'S', 'Sp-i', '22', 'атриб', '_', '_', '2393'], ['25', 'бордовой', 'бордовый', 'A', 'A', 'Afpfsif', '26', 'опред', '_', '_', '2396'], ['26', 'каемочкой', 'каемочка', 'N', 'N', 'Ncfsin', '24', 'предл', '_', '_', '2405'], ['27', 'по', 'по', 'S', 'S', 'Sp-d', '26', 'атриб', '_', '_', '2416'], ['28', 'блеклому', 'блеклый', 'A', 'A', 'Afpnsdf', '29', 'опред', '_', '_', '2420'], ['29', 'полю', 'поле', 'N', 'N', 'Ncnsdn', '27', 'предл', '_', '_', '2429'], ['30', '.', '.', 'S', 'S', 'SENT', '29', 'PUNC', '_', '_', '2433']], [['1', 'Как', 'как', 'C', 'C', 'C', '7', 'вводн', '_', '_', '2435'], ['2', 'увидит', 'увидеть', 'V', 'V', 'Vmif3s-a-p', '1', 'сравн-союзн', '_', '_', '2439'], ['3', 'его', 'он', 'P', 'P', 'P-3msan', '4', 'атриб', '_', '_', '2446'], ['4', 'Иван', 'иван', 'N', 'N', 'Npmsny', '2', 'предик', '_', '_', '2450'], ['5', 'Тихонович', 'тихонович', 'N', 'N', 'Npmsny', '4', 'аппоз', '_', '_', '2455'], ['6', '-', '-', '-', '-', '-', '5', 'PUNC', '_', '_', '2465'], ['7', 'стронется', 'стронться', 'V', 'V', 'Vmip3s-m-e', '0', 'ROOT', '_', '_', '2467'], ['8', 'его', 'его', 'P', 'P', 'P-----a', '9', 'квазиагент', '_', '_', '2478'], ['9', 'сердце', 'сердце', 'N', 'N', 'Ncnsnn', '7', 'предик', '_', '_', '2482'], ['10', 'с', 'с', 'S', 'S', 'Sp-g', '9', '2-компл', '_', '_', '2489'], ['11', 'места', 'место', 'N', 'N', 'Ncnsgn', '10', 'предл', '_', '_', '2491'], ['12', 'или', 'или', 'C', 'C', 'C', '7', 'сент-соч', '_', '_', '2497'], ['13', 'в', 'в', 'S', 'S', 'Sp-l', '15', 'обст', '_', '_', '2501'], ['14', 'сердце', 'сердце', 'N', 'N', 'Ncnsln', '13', 'предл', '_', '_', '2503'], ['15', 'сдвинется', 'сдвинуться', 'V', 'V', 'Vmif3s-m-p', '12', 'соч-союзн', '_', '_', '2510'], ['16', 'что-то', 'что-то', 'N', 'N', 'Ncnsnn', '15', 'предик', '_', '_', '000'], ['17', 'в', 'в', 'S', 'S', 'Sp-a', '16', 'атриб', '_', '_', '2527'], ['18', 'то', 'тот', 'P', 'P', 'P--nsaa', '19', 'опред', '_', '_', '2529'], ['19', 'место', 'место', 'N', 'N', 'Ncnsan', '17', 'предл', '_', '_', '2532'], ['20', ',', ',', ',', ',', ',', '19', 'PUNC', '_', '_', '2537'], ['21', 'где', 'где', 'P', 'P', 'P-----r', '26', 'обст', '_', '_', '2539'], ['22', 'теплые', 'теплый', 'A', 'A', 'Afpmpnf', '23', 'опред', '_', '_', '2543'], ['23', 'слезы', 'слеза', 'N', 'N', 'Ncfpnn', '26', 'предик', '_', '_', '2550'], ['24', ',', ',', ',', ',', ',', '23', 'PUNC', '_', '_', '2555'], ['25', '-', '-', '-', '-', '-', '23', 'PUNC', '_', '_', '2557'], ['26', 'вскипят', 'вскипеть', 'V', 'V', 'Vmip3p-a-e', '7', 'разъяснит', '_', '_', '2559'], ['27', 'они', 'они', 'P', 'P', 'P-3-pnn', '26', 'предик', '_', '_', '2568'], ['28', 'ни', 'ни', 'Q', 'Q', 'Q', '29', 'огранич', '_', '_', '2572'], ['29', 'с', 'с', 'S', 'S', 'Sp-g', '26', 'обст', '_', '_', '2575'], ['30', 'того', 'то', 'P', 'P', 'P--nsgn', '29', 'предл', '_', '_', '2577'], ['31', 'ни', 'ни', 'C', 'C', 'C', '45', 'соотнос', '_', '_', '2582'], ['32', 'с', 'с', 'S', 'S', 'Sp-g', '26', 'обст', '_', '_', '2586'], ['33', 'сего', 'сие', 'P', 'P', 'P--nsgn', '32', 'предл', '_', '_', '2588'], ['34', ',', ',', ',', ',', ',', '33', 'PUNC', '_', '_', '2592'], ['35', 'порой', 'пора', 'N', 'N', 'Ncfsin', '45', 'огранич', '_', '_', '2595'], ['36', 'из-за', 'из-за', 'N', 'N', 'Ncmsgn', '35', '1-компл', '_', '_', '2601'], ['37', 'совершенного', 'совершенный', 'A', 'A', 'Afpmsgf', '38', 'опред', '_', '_', '2607'], ['38', 'пустяка', 'пустяк', 'N', 'N', 'Ncmsgn', '36', '1-компл', '_', '_', '2620'], ['39', ',', ',', ',', ',', ',', '38', 'PUNC', '_', '_', '2627'], ['40', 'из-за', 'из-за', 'N', 'N', 'Ncmsgn', '38', 'разъяснит', '_', '_', '2630'], ['41', 'картинки', 'картинка', 'N', 'N', 'Ncfsgn', '40', '1-компл', '_', '_', '2636'], ['42', 'в', 'в', 'S', 'S', 'Sp-l', '41', 'атриб', '_', '_', '2645'], ['43', 'газете', 'газета', 'N', 'N', 'Ncfsln', '42', 'предл', '_', '_', '2647'], ['44', ',', ',', ',', ',', ',', '43', 'PUNC', '_', '_', '2653'], ['45', 'или', 'или', 'C', 'C', 'C', '32', 'сочин', '_', '_', '2655'], ['46', 'покажут', 'показать', 'V', 'V', 'Vmif3p-a-p', '45', 'соч-союзн', '_', '_', '2659'], ['47', 'по', 'по', 'S', 'S', 'Sp-d', '46', 'обст', '_', '_', '2667'], ['48', 'телевизору', 'телевизор', 'N', 'N', 'Ncmsdn', '47', 'предл', '_', '_', '2670'], ['49', 'что', 'что', 'C', 'C', 'C', '50', 'предик', '_', '_', '2681'], ['50', 'военное', 'военный', 'A', 'A', 'Afpnsnf', '46', '1-компл', '_', '_', '2686'], ['51', ',', ',', ',', ',', ',', '50', 'PUNC', '_', '_', '2693'], ['52', 'либо', 'либо', 'C', 'C', 'C', '26', 'сент-соч', '_', '_', '2695'], ['53', 'про', 'про', 'S', 'S', 'Sp-a', '55', '3-компл', '_', '_', '2701'], ['54', 'разлуку', 'разлука', 'N', 'N', 'Ncfsan', '53', 'предл', '_', '_', '2705'], ['55', 'запоют', 'запеть', 'V', 'V', 'Vmif3p-a-p', '52', 'соч-союзн', '_', '_', '2713'], ['56', 'по', 'по', 'S', 'S', 'Sp-d', '55', 'обст', '_', '_', '2720'], ['57', 'радио', 'радио', 'N', 'N', 'Ncnsdn', '56', 'предл', '_', '_', '2724'], ['58', '-', '-', '-', '-', '-', '57', 'PUNC', '_', '_', '2731'], ['59', 'и', 'и', 'C', 'C', 'C', '55', 'сент-соч', '_', '_', '2734'], ['60', 'вот', 'вот', 'Q', 'Q', 'Q', '62', 'огранич', '_', '_', '2737'], ['61', 'уж', 'уж', 'Q', 'Q', 'Q', '60', 'огранич', '_', '_', '2741'], ['62', 'подмоет', 'подмыть', 'V', 'V', 'Vmip3s-a-e', '59', 'соч-союзн', '_', '_', '2745'], ['63', 'ретивое', 'ретивое', 'N', 'N', 'Ncnsnn', '62', '1-компл', '_', '_', '2753'], ['64', ',', ',', ',', ',', ',', '63', 'PUNC', '_', '_', '2760'], ['65', 'затрясет', 'затрясть', 'V', 'V', 'Vmip3s-a-e', '7', 'вводн', '_', '_', '2763'], ['66', 'его', 'он', 'P', 'P', 'P-3msan', '65', 'предик', '_', '_', '2772'], ['67', 'что', 'что', 'C', 'C', 'C', '65', '1-компл', '_', '_', '2777'], ['68', 'осенний', 'осенний', 'A', 'A', 'Afpmsnf', '70', 'опред', '_', '_', '2782'], ['69', 'выветренный', 'выветренный', 'A', 'A', 'Afpmsnf', '70', 'опред', '_', '_', '2790'], ['70', 'лист', 'лист', 'N', 'N', 'Ncmsnn', '71', 'предик', '_', '_', '2802'], ['71', '...', '...', 'V', 'V', 'Vmip3s-a-e', '67', 'подч-союзн', '_', '_', '2806'], ['72', 'Н-да', 'н-да', 'N', 'N', 'Ncfsnn', '71', '1-компл', '_', '_', '000'], ['73', ',', ',', ',', ',', ',', '72', 'PUNC', '_', '_', '2820'], ['74', 'время', 'время', 'N', 'N', 'Ncnsnn', '71', 'длительн', '_', '_', '2822'], ['75', '!', '!', 'S', 'S', 'SENT', '74', 'PUNC', '_', '_', '2827']], [['1', 'Не', 'не', 'Q', 'Q', 'Q', '2', 'огранич', '_', '_', '2829'], ['2', 'один', 'один', 'P', 'P', 'P--msna', '6', 'количест', '_', '_', '2832'], ['3', 'он', 'он', 'P', 'P', 'P-3msnn', '6', 'предик', '_', '_', '2837'], ['4', 'такой', 'такой', 'P', 'P', 'P--msna', '5', 'опред', '_', '_', '2841'], ['5', 'слезливый', 'слезливый', 'A', 'A', 'Afpmsnf', '6', 'предик', '_', '_', '2847'], ['6', 'сделался', 'сделаться', 'V', 'V', 'Vmis-smm-p', '0', 'ROOT', '_', '_', '2858'], ['7', '.', '.', 'S', 'S', 'SENT', '6', 'PUNC', '_', '_', '2866']], [['1', 'Не', 'не', 'Q', 'Q', 'Q', '2', 'огранич', '_', '_', '2868'], ['2', 'одного', 'один', 'M', 'M', 'Mom-g', '4', 'количест', '_', '_', '2872'], ['3', 'его', 'он', 'P', 'P', 'P-3msan', '4', '1-компл', '_', '_', '2879'], ['4', 'мяла', 'мять', 'V', 'V', 'Vmis-sfa-p', '0', 'ROOT', '_', '_', '2883'], ['5', 'жизнь', 'жизнь', 'N', 'N', 'Ncfsnn', '3', 'предик', '_', '_', '2888'], ['6', ',', ',', ',', ',', ',', '5', 'PUNC', '_', '_', '2893'], ['7', 'валяла', 'валять', 'V', 'V', 'Vmis-sfa-e', '4', 'сочин', '_', '_', '2895'], ['8', ',', ',', ',', ',', ',', '7', 'PUNC', '_', '_', '2901'], ['9', 'утюжила', 'утюжить', 'V', 'V', 'Vmis-sfa-e', '7', 'сочин', '_', '_', '2904'], ['10', ',', ',', ',', ',', ',', '9', 'PUNC', '_', '_', '2911'], ['11', 'мочила', 'мочить', 'V', 'V', 'Vmis-sfa-e', '9', 'сочин', '_', '_', '2913'], ['12', 'и', 'и', 'C', 'C', 'C', '11', 'сочин', '_', '_', '2920'], ['13', 'сушила', 'сушить', 'V', 'V', 'Vmis-sfa-e', '12', 'соч-союзн', '_', '_', '2922'], ['14', '.', '.', 'S', 'S', 'SENT', '13', 'PUNC', '_', '_', '2928']], ['3', '2879']]

#sent_arr_np = [[['1', 'Ивану', '2256', '2', 'Тихоновичу', '2263'], ['2', 'Тихоновичу', '2263'], ['5', 'сердцу', '2283'], ['10', 'платочек', '2308', '9', 'синий', '2301'], ['12', 'краса', '2319', '7', 'конечно', '2291', '10', 'платочек', '2308', '9', 'синий', '2301', '13', 'и', '2326', '14', 'память', '2328', '16', 'лет', '2348', '15', 'незабвенных', '2335', '17', 'войны', '2352', '22', 'платочек', '2383', '21', 'отцветший', '2372', '24', 'с', '2393', '26', 'каемочкой', '2405', '25', 'бордовой', '2396', '27', 'по', '2416', '29', 'полю', '2429', '28', 'блеклому', '2420', '21', 'отцветший', '2372', '24', 'с', '2393', '26', 'каемочкой', '2405', '25', 'бордовой', '2396', '27', 'по', '2416', '29', 'полю', '2429', '28', 'блеклому', '2420'], ['14', 'память', '2328', '16', 'лет', '2348', '15', 'незабвенных', '2335', '17', 'войны', '2352'], ['16', 'лет', '2348', '15', 'незабвенных', '2335', '17', 'войны', '2352'], ['17', 'войны', '2352'], ['22', 'платочек', '2383', '21', 'отцветший', '2372', '24', 'с', '2393', '26', 'каемочкой', '2405', '25', 'бордовой', '2396', '27', 'по', '2416', '29', 'полю', '2429', '28', 'блеклому', '2420'], ['26', 'каемочкой', '2405', '25', 'бордовой', '2396', '27', 'по', '2416', '29', 'полю', '2429', '28', 'блеклому', '2420'], ['29', 'полю', '2429', '28', 'блеклому', '2420']], [['4', 'Иван', '2450', '3', 'его', '2446', '5', 'Тихонович', '2455'], ['5', 'Тихонович', '2455'], ['9', 'сердце', '2482', '8', 'его', '2478', '10', 'с', '2489', '11', 'места', '2491'], ['11', 'места', '2491'], ['14', 'сердце', '2503'], ['16', 'что-то', '000', '17', 'в', '2527', '19', 'место', '2532', '18', 'то', '2529'], ['19', 'место', '2532', '18', 'то', '2529'], ['23', 'слезы', '2550', '22', 'теплые', '2543'], ['35', 'порой', '2595', '36', 'из-за', '2601', '38', 'пустяка', '2620', '37', 'совершенного', '2607', '40', 'из-за', '2630', '41', 'картинки', '2636', '42', 'в', '2645', '43', 'газете', '2647'], ['36', 'из-за', '2601', '38', 'пустяка', '2620', '37', 'совершенного', '2607', '40', 'из-за', '2630', '41', 'картинки', '2636', '42', 'в', '2645', '43', 'газете', '2647'], ['38', 'пустяка', '2620', '37', 'совершенного', '2607', '40', 'из-за', '2630', '41', 'картинки', '2636', '42', 'в', '2645', '43', 'газете', '2647'], ['40', 'из-за', '2630', '41', 'картинки', '2636', '42', 'в', '2645', '43', 'газете', '2647'], ['41', 'картинки', '2636', '42', 'в', '2645', '43', 'газете', '2647'], ['43', 'газете', '2647'], ['48', 'телевизору', '2670'], ['54', 'разлуку', '2705'], ['57', 'радио', '2724'], ['63', 'ретивое', '2753'], ['70', 'лист', '2802', '68', 'осенний', '2782', '69', 'выветренный', '2790'], ['72', 'Н-да', '000'], ['74', 'время', '2822']], [['0', 'None', '000']], [['5', 'жизнь', '2888']]]

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
    #pronouns = ['он', 'она', 'оно', 'они', 'его', 'её', 'их', 'свой', 'мой', 'себя', 'который']
    perpronouns = ['он', 'она', 'оно', 'они', 'мой', 'их', 'его', 'её']
    refpronouns = ['свой', 'себя']
    relpronouns = ['который']
    pronoun_gram_info = s[-1][int(a_id)-1]
    #pronoun_gram_info = pronoun_gram_info.split('\t')
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
        #print('1')
        arr.append(sent[int(ordinal_n)-1][0])
    else:
        #print('2')
        arr.append(sent[int(ordinal_n)-1][0])
        syntax_depth_root(sent, sent[int(ordinal_n)-1][6], arr)
    return d


def syntax_1_exp(sents, a_id):
    """Возращает глубину местоимения, тип связи местоимения, количество запятых, отношение глубины мест к глубине дерева и количество узлов с той же глубиной"""
    connections = {'вспом': 0, 'сравнит': 0, 'предик': 1, '1-компл': 4, 'атриб': 0, 'ROOT': 0, 'опред': 2, 'обст': 25, 'соч-союзн': 0, 'квазиагент': 5, 'дат-субъект': 0, 'сент-соч': 0, 'агент': 0, 'предл': 3, 'неакт-компл': 0, 'суб-копр': 0, '2-компл': 6}
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

#syntax_1(sent_arr[:-1], sent_arr[-1][0])
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




#syntax_2_exp(sent_arr[:-1], ['5', 'жизнь', '2888'], 3, sent_arr[-1][0])

def get_features(sents, nps, conll_text, chains):
    vectors = []
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
                #syntax info
                distance_to_pronoun, con_type, commas, depth_ratio, same_depth_ration = syntax_1_exp(snips, anaph_id)
                vect.append(distance_to_pronoun)
                vect.append(con_type)
                vect.append(commas)
                vect.append(depth_ratio)
                vect.append(same_depth_ration)
                #syntax_info_2nd_exp
                coref_interval, depth_dif, dist_2_ant, ant_con = syntax_2_exp(snips, np, s, anaph_id)
                vect.append(coref_interval)
                vect.append(depth_dif)
                vect.append(dist_2_ant)
                vect.append(ant_con)
                #target
                target, db = target_value(np, chains)
                #if db is True:
                    #dbl = True
                vect.append(target)                                    #UNCOMMEND
                vectors.append(vect)
            #if dbl is True:
                #print('GOT IT')
    #print('NEXT')
    return vectors

#p = get_features(sent_arr, sent_arr_np, conll_text, chains_arr)
#for q in p:
    #print(q)