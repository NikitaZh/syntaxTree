# -*- coding: utf8 -*-

def get_doc_ids(txt_file):
    '''Достает из документа с айди массив где первый элемент айди, второй - название документа'''
    doc = open(txt_file,'r', encoding='utf-8')
    arr = []
    i = False
    for line in doc:
        line = line.split()
        if i is False:
            i = True
        else:
            arr.append(line[:2])
    doc.close()
    return arr

def get_ids_text(groups_text, id):
    '''Достает из текста с чейнами только нужные строчки, соответствующие тексту(по айди)'''
    t = open(groups_text, 'r', encoding='utf-8')
    id_text = []
    for line in t:
        line = line.split('\t')
        if line[0] == str(id):
            id_text.append(line)
    t.close()
    return id_text

def get_chain(chains_arr, numb):
    chain = []
    for line in chains_arr:
        if line[3] == numb:
            if len(line[10]) > 0:
                l = line[11].strip('\n')
                if ',' in l:
                    l = l.split(',')
                    chain.append([line[7], l[0]])
                else:
                    chain.append([line[7], l])
            else:
                chain.append([line[7], line[5]])
    return chain

def get_coref_chains(chains_arr):
    '''Из массива с чейнами достает местоимения и их цепочки'''
    pron_chains = []
    for line in chains_arr:
        if 'str:pron' in line[9]:
            chain = get_chain(chains_arr, line[3])
            pron_chains.append([[line[7], line[5]], chain])
        elif 'str:refl' in line[9]:
            chain = get_chain(chains_arr, line[3])
            pron_chains.append([[line[7], line[5]], chain])
        elif 'str:rel' in line[9]:
            chain = get_chain(chains_arr, line[3])
            pron_chains.append([[line[7], line[5]], chain])
        elif 'str:poss' in line[9]:
            chain = get_chain(chains_arr, line[3])
            pron_chains.append([[line[7], line[5]], chain])
    return pron_chains

#p = get_ids_text('Groups.txt', 66)
#ch = get_coref_chains(p)
#print(ch)