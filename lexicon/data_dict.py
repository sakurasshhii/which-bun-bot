with open('lexicon/data_raw.txt', 'r', encoding='utf-8') as f:
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
            # res = res.split(',')
            val.update({txt: 'quest,' + res})
            # names.update(set(res))

# print(QUEST)
# print(names)

# {question: {
#     answer1: [
#         v1,
#         v2...
#         ]
#     }...
# }
