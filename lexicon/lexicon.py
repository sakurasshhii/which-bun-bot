LEXICON_RU = {
    '/start': 'Привет! Говорят, в прошлой жизни все мы были булками...\n'\
        'Так сложилось, что я могу заглянуть внутрь тебя, задав всего  несколько вопросов.\n\n'\
        'Ты хочешь узнать кое-что новое о себе?',
    '/help': 'Для запуска нажмите /start\n\n'\
        'Тест создан при поддержке @sakurasshhii 🥰',
    'quest_start': 'Класс, поехали!',
    'quest_load': 'Такс... посмотрим, секундлчку...\n'\
        'Щас-щас... секундочку...',
    'quest_end': 'С точностью 99.999097438% могу сказать,\n'\
         'твое истинное обличие — это\n\n{}'
}

BUTTONS_LEXIC: dict[str, str] = {
    'quest_y': 'Конечно!',
    'quest_n': 'Отказываюсь :/'
}

QUEST_RES = dict(zip(
    ['печень', 'блин', 'багет', 'кулич', 'пирог', 'корги', \
    'пицца', 'наполеон', 'эчпочмак', 'слойка'],
    'Пирожок с печенью 🍘,Блинчик со сметанкой 🥞,Багет 🥖,Кулич 🍮,Вишневый пирог 🥧,Булка-корги 🐶,'\
    'Школьная питса 🍕,Наполеон! 🍰,Эчпочмак 🥟,Куассссан 🥐'.split(',')
))
