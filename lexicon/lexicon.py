LEXICON_EN: dict[str, str] = {
    '/start': 'Hi! I\'m here to demonstrate how routers work =)',
    '/help': 'To tell the truth, i can only send copies...',
    'no_echo': 'It\'s unsupportable type O_o'
}

LEXICON_RU = {
    '/start': 'Привет! Говорят, в прошлой жизни все мы были булками...\n'\
        'Так сложилось, что я могу заглянуть внутрь тебя, задав всего  несколько вопросов.\n\n'\
        'Ты хочешь узнать кое-что новое о себе?',
    'quest_start': 'Класс, поехали!'
}

BUTTONS_TEST: dict[str, str] = {
    'bt1': 'BUTTON 1',
    'bt2': 'BUTTON 2',
    'bt3': 'BUTTON 3'
}

BUTTONS_LEXIC: dict[str, str] = {
    'quest_y': 'Конечно!',
    'quest_n': 'Отказываюсь :/'
}

QUEST_RES = dict(zip(
    ['печень', 'блин', 'багет', 'кулич', 'пирог', 'корги', \
    'пицца', 'наполеон', 'эчпочмак', 'слойка'],
    'Пирожок с печенью,Блинчик со сметанкой,Багет,Кулич,Вишневый пирог,Булка-корги,'\
    'Школьная питса,Наполеон!,Эчпочмак,Слойка с творогом'.split(',')
))
