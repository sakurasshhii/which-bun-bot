def data_convert(filename: str) -> dict:
    with open(filename, 'r', encoding='utf-8') as f:
        QUEST = {}
        # names = set()
        flag = True
        for line in f.readlines():
            if flag:
                key = line.rstrip()
                flag, val = False, {}
            elif line == '\n':
                QUEST.update({key: val})
                flag = True
            else:
                txt, res = line.rstrip().split('\\')
                val.update({txt: 'quest,' + res})
    return QUEST
