with open('lexicon/data_raw.txt', 'r', encoding='utf-8') as f:
    questions = {}
    flag = True
    for line in f.readlines():
        if flag:
            key = line.rstrip()
            flag, val = False, []
        elif line == '\n':
            questions.update({key: val})
            flag = True
        else:
            txt, res = line.rstrip().split('\\')
            res = res.split(',')
            val.append({txt: res})

# {question: {
#     answer1: [
#         v1,
#         v2...
#         ]
#     }...
# }
