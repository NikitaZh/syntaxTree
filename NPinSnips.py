# -*- coding: utf8 -*-
#sent_arr = [['1\tХозяин\tхозяин\tN\tN\tNcmsny\t2\tпредик\t_\t_\n', '2\tсидит\tсидеть\tV\tV\tVmip3s-a-e\t0\tROOT\t_\t_\n', '3\tна\tна\tS\tS\tSp-l\t2\t1-компл\t_\t_\n', '4\tскамейке\tскамейка\tN\tN\tNcfsln\t3\tпредл\t_\t_\n', '5\tножка\tножка\tN\tN\tNcfsnn\t2\tсочин\t_\t_\n', '6\tна\tна\tS\tS\tSp-a\t5\tатриб\t_\t_\n', '7\tножку\tножка\tN\tN\tNcfsan\t6\tпредл\t_\t_\n', '8\t,\t,\t,\t,\t,\t7\tPUNC\t_\t_\n', '9\tсложив\tсложить\tV\tV\tVmgs---a-p\t2\tобст\t_\t_\n', '10\tих\tони\tP\tP\tP-3-pan\t9\t1-компл\t_\t_\n', '11\tвроде\tвроде\tS\tS\tSp-g\t9\tатриб\t_\t_\n', '12\tножниц\tножницы\tN\tN\tNcfpgn\t11\tпредл\t_\t_\n', '13\tи\tи\tC\tC\tC\t2\tсочин\t_\t_\n', '14\tвытянув\tвытянуть\tV\tV\tVmgs---a-p\t13\tсоч-союзн\t_\t_\n', '15\tнасколько\tнасколько\tR\tR\tR\t16\tобст\t_\t_\n', '16\tпозволяет\tпозволять\tV\tV\tVmip3s-a-e\t2\tизъясн\t_\t_\n', '17\tне\tне\tQ\tQ\tQ\t18\tогранич\t_\t_\n', '18\tтакая\tтакой\tP\tP\tP--fsna\t21\tопред\t_\t_\n', '19\tуж\tуж\tQ\tQ\tQ\t18\tогранич\t_\t_\n', '20\tвыразительная\tвыразительный\tA\tA\tAfpfsnf\t21\tопред\t_\t_\n', '21\tдлина\tдлина\tN\tN\tNcfsnn\t16\tпредик\t_\t_\n', '22\t.\t.\tS\tS\tSENT\t21\tPUNC\t_\t_\n'], ['1\tРуки\tрука\tN\tN\tNcfpnn\t4\tобст\t_\t_\n', '2\tон\tон\tP\tP\tP-3msnn\t4\tпредик\t_\t_\n', '3\tотчего-то\tотчего-то\tR\tR\tR\t4\tобст\t_\t_\n', '4\tдержал\tдержать\tV\tV\tVmis-sma-e\t0\tROOT\t_\t_\n', '5\tпереплетенными\tпереплетеннымь\tV\tV\tVmn----a-e\t4\t2-компл\t_\t_\n', '6\tна\tна\tS\tS\tSp-n\t5\t1-компл\t_\t_\n', '7\tгруди\tгрудь\tN\tN\tNcfsnnl\t6\tпредл\t_\t_\n', '8\t,\t,\t,\t,\t,\t7\tPUNC\t_\t_\n', '9\tвроде\tвроде\tQ\tQ\tQ\t13\tвводн\t_\t_\n', '10\tбы\tбы\tQ\tQ\tQ\t9\tвспом\t_\t_\n', '11\tкак\tкак\tC\tC\tC\t13\tсравнит\t_\t_\n', '12\tгрея\tгрея\tN\tN\tNcfsnn\t11\tсравн-союзн\t_\t_\n', '13\tпальцы\tпалец\tN\tN\tNcmpnn\t4\t1-компл\t_\t_\n', '14\tпод\tпод\tS\tS\tSp-i\t13\tатриб\t_\t_\n', '15\tмышками\tмышка\tN\tN\tNcfpin\t14\tпредл\t_\t_\n', '16\t,\t,\t,\t,\t,\t15\tPUNC\t_\t_\n', '17\t-\t-\t-\t-\t-\t15\tPUNC\t_\t_\n', '18\tпоза\tпоза\tN\tN\tNcfsnn\t4\tпредик\t_\t_\n', '19\tскорей\tскорей\tR\tR\tR\t20\tогранич\t_\t_\n', '20\tженская\tженский\tA\tA\tAfpfsnf\t4\tсуб-копр\t_\t_\n', '21\t,\t,\t,\t,\t,\t20\tPUNC\t_\t_\n', '22\tчем\tчем\tC\tC\tC\t19\tсравнит\t_\t_\n', '23\tмужская\tмужской\tA\tA\tAfpfsnf\t22\tсравн-союзн\t_\t_\n', '24\t.\t.\tS\tS\tSENT\t23\tPUNC\t_\t_\n'], ['1\tУ\tу\tS\tS\tSp-g\t4\tобст\t_\t_\n', '2\tТатьяны\tтатьяна\tN\tN\tNpfsgy\t1\tпредл\t_\t_\n', '3\tже\tже\tQ\tQ\tQ\t2\tогранич\t_\t_\n', '4\tФиногеновны\tфиногеновный\tA\tA\tAfpmpns\t0\tROOT\t_\t_\n', '5\tруки\tрука\tN\tN\tNcfpnn\t4\tпредик\t_\t_\n', '6\tобычно\tобычно\tR\tR\tR\t7\tогранич\t_\t_\n', '7\tв\tв\tS\tS\tSp-l\t4\tобст\t_\t_\n', '8\tколенях\tколено\tN\tN\tNcnpln\t7\tпредл\t_\t_\n', '9\t,\t,\t,\t,\t,\t8\tPUNC\t_\t_\n', '10\tладошка\tладошка\tN\tN\tNcfsnn\t4\tпредик\t_\t_\n', '11\tв\tв\tS\tS\tSp-l\t10\tатриб\t_\t_\n', '12\tладошке\tладошка\tN\tN\tNcfsln\t11\tпредл\t_\t_\n', '13\t,\t,\t,\t,\t,\t12\tPUNC\t_\t_\n', '14\tноги\tнога\tN\tN\tNcfpnn\t16\tпредик\t_\t_\n', '15\tшироко\tшироко\tR\tR\tR\t16\tобст\t_\t_\n', '16\tрасставлены\tрасставить\tV\tV\tVmps-p-psp\t4\tсент-соч\t_\t_\n', '17\t,\t,\t,\t,\t,\t16\tPUNC\t_\t_\n', '18\tупористо\tупористо\tR\tR\tR\t16\tсент-соч\t_\t_\n', '19\t,\t,\t,\t,\t,\t18\tPUNC\t_\t_\n', '20\tно\tно\tC\tC\tC\t18\tсочин\t_\t_\n', '21\tне\tне\tQ\tQ\tQ\t22\tогранич\t_\t_\n', '22\tчасто\tчасто\tR\tR\tR\t20\tсоч-союзн\t_\t_\n', '23\tдоводилось\tдоводиться\tV\tV\tVmis-snm-e\t4\tвводн\t_\t_\n', '24\tей\tона\tP\tP\tP-3fsdn\t23\tпредик\t_\t_\n', '25\tпосидеть\tпосидеть\tV\tV\tVmn----a-p\t4\tпредик\t_\t_\n', '26\tтак\tтак\tP\tP\tP-----r\t4\tобст\t_\t_\n', '27\tвот\tвот\tQ\tQ\tQ\t26\tогранич\t_\t_\n', '28\t,\t,\t,\t,\t,\t27\tPUNC\t_\t_\n', '29\tвольно\tвольно\tR\tR\tR\t0\tROOT\t_\t_\n', '30\t,\t,\t,\t,\t,\t29\tPUNC\t_\t_\n', '31\tв\tв\tS\tS\tSp-a\t0\tROOT\t_\t_\n', '32\tсвое\tсвой\tP\tP\tP--nsaa\t33\tопред\t_\t_\n', '33\tудовольствие\tудовольствие\tN\tN\tNcnsan\t31\tпредл\t_\t_\n', '34\t.\t.\tS\tS\tSENT\t33\tPUNC\t_\t_\n'], ['1\tКак\tкак\tC\tC\tC\t4\tобст\t_\t_\n', '2\tбы\tбы\tQ\tQ\tQ\t4\tаналит\t_\t_\n', '3\tнечаянно\tнечаянно\tR\tR\tR\t4\tобст\t_\t_\n', '4\tвцепившись\tвцепиться\tV\tV\tVmgs---m-p\t0\tROOT\t_\t_\n', '5\tв\tв\tS\tS\tSp-a\t4\t1-компл\t_\t_\n', '6\tскамейку\tскамейка\tN\tN\tNcfsan\t5\tпредл\t_\t_\n', '7\t,\t,\t,\t,\t,\t6\tPUNC\t_\t_\n', '8\tопершись\tопереться\tV\tV\tVmgs---m-p\t4\tобст\t_\t_\n', '9\tна\tна\tS\tS\tSp-a\t8\t1-компл\t_\t_\n', '10\tруки\tрука\tN\tN\tNcfpan\t9\tпредл\t_\t_\n', '11\t,\t,\t,\t,\t,\t10\tPUNC\t_\t_\n', '12\tспеленатая\tспеленатать\tV\tV\tVmgp---a-e\t8\tобст\t_\t_\n', '13\tболью\tболь\tN\tN\tNcfsin\t12\t2-компл\t_\t_\n', '14\tи\tи\tC\tC\tC\t13\tсочин\t_\t_\n', '15\tвнутренним\tвнутренний\tA\tA\tAfpnsif\t16\tопред\t_\t_\n', '16\tнапряжением\tнапряжение\tN\tN\tNcnsin\t14\tсоч-союзн\t_\t_\n', '17\t,\t,\t,\t,\t,\t16\tPUNC\t_\t_\n', '18\tбудто\tбудто\tC\tC\tC\t12\t1-компл\t_\t_\n', '19\tбеспомощный\tбеспомощный\tA\tA\tAfpmsnf\t20\tопред\t_\t_\n', '20\tмладенец\tмладенец\tN\tN\tNcmsny\t23\tпролепт\t_\t_\n', '21\tпеленальником\tпеленальник\tN\tN\tNcmsin\t20\tатриб\t_\t_\n', '22\t-\t-\t-\t-\t-\t21\tPUNC\t_\t_\n', '23\tвот\tвот\tQ\tQ\tQ\t24\tогранич\t_\t_\n', '24\tкак\tкак\tP\tP\tP-----r\t28\tобст\t_\t_\n', '25\tона\tона\tP\tP\tP-3fsnn\t28\tсуб-копр\t_\t_\n', '26\tпоследнее\tпоследний\tA\tA\tAfpnsaf\t27\tопред\t_\t_\n', '27\tвремя\tвремя\tN\tN\tNcnsan\t28\tпредик\t_\t_\n', '28\tсидела\tсидеть\tV\tV\tVmis-sfa-e\t18\tподч-союзн\t_\t_\n', '29\t:\t:\t-\t-\t-\t28\tPUNC\t_\t_\n', '30\tчаще\tчасто\tR\tR\tRc\t31\tобст\t_\t_\n', '31\tстало\tстать\tV\tV\tVmis-sna-p\t28\tизъясн\t_\t_\n', '32\tее\tона\tP\tP\tP-3fsan\t33\t1-компл\t_\t_\n', '33\tсхватывать\tсхватывать\tV\tV\tVmn----a-e\t31\t1-компл\t_\t_\n', '34\t,\t,\t,\t,\t,\t33\tPUNC\t_\t_\n', '35\tи\tи\tC\tC\tC\t31\tсент-соч\t_\t_\n', '36\tона\tона\tP\tP\tP-3fsnn\t37\tпредик\t_\t_\n', '37\tбоялась\tбояться\tV\tV\tVmis-sfm-e\t35\tсоч-союзн\t_\t_\n', '38\tупасть\tупасть\tV\tV\tVmn----a-p\t37\t1-компл\t_\t_\n', '39\tназемь\tназемь\tR\tR\tR\t38\tобст\t_\t_\n', '40\t.\t.\tS\tS\tSENT\t39\tPUNC\t_\t_\n'], '25']

def NP_connections(s, order=None, reference = None):
    arr = []
    for word in s:
        word = word.split('\t')
        if order and word[6] == order and word[7] != 'PUNC':
            arr += word[:2]
            arr += NP_connections(s, order=word[0])
        if reference and word[0] == reference and word[3] != 'V':
            arr += word[:2]
            arr += NP_connections(s, reference=word[6])

    return arr


def get_noun_phrases(snip):
    '''Возвращает именные группы по заданному снипу(предложения расположены соответствующим образом)'''
    sent_nps = []
    sentences, deadline = snip[:-1], snip[-1]
    for q in range(len(sentences)):
        np = []
        if q != len(sentences)-1:
            for word in sentences[q]:
                word = word.split('\t')
                orderN, gram, refer2 = word[0], word[3], word[6]
                if gram == 'N':
                    np.append(word[:2])
                    np[-1] += NP_connections(sentences[q], orderN, refer2)
        sent_nps.append(np)
    return sent_nps

#np = get_noun_phrases(sent_arr)


